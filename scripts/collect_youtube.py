#!/usr/bin/env python3
"""Collect videos from his YouTube channel: captions in ~30-second [mm:ss] blocks.

Discovers the channel's video list with yt-dlp, then fetches captions with
youtube-transcript-api for every pending video, teaching material first. Videos linked
from other sources that turn out to be on another channel become `talk` items for triage.

Usage: python scripts/collect_youtube.py [--dry-run] [--limit N] [--priority teaching]
"""
import json
import sys

import rawstore as rs
from rawstore import Skip

CHANNEL_ID = "UCXUPKJO5MZQN11PqgIvyuvQ"
CHANNEL = "https://www.youtube.com/@AndrejKarpathy/videos"
YT = [sys.executable, "-m", "yt_dlp", "--no-warnings"]


def url(vid):
    return f"https://www.youtube.com/watch?v={vid}"


def listing():
    return json.loads(rs.run(YT + ["--flat-playlist", "-J", CHANNEL]))["entries"]


def metadata(vid):
    return json.loads(rs.run(YT + ["-j", "--skip-download", url(vid)]))


def captions(vid):
    from youtube_transcript_api import YouTubeTranscriptApi
    from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled
    try:
        return YouTubeTranscriptApi().fetch(vid, languages=["en"])
    except (NoTranscriptFound, TranscriptsDisabled):
        raise Skip("pending", "no-transcript")


def blocks(snippets):
    # one block per ~30 s so citations can point at mm:ss without a line per caption
    out, cur, start = [], [], None
    for sn in snippets:
        if start is None:
            start = sn.start
        cur.append(sn.text.replace("\n", " "))
        if sn.start - start >= 30:
            out.append(f"[{rs.stamp(start)}] {' '.join(cur)}")
            cur, start = [], None
    if cur:
        out.append(f"[{rs.stamp(start)}] {' '.join(cur)}")
    return "\n\n".join(out)


def published(meta):
    d = meta["upload_date"]
    return f"{d[:4]}-{d[4:6]}-{d[6:]}"


def video(vid, medium="youtube", meta=None):
    """Captions and metadata for one video. Also used by the talks collector."""
    meta = meta or metadata(vid)
    body = blocks(captions(vid))
    return dict(id=vid, url=url(vid), medium=medium, author="Andrej Karpathy",
                published=published(meta), title=meta["title"],
                duration_or_length=rs.stamp(meta["duration"])), body


def fetch(ref, commit=None):
    return video(ref)


def fetch_item(item, since):
    meta = metadata(item["ref"])
    if meta.get("channel_id") != CHANNEL_ID:
        # linked from one of his posts but uploaded elsewhere: a talk, or not him at all
        raise Skip("pending", "needs-triage", medium="talk", title=meta.get("title", ""),
                   published=published(meta))
    if not rs.in_scope(published(meta), item["priority"], since):
        # the listing has no dates; check before downloading captions
        raise Skip("excluded", f"before-{since[:4]}", published=published(meta))
    return video(item["ref"], meta=meta)


def main(argv=None):
    args = rs.parser(__doc__).parse_args(argv)
    q = rs.Queue()
    for e in listing():
        q.add(e["id"], medium="youtube", url=url(e["id"]), title=e.get("title") or "",
              priority=rs.priority("youtube", e["id"], e.get("title")),
              found_in="discovery:youtube")
    if not args.dry_run:
        q.save()
    return rs.collect(q, "youtube", fetch_item, args)


if __name__ == "__main__":
    sys.exit(main())
