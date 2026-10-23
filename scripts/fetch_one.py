#!/usr/bin/env python3
"""Fetch one source into raw/, or rebuild raw/ from the manifest.

The per-medium collectors (`collect_*.py`) do the bulk work; this is for one-off items and
for `--restore`. The manifest records how each file was fetched (`ref`, plus the pinned
`commit` for GitHub) and a sha256 of the body, so a fresh checkout can rebuild raw/.
Restoring re-downloads from the original URL: GitHub is exact (pinned commit); other
media are only as stable as the source, and a hash mismatch is reported, not hidden.

Usage:
  python scripts/fetch_one.py youtube <video_id>
  python scripts/fetch_one.py x <tweet_id>[,<tweet_id>...]   # a thread, in order
  python scripts/fetch_one.py github <owner/repo>|<owner/repo/discussions/N>
  python scripts/fetch_one.py blog <post url>
  python scripts/fetch_one.py talk <video_id>|<transcript page url>
  python scripts/fetch_one.py --restore      # rebuild every missing raw file
"""
import sys

import collect_blog
import collect_github
import collect_talks
import collect_x
import collect_youtube
import rawstore as rs
from rawstore import Text, digest  # noqa: F401  (re-exported for callers and tests)

FETCHERS = {"youtube": collect_youtube.fetch, "x": collect_x.fetch,
            "github": collect_github.fetch, "blog": collect_blog.fetch,
            "talk": collect_talks.fetch}


def fetch(medium, ref, commit=None):
    return FETCHERS[medium](ref, commit)


def restore():
    return rs.restore(lambda *a: fetch(*a))


def main(medium, ref):
    meta, body = fetch(medium, ref)
    known = next((i for i in rs.read_manifest()["items"] if i["id"] == meta["id"]), None)
    if known and (rs.ROOT / known["path"]).exists():
        print(f"skip {meta['id']}: already fetched (use --restore for missing files)")
        return
    path = rs.save(meta, body, ref)
    q = rs.Queue()
    q.add(ref.split(",")[0], medium=medium, url=meta["url"], title=meta["title"],
          published=meta["published"], found_in="fetch_one")
    q.save()
    print(f"wrote {path} ({meta['duration_or_length']})")


if __name__ == "__main__":
    if sys.argv[1:] == ["--restore"]:
        sys.exit(restore())
    main(sys.argv[1], sys.argv[2])
