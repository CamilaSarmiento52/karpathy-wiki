#!/usr/bin/env python3
"""Phase 3 batch bookkeeping: which raw file is in which ingest batch, and how far along it is.

Batches are assigned from `raw/_manifest.json` by `published` date, so the split is
reproducible. Status per source: raw file present, digest in `staging/digests/`, source
page in `wiki/sources/` (matched by `raw_path`), verified (listed in a report under
`staging/verify/`).

Usage:
  python3 scripts/batches.py                 # summary per batch
  python3 scripts/batches.py --batch 1       # one line per source in batch 1
  python3 scripts/batches.py --batch 1 --json
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
# first `published` date of batches 2, 3 and 4; everything before the first is batch 1
BOUNDARIES = [dt.date(2023, 2, 1), dt.date(2024, 8, 1), dt.date(2025, 10, 20)]
LINK = re.compile(r"\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]")


def batch_of(published):
    d = dt.date.fromisoformat(str(published))
    return 1 + sum(d >= b for b in BOUNDARIES)


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    try:
        return yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return {}


def slug_for(item):
    """Digest file stem: the raw file's stem, so it needs no lookup."""
    return Path(item["path"]).stem


def status(root=ROOT):
    manifest = json.loads((root / "raw" / "_manifest.json").read_text())["items"]
    source_pages = {}
    for p in (root / "wiki" / "sources").glob("*.md"):
        meta = frontmatter(p)
        if meta.get("raw_path"):
            source_pages[str(meta["raw_path"])] = p.stem
    verified = set()
    for p in (root / "staging" / "verify").glob("*.md"):
        verified.update(LINK.findall(p.read_text(encoding="utf-8")))
    rows = []
    for item in sorted(manifest, key=lambda i: (str(i["published"]), i["path"])):
        page = source_pages.get(item["path"])
        rows.append({
            "batch": batch_of(item["published"]),
            "published": str(item["published"]),
            "medium": item["medium"],
            "id": item["id"],
            "path": item["path"],
            "raw": (root / item["path"]).exists(),
            "digest": (root / "staging" / "digests" / f"{slug_for(item)}.md").exists(),
            "source_page": page,
            "verified": bool(page and page in verified),
        })
    return rows


def summary(rows):
    out = {}
    for r in rows:
        s = out.setdefault(r["batch"], {"sources": 0, "raw": 0, "digest": 0, "source_page": 0,
                                         "verified": 0})
        s["sources"] += 1
        s["raw"] += r["raw"]
        s["digest"] += r["digest"]
        s["source_page"] += bool(r["source_page"])
        s["verified"] += r["verified"]
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--batch", type=int)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    rows = status(args.root)
    if args.batch:
        rows = [r for r in rows if r["batch"] == args.batch]
        if args.json:
            print(json.dumps(rows, indent=1))
            return 0
        for r in rows:
            flags = ("raw " if r["raw"] else "--- ") + ("digest " if r["digest"] else "------ ")
            flags += (f"page:{r['source_page']} " if r["source_page"] else "no-page ")
            flags += "verified" if r["verified"] else ""
            print(f"{r['published']} {r['medium']:7} {r['id']:45} {flags}")
        return 0
    s = summary(rows)
    if args.json:
        print(json.dumps(s, indent=1))
        return 0
    print("batch  sources  raw  digests  source pages  verified")
    for b in sorted(s):
        x = s[b]
        print(f"{b:>5}  {x['sources']:>7}  {x['raw']:>3}  {x['digest']:>7}  {x['source_page']:>12}  {x['verified']:>8}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
