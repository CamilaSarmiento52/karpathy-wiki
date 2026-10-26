# Phase 4 — Rules and agent: plan

_Drafted 2026-10-26 at the start of the phase, before any code. Decisions at the end are
for the user._

## Goal

Turn the compiled wiki into a teacher and a reviewer that work the way he does. Phase 3
built the evidence: 331 pages on what he said. Phase 4 extracts the small set of rules he
actually follows, builds a `karpathy` sub-agent that applies them, and two skills that use
it: `/karpathy-teach` (explain or build something his way) and `/karpathy-review` (review
code his way, proven by running it). A run-gate hook stops the agent from claiming code
works without running it.

## Starting point

- 331 wiki pages, lint 0, 101 tests; `wiki/principles/` and `_bench/` are empty.
- 26 method pages (how he builds, explains, debugs, evaluates), 135 claims, 52 topics.
- DESIGN.md §4 lists seven hypothesised rules (build it to understand it; first-order term
  first; predict, run, compare; show the wrong version first; prove it, don't claim it; say
  what you assumed; simpler wins). The roadmap's known gaps say they stay hypotheses until
  quotes are found in independent sources.
- Lint already supports `principle` pages: required `status`, `quotes`, `inferred`; quotes
  checked verbatim against raw. It does not yet check promotion rules.
- Query answers are now explanations with paragraph-end citations (CLAUDE.md §7). That is
  the floor; the teach skill adds his method on top.

## What this phase builds

### 1. Rules (principles)

```
methods + claims + topics ──► extract (one agent) ──► candidate rules with quotes
                                                          │
                     verify (fresh agent, reads raw) ◄────┘
                          │
              2+ independent sources ──► wiki/principles/<slug>.md   (promoted)
              1 source                ──► wiki/principles/_bench/    (bench)
              no direct quote          ──► inferred: true, says so in the body
```

- **Extract**: one agent reads every method page, every claim, and the topic pages they
  point to, and proposes the smallest set of rules that explains how he builds, teaches and
  reviews. The seven DESIGN.md rules are hypotheses to confirm, reword, merge or reject; the
  agent may add rules the evidence supports and must say which hypotheses it rejected and
  why. Target: 6–12 rules. Each rule: an imperative title, 1+ verbatim quotes (under 15
  words) with source and location, the wiki pages it rests on, and `## In practice` (what
  the agent does differently because of it).
- **Independence** (for promotion): two quotes count as independent only if they come from
  different source pages that are not the same text (the Sutton X post repeats the animals
  vs ghosts blog), not an AI-written part of a source (CLAUDE.md §3), and not a summary of
  the other. Two lectures of one series count as two sources.
- **Verify**: a fresh agent checks every quote against raw, the independence of each pair,
  and that the rule says no more than the quotes and pages support. Fixes are logged as
  corrections, like phase 3.
- **Lint additions**: a `promoted` principle has quotes from 2+ independent sources (by
  source slug; the same-text pairs are listed in a small file lint reads); a `bench`
  principle has fewer; `inferred: true` requires a body line saying so; principle quotes
  are cited by source page with a location.

### 2. Voice

`wiki/methods/how-he-explains.md` (new method page, compiled like any other, from the
existing teaching methods: spelled-out-build-from-scratch, learn-by-building-and-explaining,
small-hackable-educational-code, check-shapes-and-broadcasting, training-diagnostics and the
lectures they cite). Steps such as: start from the smallest working thing, use tiny concrete
numbers, show the tensor shape, predict before running, leave the bug in and show it fail,
name the gotcha. Every step cited.

### 3. The `karpathy` sub-agent

`.claude/agents/karpathy.md`, **generated** by `scripts/build_agent.py` from the wiki, never
edited by hand (tech-stack.md):

1. **Rules**: every promoted principle with one quote and its link; bench and inferred
   rules listed separately and labelled, so the agent says when it leans on one.
2. **Voice**: the steps of `how-he-explains`.
3. **Task loop** (DESIGN.md §5a): define done; say what you assumed and ask if the request
   is thin; smallest version on a tiny input; predict; run and compare; break it and show
   why; fix and trim; report which rule governed each move.
4. **Grounding**: answer questions about his views from the wiki only (CLAUDE.md §7 Query);
   "the wiki has nothing on this" when silent; a one-line disclosure at the top of each
   walkthrough that this is a simulated style grounded in cited sources, never him.

The generator is idempotent and fails if a rule has no quote or a link is broken.

### 4. Skills

- **`/karpathy-teach <topic or task>`**: hands the request to the sub-agent. For "explain
  X", it returns a walkthrough built up from the smallest version, with his examples, cited
  per paragraph. For "build X", it runs the task loop in a working folder and returns real
  outputs and a per-rule checklist.
- **`/karpathy-review <files | folder | --staged>`**: "Would he ship this? What would he
  delete?" Predicts concrete failure conditions, reproduces one by running the code, trims,
  and shows trimmed and original behaving the same side by side.

### 5. Run gate hook

A hook on the sub-agent's stop: if the turn wrote or edited code files and never executed
any of them (no Bash run after the last code write), it blocks with "You have to run this
before you say it works." Python script in `.claude/hooks/`, reading the transcript the hook
receives. The exact hook event and scoping (sub-agent only, not every session in the repo)
is confirmed against Claude Code's current hook docs before building; a project-wide Stop
hook would also block ordinary wiki maintenance turns, which is not wanted.

### 6. Install for use outside this repo

Skills and agents in `karpathy-wiki/.claude/` load only in sessions opened in this folder,
but review is for client repos. `scripts/install.py` links the agent and the two skills
into `~/.claude/` (user level), and the agent reads the wiki by absolute path, so
`/karpathy-review` works from any project. Uninstall removes only those links.

### 7. Validation prompts

`tests/prompts.md`: the real-task prompts from DESIGN.md §8 that belong to this phase (see
validation.md). Run after the build and after any change to rules or the agent.

## Order of work

1. Lint: principle promotion checks, with tests (before any principle page exists).
2. Voice page `how-he-explains`, compiled and verified like phase 3 pages.
3. Extract rules → verify → fix; principles written; lint clean.
4. `build_agent.py` + tests; generate the agent.
5. Run gate hook + tests (fixture transcripts).
6. Skills; `install.py` + tests.
7. Run `tests/prompts.md`; fix; record results.

## Out of scope

`/karpathy-ingest`, scheduled collection, the morning brief, bench promotion on new ingest
(phase 5). A pre-commit review hook for client repos (later). Changing wiki content beyond
the voice page, principles and any corrections the verification finds.

## Decisions for the user

1. **Skills usable from any project** (install into `~/.claude/` by links). Recommended:
   yes, since review is for client code. The alternative keeps them inside this repo only.
2. **Independence rule** as defined above (different source pages, not the same text, not
   AI-written, not a summary; lectures of one series count separately). Recommended: yes.
3. **Rule count**: aim for 6–12 rules, with the seven DESIGN.md rules as hypotheses the
   extraction may reject. Recommended: yes; fewer strong rules beat many weak ones.
4. **Where teach builds code**: a gitignored `playground/<yyyy-mm-dd>-<slug>/` in this repo
   when run here; a `karpathy-playground/` folder in the current project when run elsewhere.
   Recommended: yes; nothing it builds is committed unless you ask.
5. **Learning prompt** (`/karpathy-ingest`) moves to the phase 5 gate, since the ingest
   skill is phase 5. Phase 4's gate is the other five prompts. Recommended: yes; the roadmap
   gate is updated to match.
6. **Phase 3 gate**: your own fresh-session check is still open. Recommended: do it before
   the extraction step (step 3), since rules are built on those pages.
