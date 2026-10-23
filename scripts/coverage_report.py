#!/usr/bin/env python3
"""Write the coverage report: what was collected, what is pending, what was left out.

Reads raw/_queue.json and raw/_manifest.json; writes
specs/phases/phase-2-collectors-and-backfill/coverage.md (or --out).

Usage: python scripts/coverage_report.py [--out PATH]
"""
import argparse
import collections
import datetime as dt
from pathlib import Path

import rawstore as rs

OUT = rs.ROOT / "specs/phases/phase-2-collectors-and-backfill/coverage.md"
MEDIA = ["youtube", "github", "blog", "talk", "x", "unknown"]


def row(cells):
    return "| " + " | ".join(str(c) for c in cells) + " |"


def report(q, manifest):
    items = list(q.items.values())
    by = collections.Counter((i["medium"], i["status"]) for i in items)
    out = [f"# Coverage report", "",
           f"_Generated {dt.date.today().isoformat()} by `scripts/coverage_report.py` from "
           f"`raw/_queue.json` and `raw/_manifest.json`. Do not edit by hand._", "",
           f"{len(manifest['items'])} raw files in the manifest; {len(items)} items in the "
           "queue.", "", "## By medium", "",
           row(["medium", "collected", "pending", "excluded", "raw files"]),
           row(["---"] * 5)]
    files = collections.Counter(e["medium"] for e in manifest["items"])
    for m in MEDIA:
        if any(k[0] == m for k in by) or files[m]:
            out.append(row([m, by[m, "collected"], by[m, "pending"], by[m, "excluded"],
                            files[m]]))

    out += ["", "## Teaching material", "",
            row(["medium", "collected", "pending", "excluded"]), row(["---"] * 4)]
    t = collections.Counter((i["medium"], i["status"]) for i in items
                            if i["priority"] == "teaching")
    for m in MEDIA:
        if any(k[0] == m for k in t):
            out.append(row([m, t[m, "collected"], t[m, "pending"], t[m, "excluded"]]))

    years = sorted({str(e["published"])[:4] for e in manifest["items"]})
    out += ["", "## Raw files by year", "", row(["medium"] + years), row(["---"] * (len(years) + 1))]
    y = collections.Counter((e["medium"], str(e["published"])[:4]) for e in manifest["items"])
    for m in MEDIA:
        if files[m]:
            out.append(row([m] + [y[m, yr] for yr in years]))

    def listing(rows):
        return [row(["medium", "ref", "title", "published", "priority", "reason", "found in"]),
                row(["---"] * 7)] + [
            row([i["medium"], f"`{i['ref']}`", i["title"].replace("|", "/")[:70],
                 i["published"], i["priority"], i["reason"], i["found_in"]]) for i in rows]

    order = lambda i: (i["medium"], i["priority"] != "teaching", str(i["published"]), i["ref"])
    pending = sorted((i for i in items if i["status"] == "pending"), key=order)
    out += ["", f"## Pending ({len(pending)})", "",
            "Known but not fetched. `needs-triage`: a person decides whether it is his and "
            "which medium; `no-transcript`: no captions or transcript found.", ""]
    out += listing(pending) if pending else ["None."]

    excluded = [i for i in items if i["status"] == "excluded"]
    reasons = collections.Counter((i["medium"], i["reason"].split(" ")[0]) for i in excluded)
    out += ["", f"## Excluded ({len(excluded)})", "", row(["medium", "reason", "count"]),
            row(["---"] * 3)]
    out += [row([m, r, n]) for (m, r), n in sorted(reasons.items())]
    # X can have thousands of excluded replies; list the other media in full
    full = sorted((i for i in excluded if i["medium"] != "x"), key=order)
    if full:
        out += ["", "### Excluded items (except X)", ""] + listing(full)

    collected = sorted((i for i in items if i["status"] == "collected"), key=order)
    out += ["", f"## Collected ({len(collected)})", ""] + listing(collected)
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=OUT)
    args = ap.parse_args(argv)
    args.out.write_text(report(rs.Queue(), rs.read_manifest()))
    print(f"wrote {args.out.relative_to(rs.ROOT) if args.out.is_relative_to(rs.ROOT) else args.out}")


if __name__ == "__main__":
    main()
