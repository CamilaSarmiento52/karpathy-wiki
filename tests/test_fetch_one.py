"""Fetcher bookkeeping, with the network call replaced by a stub."""
import json

import pytest

import fetch_one
import rawstore

META = dict(id="post", url="https://example.com/post/", medium="blog", author="A",
            published="2025-01-01", title="Post", duration_or_length="2 words")


@pytest.fixture
def repo(store, monkeypatch):
    calls = []

    def fake_fetch(medium, ref, commit=None):
        calls.append((medium, ref, commit))
        return dict(META), "hello world"

    monkeypatch.setattr(fetch_one, "fetch", fake_fetch)
    return store, calls


def test_fetch_creates_medium_folder_and_manifest(repo):
    root, _ = repo
    (root / "raw" / "_manifest.json").write_text('{"items": []}')
    fetch_one.main("blog", "https://example.com/post/")
    assert (root / "raw/blog/post.md").exists()
    item = json.loads((root / "raw/_manifest.json").read_text())["items"][0]
    assert item["ref"] == "https://example.com/post/"
    assert item["sha256"] == fetch_one.digest("hello world")
    queued = json.loads((root / "raw/_queue.json").read_text())["items"]
    assert [(i["ref"], i["status"]) for i in queued] == [("https://example.com/post/",
                                                         "collected")]


def test_manifest_only_checkout_is_restored(repo):
    # review finding: a manifest entry with no raw file was skipped, so nothing was rebuilt
    root, calls = repo
    entry = dict(id="post", ref="https://example.com/post/", url=META["url"], medium="blog",
                 published="2025-01-01", path="raw/blog/post.md",
                 sha256=fetch_one.digest("hello world"))
    (root / "raw/_manifest.json").write_text(json.dumps({"items": [entry]}))
    assert fetch_one.restore() == 0
    assert (root / "raw/blog/post.md").read_text().endswith("hello world\n")
    assert calls == [("blog", "https://example.com/post/", None)]


def test_restore_reports_changed_content(repo):
    root, _ = repo
    entry = dict(id="post", ref="x", url=META["url"], medium="blog", published="2025-01-01",
                 path="raw/blog/post.md", sha256="0" * 64)
    (root / "raw/_manifest.json").write_text(json.dumps({"items": [entry]}))
    assert fetch_one.restore() == 1


def test_existing_file_is_skipped(repo):
    root, _ = repo
    (root / "raw/_manifest.json").write_text('{"items": []}')
    fetch_one.main("blog", "https://example.com/post/")
    before = (root / "raw/_manifest.json").read_text()
    fetch_one.main("blog", "https://example.com/post/")
    assert (root / "raw/_manifest.json").read_text() == before


def test_blog_parser_keeps_links():
    p = fetch_one.Text("https://karpathy.bearblog.dev/year/")
    p.feed('<p>See <a href="/verifiability/">Verifiability</a>.</p>')
    assert p.text() == "See [Verifiability](https://karpathy.bearblog.dev/verifiability/)."


def test_every_medium_has_a_fetcher():
    assert set(fetch_one.FETCHERS) == rawstore.MEDIA
