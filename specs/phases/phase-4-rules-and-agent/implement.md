# Phase 4 — Rules and agent: implementation notes

_Written during implementation, 2026-10-26. What was built, decisions made while building,
deviations from the plan._

## Decisions taken (2026-10-26)

The user approved all six recommendations in plan.md: skills usable from any project;
the independence rule as defined; 6–12 rules with the DESIGN.md seven as hypotheses; teach
builds in a gitignored playground; the Learning prompt moves to the phase 5 gate. Decision 6
(the user's own phase 3 gate check before extraction) did not happen first: the build went
ahead and that check is still open. The rules rest on pages that two fresh-reader checks
passed; if the user's check finds a page error, the principles that rest on it are rechecked.

## What was built

| File | What it does |
|---|---|
| `scripts/lint_check.py` | principle checks: promoted needs quotes from 2+ independent sources; an inferred rule cannot be promoted; bench with 2+ sources (not inferred) is flagged as promotable; status matches folder; inferred rules say so; every quote has a location; AI-written parts never count |
| `scripts/independence.json` | same-text source groups (the Sutton post and animals-vs-ghosts; the Sequoia talk and its summary) and AI-written sources with the only locations that are his |
| `wiki/methods/how-he-explains.md` | the voice: 11 steps, each cited to 2+ sources, verified (10 findings fixed) |
| `wiki/principles/` | 10 promoted rules; `_bench/` 1 inferred rule (see below) |
| `scripts/build_agent.py` | generates `.claude/agents/karpathy.md` (~1,000 words): frontmatter hooks, grounding, rules (title, one quote, page link), bench rules labelled, voice, task loop, working folder, report; `--check` fails when stale |
| `.claude/hooks/run_gate.py` | `log` (PostToolUse) records code writes and running commands per `agent_id`; `check` (Stop, SubagentStop at runtime) blocks when code was written and not run since, up to 3 times, and lets an answer that admits the code is unverified finish |
| `.claude/skills/karpathy-teach`, `karpathy-review` | `context: fork`, `agent: karpathy`, self-contained task prompts |
| `scripts/install.py` | user level: agent copy with absolute paths (agent symlinks are undocumented), links for both skills and the hook; idempotent; uninstall removes only its own |
| `tests/fixtures/review/rank_answers.py` | review fixture; expected findings live in validation.md, not beside it |
| `tests/prompts.md` | the five phase 4 prompts with run results; Learning kept for phase 5 |
| tests | 101 → 130 (lint principles 10, run gate 9, build agent 7, install 3) |

## The rules

Extraction (one agent over all 26 methods, ~40 claims and their topics) proposed 11 rules.
A fresh verifier checked all 41 quotes against raw (all verbatim, his, at the stated
location) and found 9 issues, none wrong: 6 overstated titles or practice lines, 1 status,
2 minor. All applied before the pages were written.

| Rule (title as written) | Status | From hypothesis |
|---|---|---|
| To learn something, build it yourself, without copy-paste | promoted | 1, reworded: scoped to learning |
| Start from the simplest thing that shows the idea working, then add one piece at a time, and show the steps | promoted | 2, with "build the ramp" |
| Before you run it, say what number you expect; then compare | promoted | 3 |
| Be careful with shapes and broadcasting, and write array code explicit enough that a wrong assumption raises an error | promoted | new |
| When you reimplement something, check it against a known-good reference until the numbers match | promoted | 5, split |
| When you compare a result with a baseline, state the setting and what might make the comparison unfair | promoted | 5, split |
| Keep model-written code reviewable and check it before you trust it, more carefully the more the code matters | promoted, dated: 2025 small diffs; since December he delegates and reviews by how much he cares | 5, split |
| Keep the main code small and readable; reject complexity that does not pay for itself | promoted, scoped to his reference and educational repos | 7 |
| Invite the learner to try a step before you show the answer | promoted, weakened from "let the learner try first" | new |
| When a bug is instructive, show it failing, then explain it; keep real mistakes in rather than hide them | promoted on makemore 1 and the tokenizer lecture; micrograd's bugs were accidents | 4, without "first" |
| State the assumptions you are making, and ask when the request leaves them open | bench, inferred | 6 |

Hypotheses not kept as written: H3's "silently work a bit worse" is in no raw file (the
rule rests on his micrograd "lots of bugs and it still works"); H4's "first" has no quote
for the ordering; H6's "his top complaint about coding agents" is in no raw file, so the
rule is inferred.

## Decisions made while building

- **The run gate uses documented hook input only.** The transcript format is undocumented,
  so a PostToolUse hook logs what the agent did and the Stop hook reads that log. Both are
  declared in the agent's own frontmatter, so they run only while that agent is active and
  never in ordinary wiki sessions.
- **An inferred rule stays on the bench.** The first lint version forced any rule with 2+
  quoted sources to be promoted, so the inferred assumptions rule was promoted. Lint now
  refuses to promote an inferred rule; CLAUDE.md says so.
- **The agent file is short.** The first generation inlined each rule's full `## In
  practice` section (3,100 words). It now lists title, one quote and the page, and tells the
  agent to read the page before applying a rule.
- **The task loop is labelled as this project's design**, not a procedure he states.
- **Gate behaviour against an instruction not to run.** A one-shot block was outlasted by
  an agent obeying the user's "don't run it". Now: up to three blocks with a reason that
  says the gate holds even then, and an answer that says plainly the code was never run is
  allowed to finish. The honest disclosure is the point, not forced execution.
- **Hook path that works from any project.** With the repo loaded via `--add-dir`, the
  repo's agent file wins over the user-level copy and `$CLAUDE_PROJECT_DIR` is the other
  project, so every hook call failed silently. The command now falls back to
  `~/.claude/hooks/karpathy-run-gate.py`, linked by `install.py`. Found by testing from a
  folder outside the repo, not by unit tests.
- **Headless validation uses the desktop app's Claude Code (2.1.308).** The `claude` on
  PATH is 2.0.31, older than skill forking and agent frontmatter hooks.

## Deviations from the plan

- Rule 11 is on the bench (plan expected statuses to follow source counts alone).
- Lint promotion checks were extended beyond testing.md (inferred cannot be promoted).
- `install.py` also links the run gate hook (not in the plan).
- CLAUDE.md gained a §7 "Rules and agent" procedure and ingest step 8 now notes support for
  principles; promotion on new ingest stays in phase 5.

## Cost

About 2.5M agent tokens for extraction, verification and page writing; the headless
validation runs cost about $6 at list price.
