#!/usr/bin/env python3
"""Fetch one source into raw/ with standard frontmatter and a manifest entry.

Phase 1 helper for hand-picked sources; phase 2 replaces it with per-medium collectors.
Idempotent: an id already in the manifest is skipped.

Usage:
  python scripts/fetch_one.py youtube <video_id>
  python scripts/fetch_one.py x <tweet_id>
  python scripts/fetch_one.py github <owner/repo>
  python scripts/fetch_one.py blog <bearblog post url>
"""
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "raw"
MANIFEST = RAW / "_manifest.json"
UA = {"User-Agent": "Mozilla/5.0 (karpathy-wiki fetcher)"}
FOLDER = {"youtube": "youtube", "x": "x", "github": "github", "blog": "blog", "talk": "talks"}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return r.read().decode("utf-8")


def stamp(seconds):
    s = int(seconds)
    h, m, s = s // 3600, s // 60 % 60, s % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


class Text(HTMLParser):
    """HTML to plain text, keeping paragraph breaks, headings and list bullets."""
    BLOCK = {"p", "div", "br", "li", "h1", "h2", "h3", "h4", "pre", "blockquote", "tr"}

    def __init__(self):
        super().__init__()
        self.out = []

    def handle_starttag(self, tag, attrs):
        if tag in self.BLOCK:
            self.out.append("\n\n")
        if tag in ("h1", "h2", "h3", "h4"):
            self.out.append("#" * int(tag[1]) + " ")
        if tag == "li":
            self.out.append("- ")

    def handle_data(self, data):
        self.out.append(data)

    def text(self):
        return re.sub(r"\n{3,}", "\n\n", "".join(self.out)).strip()


def youtube(vid):
    from youtube_transcript_api import YouTubeTranscriptApi
    meta = json.loads(subprocess.run(
        ["yt-dlp", "-j", "--skip-download", f"https://www.youtube.com/watch?v={vid}"],
        capture_output=True, text=True, check=True).stdout)
    snippets = YouTubeTranscriptApi().fetch(vid, languages=["en"])
    # one block per ~30 s so citations can point at mm:ss without a line per caption
    blocks, cur, start = [], [], None
    for sn in snippets:
        if start is None:
            start = sn.start
        cur.append(sn.text.replace("\n", " "))
        if sn.start - start >= 30:
            blocks.append(f"[{stamp(start)}] {' '.join(cur)}")
            cur, start = [], None
    if cur:
        blocks.append(f"[{stamp(start)}] {' '.join(cur)}")
    d = meta["upload_date"]
    return dict(id=vid, url=f"https://www.youtube.com/watch?v={vid}", medium="youtube",
                author="Andrej Karpathy", published=f"{d[:4]}-{d[4:6]}-{d[6:]}",
                title=meta["title"], duration_or_length=stamp(meta["duration"])), "\n\n".join(blocks)


def x(tid):
    t = json.loads(get(f"https://api.fxtwitter.com/karpathy/status/{tid}"))["tweet"]
    published = dt.datetime.strptime(t["created_at"], "%a %b %d %H:%M:%S %z %Y").date()
    body = t["text"]
    first = body.split("\n", 1)[0]
    title = first if len(first) <= 80 else first[:80].rsplit(" ", 1)[0] + "…"
    return dict(id=tid, url=t["url"], medium="x", author=t["author"]["name"],
                published=published.isoformat(), title=title,
                duration_or_length=f"{len(body.split())} words"), body


def github(repo):
    info = json.loads(subprocess.run(["gh", "api", f"repos/{repo}"],
                                     capture_output=True, text=True, check=True).stdout)
    # a README is a living document: date it by its last commit, not the repo's creation
    last = json.loads(subprocess.run(["gh", "api", f"repos/{repo}/commits?path=README.md&per_page=1"],
                                     capture_output=True, text=True, check=True).stdout)
    readme = subprocess.run(["gh", "api", f"repos/{repo}/readme", "-H",
                             "Accept: application/vnd.github.raw"],
                            capture_output=True, text=True, check=True).stdout
    return dict(id=repo.replace("/", "__"), url=info["html_url"], medium="github",
                author="Andrej Karpathy", published=last[0]["commit"]["committer"]["date"][:10],
                title=f"{info['name']} README", duration_or_length=f"{len(readme.split())} words"), readme


def blog(url):
    url = url.rstrip("/") + "/"
    ns = {"a": "http://www.w3.org/2005/Atom"}
    feed = ET.fromstring(get(url.rsplit("/", 2)[0] + "/feed/"))
    for e in feed.findall("a:entry", ns):
        link = e.find("a:link", ns).get("href").rstrip("/") + "/"
        if link == url:
            p = Text()
            p.feed(e.find("a:content", ns).text)
            body = p.text()
            return dict(id=url.rstrip("/").rsplit("/", 1)[1], url=url, medium="blog",
                        author="Andrej Karpathy", published=e.find("a:published", ns).text[:10],
                        title=e.find("a:title", ns).text,
                        duration_or_length=f"{len(body.split())} words"), body
    sys.exit(f"{url} not in feed")


def main(medium, ref):
    manifest = json.loads(MANIFEST.read_text())
    meta, body = {"youtube": youtube, "x": x, "github": github, "blog": blog}[medium](ref)
    if any(i["id"] == meta["id"] for i in manifest["items"]):
        print(f"skip {meta['id']}: already in manifest")
        return
    meta["fetched"] = dt.date.today().isoformat()
    order = ["id", "url", "medium", "author", "published", "fetched", "title", "duration_or_length"]
    fm = yaml.safe_dump({k: meta[k] for k in order}, sort_keys=False, allow_unicode=True)
    path = RAW / FOLDER[medium] / f"{meta['id']}.md"
    text = f"---\n{fm}---\n\n{body.strip()}\n"
    path.write_text(text, encoding="utf-8")
    manifest["items"].append(dict(id=meta["id"], url=meta["url"], medium=medium,
                                  published=meta["published"], path=str(path.relative_to(ROOT)),
                                  sha256=hashlib.sha256(text.encode()).hexdigest()))
    manifest["items"].sort(key=lambda i: (i["published"], i["id"]))
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"wrote {path.relative_to(ROOT)} ({meta['duration_or_length']})")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
