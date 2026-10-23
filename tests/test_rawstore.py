"""Shared raw store: raw files, manifest under a lock, restore, queue bookkeeping."""
import json
import multiprocessing

import pytest

import rawstore as rs

META = dict(id="v1", url="https://example.com/v1", medium="youtube", author="A",
            published="2024-01-01", title="T", duration_or_length="1:00")


def test_frontmatter_order_and_body(store):
    path = rs.write(dict(META, commit="abc"), "  body text \n")
    text = (store / path).read_text()
    keys = [line.split(":")[0] for line in text.split("---")[1].strip().splitlines()]
    assert keys == ["id", "url", "medium", "author", "published", "fetched", "title",
                    "duration_or_length", "commit"]
    assert text.endswith("---\n\nbody text\n")


def test_hash_ignores_frontmatter_and_whitespace():
    assert rs.digest("hello\n") == rs.digest("  hello")


def _add(root, n):
    rs.ROOT = root
    for i in range(n):
        rs.add_entry(dict(id=f"{root.name}-{multiprocessing.current_process().name}-{i}",
                          ref="r", url="u", medium="x", published="2024-01-01",
                          path=f"raw/x/{i}.md", sha256="0"))


def test_parallel_writers_lose_no_entries(store):
    ctx = multiprocessing.get_context("fork")
    procs = [ctx.Process(target=_add, args=(store, 20), name=f"p{k}") for k in range(4)]
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    assert len(rs.read_manifest()["items"]) == 80


def test_restore_uses_manifest_path_for_snapshots(store):
    entry = dict(id="k__r@1a2b3c4", ref="k/r", url="u", medium="github",
                 published="2025-01-01", path="raw/github/k__r@1a2b3c4.md",
                 sha256=rs.digest("readme"), commit="1a2b3c4ffff", repo="k/r")
    (store / "raw/_manifest.json").write_text(json.dumps({"items": [entry]}))
    calls = []

    def fetch(medium, ref, commit):
        calls.append(commit)
        return dict(META, id="k__r", medium="github"), "readme"

    assert rs.restore(fetch) == 0
    assert calls == ["1a2b3c4ffff"]
    assert "id: k__r@1a2b3c4" in (store / "raw/github/k__r@1a2b3c4.md").read_text()
    assert not (store / "raw/github/k__r.md").exists()


def test_queue_collected_follows_manifest(store):
    q = rs.Queue()
    q.add("v1", medium="youtube")
    q.add("v2", medium="youtube")
    q.save()
    rs.save(dict(META), "body", "v1")
    q = rs.Queue()
    q.save()
    assert q.get("v1")["status"] == "collected"
    assert q.get("v2")["status"] == "pending"


def test_queue_adds_manifest_items_it_did_not_know(store):
    rs.save(dict(META), "body", "v1")
    q = rs.Queue()
    q.save()
    assert q.get("v1")["status"] == "collected"
    assert q.get("v1")["found_in"] == "manifest"


def test_add_never_overwrites_a_decision(store):
    q = rs.Queue()
    q.add("v1", medium="youtube")
    q.set("v1", status="excluded", reason="not-karpathy", priority="teaching")
    q.add("v1", medium="youtube", priority="other", title="filled")
    assert q.get("v1")["status"] == "excluded"
    assert q.get("v1")["priority"] == "teaching"
    q.add("v2", medium="youtube")
    q.add("v2", medium="youtube", priority="teaching")
    assert q.get("v2")["priority"] == "teaching"
    assert q.get("v1")["title"] == "filled"


def test_exclusion_needs_a_reason(store):
    q = rs.Queue()
    q.add("v1", medium="youtube")
    with pytest.raises(ValueError):
        q.set("v1", status="excluded")


def test_parallel_queue_savers_keep_both_changes(store):
    a, b = rs.Queue(), rs.Queue()
    a.add("v1", medium="youtube")
    b.add("t1", medium="x")
    a.save()
    b.save()
    assert {i["ref"] for i in json.loads((store / "raw/_queue.json").read_text())["items"]} \
        == {"v1", "t1"}


def test_github_refs_match_case_insensitively(store):
    q = rs.Queue()
    q.add("karpathy/nanoGPT", medium="github")
    assert q.get("karpathy/nanogpt") is not None


def test_teaching_exception_to_the_cutoff():
    assert not rs.in_scope("2022-08-01", "other")
    assert rs.in_scope("2022-08-01", "teaching")
    assert rs.priority("github", "karpathy/micrograd", "") == "teaching"
    assert rs.priority("youtube", "x", "Let's build the GPT Tokenizer") == "teaching"
    assert rs.priority("youtube", "x", "Stable diffusion dreams of tattoos") == "other"


def test_http_and_https_are_one_item(store):
    q = rs.Queue()
    q.add("http://karpathy.github.io/2026/02/12/microgpt/", medium="blog")
    assert q.get("https://karpathy.github.io/2026/02/12/microgpt") is not None


def test_crlf_body_matches_its_hash_when_read_back(store):
    rs.save(dict(META), "line one\r\nline two\r\n", "v1")
    text = (store / "raw/youtube/v1.md").read_text()  # universal newlines, like lint
    body = text.split("---\n", 2)[2]
    assert rs.digest(body) == rs.read_manifest()["items"][0]["sha256"]
