# Phase 5 — Keep it alive: implementation notes

_Written during implementation, 2026-10-26. What was built, decisions made while building,
deviations from the plan._

## Decisions taken (2026-10-26)

The user approved all seven recommendations in plan.md: local scheduled runs; a fresh
verifier on every ingest; local commits on `main`, never pushed; weekdays 07:00 and Sunday
09:00 Lisbon; unattended work limited to the repo; a brief only on news, with a
notification; the phase 5 gate reworded so promotion is proven on a fixture.

## What was built

| File | What it does |
|---|---|
| `scripts/daily.py` | runs each collector as its own process (`--weekly` adds talk search), diffs manifest and queue against `reports/state.json`, writes `reports/collect-DATE.json`, prints `new raw files: N`; no model |
| `scripts/brief.py` | `reports/briefs/DATE.md` from the run report, the day's log entries and the new source pages: What he published, What changed, Rules, Needs you; "no brief" on a quiet day |
| `.claude/skills/karpathy-ingest/SKILL.md` | one source, URL or raw path: fetch via `fetch_one.py`, compile under CLAUDE.md §7, add principle quotes and promote when lint allows, all checks, fresh verifier, fix, one local commit; log fields the brief reads |
| `scripts/install.py` | also links `karpathy-ingest`; refuses to repoint an install made from another copy of the wiki unless `--force` |
| scheduled tasks | `karpathy-wiki-weekday` (07:00 Mon–Fri) and `karpathy-wiki-sunday-lint` (09:00 Sun) in the desktop app; both stop if the repo is not on `main` or `wiki/`/`raw/` has uncommitted changes |
| tests | 130 → 141: daily runner 4, brief 4, promotion path 2, install 1 |
| `reports/` | gitignored: run reports, state and briefs stay on this Mac |

## How it was validated

- **Live collection**: `daily.py` against the real sources: all five collectors ran clean,
  0 new raw files, 0 triage candidates (nothing published since the backfill on his
  channel, GitHub or blog; X has no discovery).
- **Real ingest in a throwaway copy**: no in-scope source was waiting (every 2023+ queue
  item is collected or excluded as a re-upload, someone else's video, or generated output),
  and adding pre-2023 material to the real wiki would change the phase 2 scope decision. So
  the repo was copied without its remote, the 2019 post "A Recipe for Training Neural
  Networks" was fetched into the copy only, and `/karpathy-ingest raw/blog/recipe.md` ran
  headless there (~$2.70): source page, 1 method, 2 claims, 5 updated pages, 2 `supports`
  relations, quotes added to 2 promoted principles, fresh verifier with 5 findings all
  fixed, all checks clean, one local commit. `brief.py` on that copy produced a correct
  four-section brief. The real wiki's manifest stayed at 82 items.
- The ingest in the copy noticed that running `install.py` there would repoint the
  user-level agent at the temporary folder and declined; the installer now refuses that
  case itself.

## Decisions made while building

- **Ingest runs inline, not forked.** A forked skill runs in a sub-agent, and sub-agents
  cannot start the fresh verifier the procedure needs, so the skill runs in the calling
  session and starts the verifier itself.
- **The skill works in the current folder when it is a wiki repo**, so a copy can be tested
  without touching the real wiki.
- **Run reports and briefs are local-only** (gitignored): quiet days make no commits, and
  the brief is for the owner on this Mac.
- **Branch and dirty-tree guards** in both scheduled prompts: a run on a feature branch or
  over uncommitted wiki edits stops and notifies instead of committing.
- **Permissions**: the scheduled-task tool has no permission field; runs start in the
  app's default mode and may pause on first use. The limits of decision 5 are in the task
  prompts; the owner grants the tool approvals once (Run now), which are stored on the task.

## Deviations from the plan

- The brief and run reports are not committed (plan implied they might be).
- No real new source was published during the phase, so gate step 1 (a real source picked
  up by the scheduled run) and the Learning prompt on the real wiki wait for one.

## Cost

About 1.5M agent tokens, plus ~$3 for the headless ingest test.
