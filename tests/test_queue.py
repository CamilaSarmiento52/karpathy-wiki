"""Coverage queue: classifying leads, seeding, and the consistency check."""
import json

import pytest

import coverage_queue as cq
import rawstore as rs


@pytest.mark.parametrize("url, expected", [
    ("https://x.com/karpathy/status/2031135152349524125", ("x", "2031135152349524125")),
    ("https://twitter.com/karpathy/status/123?s=20", ("x", "123")),
    ("https://x.com/someone/status/123", None),
    ("https://www.youtube.com/watch?v=kCc8FmEb1nY", ("youtube", "kCc8FmEb1nY")),
    ("https://youtu.be/kCc8FmEb1nY", ("youtube", "kCc8FmEb1nY")),
    ("https://github.com/karpathy/minGPT", ("github", "karpathy/minGPT")),
    ("https://github.com/karpathy/nanochat}", ("github", "karpathy/nanochat")),
    ("https://github.com/karpathy/nanochat/discussions/164",
     ("github", "karpathy/nanochat/discussions/164")),
    ("https://github.com/karpathy/nanochat/discussions", None),
    ("https://github.com/karpathy/nanoGPT/issues/28", None),
    ("https://github.com/KellerJordan/modded-nanogpt", None),
    ("https://karpathy.bearblog.dev/the-space-of-minds", ("blog",
     "https://karpathy.bearblog.dev/the-space-of-minds/")),
    ("https://karpathy.bearblog.dev/blog/", None),
    ("https://pytorch.org/get-started/locally/", None),
    ("https://huggingface.co/datasets/openwebtext", None),
    ("https://www.dwarkesh.com/p/andrej-karpathy",
     ("unknown", "https://www.dwarkesh.com/p/andrej-karpathy")),
])
def test_classify(url, expected):
    assert cq.classify(url) == expected


def write_raw(root, rel, body):
    f = root / rel
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(f"---\nid: a\n---\n\n{body}\n")


def test_seed_twice_adds_nothing(store):
    write_raw(store, "raw/blog/a.md", "see https://github.com/karpathy/minbpe and "
              "https://www.dwarkesh.com/p/andrej-karpathy and https://pytorch.org/")
    q = rs.Queue()
    assert cq.seed(q) == 2
    q.save()
    before = (store / "raw/_queue.json").read_text()
    q = rs.Queue()
    assert cq.seed(q) == 0
    q.save()
    assert (store / "raw/_queue.json").read_text() == before
    item = q.get("karpathy/minbpe")
    assert (item["priority"], item["found_in"]) == ("teaching", "raw/blog/a.md")
    triage = q.get("https://www.dwarkesh.com/p/andrej-karpathy")
    assert (triage["medium"], triage["reason"]) == ("unknown", "needs-triage")


def test_check_passes_on_consistent_queue(store):
    rs.save(dict(id="v", url="u", medium="youtube", author="A", published="2024-01-01",
                 title="t", duration_or_length="1:00"), "b", "v")
    rs.Queue().save()
    assert cq.check(rs.Queue()) == 0


def test_check_catches_disagreement_and_missing_reason(store):
    items = [{f: "" for f in rs.QUEUE_FIELDS} | dict(ref="v", medium="youtube",
                                                     status="collected", priority="other"),
             {f: "" for f in rs.QUEUE_FIELDS} | dict(ref="w", medium="youtube",
                                                     status="excluded", priority="other")]
    (store / "raw/_queue.json").write_text(json.dumps({"version": 1, "items": items}))
    q = rs.Queue()
    assert cq.check(q) == 1
