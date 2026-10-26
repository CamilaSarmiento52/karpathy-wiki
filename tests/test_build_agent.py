"""build_agent.py: generate the karpathy agent from principles and the voice page."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import build_agent  # noqa: E402


def principle(title, source, status="promoted", inferred="false", practice="Predict first."):
    return (f"---\ntype: principle\nstatus: {status}\ninferred: {inferred}\nquotes:\n"
            f'  - {{text: "predict the loss", source: "[[{source}]]", location: "00:10"}}\n'
            f"---\n# {title}\n> quote\n\n## In practice\n{practice}\n\n## Sources\n- [[{source}]]\n")


VOICE = "---\ntype: method\nsteps:\n  - Start from a blank file\n  - Use tiny numbers\nsources: []\n---\n# How he explains\n"


def wiki(tmp_path, extra=None):
    files = {
        "wiki/sources/talk-a.md": "---\ntype: source\n---\n# A\n",
        "wiki/principles/predict-first.md": principle("Predict, then run", "talk-a"),
        "wiki/principles/_bench/simpler-wins.md": principle("Simpler wins", "talk-a", "bench"),
        "wiki/principles/_bench/say-assumptions.md": principle("Say what you assumed", "talk-a",
                                                               "bench", inferred="true"),
        build_agent.VOICE: VOICE,
    }
    files.update(extra or {})
    for rel, text in files.items():
        if text is None:
            continue
        f = tmp_path / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text)
    return tmp_path


def test_sections_and_rules(tmp_path):
    text = build_agent.render(wiki(tmp_path), ".", "/h/run_gate.py")
    for heading in ("## Grounding", "## Rules", "## Voice", "## Task loop", "## Report"):
        assert heading in text
    assert '"predict the loss" (talk-a 00:10)' in text
    assert "**Simpler wins** (bench)" in text and "(bench, inferred)" in text
    assert "1. Start from a blank file" in text
    assert 'f="/h/run_gate.py"; [ -f "$f" ] || f="$HOME/.claude/hooks/karpathy-run-gate.py"; python3 "$f" check' in text
    assert "not Andrej Karpathy" in text


def test_output_is_deterministic(tmp_path):
    root = wiki(tmp_path)
    assert build_agent.render(root, ".", "h") == build_agent.render(root, ".", "h")


def test_check_mode_detects_stale_file(tmp_path):
    root = wiki(tmp_path)
    assert build_agent.main(["--root", str(root)]) == 0
    assert build_agent.main(["--root", str(root), "--check"]) == 0
    (root / build_agent.OUT).write_text("stale")
    assert build_agent.main(["--root", str(root), "--check"]) == 1


def test_principle_without_quote_fails(tmp_path):
    root = wiki(tmp_path, {"wiki/principles/bad.md":
                           "---\ntype: principle\nstatus: promoted\ninferred: false\nquotes: []\n---\n# Bad\n"})
    with pytest.raises(build_agent.BuildError, match="without a quote"):
        build_agent.render(root, ".", "h")


def test_missing_source_page_fails(tmp_path):
    root = wiki(tmp_path, {"wiki/principles/bad.md": principle("Bad", "no-such-source")})
    with pytest.raises(build_agent.BuildError, match="not found"):
        build_agent.render(root, ".", "h")


def test_missing_voice_page_fails(tmp_path):
    root = wiki(tmp_path, {build_agent.VOICE: None})
    with pytest.raises(build_agent.BuildError, match="voice page missing"):
        build_agent.render(root, ".", "h")


def test_rules_are_short_and_point_to_their_pages(tmp_path):
    text = build_agent.render(wiki(tmp_path), ".", "h")
    assert "Predict first." not in text  # In practice stays on the page
    assert "Page: `./wiki/principles/predict-first.md`" in text
    assert "do not attribute it to him" in text
