# Phase 2 — Collectors and backfill: validation

_How we know the phase is done. Drafted at the start of the phase._

## Done when

- [x] Five collectors exist (`collect_youtube.py`, `collect_x.py`, `collect_github.py`,
      `collect_blog.py`, `collect_talks.py`), all using the shared raw store.
- [x] **Idempotent**: running each collector a second time right after a full run fetches
      nothing and leaves `_manifest.json` and `_queue.json` byte-identical.
- [x] **Versioned snapshots**: a GitHub README with a newer commit than its latest snapshot
      produces a new `<repo-id>@<short-commit>` raw file; an unchanged README produces none.
- [x] **Manifest**: every raw file has an entry with `id, ref, url, medium, published, path,
      sha256` (+ `commit` and `repo` for GitHub); `version` is 3; every hash matches.
- [~] **Restore**: on a copy of the repo with `raw/` emptied except the manifest,
      `fetch_one.py --restore` rebuilds every file. GitHub files match their hashes exactly;
      any other mismatch is reported by name, not hidden.
- [x] **Coverage queue**: every item is `collected`, `pending` or `excluded`; every excluded
      item has a reason; every `collected` item is in the manifest and vice versa.
- [x] **Leads seeded**: every link in the raw files that points at his own posts, videos or
      repos appears in the queue (checked by re-running the seeder: no new items).
- [x] **Teaching first**: every queue item tagged `teaching` that is in scope is collected,
      or pending/excluded with a stated reason.
- [ ] **Coverage report** `coverage.md` written and reviewed by the user.
- [x] `pytest tests` passes; `lint_check.py` has zero findings (uncompiled raw files show
      as a backlog count, not as findings).
- [x] Specs updated in the same change as each decision (tech-stack, CLAUDE.md §3, roadmap).

## Phase gate 2 → 3 (from the roadmap)

1. **Counts match expectations.** For each medium, compare the manifest + queue against an
   independent count:
   - YouTube: number of videos on his channel since the cut-off date, as shown on the
     channel page.
   - GitHub: his public non-fork repos on his profile, filtered by README date.
   - Blog: number of posts on the bearblog post list.
   - X: number of original posts and threads the search returns for the period
     (only if decision 1 is yes).
   - Talks: no independent count exists; the user reviews the list in the report instead.
   Any gap is either explained in the report or fixed.
2. **Ten random raw files spot-checked** against the originals (`scripts/spot_check.py`
   prints ten random files with their URL, `published` date and opening and closing lines).
   For each: right person, right date, body complete (not cut off), timestamps line up with
   the video for YouTube and talks, posts in order for X threads.

## Manual checks

- Pilot batch (about ten teaching items) spot-checked by the user before the full run.
- Open three raw files of different media in Obsidian to confirm frontmatter renders.
- Confirm no secret reached git: `.env` untracked, no key in any committed file or log.
- Confirm `raw/` bodies are still gitignored: only `_manifest.json` and `_queue.json`
  are tracked under `raw/`.

## Status (2026-10-21)

- `[x]` checked as described; `[~]` restore verified for GitHub, blog and X (59 files,
  all hashes match) but not YouTube/talks, because YouTube was rate-limiting this
  connection. Versioned snapshots are verified by tests only: no README changed during
  the phase.
- Teaching first: every teaching item is collected; nothing is pending (2026-10-22).
- Phase gate: counts match for GitHub (63/63), YouTube (17/17) and the blog (13/13 +
  10/10 old); X has no independent count without an API key. Ten random files
  spot-checked (`spot_check.py --seed 2`); the check found and fixed the blog
  page-fallback issue (see implement.md).
- Open: the coverage report and the pilot have been reviewed by Claude, not yet by the
  user.

- **Closed 2026-10-23:** the user reviewed and merged PR #2; phase gate 2 → 3 passed.
