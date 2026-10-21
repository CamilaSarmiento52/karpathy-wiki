# Phase 2 — Collectors and backfill: testing

_What the automated tests cover and why. Drafted at the start of the phase._

## Principle

Tests never touch the network. Each collector's network calls (yt-dlp, the transcript API,
`gh`, twitterapi.io, fxtwitter, bearblog) go through a small function that tests replace
with canned responses, as `tests/test_fetch_one.py` already does. The live sources are
checked by hand with `--limit 1` runs and the phase gate spot-check, because a test against
the live internet would fail for reasons unrelated to our code.

## Automated tests

### Shared raw store (`tests/test_rawstore.py`)

- Writing a raw file produces the CLAUDE.md §3 frontmatter in the standard order.
- The body hash ignores frontmatter, so a refetch on another day still matches.
- **Parallel writes**: several processes adding entries at once lose none of them (the lock
  and re-read work).
- **Restore** rebuilds a missing file at the manifest's path, including a versioned GitHub
  snapshot, and reports a changed body instead of hiding it.
- The existing `tests/test_fetch_one.py` keeps passing on top of the new module.

### Per collector (`tests/test_collect_<medium>.py`)

For each collector, with canned discovery and fetch responses:

- **Idempotency**: a second run fetches nothing and leaves manifest and queue unchanged.
- **Date filter**: items before `--since` become `excluded: before-2023` (or the agreed
  cut-off), not silently dropped.
- **Manifest entry** has every required field for its medium.
- `--dry-run` writes nothing; `--limit N` fetches at most N.

Medium-specific:

- GitHub: unchanged README → no new snapshot; README with a newer commit → new
  `<repo-id>@<short-commit>` file dated by that commit, old snapshot untouched; forks are
  skipped; a discussion yields only his opening post.
- YouTube: caption snippets are grouped into ~30-second `[mm:ss]` blocks; videos without
  captions become `pending: no-transcript`.
- X: a thread is assembled in posting order from his own replies only; retweets and replies
  to others are excluded with a reason; missing API key falls back to known ids and says so.
- Blog: a post missing from the feed is still fetched from the post list; links are kept.
- Talks: a YouTube upload on another channel gets `medium: talk` and the `talks/` folder.

### Coverage queue (`tests/test_queue.py`)

- Link classification: his posts, videos and repos → `pending`; known third-party sites
  → dropped; unknown sites → `pending` with `needs-triage`.
- Seeding twice adds nothing the second time.
- `collected` agrees with the manifest in both directions.
- An `excluded` item without a reason is rejected.

### Lint (`tests/test_lint_check.py`, extended)

- A raw file with no source page is counted as uncompiled backlog, not a finding.
- A raw file missing from the manifest, or with a wrong hash, is still a finding.
- Wikilinks to snapshot paths (`[[raw/github/<repo-id>@<sha>]]`) resolve.

## Not automated, and why

- Whether a live source still answers the way our canned responses assume: checked by the
  `--limit 1` runs and the phase gate spot-check.
- Whether a caption transcript is accurate: auto-captions misspell names; phase 3 pages use
  correct spellings, and the spot-check catches truncated or misaligned transcripts.
- Whether the queue's `teaching` tags are right: a judgement the user reviews in the
  coverage report.

Run: `.venv/bin/python -m pytest tests && python3 scripts/lint_check.py`.
