# Phase 5 — Keep it alive: plan

_Drafted 2026-10-26 at the start of the phase, before any code. Decisions at the end are
for the user._

## Goal

The wiki keeps itself current. When he publishes something, it arrives in `raw/`, gets
compiled into the wiki with the same care as phase 3, and the user hears about it in a
short weekday brief, without editing a page by hand. Two ways in: a weekday scheduled run,
and `/karpathy-ingest <url>` at any time. A Sunday lint keeps it healthy, promotes a bench
rule when the evidence arrives, and regenerates the karpathy agent if rules changed.

## Starting point

- 343 pages, 82 sources, 11 principles (10 promoted, 1 inferred on the bench), lint 0,
  130 tests. Phase 3 and 4 gates: the user's own checks are still open.
- Collectors (`scripts/collect_*.py`) are idempotent and write raw files plus manifest
  entries; `fetch_one.py` fetches one item. YouTube rate-limits after ~25 caption fetches,
  which a daily run stays far below.
- **X has no discovery**: no `TWITTERAPI_IO_KEY`, so the X collector only refetches posts
  already queued.
- **Talk discovery needs a person**: YouTube search results are mostly re-uploads and
  commentary (phase 2), so candidates wait for triage; they are never ingested automatically.
- The phase 3 method (digest, merge, fresh verifier, fix) is in CLAUDE.md §7 and
  `staging/*-brief.md`; a single new source is small enough for one pass.
- **raw/ is local only** (gitignored for copyright), so the scheduled run must run on this
  Mac. A cloud routine would not have the raw files.

## What this phase builds

### 1. `scripts/daily.py`, the deterministic part

No model involved; safe to run any time, and testable.

1. Run the collectors with their normal idempotent settings: YouTube channel, GitHub
   (repos, README snapshots, Discussions, gists), blog feeds, talks from the queue, X for
   queued posts only. `--search` for talks runs weekly, not daily.
2. Diff the manifest against the last run (state in `reports/state.json`) and list the new
   raw files and new triage candidates.
3. Run lint (backlog count) and write `reports/collect-YYYY-MM-DD.json`: new raw files,
   failures (rate limits are a pending reason, not an error), candidates for triage.
4. Exit 0 with nothing new and the scheduled job stops there at no model cost.

### 2. `/karpathy-ingest <url | raw path>`, the compile step

A skill (`context: fork`, general-purpose agent, its own context). It runs CLAUDE.md §7 Ingest for
one source:

1. If given a URL, work out the medium and id and run `fetch_one.py` (the only way anything
   enters `raw/`). If given a raw path (from the scheduled run), skip the fetch.
2. Digest and merge in one pass under the existing briefs: source page, reuse before create,
   relations by the weakest true link, timelines, index, hot, log, lint after each step.
3. **Principles**: if the source has a verbatim quote supporting a principle, add it to the
   page's quotes. If that gives a bench rule 2+ independent sources (and it is not
   inferred), promote it (lint enforces the conditions), and regenerate the agent with
   `build_agent.py` and, if installed, `install.py`.
4. Run lint, `quote_check.py`, `build_agent.py --check`, and the tests; stop and report on
   any failure instead of committing.
5. Hand off to a **fresh verifier** (decision 2), then fix and log corrections.
6. Commit (decision 3) and report: pages created and updated, relations set, principles
   touched, verifier findings.

Installed at user level like the phase 4 skills, so a link can be ingested from any project.

### 3. Weekday scheduled run (local, desktop app scheduled task)

At the time in decision 4: run `daily.py`; for each new raw file, run `/karpathy-ingest`
on its path, one at a time, oldest first; then write the brief. Unattended, so its tool
permissions are limited to this repo (decision 5).

### 4. The brief

`reports/briefs/YYYY-MM-DD.md`, at most a screen:

- **What he published** (each new source: title, date, medium, one line in plain language).
- **What changed in the wiki** (pages created and updated, any `extends` or `contradicts`
  set, any timeline entry).
- **Rules** (any quote added to a principle, any promotion, agent regenerated or not).
- **Needs you** (triage candidates, fetch failures, verifier findings it could not fix).
- Nothing new: no brief, or a one-line one (decision 6).

Delivery per decision 6.

### 5. Sunday lint (scheduled weekly)

CLAUDE.md §7 Lint on a schedule: structural lint, `quote_check.py`, `build_agent.py --check`;
a fresh reader re-checks every page changed that week against raw; talk `--search` for new
candidates; any bench rule lint reports as promotable is checked and promoted; agent
regenerated if rules changed. Appends a `lint` entry to `log.md`; its summary goes into
Monday's brief.

## Order of work

1. `daily.py` and its tests (manifest diff, state, report; collectors mocked).
2. `/karpathy-ingest` skill, tested on a real new item and on a raw path.
3. Brief writer and its tests (from a fixture of a run report and a log tail).
4. Scheduled tasks: weekday run, Sunday lint.
5. Validation: the Learning prompt; one real scheduled run end to end.

## Out of scope

X discovery until a key exists (adding `TWITTERAPI_IO_KEY` turns it on with no code change).
Whisper for videos without captions. Pre-2023 backfill. A pre-commit review hook for client
repos. Pushing to GitHub from a scheduled run.

## Decisions for the user

1. **Scheduled runs are local** (desktop app scheduled tasks on this Mac), because raw files
   never leave it. Recommended: yes. They run only when the Mac is on and the app is open;
   a missed day is caught up by the next run, since collectors are idempotent.
2. **A fresh verifier checks every new ingest** before commit, like phase 3. Recommended:
   yes; it roughly doubles the cost of an ingest (about $1–2 per long talk, cents for a post)
   and is what caught most errors so far.
3. **Commits**: the scheduled run commits locally on `main` (one commit per source) and
   never pushes; you push when you have looked. Recommended: yes. Alternative: leave changes
   uncommitted for you to review.
4. **Times**: weekday run at 07:00 and Sunday lint at 09:00, Lisbon time. Recommended: yes,
   so the brief is ready for your morning build time.
5. **Unattended permissions**: the scheduled session may read and write inside this repo
   and run its scripts and Python; nothing outside the repo; no push, no network except what
   the collectors fetch. Recommended: yes.
6. **Brief delivery**: write the markdown file and send a short desktop notification only
   when he published something; quiet days produce no brief. Recommended: yes. Alternative:
   also feed it into your existing morning brief.
7. **Phase 5 gate** reworded. The roadmap says "a bench rule promoted", but the only bench
   rule is inferred, and lint refuses to promote inferred rules, so that can happen only if a
   new post states the rule directly. Recommended gate: one real new source ingested end to
   end by the scheduled run with its brief received; the promotion path proven on a fixture
   (a bench rule plus a new source that supports it → promoted, agent regenerated); and the
   Learning prompt passing. A real promotion counts when it happens.
