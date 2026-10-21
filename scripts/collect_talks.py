#!/usr/bin/env python3
"""Collect talks, podcasts and interviews hosted by someone else (`medium: talk`).

There is no single feed, so this works from the coverage queue only: items reach it from
leads in other sources or are added by hand with `coverage_queue.py add`. A YouTube upload
gets captions like his own videos; any other page is kept only if it carries a transcript.

Usage: python scripts/collect_talks.py [--dry-run] [--limit N] [--priority teaching]
"""
import re
import sys
import urllib.parse

import collect_youtube as yt
import rawstore as rs
from rawstore import Skip

MIN_WORDS = 1500  # shorter pages are show notes, not transcripts
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


def main(argv=None):
    args = rs.parser(__doc__).parse_args(argv)
    return rs.collect(rs.Queue(), "talk", fetch_item, args)


if __name__ == "__main__":
    sys.exit(main())
