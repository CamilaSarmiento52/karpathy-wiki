#!/usr/bin/env python3
"""Report quoted spans in evidence text that are not verbatim in a cited raw file.

Lint checks each claim page's opening blockquote. This script checks the other quotes:
every span of 3+ words in straight or curly quotation marks, inside a paragraph or list
item that cites at least one source page, is looked for in the raw files those source
pages point to. Matching ignores case, whitespace, curly-vs-straight quotes and the
`[mm:ss]` caption markers between 30-second blocks.

A hit is not always an error: a paper title, a prompt string, or another person's words
can be quoted correctly from somewhere the sentence does not cite. Read each hit against
the raw file. Report-only: always exits 0.

Usage: python3 scripts/quote_check.py [--root PATH]
"""
import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint_check as L  # noqa: E402

QUOTES = [re.compile(r'"([^"\n]+)"'), re.compile(r'“([^”\n]+)”')]
MARKER = re.compile(r"\[\d{1,2}:\d{2}(?::\d{2})?\]")
PUNCT = re.compile(r"[,;:.!?…]")


def norm(text):
    text = MARKER.sub(" ", text).replace("`", "")
    return re.sub(r"\s+", " ", PUNCT.sub("", L.norm(text))).strip()


def check(root):
    pages = {}
    for p in (root / "wiki").rglob("*.md"):
        meta, body = L.split_frontmatter(p.read_text(encoding="utf-8"))
        pages[p.stem] = (p, meta if isinstance(meta, dict) else {}, body)
    raw_cache = {}

    def raw_text(slug):
        meta = pages.get(slug, (None, {}, ""))[1]
        if meta.get("type") != "source" or not meta.get("raw_path"):
            return None
        path = root / meta["raw_path"]
        if not path.exists():
            return None
        if path not in raw_cache:
            raw_cache[path] = norm(L.raw_body(path))
        return raw_cache[path]

    hits, total = [], 0
    for slug, (p, meta, body) in sorted(pages.items()):
        if meta.get("type") in (None, "source"):
            continue
        for block in L.blocks(L.FENCE.sub("", body)):
            if block.startswith(">"):
                continue
            raws = [r for r in (raw_text(t.strip()) for t in L.LINK.findall(block)) if r]
            if not raws:
                continue
            text = re.sub(r"\[\[[^\]]*\]\]", "", block)
            for rx in QUOTES:
                for q in rx.findall(text):
                    q = q.replace("`", "")
                    if len(q.split()) < 3:
                        continue
                    total += 1
                    if not any(norm(q) in r for r in raws):
                        hits.append((p.relative_to(root), q))
    return total, hits


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    total, hits = check(ap.parse_args(argv).root)
    for path, q in hits:
        print(f"{path} | {q[:90]}")
    print(f"{total} inline quotes checked, {len(hits)} not found in a raw file cited in the same block")
    return 0


if __name__ == "__main__":
    sys.exit(main())
