#!/usr/bin/env python3
"""Collect his X posts: one raw file per thread, posts in order.

Discovery needs a twitterapi.io key (`TWITTERAPI_IO_KEY` in .env): it lists his posts
since the cut-off, groups his own replies to himself into threads, and excludes retweets
and replies to other people (recorded in the queue with a reason). Post text always comes
from the free fxtwitter API, which returns long posts in full and needs no key, so a
thread can be restored from the manifest alone. `ref` is the thread's post ids, in order,
comma-separated.

Without a key, only posts already in the queue (leads from other sources) are fetched.

Usage: python scripts/collect_x.py [--dry-run] [--limit N] [--full]
"""
import datetime as dt
import json
import os
import sys
import urllib.parse

import rawstore as rs
from rawstore import Skip

USER = "karpathy"
SEARCH = "https://api.twitterapi.io/twitter/tweet/advanced_search"
THREADS = {}  # root id -> all post ids in the thread, filled by discovery


def api_key():
    if os.environ.get("TWITTERAPI_IO_KEY"):
        return os.environ["TWITTERAPI_IO_KEY"]
    env = rs.ROOT / ".env"
    for line in env.read_text().splitlines() if env.exists() else []:
        name, _, value = line.partition("=")
        if name.strip() == "TWITTERAPI_IO_KEY" and value.strip():
            return value.strip().strip("\"'")
    return None


def post(tid):
    t = json.loads(rs.get(f"https://api.fxtwitter.com/{USER}/status/{tid}"))["tweet"]
    return dict(id=tid, url=t["url"], text=t["text"], author=t["author"]["name"],
                handle=t["author"]["screen_name"], replying_to=t.get("replying_to"),
                published=dt.datetime.strptime(t["created_at"],
                                               "%a %b %d %H:%M:%S %z %Y").date().isoformat())


def thread(ids):
    posts = [post(i) for i in ids]
    first = posts[0]
    body = "\n\n---\n\n".join(p["text"] for p in posts)
    line = first["text"].split("\n", 1)[0]
    title = line if len(line) <= 80 else line[:80].rsplit(" ", 1)[0] + "…"
    return dict(id=ids[0], url=first["url"], medium="x", author=first["author"],
                published=first["published"], title=title,
                duration_or_length=f"{len(body.split())} words"), body, posts


def fetch(ref, commit=None):
    meta, body, _ = thread(ref.split(","))
    return meta, body


def search(key, since):
    """Every post from:karpathy since `since` (ISO date), newest first."""
    ts = int(dt.datetime.fromisoformat(since).replace(tzinfo=dt.timezone.utc).timestamp())
    query = urllib.parse.quote(f"from:{USER} since_time:{ts}")
    cursor = ""
    while True:
        page = json.loads(rs.get(f"{SEARCH}?query={query}&queryType=Latest&cursor="
                                 f"{urllib.parse.quote(cursor)}", {"X-API-Key": key}))
        yield from page["tweets"]
        if not page.get("has_next_page") or not page.get("next_cursor"):
            return
        cursor = page["next_cursor"]


def group(tweets):
    """Split search results into threads (his own reply chains), retweets and replies."""
    threads, excluded = {}, {}
    for t in tweets:
        if t.get("retweeted_tweet"):
            excluded[t["id"]] = "retweet"
        elif t.get("isReply") and (t.get("inReplyToUsername") or "").lower() != USER:
            excluded[t["id"]] = "reply-to-other"
        else:
            threads.setdefault(t.get("conversationId") or t["id"], []).append(t)
    out = {}
    for root, posts in threads.items():
        ids = sorted({p["id"] for p in posts}, key=int)
        if ids[0] != root:  # self-replies inside someone else's conversation
            for i in ids:
                excluded[i] = "reply-to-other"
            continue
        out[root] = ids
    return out, excluded


def discover(q, key, args):
    seen = [i["published"] for i in q.of("x") if i["found_in"] == "discovery:x"]
    # incremental: re-read a week before the newest post we know, unless --full
    since = args.since
    if seen and not args.full:
        since = max(since, (dt.date.fromisoformat(max(seen)) - dt.timedelta(days=7)).isoformat())
    tweets = list(search(key, since))
    threads, excluded = group(tweets)
    dates = {t["id"]: dt.datetime.strptime(t["createdAt"], "%a %b %d %H:%M:%S %z %Y")
             .date().isoformat() for t in tweets}
    for root, ids in threads.items():
        THREADS[root] = ids
        q.add(root, medium="x", url=f"https://x.com/{USER}/status/{root}",
              published=dates[root], found_in="discovery:x")
        for i in ids[1:]:  # later posts of a thread are covered by its root
            if q.get(i) and q.get(i)["status"] == "pending":
                q.set(i, status="excluded", reason=f"part-of-thread {root}")
    for tid, reason in excluded.items():
        if q.get(tid) is None:
            q.add(tid, medium="x", url=f"https://x.com/{USER}/status/{tid}",
                  published=dates[tid], found_in="discovery:x")
            q.set(tid, status="excluded", reason=reason)
    print(f"x: {len(tweets)} posts since {since}: {len(threads)} threads, "
          f"{len(excluded)} excluded")


def fetch_item(item, since):
    ids = THREADS.get(item["ref"], [item["ref"]])
    meta, body, posts = thread(ids)
    if posts[0]["handle"].lower() != USER:
        raise Skip("excluded", "not-karpathy")
    if posts[0]["replying_to"] and posts[0]["replying_to"].lower() != USER:
        raise Skip("excluded", "reply-to-other")
    if not body.strip():
        # an X Article: the text is not in the post; he usually also posts it on his blog
        raise Skip("pending", "no-text (X article)")
    meta["ref"] = ",".join(ids)  # the manifest records every post, so restore needs no key
    return meta, body


def main(argv=None):
    ap = rs.parser(__doc__)
    ap.add_argument("--full", action="store_true", help="re-read everything since --since")
    args = ap.parse_args(argv)
    q = rs.Queue()
    key = api_key()
    if key:
        discover(q, key, args)
        if not args.dry_run:
            q.save()
    else:
        print("x: no TWITTERAPI_IO_KEY in .env; skipping discovery, fetching known posts only")
    return rs.collect(q, "x", fetch_item, args)


if __name__ == "__main__":
    sys.exit(main())
