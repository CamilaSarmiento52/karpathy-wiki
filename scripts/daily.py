#!/usr/bin/env python3
"""Weekday collection run: fetch anything new, report it, no model involved.

1. Runs each collector as its own process (one failing never stops the others):
   youtube, github, blog, talks (queued items; `--search` only with --weekly), x (queued
   posts only unless TWITTERAPI_IO_KEY is set; the collector decides).
2. Compares the manifest and the coverage queue with the last run's state
   (`reports/state.json`): new raw files to ingest, new items waiting for triage.
3. Writes `reports/collect-YYYY-MM-DD.json` and updates the state.

Prints `new raw files: N` last. With nothing new the scheduled job stops there and no
model is started. Rate limits and network errors are reported per collector, not raised.

Usage: python3 scripts/daily.py [--weekly] [--root PATH] [--date YYYY-MM-DD] [--skip NAME]
"""
import argparse
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLLECTORS = ["youtube", "github", "blog", "talks", "x"]


def run_collector(root, name, weekly):
    cmd = [sys.executable, str(root / "scripts" / f"collect_{name}.py")]
    if name == "talks" and weekly:
        cmd.append("--search")
    try:
        p = subprocess.run(cmd, cwd=root, capture_output=True, text=True, timeout=1800)
        out = (p.stdout + p.stderr).strip().splitlines()
        return {"exit": p.returncode, "tail": out[-8:]}
    except Exception as e:  # noqa: BLE001  a collector crash is a report line, not a stop
        return {"exit": -1, "tail": [f"{type(e).__name__}: {e}"]}


def manifest_paths(root):
    f = root / "raw" / "_manifest.json"
    items = json.loads(f.read_text())["items"] if f.exists() else []
    return {i["path"]: i for i in items}


def triage_refs(root):
    f = root / "raw" / "_queue.json"
    if not f.exists():
        return {}
    data = json.loads(f.read_text())
    items = data.get("items", data) if isinstance(data, dict) else data
    if isinstance(items, dict):
        items = list(items.values())
    return {i["ref"]: i for i in items
            if isinstance(i, dict) and i.get("status") == "pending" and i.get("reason") == "needs-triage"}


def pending_reasons(tail):
    """Lines a collector prints for items it left pending (rate limits, missing captions)."""
    return [l for l in tail if l.startswith("pending ")]


def main(argv=None, runner=run_collector):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--weekly", action="store_true", help="also search for new talk candidates")
    ap.add_argument("--date", default=dt.date.today().isoformat())
    ap.add_argument("--skip", action="append", default=[], choices=COLLECTORS)
    args = ap.parse_args(argv)
    root = args.root
    state_f = root / "reports" / "state.json"
    state = json.loads(state_f.read_text()) if state_f.exists() else {}
    known = set(state.get("raw_paths", manifest_paths(root)))
    known_triage = set(state.get("triage_refs", triage_refs(root)))

    collectors = {}
    for name in COLLECTORS:
        if name in args.skip:
            continue
        collectors[name] = runner(root, name, args.weekly)

    manifest = manifest_paths(root)
    new = sorted((p for p in manifest if p not in known),
                 key=lambda p: (str(manifest[p].get("published")), p))
    triage = triage_refs(root)
    new_triage = sorted(r for r in triage if r not in known_triage)
    report = {
        "date": args.date,
        "weekly": args.weekly,
        "new_raw": [{"path": p, "medium": manifest[p].get("medium"),
                     "published": str(manifest[p].get("published")), "url": manifest[p].get("url")}
                    for p in new],
        "new_triage": [{"ref": r, "title": triage[r].get("title"), "url": triage[r].get("url")}
                       for r in new_triage],
        "collectors": {n: {"ok": c["exit"] == 0, "pending": pending_reasons(c["tail"]),
                           "tail": c["tail"] if c["exit"] != 0 else []}
                       for n, c in collectors.items()},
    }
    out = root / "reports" / f"collect-{args.date}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=1) + "\n")
    state_f.write_text(json.dumps({"last_run": args.date, "raw_paths": sorted(manifest),
                                   "triage_refs": sorted(triage)}, indent=1) + "\n")
    failed = [n for n, c in report["collectors"].items() if not c["ok"]]
    if failed:
        print(f"collectors with errors: {', '.join(failed)}")
    print(f"new triage candidates: {len(new_triage)}")
    print(f"new raw files: {len(new)}")
    for r in report["new_raw"]:
        print(f"  {r['path']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
