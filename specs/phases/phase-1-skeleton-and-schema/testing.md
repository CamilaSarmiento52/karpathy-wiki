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

- `scripts/lint_check.py` is **structural lint**: it proves the wiki is well-formed, not
  that summaries are right. Checks: required and non-empty frontmatter, allowed values,
  dates, type/folder, broken links, orphans, index coverage, a source citation in every
  evidence block (paragraphs and list items), body citations matching `sources`/`context`,
  Fed pages matching who cites each source, `contradicts`/`extends` set on both sides and
  on a timeline, claim and principle quotes found verbatim in the cited raw file and under
  15 words, raw files matching manifest hashes.
- `tests/test_lint_check.py` (20 tests) builds a tiny wiki per test and breaks one rule;
  it includes the two false negatives the review demonstrated (uncited bullet, empty
  `sources`).
- `tests/test_fetch_one.py` (5 tests) stubs the network and checks the fetcher's
  bookkeeping: folders created, manifest-only restore, changed-content report, skip of an
  existing file, blog links kept.
- Not automated: whether a citation supports its sentence. That is the semantic pass in
  CLAUDE.md §7 and a manual check in validation.md.
- Run: `.venv/bin/python -m pytest tests && python3 scripts/lint_check.py`.
