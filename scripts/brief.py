#!/usr/bin/env python3
"""Write the weekday brief: what he published, what changed, rules, what needs you.

Reads `reports/collect-DATE.json` (from daily.py), the `wiki/log.md` entries dated DATE
(ingest, correction, lint, compile), and the new source pages. Writes
`reports/briefs/DATE.md` only when there is something to say: a new source, a triage
candidate, a collector failure, or a lint entry. Otherwise writes nothing and prints
"no brief". Deterministic; no model.

Log entries the ingest skill writes carry `- created:`, `- updated:`, `- relations:`,
`- principles:`, `- verifier:` lines; this script copies them, it does not interpret prose.

Usage: python3 scripts/brief.py [--date YYYY-MM-DD] [--root PATH]
"""
import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint_check as L  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ENTRY = re.compile(r"^## (\d{4}-\d{2}-\d{2}) (\w[\w ]*?)(?: \[\[([^\]]+)\]\])?\s*$")


def log_entries(log_text, date):
    """[(kind, slug, {field: text})] for log entries dated `date`, in order."""
    out, cur = [], None
    for line in log_text.splitlines():
        m = ENTRY.match(line)
        if m:
            cur = None
            if m.group(1) == date:
                cur = (m.group(2).strip(), m.group(3), {})
                out.append(cur)
            continue
        if cur and line.startswith("- "):
            field, _, text = line[2:].partition(":")
            if text and re.fullmatch(r"[a-z ]+", field.strip()):
                cur[2].setdefault(field.strip(), []).append(text.strip())
            else:
                cur[2].setdefault("bullets", []).append(line[2:].strip())
    return out


def source_line(root, slug):
    p = root / "wiki" / "sources" / f"{slug}.md"
    meta = L.split_frontmatter(p.read_text())[0] if p.exists() else {}
    meta = meta if isinstance(meta, dict) else {}
    title = meta.get("title") or slug
    return (f"- **{title}** ({meta.get('medium', '?')}, published {meta.get('published', '?')})"
            f" — {meta.get('summary', '').strip()} [[{slug}]]")


def build(root, date):
    rep_f = root / "reports" / f"collect-{date}.json"
    rep = json.loads(rep_f.read_text()) if rep_f.exists() else {"new_raw": [], "new_triage": [],
                                                                   "collectors": {}}
    log_f = root / "wiki" / "log.md"
    entries = log_entries(log_f.read_text() if log_f.exists() else "", date)
    ingests = [e for e in entries if e[0] == "ingest" and e[1]]
    failed = {n: c for n, c in rep.get("collectors", {}).items() if not c.get("ok")}
    pending = [p for c in rep.get("collectors", {}).values() for p in c.get("pending", [])]
    lint = [e for e in entries if e[0] == "lint"]
    if not (ingests or rep.get("new_raw") or rep.get("new_triage") or failed or lint):
        return None

    lines = [f"# Karpathy wiki brief, {date}", ""]
    lines += ["## What he published", ""]
    if ingests:
        lines += [source_line(root, slug) for _, slug, _ in ingests]
    else:
        lines.append("- Nothing new compiled today.")
    compiled_raw = set()
    for sp in (root / "wiki" / "sources").glob("*.md"):
        meta = L.split_frontmatter(sp.read_text())[0]
        if isinstance(meta, dict) and meta.get("raw_path"):
            compiled_raw.add(str(meta["raw_path"]))
    uncompiled = [r for r in rep.get("new_raw", []) if r["path"] not in compiled_raw]
    lines += ["", "## What changed in the wiki", ""]
    if ingests:
        for _, slug, f in ingests:
            parts = []
            for field in ("created", "updated", "relations"):
                if f.get(field):
                    parts.append(f"{field}: {'; '.join(f[field])}")
            lines.append(f"- From [[{slug}]]: " + (" · ".join(parts) or "see the log entry"))
    fixed = sum(len(f.get("bullets", [])) for kind, _, f in entries if kind == "correction")
    if fixed:
        lines.append(f"- Corrections: {fixed} page fix(es) logged today, see `wiki/log.md`.")
    for kind, slug, f in entries:
        if kind == "lint":
            lines.append(f"- Sunday lint: {'; '.join(f.get('bullets', []) or f.get('notes', [])) or 'see the log'}")
    if not ingests and not any(k in ("correction", "lint") for k, _, _ in entries):
        lines.append("- No pages changed.")
    lines += ["", "## Rules", ""]
    rules = [t for _, _, f in entries for t in f.get("principles", [])]
    lines += [f"- {t}" for t in rules] or ["- No rule changed."]
    lines += ["", "## Needs you", ""]
    needs = []
    for t in rep.get("new_triage", []):
        needs.append(f"- Triage: {t.get('title') or t['ref']} ({t.get('url')}). Approve: "
                     f"`python3 scripts/coverage_queue.py set {t['ref']} --reason approved`; "
                     f"exclude: `... set {t['ref']} --status excluded --reason <why>`.")
    for n, c in failed.items():
        needs.append(f"- Collector `{n}` failed: {(c.get('tail') or ['no output'])[-1]}")
    for p in pending:
        needs.append(f"- Waiting, retried next run: {p}")
    for r in uncompiled:
        needs.append(f"- Collected but not compiled: `{r['path']}`. Run `/karpathy-ingest {r['path']}`.")
    for _, slug, f in ingests:
        for t in f.get("verifier", []):
            if "open" in t.lower() or "left" in t.lower():
                needs.append(f"- Verifier on [[{slug}]]: {t}")
    lines += needs or ["- Nothing."]
    lines += ["", "Commits are local; push when you have looked: `git log origin/main..main`.", ""]
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--date", default=dt.date.today().isoformat())
    args = ap.parse_args(argv)
    text = build(args.root, args.date)
    if text is None:
        print("no brief")
        return 0
    out = args.root / "reports" / "briefs" / f"{args.date}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text)
    print(f"wrote {out.relative_to(args.root)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
