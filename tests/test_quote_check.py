"""quote_check.py finds inline quotes missing from the cited raw, across caption markers."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import quote_check  # noqa: E402

RAW = "---\nid: v\n---\n\n[00:00] he says i'm pretty willing\n\n[00:30] to be convinced, he said\n"
SOURCE = "---\ntype: source\nraw_path: raw/youtube/v.md\n---\n# V\n"


def make(tmp_path, topic_body):
    for rel, text in {"raw/youtube/v.md": RAW, "wiki/sources/talk-v.md": SOURCE,
                      "wiki/topics/t.md": "---\ntype: topic\n---\n# T\n" + topic_body}.items():
        f = tmp_path / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text)
    return quote_check.check(tmp_path)


def test_quote_across_caption_marker_is_found(tmp_path):
    total, hits = make(tmp_path, 'He is "pretty willing to be convinced" ([[talk-v]] @00:00).\n')
    assert (total, hits) == (1, [])


def test_misquote_is_reported(tmp_path):
    total, hits = make(tmp_path, 'He is "very willing to be persuaded" ([[talk-v]] @00:00).\n')
    assert total == 1 and len(hits) == 1


def test_uncited_quote_is_not_checked(tmp_path):
    total, hits = make(tmp_path, 'He is "very willing to be persuaded".\n')
    assert (total, hits) == (0, [])
