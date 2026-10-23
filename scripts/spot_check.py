#!/usr/bin/env python3
"""Print N random raw files for a human to compare against the originals (phase gate 2→3).

For each: path, URL, date, title, length, and the opening and closing lines of the body.
Check: right person, right date, body complete (not cut off), timestamps line up with the
video, thread posts in order.

Usage: python scripts/spot_check.py [-n 10] [--seed S]
"""
import argparse
import random

import rawstore as rs


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("-n", type=int, default=10)
    ap.add_argument("--seed", type=int, default=None)
    args = ap.parse_args(argv)
    items = [i for i in rs.read_manifest()["items"] if (rs.ROOT / i["path"]).exists()]
    rng = random.Random(args.seed)
    for i in rng.sample(items, min(args.n, len(items))):
        text = (rs.ROOT / i["path"]).read_text(encoding="utf-8")
        _, fm, body = text.split("---\n", 2)
        lines = [ln for ln in body.strip().splitlines() if ln.strip()]
        print(f"=== {i['path']}\n{fm.strip()}\n--- first lines")
        print("\n".join(ln[:200] for ln in lines[:3]))
        print("--- last lines")
        print("\n".join(ln[:200] for ln in lines[-2:]))
        print()


if __name__ == "__main__":
    main()
