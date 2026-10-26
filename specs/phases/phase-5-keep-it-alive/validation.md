# Phase 5 — Keep it alive: validation

_How we know the phase is done. Drafted 2026-10-26 at the start of the phase._

## Done when

- [x] `scripts/daily.py` runs every collector, records new raw files and triage candidates
      in `reports/collect-YYYY-MM-DD.json`, and with nothing new exits without starting a
      model.
- [x] `/karpathy-ingest <url>` and `/karpathy-ingest <raw path>` each compile one source
      under CLAUDE.md §7: source page, fed pages, index, hot, log; lint, quote check and
      tests pass; a fresh verifier ran and its findings are fixed or listed.
- [x] Principle path: a supporting quote is added to a principle; a bench rule that reaches
      2+ independent sources is promoted; the agent is regenerated (and the user-level copy
      reinstalled); an inferred rule is never promoted.
- [x] The brief has the four sections, fits a screen, and is written only when there is
      news.
- [x] The weekday task and the Sunday lint task exist in the desktop app, run locally, with
      the permissions of decision 5, and never push.
- [x] `pytest tests` passes; CLAUDE.md, tech-stack.md and the roadmap describe the
      scheduled operations.

_Checked 2026-10-26: daily.py live (all collectors clean, nothing new); `/karpathy-ingest`
on a raw path in a throwaway copy (the URL path is the same skill after a `fetch_one.py`
call, which ran in that copy); the promotion path and the inferred-rule refusal by
`tests/test_promotion.py`; the brief on the copy; both scheduled tasks created. Details in
implement.md._

## Phase gate 5 → done (as amended by decision 7)

1. **Real ingest end to end**: one real new source he published, picked up by the scheduled
   weekday run (not by hand), compiled, verified and committed, and its brief received.
2. **Promotion path** on a fixture: a bench rule with one source, plus a new source with a
   verbatim supporting quote from an independent source → the ingest promotes it, lint
   passes, the agent file changes and `build_agent.py --check` passes.
3. **Learning prompt** (`tests/prompts.md` #6): `/karpathy-ingest <url of a new post>` in a
   fresh session passes: source page created, touched pages updated, index, hot and log
   updated, any promotable bench rule promoted.

**Status 2026-10-26**: step 2 passes (`tests/test_promotion.py`). Steps 1 and 3 wait for a
new source: none was published during the phase. If no new source appears during the phase, gate step 1 waits; the Learning prompt can use
any post not yet in the manifest.

## Manual checks

- Read one brief on a news day: is it what you want to see at 07:00?
- After an ingest, open the new source page and one updated topic page in Obsidian.
- Check `git log` after a scheduled run: one commit per source, nothing pushed.
