#!/usr/bin/env python3
"""The coverage queue (raw/_queue.json): seed it from leads, edit it, check it.

  seed                     scan every raw file for links to his posts, videos and repos
  add <ref> --medium M     add an item by hand (e.g. a talk found elsewhere)
  set <ref> [--status S] [--reason R] [--medium M] [--priority P]
  check                    exit 1 if the queue is inconsistent

Links are classified: his own posts, videos and repos become `pending`; known third-party
sites are dropped; links that could be his own writing elsewhere
(his domains, gists, Medium) become `pending` with reason `needs-triage` and medium
`unknown`, for a person to decide; everything else (products, papers, docs) is dropped.
"""
import argparse
import re
import sys
import urllib.parse

import rawstore as rs

URL = re.compile(r"https?://[^\s)\]>\"'}]+")
THIRD_PARTY = {"pytorch.org", "huggingface.co", "numpy.org", "docs.astral.sh", "lambda.ai",
               "lambdalabs.com", "discord.com", "discord.gg", "dcbadge.vercel.app",
               "deepwiki.com", "openwebtext2.readthedocs.io", "arxiv.org", "wikipedia.org",
               "en.wikipedia.org", "openai.com", "google.com", "colab.research.google.com",
               "pypi.org", "docs.python.org", "t.co", "pbs.twimg.com", "imgur.com",
               "i.imgur.com"}
DATA_HOSTS = {"raw.githubusercontent.com", "llmc.s3-us-west-2.amazonaws.com"}


def classify(url):
    """(medium, ref) for a lead, ("unknown", url) for triage, or None to drop."""
    url = url.rstrip(".,;:!?")
    u = urllib.parse.urlparse(url)
    host = u.netloc.lower().removeprefix("www.").removeprefix("m.")
    parts = [p for p in u.path.split("/") if p]
    if host in ("x.com", "twitter.com"):
        if len(parts) >= 3 and parts[0].lower() == "karpathy" and parts[1] == "status":
            return "x", re.match(r"\d+", parts[2]).group()
        return None
    if host in ("youtube.com", "youtu.be"):
        q = urllib.parse.parse_qs(u.query)
        vid = (q.get("v") or [None])[0] if host == "youtube.com" else (parts or [None])[0]
        if host == "youtube.com" and len(parts) == 2 and parts[0] in ("live", "embed",
                                                                      "shorts"):
            vid = parts[1]
        return ("youtube", vid) if vid and re.fullmatch(r"[\w-]{11}", vid) else None
    if host == "github.com":
        if len(parts) < 2 or parts[0].lower() != "karpathy":
            return None
        repo = "karpathy/" + re.match(r"[\w.-]*", parts[1]).group().removesuffix(".git")
        if len(parts) == 2 or parts[2] in ("tree", "blob"):
            return "github", repo
        if parts[2] == "discussions" and len(parts) > 3 and parts[3].isdigit():
            return "github", f"{repo}/discussions/{parts[3]}"
        return None  # issues, pulls, discussion lists: not his authored text
    if host == "karpathy.bearblog.dev":
        if not parts or parts[0] in ("blog", "feed"):
            return None
        return "blog", f"https://karpathy.bearblog.dev/{parts[0]}/"
    if host == "karpathy.github.io":
        return ("blog", f"https://karpathy.github.io{u.path}") if len(parts) >= 4 else None
    if host in THIRD_PARTY or any(host.endswith("." + d) for d in THIRD_PARTY):
        return None
    # only links that could be his own writing go to a person: his domains, his gists,
    # his Medium; data files and downloads are not sources
    if host in DATA_HOSTS or "karpathy-public" in host or re.search(r"\.(bin|log|zip|txt|sh)$",
                                                                     u.path):
        return None
    if host == "gist.github.com" and parts[:1] == ["karpathy"] and len(parts) > 1:
        return "github", f"gist/{parts[1]}"
    if "karpathy" in host:
        return "unknown", url
    return None


def seed(q):
    # drop triage items the current rules would drop or now classify as a known medium
    for i in list(q.items.values()):
        if (i["medium"], i["status"], i["reason"]) == ("unknown", "pending", "needs-triage") \
                and i["found_in"].startswith("raw/") \
                and classify(i["ref"]) != ("unknown", i["ref"]):
            q.drop(i["ref"])
    added = 0
    for f in sorted(rs.raw().rglob("*.md")):
        text = f.read_text(encoding="utf-8")
        for url in URL.findall(text):
            c = classify(url)
            if c is None:
                continue
            medium, ref = c
            if q.get(ref) is None:
                added += 1
            q.add(ref, medium=medium, url=url if medium == "unknown" else lead_url(medium, ref),
                  priority=rs.priority(medium, ref, "") if medium == "github" else "other",
                  found_in=str(f.relative_to(rs.ROOT)))
            if medium == "unknown" and q.get(ref)["status"] == "pending":
                q.set(ref, reason=q.get(ref)["reason"] or "needs-triage")
    return added


def lead_url(medium, ref):
    return {"x": f"https://x.com/karpathy/status/{ref}",
            "youtube": f"https://www.youtube.com/watch?v={ref}",
            "github": f"https://github.com/{ref}"}.get(medium, ref)


def check(q):
    problems = []
    manifest = rs.read_manifest()
    for i in q.items.values():
        if i["status"] not in rs.STATUS:
            problems.append(f"bad status: {i['ref']} {i['status']!r}")
        if i["status"] == "excluded" and not i["reason"]:
            problems.append(f"excluded without a reason: {i['ref']}")
        # "unknown" is fine while awaiting triage, or once triage decided it is not his
        if i["medium"] not in rs.MEDIA and not (i["medium"] == "unknown" and (
                i["reason"] == "needs-triage" or i["status"] == "excluded")):
            problems.append(f"bad medium: {i['ref']} {i['medium']!r}")
    # `collected` must agree with the manifest in both directions
    derived = {k: dict(v) for k, v in q.items.items()}
    rs.derive(derived, manifest)
    for k, i in derived.items():
        if k not in q.items:
            problems.append(f"in manifest, missing from queue: {i['ref']}")
        elif i["status"] != q.items[k]["status"]:
            problems.append(f"status disagrees with manifest: {i['ref']} "
                            f"({q.items[k]['status']}, manifest says {i['status']})")
    for p in problems:
        print(p)
    print(f"{len(q.items)} queue items, {len(problems)} problems")
    return 1 if problems else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("seed")
    sub.add_parser("check")
    for name in ("add", "set"):
        s = sub.add_parser(name)
        s.add_argument("ref")
        s.add_argument("--medium", choices=sorted(rs.MEDIA | {"unknown"}))
        s.add_argument("--status", choices=sorted(rs.STATUS))
        s.add_argument("--reason")
        s.add_argument("--priority", choices=["teaching", "other"])
        s.add_argument("--title")
        s.add_argument("--url")
        s.add_argument("--published")
    args = ap.parse_args(argv)
    q = rs.Queue()
    if args.cmd == "check":
        return check(q)
    if args.cmd == "seed":
        n = seed(q)
        q.save()
        print(f"seeded {n} new items from raw/ leads")
        return 0
    fields = {k: v for k in ("medium", "status", "reason", "priority", "title", "url",
                             "published") if (v := getattr(args, k)) is not None}
    if args.cmd == "add":
        q.add(args.ref, found_in="manual", **fields)
        if {"status", "reason", "priority"} & set(fields):
            q.set(args.ref, **{k: fields[k] for k in ("status", "reason", "priority")
                               if k in fields})
    else:
        if q.get(args.ref) is None:
            sys.exit(f"{args.ref} is not in the queue (use add)")
        q.set(args.ref, **fields)
    q.save()
    print(q.get(args.ref))
    return 0


if __name__ == "__main__":
    sys.exit(main())
