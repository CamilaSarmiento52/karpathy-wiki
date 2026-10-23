"""batches.py: every manifest item lands in exactly one batch, stably, with correct status."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import batches  # noqa: E402

ITEMS = [
    {"id": "a", "medium": "youtube", "published": "2022-08-16", "path": "raw/youtube/a.md"},
    {"id": "b", "medium": "github", "published": "2023-01-31", "path": "raw/github/b.md"},
    {"id": "c", "medium": "talk", "published": "2023-02-01", "path": "raw/talks/c.md"},
    {"id": "d", "medium": "blog", "published": "2024-07-31", "path": "raw/blog/d.md"},
    {"id": "e", "medium": "x", "published": "2024-08-01", "path": "raw/x/e.md"},
    {"id": "f", "medium": "talk", "published": "2025-10-17", "path": "raw/talks/f.md"},
    {"id": "g", "medium": "github", "published": "2025-10-24", "path": "raw/github/g.md"},
    {"id": "h", "medium": "github", "published": "2026-08-03", "path": "raw/github/h.md"},
]


def test_batch_boundaries():
    assert [batches.batch_of(i["published"]) for i in ITEMS] == [1, 1, 2, 2, 3, 3, 4, 4]


def make_repo(tmp_path):
    (tmp_path / "raw").mkdir()
    (tmp_path / "raw" / "_manifest.json").write_text(json.dumps({"version": 3, "items": ITEMS}))
    for rel in ("wiki/sources", "staging/digests", "staging/verify"):
        (tmp_path / rel).mkdir(parents=True)
    (tmp_path / "raw/youtube").mkdir()
    (tmp_path / "raw/youtube/a.md").write_text("---\nid: a\n---\nbody\n")
    (tmp_path / "staging/digests/a.md").write_text("# digest\n")
    (tmp_path / "wiki/sources/youtube-2022-08-16-a.md").write_text(
        "---\ntype: source\nraw_path: raw/youtube/a.md\n---\n# A\n")
    (tmp_path / "staging/verify/batch-1.md").write_text("- [[youtube-2022-08-16-a]]: ok\n")
    return tmp_path


def test_status_and_summary(tmp_path):
    rows = batches.status(make_repo(tmp_path))
    assert len(rows) == len(ITEMS)
    a = next(r for r in rows if r["id"] == "a")
    assert a == {"batch": 1, "published": "2022-08-16", "medium": "youtube", "id": "a",
                 "path": "raw/youtube/a.md", "raw": True, "digest": True,
                 "source_page": "youtube-2022-08-16-a", "verified": True}
    b = next(r for r in rows if r["id"] == "b")
    assert (b["raw"], b["digest"], b["source_page"], b["verified"]) == (False, False, None, False)
    s = batches.summary(rows)
    assert s[1] == {"sources": 2, "raw": 1, "digest": 1, "source_page": 1, "verified": 1}
    assert s[2]["sources"] == 2 and s[3]["sources"] == 2 and s[4]["sources"] == 2
    assert sum(x["sources"] for x in s.values()) == len(ITEMS)


def test_status_is_stable(tmp_path):
    root = make_repo(tmp_path)
    assert batches.status(root) == batches.status(root)


def test_cli_batch_listing(tmp_path, capsys):
    root = make_repo(tmp_path)
    assert batches.main(["--root", str(root), "--batch", "1"]) == 0
    out = capsys.readouterr().out
    assert "page:youtube-2022-08-16-a verified" in out and "no-page" in out
