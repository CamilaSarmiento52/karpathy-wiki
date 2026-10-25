# Phase 3 — Compile the wiki: validation

_How we know the phase is done. Drafted at the start of the phase._

## Done when

- [x] Every raw file in the manifest has a source page; lint reports a backlog of 0.
      _82 of 82, 2026-10-25._
- [x] Structural lint: 0 findings _(331 pages, 2026-10-25; `quote_check.py` also finds
      every inline quote verbatim in its cited raw)_ (no orphans, no uncited evidence blocks, quotes found
      verbatim in raw, Fed pages and `sources` consistent).
- [x] Every batch has a verification report in `staging/verify/`, and every finding in it
      is fixed or explained, with corrections logged in `log.md`. _Batch 1: three reports
      (one per merge group), 21 findings, all fixed and logged 2026-10-23. Batch 2: four
      reports, 31 findings, 30 fixed and 1 left as asked, logged 2026-10-24. Batch 3: four
      reports, 32 findings, all fixed, logged 2026-10-25. Batch 4: four reports, 28
      findings, all fixed, logged 2026-10-25._
- [x] `log.md` has one ingest entry per source and one correction entry per verification
      round; `hot.md` shows the last 20 changes. _82 ingest entries for 82 sources._
- [x] Index covers every page; if it was split, the split is recorded in `tech-stack.md`
      and lint checks the split files. _Split 2026-10-24 between batches 1 and 2._
- [x] Every schema change made during the phase is in `CLAUDE.md` and noted in
      `implement.md`, and pages written before the change were migrated. _Index split;
      published-date rule (14 phrases migrated); AI-written text rule (no earlier source
      affected)._
- [x] Batch 1 pilot reviewed and approved by the user before batches 2–4 ran. _Batch 1
      compiled and verified 2026-10-23; the user waived the review on 2026-10-24._
- [x] `pytest tests` passes. _98 tests, 2026-10-24._

## Phase gate 3 → 4 (from the roadmap)

1. Lint reports zero orphans and zero uncited evidence blocks.
2. Three free questions, asked in a **fresh session** opened in `karpathy-wiki/`, are
   answered with correct citations. Proposed questions:
   - "How does he explain backpropagation, and what does he build to teach it?"
     (expects micrograd, the Zero to Hero lecture, citations with timestamps)
   - "How did his view of LLM agents change between 2023 and 2026?"
     (expects a timeline and dated claims across talks and posts)
   - "What does he say about tokenization being a source of LLM problems?"
     (expects the tokenizer lecture and related claims)
   Plus one question he has not addressed in the corpus, which must get "the wiki has
   nothing on this".
3. For each answer, the user clicks two citations through to the raw text and confirms
   them.

### Question-and-citation check — 2026-10-23

Run against the current 16-source pilot wiki, using a fresh isolated reader rather than
a separate user-opened session. Answers and raw citation checks are recorded in
`staging/phase-3-question-validation.md`.

- Backpropagation: answerable from the compiled lectures and micrograd pages.
- Agents, 2023–2026: only partially answerable. The wiki has later evidence, but no
  compiled 2023 agent baseline or agent timeline; a change of view cannot yet be established.
- Tokenization as a source of problems: only partially answerable. Basic tokenization
  and the vocabulary/sequence-length tradeoff are compiled; the dedicated 2024 tokenizer
  lecture is collected but not compiled.
- Negative control (apple-tree pruning): no supporting wiki content; the expected answer
  is "the wiki has nothing on this".

Structural lint was rerun: 94 pages, 82 raw files, 66 uncompiled, 0 findings. This check
does **not** pass the phase 3 → 4 gate: question coverage is incomplete, and the user's
two-citation-per-answer click-through confirmation remains pending. Re-run the full gate
after the remaining sources have been compiled.

### Status of the gate (2026-10-25)

A second fresh-reader check (`staging/phase-3-question-validation-2.md`) found all three
questions now answered with Sufficient coverage and the negative control refused; 18
citations checked against raw, all correct. It flagged three gaps on
`llm-agents-over-time`, fixed and logged the same day. **Still open:** the user's own
fresh-session run of the questions and the two-citation click-through per answer. The
phase is not done until the user has done that.

## Manual checks

- Open three topic pages from different batches: links resolve, the timeline (if any)
  reads in order, the graph has no isolated nodes.
- Pick three quotes at random and find them in the raw file.
- Check one talk source page: nothing attributed to him was said by the host.
