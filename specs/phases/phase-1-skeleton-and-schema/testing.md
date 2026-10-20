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

## As built

- `scripts/lint_check.py` checks everything in the list above, and two more things: pages
  missing from `index.md`, and pages whose type does not match their folder.
  "Every factual sentence cites" is approximated per paragraph: every prose paragraph on a
  topic or claim page must link at least one source page.
- `tests/test_lint_check.py` (pytest, 9 tests) builds a tiny wiki in a temp dir, breaks one
  rule per test, and asserts lint reports it; one test asserts a clean wiki passes. This
  keeps the checker honest as later phases change it.
- Run: `.venv/bin/python -m pytest tests && python3 scripts/lint_check.py`.
