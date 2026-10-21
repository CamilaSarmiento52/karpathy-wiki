#!/usr/bin/env python3
"""Fetch one source into raw/ with standard frontmatter and a manifest entry.

Phase 1 helper for hand-picked sources; phase 2 replaces it with per-medium collectors.

The manifest records how each file was fetched (`ref`, plus the pinned `commit` for
GitHub) and a sha256 of the body, so a fresh checkout can rebuild raw/ with --restore.
Restoring re-downloads from the original URL: GitHub is exact (pinned commit); other
media are only as stable as the source, and a hash mismatch is reported, not hidden.

Usage:
  python scripts/fetch_one.py youtube <video_id>
  python scripts/fetch_one.py x <tweet_id>
  python scripts/fetch_one.py github <owner/repo>
  python scripts/fetch_one.py blog <bearblog post url>
  python scripts/fetch_one.py --restore      # rebuild every missing raw file
"""
import datetime as dt
import hashlib
import json
import re
import subprocess
import sys
import urllib.parse
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
    """HTML to plain text, keeping paragraph breaks, headings, list bullets and links."""
    BLOCK = {"p", "div", "br", "li", "h1", "h2", "h3", "h4", "pre", "blockquote", "tr"}

    def __init__(self, base):
        super().__init__()
        self.out, self.base, self.href = [], base, None

    def handle_starttag(self, tag, attrs):
        if tag in self.BLOCK:
            self.out.append("\n\n")
        if tag in ("h1", "h2", "h3", "h4"):
            self.out.append("#" * int(tag[1]) + " ")
        if tag == "li":
            self.out.append("- ")
        if tag == "a" and dict(attrs).get("href"):
            # keep link targets: they are leads to his other posts
            self.href = urllib.parse.urljoin(self.base, dict(attrs)["href"])
            self.out.append("[")

    def handle_endtag(self, tag):
        if tag == "a" and self.href:
            self.out.append(f"]({self.href})")
            self.href = None

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


def gh(path, raw=False):
    cmd = ["gh", "api", path] + (["-H", "Accept: application/vnd.github.raw"] if raw else [])
    out = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
    return out if raw else json.loads(out)


def github(repo, commit=None):
    info = gh(f"repos/{repo}")
    # a README is a living document: pin it to the last commit that touched it, and date it
    # by that commit, so the snapshot can be fetched again exactly
    if commit is None:
        commit = gh(f"repos/{repo}/commits?path=README.md&per_page=1")[0]["sha"]
    c = gh(f"repos/{repo}/commits/{commit}")
    readme = gh(f"repos/{repo}/readme?ref={commit}", raw=True)
    return dict(id=repo.replace("/", "__"), url=info["html_url"], medium="github",
                author="Andrej Karpathy", published=c["commit"]["committer"]["date"][:10],
                title=f"{info['name']} README", duration_or_length=f"{len(readme.split())} words",
                commit=commit), readme


def blog(url):
    url = url.rstrip("/") + "/"
    ns = {"a": "http://www.w3.org/2005/Atom"}
    feed = ET.fromstring(get(url.rsplit("/", 2)[0] + "/feed/"))
    for e in feed.findall("a:entry", ns):
        link = e.find("a:link", ns).get("href").rstrip("/") + "/"
        if link == url:
            p = Text(url)
            p.feed(e.find("a:content", ns).text)
            body = p.text()
            return dict(id=url.rstrip("/").rsplit("/", 1)[1], url=url, medium="blog",
                        author="Andrej Karpathy", published=e.find("a:published", ns).text[:10],
                        title=e.find("a:title", ns).text,
                        duration_or_length=f"{len(body.split())} words"), body
    sys.exit(f"{url} not in feed")


def digest(body):
    # hash the verbatim body only, so a refetch on another day (new `fetched`) still matches
    return hashlib.sha256(body.strip().encode()).hexdigest()


def fetch(medium, ref, commit=None):
    fn = {"youtube": youtube, "x": x, "github": github, "blog": blog}[medium]
    return fn(ref, commit) if medium == "github" else fn(ref)


def write(meta, body):
    meta["fetched"] = dt.date.today().isoformat()
    order = ["id", "url", "medium", "author", "published", "fetched", "title",
             "duration_or_length", "commit"]
    fm = yaml.safe_dump({k: meta[k] for k in order if k in meta}, sort_keys=False,
                        allow_unicode=True)
    path = RAW / FOLDER[meta["medium"]] / f"{meta['id']}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{fm}---\n\n{body.strip()}\n", encoding="utf-8")
    return path


def save(manifest):
    manifest["items"].sort(key=lambda i: (i["published"], i["id"]))
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")


def restore(manifest):
    """Rebuild missing raw files from the manifest; report any whose content changed."""
    changed = 0
    for item in manifest["items"]:
        if (ROOT / item["path"]).exists():
            continue
        meta, body = fetch(item["medium"], item["ref"], item.get("commit"))
        write(meta, body)
        same = digest(body) == item["sha256"]
        changed += not same
        print(f"restored {item['path']}" + ("" if same else " (CONTENT CHANGED since manifest)"))
    return 1 if changed else 0


def main(medium, ref):
    manifest = json.loads(MANIFEST.read_text())
    meta, body = fetch(medium, ref)
    known = next((i for i in manifest["items"] if i["id"] == meta["id"]), None)
    if known and (ROOT / known["path"]).exists():
        print(f"skip {meta['id']}: already fetched (use --restore for missing files)")
        return
    path = write(meta, body)
    entry = dict(id=meta["id"], ref=ref, url=meta["url"], medium=medium,
                 published=meta["published"], path=str(path.relative_to(ROOT)),
                 sha256=digest(body))
    if "commit" in meta:
        entry["commit"] = meta["commit"]
    manifest["items"] = [i for i in manifest["items"] if i["id"] != meta["id"]] + [entry]
    save(manifest)
    print(f"wrote {path.relative_to(ROOT)} ({meta['duration_or_length']})")


if __name__ == "__main__":
    if sys.argv[1:] == ["--restore"]:
        sys.exit(restore(json.loads(MANIFEST.read_text())))
    main(sys.argv[1], sys.argv[2])
