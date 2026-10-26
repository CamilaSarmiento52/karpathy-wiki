# Phase 5 — Keep it alive: testing

_What the automated tests cover and why. Drafted 2026-10-26 at the start of the phase._

## Automated

- **`tests/test_daily.py`**: with collectors mocked, `daily.py` reports exactly the
  manifest entries added since the last run; state is updated only after a successful run;
  a rate-limited collector is reported as pending, not as a failure; nothing new means
  exit 0, an empty report, and no ingest list.
- **`tests/test_brief.py`**: from a fixture run report and log tail, the brief has the four
  sections in order, lists each new source once with its date, includes promotions and
  "needs you" items, and is not written on a day with nothing new.
- **Promotion fixture** (`tests/test_lint_check.py` or its own file): a bench principle plus
  a second independent quote → lint reports it promotable; after promotion lint is clean;
  an inferred bench rule with two quotes is not promotable (phase 4 test kept).
- Existing suites keep passing, including `build_agent.py --check` on the repo.

## Not automated, and why

Whether an ingest is faithful is judged by the fresh verifier on each run and by the user
reading the brief; whether the schedule fires is checked by a real run. The skill and the
scheduled task are prompts, not code; they are validated by running them, as in phase 4.
