#!/usr/bin/env python3
"""Collect his blog posts: karpathy.bearblog.dev (current) and karpathy.github.io (old).

The bearblog Atom feed only holds the latest posts, so discovery reads the post list page.
A post's body comes from the feed while it is there (as in phase 1, so hashes stay
comparable), otherwise from the post page. Link targets are kept: they are leads.

Usage: python scripts/collect_blog.py [--dry-run] [--limit N] [--priority teaching]
"""
import re
import sys
import xml.etree.ElementTree as ET

import rawstore as rs

BEAR = "https://karpathy.bearblog.dev"
OLD = "https://karpathy.github.io"
ATOM = {"a": "http://www.w3.org/2005/Atom"}


def bear_listing():
    html = rs.get(f"{BEAR}/blog/")
    for date, href, title in re.findall(
            r'<time datetime="(\d{4}-\d{2}-\d{2})[^"]*"[^>]*>.*?</time>(?:\s*</?\w+>)*\s*'
            r'<a href="(/[^"]+/)"[^>]*>(.*?)</a>', html, re.S):
        yield f"{BEAR}{href}", date, rs.html_text(title, BEAR)


def old_listing():
    feed = ET.fromstring(rs.get(f"{OLD}/feed.xml"))
    for item in feed.iter("item"):
        date = item.findtext("pubDate", "")
        m = re.search(r"(\d{1,2}) (\w{3}) (\d{4})", date)
        months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
        iso = f"{m.group(3)}-{months.index(m.group(2)) + 1:02d}-{int(m.group(1)):02d}" if m else ""
        yield item.findtext("link").strip(), iso, item.findtext("title", "")


def slug(url):
    return url.rstrip("/").rsplit("/", 1)[1].removesuffix(".html")


def from_feed(url):
    feed = ET.fromstring(rs.get(url.rsplit("/", 2)[0] + "/feed/"))
    for e in feed.findall("a:entry", ATOM):
        if e.find("a:link", ATOM).get("href").rstrip("/") + "/" == url:
            body = rs.html_text(e.find("a:content", ATOM).text, url)
            return dict(id=slug(url), url=url, medium="blog", author="Andrej Karpathy",
                        published=e.find("a:published", ATOM).text[:10],
                        title=e.find("a:title", ATOM).text,
                        duration_or_length=f"{len(body.split())} words"), body
    return None


def from_page(url):
    html = rs.get(url)
    body = rs.html_text(rs.region(html), url)
    title = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    # bearblog pages carry <time datetime>; old github.io posts are dated by their URL
    date = re.search(r'datetime="(\d{4}-\d{2}-\d{2})', html)
    in_url = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", url)
    published = date.group(1) if date else "-".join(in_url.groups()) if in_url else ""
    return dict(id=slug(url), url=url, medium="blog", author="Andrej Karpathy",
                published=published,
                title=rs.html_text(title.group(1), url).split(" | ")[0] if title else slug(url),
                duration_or_length=f"{len(body.split())} words"), body


def fetch(ref, commit=None):
    url = ref if ref.endswith(".html") else ref.rstrip("/") + "/"
    return (url.startswith(BEAR) and from_feed(url)) or from_page(url)


def fetch_item(item, since):
    return fetch(item["ref"])


def main(argv=None):
    args = rs.parser(__doc__).parse_args(argv)
    q = rs.Queue()
    for listing in (bear_listing, old_listing):
        for url, date, title in listing():
            q.add(url, medium="blog", url=url, title=title, published=date,
                  priority=rs.priority("blog", url, title), found_in="discovery:blog")
    if not args.dry_run:
        q.save()
    return rs.collect(q, "blog", fetch_item, args)


if __name__ == "__main__":
    sys.exit(main())
