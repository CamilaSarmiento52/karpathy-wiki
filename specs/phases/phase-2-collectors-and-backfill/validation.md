# Phase 2 — Collectors and backfill: validation

_How we know the phase is done. Drafted at the start of the phase._

## Done when

- [ ] Five collectors exist (`collect_youtube.py`, `collect_x.py`, `collect_github.py`,
      `collect_blog.py`, `collect_talks.py`), all using the shared raw store.
- [ ] **Idempotent**: running each collector a second time right after a full run fetches
      nothing and leaves `_manifest.json` and `_queue.json` byte-identical.
- [ ] **Versioned snapshots**: a GitHub README with a newer commit than its latest snapshot
      produces a new `<repo-id>@<short-commit>` raw file; an unchanged README produces none.
- [ ] **Manifest**: every raw file has an entry with `id, ref, url, medium, published, path,
      sha256` (+ `commit` and `repo` for GitHub); `version` is 3; every hash matches.
- [ ] **Restore**: on a copy of the repo with `raw/` emptied except the manifest,
      `fetch_one.py --restore` rebuilds every file. GitHub files match their hashes exactly;
      any other mismatch is reported by name, not hidden.
- [ ] **Coverage queue**: every item is `collected`, `pending` or `excluded`; every excluded
      item has a reason; every `collected` item is in the manifest and vice versa.
- [ ] **Leads seeded**: every link in the raw files that points at his own posts, videos or
      repos appears in the queue (checked by re-running the seeder: no new items).
- [ ] **Teaching first**: every queue item tagged `teaching` that is in scope is collected,
      or pending/excluded with a stated reason.
- [ ] **Coverage report** `coverage.md` written and reviewed by the user.
- [ ] `pytest tests` passes; `lint_check.py` has zero findings (uncompiled raw files show
      as a backlog count, not as findings).
- [ ] Specs updated in the same change as each decision (tech-stack, CLAUDE.md §3, roadmap).

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
