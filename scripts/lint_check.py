#!/usr/bin/env python3
"""Mechanical wiki checks. Exits 1 on any finding.

Checks: required frontmatter per page type, type/folder match, broken wikilinks,
orphan pages, source raw_path existence, raw files with no source page, pages
missing from index.md, and prose paragraphs on topic/claim pages with no source
citation. What it cannot check (uncited sentences inside a cited paragraph,
duplicates, quality) is left to the lint procedure in CLAUDE.md.

Usage: python3 scripts/lint_check.py [--root PATH]
"""
import argparse
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
FIXED = {"index", "hot", "log"}
LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
FENCE = re.compile(r"^```.*?^```", re.S | re.M)


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
    return [m.strip() for m in LINK.findall(FENCE.sub("", text))]


def main(root):
    wiki, raw = root / "wiki", root / "raw"
    findings = []
    pages = {}  # slug -> (path, meta, body, raw text)
    for p in sorted(wiki.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        meta, body = split_frontmatter(text)
        if p.stem in pages:
            findings.append(f"duplicate slug: {p.stem} ({pages[p.stem][0]} and {p})")
        pages[p.stem] = (p, meta, body, text)
    raw_files = sorted(f for f in raw.rglob("*.md")) if raw.exists() else []
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

    inbound = {s: set() for s in pages}
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
        missing = [k for k in REQUIRED[kind] if k not in meta or meta[k] in (None, "")]
        if missing:
            findings.append(f"missing frontmatter {missing}: {rel(p)}")
        if kind == "source" and meta.get("raw_path"):
            if not (root / meta["raw_path"]).exists():
                findings.append(f"raw_path not found: {rel(p)} -> {meta['raw_path']}")
        if kind in ("topic", "claim"):
            for para in re.split(r"\n\s*\n", FENCE.sub("", body)):
                para = para.strip()
                if not para or para[0] in "#->*|" or re.match(r"\d+\.", para):
                    continue
                cited = [resolve(t) for t in links_in(para)]
                if not any(c in pages and pages[c][1] and pages[c][1].get("type") == "source"
                           for c in cited):
                    findings.append(f"uncited paragraph: {rel(p)}: {para[:60]!r}")

    for slug, srcs in inbound.items():
        if slug not in FIXED and not srcs:
            findings.append(f"orphan: {rel(pages[slug][0])}")

    raw_paths = {str(m.get("raw_path")) for _, m, _, _ in pages.values()
                 if m and m.get("type") == "source"}
    for f in raw_files:
        if str(rel(f)) not in raw_paths:
            findings.append(f"raw file with no source page: {rel(f)}")

    if "index" in pages:
        listed = {resolve(t) for t in links_in(pages["index"][3])}
        for slug in pages:
            if slug not in FIXED and slug not in listed:
                findings.append(f"not in index: {rel(pages[slug][0])}")
    else:
        findings.append("missing wiki/index.md")

    for line in findings:
        print(line)
    print(f"{len(pages)} pages, {len(raw_files)} raw files, {len(findings)} findings")
    return 1 if findings else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    sys.exit(main(ap.parse_args().root))
