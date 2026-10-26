"""brief.py: four sections from a run report and the day's log; nothing on a quiet day."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import brief  # noqa: E402

LOG = """# Log

## 2026-11-03 ingest [[blog-2026-11-02-new-post]]
- created: [[blog-2026-11-02-new-post]], [[new-claim]]
- updated: [[vibe-coding]]
- relations: [[new-claim]] extends [[old-claim]] (timeline [[vibe-coding-over-time]])
- principles: quote added to [[predict-the-number-before-you-run]]; promoted [[simpler-wins]]
- verifier: 2 findings, both fixed

## 2026-11-02 ingest [[blog-2026-11-01-older]]
- created: [[blog-2026-11-01-older]]
"""
SOURCE = ("---\ntype: source\nraw_path: raw/blog/new-post.md\npublished: 2026-11-02\nmedium: blog\n"
          "summary: A post on agents.\ntitle: New post\n---\n# New post\n")


def repo(tmp_path, report=None, log=LOG):
    (tmp_path / "wiki/sources").mkdir(parents=True)
    (tmp_path / "wiki/log.md").write_text(log)
    (tmp_path / "wiki/sources/blog-2026-11-02-new-post.md").write_text(SOURCE)
    if report is not None:
        (tmp_path / "reports").mkdir()
        (tmp_path / "reports/collect-2026-11-03.json").write_text(json.dumps(report))
    return tmp_path


REPORT = {"new_raw": [{"path": "raw/blog/new-post.md"}],
          "new_triage": [{"ref": "talk-x", "title": "A talk", "url": "https://y"}],
          "collectors": {"youtube": {"ok": True, "pending": ["pending v1: rate-limited"]},
                         "github": {"ok": False, "tail": ["HTTP 502"]}}}


def test_four_sections_in_order(tmp_path):
    text = brief.build(repo(tmp_path, REPORT), "2026-11-03")
    heads = [l for l in text.splitlines() if l.startswith("## ")]
    assert heads == ["## What he published", "## What changed in the wiki", "## Rules", "## Needs you"]
    assert text.count("New post") == 1 and "published 2026-11-02" in text
    assert "blog-2026-11-01-older" not in text


def test_rules_relations_and_needs_you(tmp_path):
    text = brief.build(repo(tmp_path, REPORT), "2026-11-03")
    assert "promoted [[simpler-wins]]" in text and "extends [[old-claim]]" in text
    assert "Triage: A talk" in text and "Collector `github` failed: HTTP 502" in text
    assert "rate-limited" in text
    assert "Collected but not compiled" not in text


def test_uncompiled_raw_is_flagged(tmp_path):
    rep = dict(REPORT, new_raw=[{"path": "raw/blog/new-post.md"}, {"path": "raw/x/1.md"}])
    text = brief.build(repo(tmp_path, rep), "2026-11-03")
    assert "Collected but not compiled: `raw/x/1.md`" in text


def test_quiet_day_writes_nothing(tmp_path, capsys):
    root = repo(tmp_path, {"new_raw": [], "new_triage": [], "collectors": {"blog": {"ok": True}}},
                log="# Log\n")
    assert brief.main(["--root", str(root), "--date", "2026-11-03"]) == 0
    assert capsys.readouterr().out.strip() == "no brief"
    assert not (root / "reports/briefs").exists()
