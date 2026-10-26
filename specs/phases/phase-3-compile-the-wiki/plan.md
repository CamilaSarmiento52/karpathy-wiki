# Phase 3 — Compile the wiki: plan

_Drafted 2026-10-23 at the start of the phase, before any ingest._

## Goal

Compile the 76 uncompiled raw files from phase 2 into the wiki under the phase 1 schema,
so a free question about anything he covered since 2022 gets a cited answer. The schema
stays as approved; changes happen only between batches, recorded in `CLAUDE.md` first.

## Starting point

- 82 raw files, about 480,000 words: 13 videos on his channel (288k words; the longest are
  44k and 42k), 9 talks (109k), 36 GitHub READMEs/Discussions/gists (51k), 14 blog posts
  (29k), 10 X posts (4k). 6 are already compiled (phase 1); 76 are the backlog.
- Wiki: 30 pages, structural lint clean, 25 tests passing at the end of phase 1 (90 after
  phase 2).

## Why the phase 1 method cannot simply be repeated

Phase 1 compiled six sources in one conversation. Here the raw text is about 640,000
tokens. No single context can hold it, and a 3-hour transcript alone fills a large share of
one. The ingest must be split so that each step reads a bounded amount, while keeping the
rule that matters most: **one writer changes the wiki at a time**, so two steps never
create competing pages for the same idea.

## Approach: digest in parallel, merge in sequence, verify independently

```
raw file ──► digest (one agent per source, parallel) ──► staging/digests/<slug>.md
                                                              │
batch of digests ──► merge (one agent, sequential) ──► wiki/ + index, hot, log, lint
                                                              │
new and changed pages ──► verify (fresh agent) ──► corrections, logged
```

1. **Digest** (parallel, read-only on `wiki/`). One agent reads `CLAUDE.md`, `index.md` and
   one raw file, and writes `staging/digests/<source-slug>.md`:
   - the complete source page, ready to copy;
   - every candidate topic, claim, artifact and method, each with a proposed slug (an
     existing one if the index has it), aliases, and the statements that support it with
     their `@mm:ss` or `§section`;
   - quotes, under 15 words, copied verbatim from the raw file;
   - for talks, a note confirming each statement is his and not the host's.
   A digest never writes to `wiki/`, so any number can run at once.
2. **Merge** (sequential, one batch at a time, in `published` order). One agent reads the
   index and a group of digests (about five at a time, to keep its context bounded), opens
   the existing pages each item touches, and writes the wiki following `CLAUDE.md` §7
   steps 3–10: reuse before create, `supports` / `extends` / `contradicts` with
   timelines, Fed pages, index, hot, log. Lint must be clean before the next group.
3. **Verify** (fresh agent per batch, has not seen the merge). Checks every new or changed
   claim page and every quote against the raw file, and one in five sentences on other
   new or changed pages. Findings are fixed by the merge step and logged as corrections
   (invariant 6). This is the semantic pass, done by someone other than the writer, which
   is what caught the phase 1 errors.

## Batches (published order, so timelines build forwards)

| Batch | Dates | Sources | Words | Highlights |
|---|---|---|---|---|
| 1 | 2022-08 → 2023-01 | 10 | ~133k | Zero to Hero: micrograd, makemore 1–5, GPT from scratch; makemore, minGPT, ng-video-lecture READMEs |
| 2 | 2023-05 → 2024-07 | 21 | ~150k | CS25, State of GPT, Intro to LLMs, tokenizer, GPT-2 reproduction, llm.c Discussions, minbpe, llama2.c, build-nanogpt, Sequoia and Berkeley talks |
| 3 | 2024-08 → 2025-10 | 23 | ~135k | LLM101n, llm.c, No Priors, CUDA keynote, Deep Dive, How I use LLMs, the 2025 blog posts, Dwarkesh |
| 4 | 2025-10 → 2026-08 | 22 | ~60k | nanochat Discussions, microgpt, autoresearch, Skill Issue, Sequoia 2026, llm-wiki gist, recent X posts |

Phase 1's six sources are not re-ingested; merge links them to new pages as they come up.
`scripts/batches.py` assigns sources to batches from the manifest, so the split is
reproducible and lint can report progress per batch.

**Batch 1 is the pilot**: after it, stop for the user's review in Obsidian (and an external
review if wanted) before batches 2–4. It is the first time the schema meets lecture
material, so it is where page types are most likely to need a correction.

## Scaling the wiki itself

- Expect roughly 250–400 pages by the end. When `index.md` passes 200 lines, split it:
  `index.md` becomes a short top-level page linking `wiki/index/<type>.md` per page type,
  and lint learns to treat those as index files. Decide at the end of the batch where it
  happens, and record it in `tech-stack.md`.
- Merge finds existing pages by searching file names and `aliases`, not by reading the
  whole index, once the index is split.
- Lecture videos produce many fine-grained ideas. A topic page is created only for an idea
  that is explained, not just mentioned; mentions become a sentence on the nearest page.

## Tooling to build

- `scripts/batches.py`: batch assignment and per-batch status (raw files, digests, source
  pages, verified).
- Lint: recognise split index files if the split happens; report backlog per batch.
- `staging/` folder for digests and verification reports; `.obsidian/app.json` hides it
  from the vault so it does not appear in the graph.

## Out of scope

Principle extraction and the agent (phase 4), scheduled collection (phase 5), X discovery
(needs a twitterapi.io key), pre-2023 material outside the Zero to Hero series.

## Decisions for the user

1. **Run with parallel helper agents?** Recommended: digests run as background helper
   agents, up to 8 at a time; merge and verify run one at a time. The alternative is one
   source at a time in a single session, which would take many sessions. Either way the
   whole phase reads the 480k words at least once, plus merging and verification: a large
   token spend, several million tokens.
2. **Personal posts** (sleep tracker, chemical and digital hygiene, calorie app, grocery
   store, jobs). Recommended: ingest them with full source pages, but create topic pages
   only where an idea recurs in two or more sources; no claim pages unless he takes a
   clear position.
3. **Pilot gate after batch 1.** Recommended: yes, stop for your review.
4. **Commit the digests.** Recommended: yes, in `staging/`. They hold only paraphrase and
   short quotes, and they let a reviewer check the merge against what was extracted.
5. **External review.** Recommended: after batch 1 and at the end of the phase, not after
   every batch.
