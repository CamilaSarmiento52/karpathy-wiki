"""The five collectors, with every network call replaced by canned responses."""
import json
from types import SimpleNamespace as NS

import pytest

import collect_blog
import collect_github
import collect_talks
import collect_x
import collect_youtube
import rawstore as rs

REAL_METADATA = collect_youtube.metadata  # fixtures replace it; one test needs the real one


def files(root):
    return (root / "raw/_manifest.json").read_text(), (root / "raw/_queue.json").read_text()


def snippets(n, step=10):
    return [NS(start=i * step, text=f"line {i}") for i in range(n)]


# --- YouTube ---------------------------------------------------------------------------

VIDEOS = {
    "AAAAAAAAAAA": dict(title="Let's build the GPT Tokenizer", upload_date="20240220",
                        duration=100, channel_id=collect_youtube.CHANNEL_ID),
    "BBBBBBBBBBB": dict(title="Stable diffusion dreams", upload_date="20220801",
                        duration=60, channel_id=collect_youtube.CHANNEL_ID),
    "CCCCCCCCCCC": dict(title="Some podcast", upload_date="20250101", duration=60,
                        channel_id="other"),
}


@pytest.fixture
def youtube(store, monkeypatch):
    fetched = []
    monkeypatch.setattr(collect_youtube, "listing", lambda: [
        {"id": v, "title": VIDEOS[v]["title"]} for v in ("AAAAAAAAAAA", "BBBBBBBBBBB")])
    monkeypatch.setattr(collect_youtube, "metadata", lambda v: VIDEOS[v])

    def captions(v):
        fetched.append(v)
        return snippets(7)

    monkeypatch.setattr(collect_youtube, "captions", captions)
    return store, fetched


def test_youtube_collects_then_is_idempotent(youtube):
    root, fetched = youtube
    assert collect_youtube.main([]) == 0
    assert fetched == ["AAAAAAAAAAA"]
    before = files(root)
    collect_youtube.main([])
    assert fetched == ["AAAAAAAAAAA"]
    assert files(root) == before


def test_youtube_cutoff_excludes_with_reason(youtube):
    collect_youtube.main([])
    item = rs.Queue().get("BBBBBBBBBBB")
    assert (item["status"], item["reason"]) == ("excluded", "before-2023")


def test_youtube_blocks_are_30_seconds(youtube):
    root, _ = youtube
    collect_youtube.main([])
    body = (root / "raw/youtube/AAAAAAAAAAA.md").read_text().split("---\n", 2)[2]
    assert [b.split("]")[0] for b in body.strip().split("\n\n")] == ["[00:00", "[00:40"]


def test_youtube_manifest_entry_fields(youtube):
    root, _ = youtube
    collect_youtube.main([])
    e = rs.read_manifest()["items"][0]
    assert set(e) == {"id", "ref", "url", "medium", "published", "path", "sha256"}
    assert (e["published"], e["path"]) == ("2024-02-20", "raw/youtube/AAAAAAAAAAA.md")


def test_youtube_lead_on_another_channel_becomes_talk(youtube):
    q = rs.Queue()
    q.add("CCCCCCCCCCC", medium="youtube")
    q.save()
    collect_youtube.main([])
    item = rs.Queue().get("CCCCCCCCCCC")
    assert (item["medium"], item["status"], item["reason"]) == ("talk", "pending",
                                                                "needs-triage")


def test_youtube_without_captions_stays_pending(youtube, monkeypatch):
    def none(v):
        raise rs.Skip("pending", "no-transcript")
    monkeypatch.setattr(collect_youtube, "captions", none)
    collect_youtube.main([])
    assert rs.Queue().get("AAAAAAAAAAA")["reason"] == "no-transcript"


def test_dry_run_and_limit(youtube):
    root, fetched = youtube
    collect_youtube.main(["--dry-run"])
    assert fetched == [] and not (root / "raw/_queue.json").exists()
    collect_youtube.main(["--limit", "0"])
    assert fetched == []


# --- GitHub ----------------------------------------------------------------------------

class FakeGitHub:
    def __init__(self):
        self.readme_sha = "a" * 40
        self.discussion_author = "karpathy"

    def gh(self, path, raw=False):
        if raw:
            return f"README at {path.rsplit('=', 1)[1][:7]}"
        if path.endswith("/readme"):
            return {"path": "README.md"}
        if "commits?path=" in path:
            return [{"sha": self.readme_sha}]
        if "/commits/" in path:
            sha = path.rsplit("/", 1)[1]
            return {"commit": {"committer": {"date": "2025-0%s-01T00:00:00Z" %
                                             (1 if sha[0] == "a" else 2)}}}
        name = path.split("/")[-1]
        return {"html_url": f"https://github.com/karpathy/{name}", "name": name}

    def graphql(self, query, **v):
        if "discussions(" in query:
            return {"repository": {"discussions": {"nodes": [
                {"number": 1, "title": "Walkthrough", "createdAt": "2025-10-13T00:00:00Z",
                 "author": {"login": "karpathy"}},
                {"number": 2, "title": "Question", "createdAt": "2025-10-14T00:00:00Z",
                 "author": {"login": "someone"}}]}}}
        return {"repository": {"discussion": {
            "title": "Walkthrough", "body": "how it works", "createdAt": "2025-10-13T00:00:00Z",
            "url": "https://github.com/karpathy/nanochat/discussions/1",
            "author": {"login": self.discussion_author}}}}


REPOS = [
    {"full_name": "karpathy/nanochat", "fork": False, "pushed_at": "2025-10-01T00:00:00Z",
     "html_url": "https://github.com/karpathy/nanochat", "has_discussions": True},
    {"full_name": "karpathy/old", "fork": False, "pushed_at": "2019-01-01T00:00:00Z",
     "html_url": "https://github.com/karpathy/old", "has_discussions": False},
    {"full_name": "karpathy/forked", "fork": True, "pushed_at": "2025-01-01T00:00:00Z",
     "html_url": "https://github.com/karpathy/forked", "has_discussions": False},
]


@pytest.fixture
def github(store, monkeypatch):
    fake = FakeGitHub()
    monkeypatch.setattr(collect_github, "gh", fake.gh)
    monkeypatch.setattr(collect_github, "graphql", fake.graphql)
    monkeypatch.setattr(collect_github, "repos", lambda: REPOS)
    return store, fake


def test_github_first_run(github):
    root, _ = github
    collect_github.main([])
    q = rs.Queue()
    assert q.get("karpathy/nanochat")["status"] == "collected"
    assert q.get("karpathy/nanochat/discussions/1")["status"] == "collected"
    assert q.get("karpathy/nanochat/discussions/2") is None  # not his
    assert (q.get("karpathy/old")["status"], q.get("karpathy/old")["reason"]) == \
        ("excluded", "before-2023")
    assert q.get("karpathy/forked")["reason"] == "fork"
    e = next(i for i in rs.read_manifest()["items"] if i["id"] == "karpathy__nanochat")
    assert (e["commit"], e["repo"], e["published"]) == ("a" * 40, "karpathy/nanochat",
                                                        "2025-01-01")


def test_github_unchanged_readme_no_new_snapshot(github):
    root, _ = github
    collect_github.main([])
    before = files(root)
    collect_github.main([])
    assert files(root) == before


def test_github_changed_readme_new_snapshot(github):
    root, fake = github
    collect_github.main([])
    old = (root / "raw/github/karpathy__nanochat.md").read_text()
    fake.readme_sha = "b" * 40
    collect_github.main([])
    snap = root / "raw/github/karpathy__nanochat@bbbbbbb.md"
    assert snap.exists() and "published: '2025-02-01'" in snap.read_text()
    assert (root / "raw/github/karpathy__nanochat.md").read_text() == old
    assert len(collect_github.snapshots("karpathy/nanochat")) == 2
    before = files(root)
    collect_github.main([])
    assert files(root) == before


def test_github_discussion_by_someone_else_is_excluded(github):
    root, fake = github
    fake.discussion_author = "someone"
    q = rs.Queue()
    q.add("karpathy/other/discussions/9", medium="github")
    q.save()
    collect_github.main([])
    assert rs.Queue().get("karpathy/other/discussions/9")["reason"] == "not-karpathy"


# --- X ---------------------------------------------------------------------------------

def tweet(tid, text, reply_to=None, handle="karpathy"):
    return {"id": tid, "url": f"https://x.com/{handle}/status/{tid}", "text": text,
            "author": "Andrej Karpathy", "handle": handle, "replying_to": reply_to,
            "published": "2025-03-0" + tid[-1]}


SEARCH = [
    {"id": "103", "createdAt": "Mon Mar 03 10:00:00 +0000 2025", "isReply": True,
     "inReplyToUsername": "karpathy", "conversationId": "101"},
    {"id": "102", "createdAt": "Mon Mar 03 09:00:00 +0000 2025", "isReply": True,
     "inReplyToUsername": "someone", "conversationId": "900"},
    {"id": "101", "createdAt": "Mon Mar 03 08:00:00 +0000 2025", "isReply": False,
     "conversationId": "101"},
    {"id": "104", "createdAt": "Tue Mar 04 08:00:00 +0000 2025", "isReply": False,
     "conversationId": "104", "retweeted_tweet": {"id": "1"}},
]


@pytest.fixture
def x(store, monkeypatch):
    posts = {"101": tweet("101", "first post\nmore"), "103": tweet("103", "second post"),
             "105": tweet("105", "lead"), "106": tweet("106", "reply", reply_to="someone")}
    fetched = []

    def post(tid):
        fetched.append(tid)
        return posts[tid]

    monkeypatch.setattr(collect_x, "post", post)
    monkeypatch.setattr(collect_x, "search", lambda key, since: iter(SEARCH))
    monkeypatch.setattr(collect_x, "api_key", lambda: "k")
    collect_x.THREADS.clear()
    return store, fetched


def test_x_thread_in_order_and_exclusions(x):
    root, _ = x
    collect_x.main([])
    body = (root / "raw/x/101.md").read_text().split("---\n", 2)[2]
    assert body.strip() == "first post\nmore\n\n---\n\nsecond post"
    e = rs.read_manifest()["items"][0]
    assert (e["id"], e["ref"]) == ("101", "101,103")
    q = rs.Queue()
    assert q.get("102")["reason"] == "reply-to-other"
    assert q.get("104")["reason"] == "retweet"
    assert q.get("103") is None


def test_x_idempotent(x):
    root, fetched = x
    collect_x.main([])
    before, n = files(root), len(fetched)
    collect_x.main([])
    assert files(root) == before and len(fetched) == n


def test_x_without_key_fetches_known_posts_only(x, monkeypatch, capsys):
    monkeypatch.setattr(collect_x, "api_key", lambda: None)
    q = rs.Queue()
    q.add("105", medium="x")
    q.add("106", medium="x")
    q.save()
    collect_x.main([])
    assert "no TWITTERAPI_IO_KEY" in capsys.readouterr().out
    q = rs.Queue()
    assert q.get("105")["status"] == "collected"
    assert q.get("106")["reason"] == "reply-to-other"
    assert q.get("101") is None


def test_x_restore_needs_no_key(x):
    meta, body = collect_x.fetch("101,103")
    assert meta["id"] == "101" and body.endswith("second post")


# --- Blog ------------------------------------------------------------------------------

FEED = """<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>New</title>
<link href="https://karpathy.bearblog.dev/new/"/><published>2025-12-01T00:00:00Z</published>
<content>&lt;p&gt;See &lt;a href="/older/"&gt;older&lt;/a&gt;&lt;/p&gt;</content></entry></feed>"""
LIST = """<ul><li><span><time datetime="2025-12-01T00:00Z">1 Dec</time></span>
<a href="/new/">New</a></li><li><span><time datetime="2024-03-01T00:00Z">1 Mar</time></span>
<a href="/older/">Older</a></li></ul>"""
OLD_PAGE = """<html><head><title>Older | karpathy</title></head><body><nav>menu</nav><main>
<h1>Older</h1><p><i><time datetime="2024-03-01T00:00Z">1 Mar</time></i></p><p>Old words.</p>
</main></body></html>"""


@pytest.fixture
def blog(store, monkeypatch):
    pages = {"https://karpathy.bearblog.dev/feed/": FEED,
             "https://karpathy.bearblog.dev/blog/": LIST,
             "https://karpathy.bearblog.dev/older/": OLD_PAGE}
    monkeypatch.setattr(rs, "get", lambda url, headers=None: pages[url])
    monkeypatch.setattr(collect_blog, "old_listing", lambda: [
        ("https://karpathy.github.io/2019/04/25/recipe/", "2019-04-25", "A Recipe")])
    return store


def test_blog_feed_and_page_fallback(blog):
    collect_blog.main([])
    new = (blog / "raw/blog/new.md").read_text()
    assert "[older](https://karpathy.bearblog.dev/older/)" in new
    old = (blog / "raw/blog/older.md").read_text()
    assert "Old words." in old and "menu" not in old and "published: '2024-03-01'" in old
    assert "title: Older\n" in old and "# Older" not in old
    item = rs.Queue().get("https://karpathy.github.io/2019/04/25/recipe/")
    assert (item["status"], item["reason"]) == ("excluded", "before-2023")


def test_blog_idempotent(blog):
    collect_blog.main([])
    before = files(blog)
    collect_blog.main([])
    assert files(blog) == before


# --- Talks -----------------------------------------------------------------------------

def test_talk_youtube_upload_goes_to_talks_folder(store, monkeypatch):
    monkeypatch.setattr(collect_youtube, "metadata", lambda v: VIDEOS["CCCCCCCCCCC"])
    monkeypatch.setattr(collect_youtube, "captions", lambda v: snippets(3))
    q = rs.Queue()
    q.add("CCCCCCCCCCC", medium="talk")
    q.save()
    collect_talks.main([])
    text = (store / "raw/talks/CCCCCCCCCCC.md").read_text()
    assert "medium: talk" in text


def test_talk_page_without_transcript_stays_pending(store, monkeypatch):
    monkeypatch.setattr(rs, "get", lambda url, headers=None:
                        '<article><time datetime="2025-10-17">x</time>show notes</article>')
    q = rs.Queue()
    q.add("https://pod.example/ep", medium="talk")
    q.save()
    collect_talks.main([])
    assert rs.Queue().get("https://pod.example/ep")["reason"] == "no-transcript"


def test_talk_page_with_transcript(store, monkeypatch):
    words = " ".join(["word"] * 2000)
    monkeypatch.setattr(rs, "get", lambda url, headers=None:
                        '<html><title>Ep 1</title><article><time datetime="2025-10-17">x'
                        f"</time><p>{words}</p></article></html>")
    q = rs.Queue()
    q.add("https://pod.example/p/ep-1", medium="talk")
    q.save()
    collect_talks.main([])
    e = rs.read_manifest()["items"][0]
    assert (e["id"], e["published"], e["medium"]) == ("pod-example-p-ep-1", "2025-10-17",
                                                      "talk")


def test_github_gist_markdown_kept_code_only_excluded(github, monkeypatch):
    gists = {"aaa": ({"llm-wiki.md": "the idea"}, "v2" * 20, "2026-04-04"),
             "bbb": ({"x.py": "print()"}, "v1" * 20, "2026-04-02")}
    monkeypatch.setattr(collect_github, "gist_files", lambda gid, commit=None: gists[gid])
    q = rs.Queue()
    q.add("gist/aaa", medium="github")
    q.add("gist/bbb", medium="github")
    q.save()
    collect_github.main([])
    e = next(i for i in rs.read_manifest()["items"] if i["id"] == "karpathy__gist-aaa")
    assert (e["commit"], e["published"]) == ("v2" * 20, "2026-04-04")
    assert rs.Queue().get("gist/bbb")["reason"] == "code-only gist"


def test_x_article_without_text_is_not_written(x, monkeypatch):
    root, _ = x
    monkeypatch.setattr(collect_x, "api_key", lambda: None)
    monkeypatch.setattr(collect_x, "post", lambda tid: tweet(tid, ""))
    q = rs.Queue()
    q.add("107", medium="x")
    q.save()
    collect_x.main([])
    assert not (root / "raw/x/107.md").exists()
    assert rs.Queue().get("107")["reason"] == "no-text (X article)"


def test_talk_search_queues_candidates_for_triage_only(store, monkeypatch):
    results = [
        dict(id="AAAAAAAAAAA", channel_id="sequoia", channel="Sequoia", duration=1800,
             title="Andrej Karpathy: fireside chat"),
        dict(id="BBBBBBBBBBB", channel_id="clips", channel="Clips", duration=120,
             title="Andrej Karpathy short clip"),
        dict(id="CCCCCCCCCCC", channel_id=collect_youtube.CHANNEL_ID, channel="Andrej Karpathy",
             duration=6000, title="Let's build GPT (Karpathy)"),
        dict(id="DDDDDDDDDDD", channel_id="x", channel="X", duration=3000,
             title="AI news this week"),
    ]
    monkeypatch.setattr(collect_talks, "search", lambda query, n=40: iter(results))
    fetched = []
    monkeypatch.setattr(collect_talks, "fetch", lambda ref, commit=None: fetched.append(ref))
    collect_talks.main(["--search"])
    q = rs.Queue()
    item = q.get("AAAAAAAAAAA")
    assert (item["medium"], item["status"], item["reason"]) == ("talk", "pending", "needs-triage")
    assert item["found_in"] == "search: Sequoia (30:00)"
    assert [q.get(v) for v in ("BBBBBBBBBBB", "CCCCCCCCCCC", "DDDDDDDDDDD")] == [None] * 3
    assert fetched == []  # nothing is collected before a person approves it


def test_youtube_removed_video_is_excluded(youtube, monkeypatch):
    import subprocess

    def gone(cmd):
        raise subprocess.CalledProcessError(1, cmd, stderr="ERROR: This video is unavailable")
    monkeypatch.setattr(rs, "run", gone)
    monkeypatch.setattr(collect_youtube, "listing", lambda: [])
    monkeypatch.setattr(collect_youtube, "metadata", REAL_METADATA)
    q = rs.Queue()
    q.add("ZZZZZZZZZZZ", medium="youtube")
    q.save()
    collect_youtube.main([])
    assert rs.Queue().get("ZZZZZZZZZZZ")["reason"] == "unavailable (removed or private)"
