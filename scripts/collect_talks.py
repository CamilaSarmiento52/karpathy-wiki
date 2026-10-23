#!/usr/bin/env python3
"""Collect talks, podcasts and interviews hosted by someone else (`medium: talk`).

There is no single feed. Items reach the queue from leads in other sources, by hand with
`coverage_queue.py add`, or from `--search`: YouTube searches for his name. Search results
are full of re-uploads, clips and videos about him, so every new result is queued as
`needs-triage` (with its channel in `found_in`) and nothing is collected until a person
approves it with `coverage_queue.py set <id> --reason ""` or excludes it.

A YouTube upload gets captions like his own videos; any other page is kept only if it
carries a transcript.

Usage: python scripts/collect_talks.py [--search] [--dry-run] [--limit N] [--priority teaching]
"""
import re
import sys
import urllib.parse

import collect_youtube as yt
import rawstore as rs
from rawstore import Skip

MIN_WORDS = 1500  # shorter pages are show notes, not transcripts
MIN_SECONDS = 15 * 60  # shorter videos are clips and trailers
SEARCHES = ["Andrej Karpathy", "Andrej Karpathy interview", "Andrej Karpathy podcast",
            "Andrej Karpathy lecture", "Andrej Karpathy talk", "Andrej Karpathy keynote",
            "Andrej Karpathy fireside chat", "Andrej Karpathy conversation"]
PER_SEARCH = 40
VIDEO_ID = re.compile(r"[\w-]{11}")


def page(url):
    html = rs.get(url)
    body = rs.html_text(rs.region(html), url)
    if len(body.split()) < MIN_WORDS:
        raise Skip("pending", "no-transcript")
    title = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    date = re.search(r'(?:article:published_time"\s+content|datetime)="(\d{4}-\d{2}-\d{2})',
                     html)
    if not date:
        raise Skip("pending", "no-date")
    u = urllib.parse.urlparse(url)
    slug = re.sub(r"[^\w-]+", "-", f"{u.netloc}{u.path}".strip("/")).strip("-").lower()
    return dict(id=slug, url=url, medium="talk", author="Andrej Karpathy",
                published=date.group(1),
                title=rs.html_text(title.group(1), url) if title else slug,
                duration_or_length=f"{len(body.split())} words"), body


def fetch(ref, commit=None):
    return yt.video(ref, medium="talk") if VIDEO_ID.fullmatch(ref) else page(ref)


def fetch_item(item, since):
    return fetch(item["ref"])


def search(query, n=PER_SEARCH):
    out = rs.run(yt.YT + ["--flat-playlist", "--print",
                          "%(id)s\t%(channel_id)s\t%(channel)s\t%(duration)s\t%(title)s",
                          f"ytsearch{n}:{query}"])
    for line in out.splitlines():
        vid, channel_id, channel, duration, title = line.split("\t", 4)
        yield dict(id=vid, channel_id=channel_id, channel=channel, title=title,
                   duration=float(duration) if duration not in ("NA", "None", "") else 0)


def candidates(results):
    """Long videos with his name in the title, not on his own channel."""
    seen = {}
    for r in results:
        if (r["channel_id"] != yt.CHANNEL_ID and r["duration"] >= MIN_SECONDS
                and "karpathy" in r["title"].lower()):
            seen.setdefault(r["id"], r)
    return list(seen.values())


def discover(q):
    found = candidates(r for query in SEARCHES for r in search(query))
    new = 0
    for r in found:
        if q.get(r["id"]) is None:
            new += 1
            q.add(r["id"], medium="talk", url=yt.url(r["id"]), title=r["title"],
                  found_in=f"search: {r['channel']} ({rs.stamp(r['duration'])})")
            q.set(r["id"], reason="needs-triage")
    print(f"talks: {len(found)} candidates from {len(SEARCHES)} searches, {new} new for triage")


def main(argv=None):
    ap = rs.parser(__doc__)
    ap.add_argument("--search", action="store_true", help="search YouTube for new candidates")
    args = ap.parse_args(argv)
    q = rs.Queue()
    if args.search:
        discover(q)
        if not args.dry_run:
            q.save()
    return rs.collect(q, "talk", fetch_item, args)


if __name__ == "__main__":
    sys.exit(main())
