# Phase 3 — Compile the wiki: testing

_What the phase's automated tests cover and why. Drafted at the start of the phase._

## Automated

- **`tests/test_batches.py`**: `scripts/batches.py` assigns every manifest entry to exactly
  one batch by `published` date; the assignment is stable across runs; status counts
  (raw, digest, source page, verified) match a fixture.
- **Lint, if the index is split**: a split index (`index.md` + `wiki/index/<type>.md`)
  counts as coverage; links from index files do not count against orphans; a page missing
  from its type's index file is reported.
- **Existing suites** (`test_lint_check.py`, `test_fetch_one.py`, collectors) must keep
  passing; no change to the raw store is planned.
- `scripts/lint_check.py` runs after every merge group, not only at the end. It is the
  gate between groups.

## Not automated, and why

The phase's real risk is semantic: a page that is well-formed but says more than the
source does. Phase 1 showed lint cannot catch that. It is covered by the verify step (a
fresh agent reading the raw file) and the phase gate questions, not by unit tests.

## Why this and not more

The phase writes content, not code. New code is limited to batch bookkeeping and, possibly,
the index split, so the tests stay small and target those two.
