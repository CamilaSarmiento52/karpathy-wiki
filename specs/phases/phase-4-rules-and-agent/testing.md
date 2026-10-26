# Phase 4 — Rules and agent: testing

_What the automated tests cover and why. Drafted 2026-10-26 at the start of the phase._

## Automated

- **Lint, principle checks** (`tests/test_lint_check.py`): a promoted principle with quotes
  from one source fails; with two different sources passes; with two same-text sources
  (listed as duplicates) fails; an AI-written source does not count; a bench principle with
  2+ independent sources is reported as promotable; `inferred: true` without a body line
  saying so fails.
- **`tests/test_build_agent.py`**: from a fixture wiki, the generator writes the four
  sections; output is identical across runs; it lists only promoted rules as rules and
  labels bench and inferred ones; it fails on a principle without a quote or with a broken
  link.
- **`tests/test_run_gate.py`**: fixture transcripts. Code written and never run → block;
  code written then run → allow; no code → allow; code run then edited again without a
  rerun → block; a non-code file (markdown) edited → allow.
- **`tests/test_install.py`**: in a temp home directory, install creates the links,
  re-running is a no-op, uninstall removes only what it created and never a real file.
- Existing suites keep passing.

## Not automated, and why

Whether the agent teaches well, reviews like him, or overstates a rule is judged by running
the real prompts in `tests/prompts.md` (validation.md) and by a fresh verifier reading
principles against raw. The scripts are small; the risk is in behaviour, which unit tests
cannot see.
