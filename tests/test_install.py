"""install.py: user-level agent copy and skill links; idempotent; uninstall removes only its own."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import install  # noqa: E402
from test_build_agent import wiki  # noqa: E402


def repo(tmp_path):
    root = wiki(tmp_path / "repo")
    (root / ".claude/hooks").mkdir(parents=True)
    (root / ".claude/hooks/run_gate.py").write_text("# gate\n")
    for name in install.SKILLS:
        d = root / ".claude" / "skills" / name
        d.mkdir(parents=True)
        (d / "SKILL.md").write_text(f"---\nname: {name}\n---\n")
    return root


def test_install_is_idempotent_and_uses_absolute_paths(tmp_path):
    root, home = repo(tmp_path), tmp_path / "home"
    assert install.install(root, home)
    agent = (home / ".claude/agents/karpathy.md").read_text()
    assert install.MARKER in agent and str(root / ".claude/hooks/run_gate.py") in agent
    assert f"`{root}/wiki/`" in agent
    for name in install.SKILLS:
        link = home / ".claude/skills" / name
        assert link.is_symlink() and (link / "SKILL.md").exists()
    assert (home / install.HOOK_LINK).is_symlink()
    assert install.install(root, home) == []


def test_never_overwrites_a_real_file(tmp_path):
    root, home = repo(tmp_path), tmp_path / "home"
    agent = home / ".claude/agents/karpathy.md"
    agent.parent.mkdir(parents=True)
    agent.write_text("my own agent")
    with pytest.raises(SystemExit):
        install.install(root, home)
    assert agent.read_text() == "my own agent"


def test_uninstall_removes_only_what_it_created(tmp_path):
    root, home = repo(tmp_path), tmp_path / "home"
    install.install(root, home)
    other = home / ".claude/skills/someone-else"
    other.mkdir()
    removed = install.uninstall(root, home)
    assert len(removed) == len(install.SKILLS) + 2 and other.exists()
    assert not (home / ".claude/agents/karpathy.md").exists()
    assert install.uninstall(root, home) == []


def test_refuses_to_repoint_an_install_from_another_copy(tmp_path):
    home = tmp_path / "home"
    install.install(repo(tmp_path / "one"), home)
    other = repo(tmp_path / "two")
    with pytest.raises(SystemExit, match="another copy"):
        install.install(other, home)
    assert install.install(other, home, force=True)
