#!/usr/bin/env python3
"""Structural lint for the wiki. Exits 1 on any finding.

Checks what can be checked mechanically: frontmatter (required, non-empty, allowed
values, dates), topic date ranges, links, orphans, index coverage, citations present in
every evidence block, frontmatter `sources` matching body citations, source pages'
`## Fed pages` matching who cites them, two-way claim relations backed by a timeline,
quotes found verbatim in the cited raw file, and raw files matching the manifest.
Raw files without a source page are counted as an uncompiled backlog, not reported as
findings: collectors add raw files before ingest compiles them.

A clean run means the wiki is well-formed. It does NOT mean a cited passage supports its
sentence; that is the semantic pass in CLAUDE.md §7 Lint.

Usage: python3 scripts/lint_check.py [--root PATH]
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

REQUIRED = {
    "source": ["raw_path", "published", "medium", "summary"],
    "topic": ["aliases", "first_seen", "last_updated", "sources"],
    "claim": ["stated_on", "confidence", "sources"],
    "artifact": ["repo_url", "language", "status", "sources"],
    "timeline": ["topic"],
    "principle": ["status", "quotes", "inferred"],
    "method": ["steps", "sources"],
    "synthesis": ["question", "answered_on", "sources", "rules_applied"],
}
FOLDER = {
    "source": "sources", "topic": "topics", "claim": "claims", "artifact": "artifacts",
    "timeline": "timeline", "principle": "principles", "method": "methods",
    "synthesis": "syntheses",
}
ALLOWED = {
    ("source", "medium"): {"youtube", "x", "github", "blog", "talk"},
    ("claim", "confidence"): {"stated", "implied", "inferred"},
    ("artifact", "status"): {"active", "archived", "superseded"},
    ("principle", "status"): {"bench", "promoted"},
}
DATES = {"source": ["published"], "claim": ["stated_on"], "topic": ["first_seen", "last_updated"],
         "synthesis": ["answered_on"]}
# sections whose every paragraph and list item must cite a source page ("" = text after H1)
EVIDENCE = {
    "topic": {"", "What he says"},
    "claim": {"Context", "Related claims"},
    "artifact": {"", "What it demonstrates"},
    "method": {"", "Steps"},
    "timeline": {""},
}
SYMMETRIC = ("contradicts", "extends")
FIXED = {"index", "hot", "log"}
MAX_QUOTE_WORDS = 14
LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
FENCE = re.compile(r"^```.*?^```", re.S | re.M)
QUOTE = re.compile(r'^>\s*"([^"]+)"')


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    try:
        meta = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        return None, text
    return meta, text[end + 4:]


def links_in(text):
    return [m.strip() for m in LINK.findall(FENCE.sub("", str(text)))]


def sections(body):
    """{heading: text} with "" for the text between the H1 and the first ## heading."""
    out, name, buf = {}, "", []
    for line in FENCE.sub("", body).splitlines():
        if line.startswith("## "):
            out[name] = "\n".join(buf)
            name, buf = line[3:].strip(), []
        elif not line.startswith("# "):
            buf.append(line)
    out[name] = "\n".join(buf)
    return out


def blocks(text):
    """Paragraphs and list items, each as one string; blockquotes are skipped."""
    out, cur = [], []
    for line in text.splitlines():
        s = line.strip()
        new_item = re.match(r"(-|\*|\d+\.)\s", s)
        if not s or s.startswith(">") or new_item:
            if cur:
                out.append(" ".join(cur))
            cur = [s] if new_item else []
        else:
            cur.append(s)
    if cur:
        out.append(" ".join(cur))
    return out


def norm(text):
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # markdown links -> their text
    text = text.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", text).strip().lower()


def as_date(v):
    if isinstance(v, dt.date):
        return v
    try:
        return dt.date.fromisoformat(str(v))
    except ValueError:
        return None


def raw_body(path):
    return split_frontmatter(path.read_text(encoding="utf-8"))[1].strip()


def main(root):
    wiki, raw = root / "wiki", root / "raw"
    findings = []
    pages = {}  # slug -> (path, meta, body, text)
    for p in sorted(wiki.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        meta, body = split_frontmatter(text)
        if p.stem in pages:
            findings.append(f"duplicate slug: {p.stem} ({pages[p.stem][0]} and {p})")
        pages[p.stem] = (p, meta, body, text)
    raw_files = sorted(raw.rglob("*.md")) if raw.exists() else []
    raw_stems = {f.stem for f in raw_files}

    def resolve(target):
        t = target.removesuffix(".md")
        if "/" in t:
            if (root / f"{t}.md").exists():
                return Path(t).stem
            t = Path(t).name
        if t in pages or t in raw_stems:
            return t
        return None

    def rel(p):
        return p.relative_to(root)

    def kind_of(slug):
        m = pages.get(slug, (None, None))[1]
        return m.get("type") if isinstance(m, dict) else None

    def source_links(text):
        return {s for s in (resolve(t) for t in links_in(text)) if kind_of(s) == "source"}

    def listed(meta, *fields):
        out = set()
        for f in fields:
            v = meta.get(f) or []
            for item in v if isinstance(v, list) else [v]:
                out.update(filter(None, (resolve(t) for t in links_in(item))))
        return out

    inbound = {s: set() for s in pages}
    cites = {s: set() for s in pages if kind_of(s) == "source"}  # source -> pages citing it
    for slug, (p, meta, body, text) in pages.items():
        for target in links_in(text):
            hit = resolve(target)
            if hit is None:
                findings.append(f"broken link: {rel(p)} -> [[{target}]]")
            elif hit in inbound and hit != slug and slug not in FIXED:
                inbound[hit].add(slug)

        if slug in FIXED:
            continue
        if meta is None:
            findings.append(f"missing or invalid frontmatter: {rel(p)}")
            continue
        kind = meta.get("type")
        if kind not in REQUIRED:
            findings.append(f"unknown type {kind!r}: {rel(p)}")
            continue
        if p.relative_to(wiki).parts[0] != FOLDER[kind]:
            findings.append(f"type {kind} in wrong folder: {rel(p)}")
        missing = [k for k in REQUIRED[kind] if meta.get(k) in (None, "", [])]
        if missing:
            findings.append(f"missing or empty frontmatter {missing}: {rel(p)}")
        for (k, field), allowed in ALLOWED.items():
            if kind == k and field in meta and meta[field] not in allowed:
                findings.append(f"invalid {field} {meta[field]!r}: {rel(p)}")
        for field in DATES.get(kind, []):
            if field in meta and as_date(meta[field]) is None:
                findings.append(f"invalid date {field}={meta[field]!r}: {rel(p)}")

        if kind == "source":
            if meta.get("raw_path") and not (root / meta["raw_path"]).exists():
                findings.append(f"raw_path not found: {rel(p)} -> {meta['raw_path']}")
            continue

        for s in source_links(text):
            cites[s].add(slug)

        # every evidence block cites a source page
        for name, sec in sections(body).items():
            if name not in EVIDENCE.get(kind, set()):
                continue
            for block in blocks(sec):
                if not source_links(block):
                    findings.append(f"uncited block: {rel(p)} §{name or 'intro'}: {block[:60]!r}")

        # frontmatter sources match body citations; listed sources must be source pages
        if "sources" in REQUIRED[kind]:
            declared = listed(meta, "sources", "context")
            for s in declared:
                if kind_of(s) != "source":
                    findings.append(f"non-source page in sources/context: {rel(p)} -> {s}")
            body_cited = source_links(body)
            for s in sorted(body_cited - declared):
                findings.append(f"cited in body but not in sources: {rel(p)} -> {s}")
            for s in sorted({d for d in declared if kind_of(d) == "source"} - body_cited):
                findings.append(f"in sources but never cited in body: {rel(p)} -> {s}")

        # topic dates follow its direct sources
        if kind == "topic":
            dates = [as_date(pages[s][1].get("published")) for s in listed(meta, "sources")
                     if kind_of(s) == "source"]
            dates = [d for d in dates if d]
            if dates:
                for field, want in (("first_seen", min(dates)), ("last_updated", max(dates))):
                    if as_date(meta.get(field)) != want:
                        findings.append(f"{field} should be {want}: {rel(p)}")

        # quotes appear verbatim in the cited raw file, and are short
        quotes = []
        if kind == "claim":
            for line in body.splitlines():
                m = QUOTE.match(line.strip())
                if m:
                    quotes.append((m.group(1), source_links(line)))
        if kind == "principle":
            for q in meta.get("quotes") or []:
                quotes.append((str(q.get("text", "")), source_links(q.get("source", ""))))
        for q, srcs in quotes:
            if len(q.split()) > MAX_QUOTE_WORDS:
                findings.append(f"quote over {MAX_QUOTE_WORDS} words: {rel(p)}: {q[:40]!r}")
            raws = [root / pages[s][1]["raw_path"] for s in srcs]
            raws = [r for r in raws if r.exists()]
            if not srcs:
                findings.append(f"quote without a source citation: {rel(p)}: {q[:40]!r}")
            elif raws and not any(norm(q) in norm(raw_body(r)) for r in raws):
                findings.append(f"quote not found in raw: {rel(p)}: {q[:40]!r}")

    # source pages list exactly the pages that cite them
    for s, citing in cites.items():
        fed = {x for x in (resolve(t) for t in links_in(sections(pages[s][2]).get("Fed pages", "")))
               if x}
        for x in sorted(citing - fed):
            findings.append(f"cites {s} but missing from its Fed pages: {x}")
        for x in sorted(fed - citing):
            findings.append(f"in Fed pages of {s} but does not cite it: {x}")

    # contradicts/extends are two-way and explained on a timeline
    timeline_links = set()
    for slug, (_, m, _, text) in pages.items():
        if m and m.get("type") == "timeline":
            timeline_links |= set(filter(None, (resolve(t) for t in links_in(text))))
    for slug, (p, m, _, _) in pages.items():
        if not (m and m.get("type") == "claim"):
            continue
        for rel_name in SYMMETRIC:
            for other in listed(m, rel_name):
                om = pages.get(other, (None, None))[1] or {}
                if slug not in listed(om, rel_name):
                    findings.append(f"{rel_name} not set on both sides: {slug} -> {other}")
                if not {slug, other} <= timeline_links:
                    findings.append(f"{rel_name} pair not on a timeline: {slug}, {other}")

    for slug, srcs in inbound.items():
        if slug not in FIXED and not srcs:
            findings.append(f"orphan: {rel(pages[slug][0])}")

    raw_paths = {str(m.get("raw_path")) for _, m, _, _ in pages.values()
                 if m and m.get("type") == "source"}
    # collected but not yet compiled into a source page: a backlog for ingest, not an error
    backlog = [f for f in raw_files if str(rel(f)) not in raw_paths]

    manifest = raw / "_manifest.json"
    if manifest.exists():
        items = {i["path"]: i for i in json.loads(manifest.read_text())["items"]}
        for f in raw_files:
            item = items.get(str(rel(f)))
            if item is None:
                findings.append(f"raw file not in manifest: {rel(f)}")
            elif hashlib.sha256(raw_body(f).encode()).hexdigest() != item["sha256"]:
                findings.append(f"raw file does not match manifest hash: {rel(f)}")
        for path in sorted(set(items) - {str(rel(f)) for f in raw_files}):
            findings.append(f"manifest entry with no raw file (run fetch_one.py --restore): {path}")
    elif raw_files:
        findings.append("missing raw/_manifest.json")

    if "index" in pages:
        in_index = {resolve(t) for t in links_in(pages["index"][3])}
        for slug in pages:
            if slug not in FIXED and slug not in in_index:
                findings.append(f"not in index: {rel(pages[slug][0])}")
    else:
        findings.append("missing wiki/index.md")

    for line in findings:
        print(line)
    print(f"{len(pages)} pages, {len(raw_files)} raw files ({len(backlog)} not yet compiled), "
          f"{len(findings)} findings (structural)")
    return 1 if findings else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    sys.exit(main(ap.parse_args().root))
