"""The promotion path end to end: a new independent quote moves a bench rule to promoted,
lint agrees at each step, and the generated agent changes accordingly."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import build_agent  # noqa: E402
from test_lint_check import principle_repo, run, Q_TALK, Q_BLOG  # noqa: E402


def write(root, files):
    for rel, text in files.items():
        f = root / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text)


def add_voice(root):
    write(root, {build_agent.VOICE: "---\ntype: method\nsteps:\n  - Start small\nsources: []\n---\n# Voice\n"})


def test_bench_rule_promoted_when_a_second_source_arrives(tmp_path, capsys):
    # one source: a valid bench rule
    bench = principle_repo("bench", [Q_TALK])
    code, out = run(tmp_path / "a", capsys, bench)
    assert code == 0, out

    # the new source adds an independent quote: lint now asks for promotion
    two = principle_repo("bench", [Q_TALK, Q_BLOG])
    code, out = run(tmp_path / "b", capsys, two)
    assert "promote it" in out

    # promoted, in the promoted folder: lint clean, agent lists it as a promoted rule
    promoted = principle_repo("promoted", [Q_TALK, Q_BLOG])
    root = tmp_path / "c"
    code, out = run(root, capsys, promoted)
    assert code == 0, out
    add_voice(root)
    text = build_agent.render(root, ".", "h")
    rules = text.split("## Rules")[1].split("## Voice")[0]
    assert "**Predict the loss**" in rules and "(bench" not in rules


def test_inferred_rule_is_never_promoted(tmp_path, capsys):
    files = principle_repo("promoted", [Q_TALK, Q_BLOG], inferred="true",
                           body="Inferred: closest quotes only.")
    code, out = run(tmp_path, capsys, files)
    assert code == 1 and "cannot be promoted" in out
