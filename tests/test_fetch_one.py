"""Fetcher bookkeeping, with the network call replaced by a stub."""
import importlib.util
import json
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location(
    "fetch_one", Path(__file__).resolve().parent.parent / "scripts" / "fetch_one.py")
fetch_one = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fetch_one)

META = dict(id="post", url="https://example.com/post/", medium="blog", author="A",
            published="2025-01-01", title="Post", duration_or_length="2 words")


@pytest.fixture
def repo(tmp_path, monkeypatch):
    monkeypatch.setattr(fetch_one, "ROOT", tmp_path)
    monkeypatch.setattr(fetch_one, "RAW", tmp_path / "raw")
    monkeypatch.setattr(fetch_one, "MANIFEST", tmp_path / "raw" / "_manifest.json")
    (tmp_path / "raw").mkdir()
    calls = []

    def fake_fetch(medium, ref, commit=None):
        calls.append((medium, ref, commit))
        return dict(META), "hello world"

    monkeypatch.setattr(fetch_one, "fetch", fake_fetch)
    return tmp_path, calls


def test_fetch_creates_medium_folder_and_manifest(repo):
    root, _ = repo
    (root / "raw" / "_manifest.json").write_text('{"items": []}')
    fetch_one.main("blog", "https://example.com/post/")
    assert (root / "raw/blog/post.md").exists()
    item = json.loads((root / "raw/_manifest.json").read_text())["items"][0]
    assert item["ref"] == "https://example.com/post/"
    assert item["sha256"] == fetch_one.digest("hello world")


def test_manifest_only_checkout_is_restored(repo):
    # review finding: a manifest entry with no raw file was skipped, so nothing was rebuilt
    root, calls = repo
    entry = dict(id="post", ref="https://example.com/post/", url=META["url"], medium="blog",
                 published="2025-01-01", path="raw/blog/post.md",
                 sha256=fetch_one.digest("hello world"))
    (root / "raw/_manifest.json").write_text(json.dumps({"items": [entry]}))
    assert fetch_one.restore(json.loads((root / "raw/_manifest.json").read_text())) == 0
    assert (root / "raw/blog/post.md").read_text().endswith("hello world\n")
    assert calls == [("blog", "https://example.com/post/", None)]


def test_restore_reports_changed_content(repo):
    root, _ = repo
    entry = dict(id="post", ref="x", url=META["url"], medium="blog", published="2025-01-01",
                 path="raw/blog/post.md", sha256="0" * 64)
    assert fetch_one.restore({"items": [entry]}) == 1


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
