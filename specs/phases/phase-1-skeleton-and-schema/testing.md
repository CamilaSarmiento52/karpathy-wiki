# Phase 1 — Skeleton and schema: testing

## Automated

A small `scripts/lint_check.py` (first version of what lint will use later) that walks
`wiki/` and reports:

- pages missing required frontmatter for their type
- orphan pages (no inbound wikilink)
- wikilinks that resolve to no file
- source pages whose `raw_path` does not exist
- raw files with no source page

It exits non-zero on any finding. Run after every ingest in this phase.

## Why this and not more

The phase has no collectors or agent yet, so there is nothing else to test automatically.
The schema itself is validated by a human looking at real pages, which is the point of the
five hand-picked sources. The lint check is kept because every later phase will need it and
it is cheap to write now.
