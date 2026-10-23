# Phase 3 — Compile the wiki: validation

_How we know the phase is done. Drafted at the start of the phase._

## Done when

- [ ] Every raw file in the manifest has a source page; lint reports a backlog of 0.
- [ ] Structural lint: 0 findings (no orphans, no uncited evidence blocks, quotes found
      verbatim in raw, Fed pages and `sources` consistent).
- [ ] Every batch has a verification report in `staging/verify/`, and every finding in it
      is fixed or explained, with corrections logged in `log.md`.
- [ ] `log.md` has one ingest entry per source and one correction entry per verification
      round; `hot.md` shows the last 20 changes.
- [ ] Index covers every page; if it was split, the split is recorded in `tech-stack.md`
      and lint checks the split files.
- [ ] Every schema change made during the phase is in `CLAUDE.md` and noted in
      `implement.md`, and pages written before the change were migrated.
- [ ] Batch 1 pilot reviewed and approved by the user before batches 2–4 ran.
- [ ] `pytest tests` passes.

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

## Manual checks

- Open three topic pages from different batches: links resolve, the timeline (if any)
  reads in order, the graph has no isolated nodes.
- Pick three quotes at random and find them in the raw file.
- Check one talk source page: nothing attributed to him was said by the host.
