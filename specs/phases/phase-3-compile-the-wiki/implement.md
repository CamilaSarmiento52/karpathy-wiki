# Phase 3 — Compile the wiki: implementation notes

_Written during implementation, from 2026-10-23. What was actually built, decisions made
while building, deviations from the plan._

## Decisions taken (2026-10-23)

The user asked to implement without choosing, so the plan's recommendations stand:

1. Digests run as parallel helper agents (one per source; the three short batch 1 READMEs
   share one agent); merge and verify run one at a time.
2. Personal posts get full source pages; topic pages only where an idea recurs; claim
   pages only for a clear position.
3. Pilot gate after batch 1: stop for the user's review in Obsidian before batches 2–4.
4. Digests are committed under `staging/`.
5. External review after batch 1 and at the end of the phase, if the user wants one.

## Tooling

| File | What it does |
|---|---|
| `scripts/batches.py` | assigns every manifest item to a batch by `published` date (boundaries 2023-02-01, 2024-08-01, 2025-10-20); reports per-batch status: raw, digest, source page, verified |
| `tests/test_batches.py` | boundaries, status fields, stability, CLI listing |
| `staging/README.md` | the digest format and the verify report convention |
| `staging/digests/`, `staging/verify/` | digest per raw file (named by raw stem), verification report per batch |
| `.obsidian/app.json` | `staging/` added to the vault's ignore filters |

Batch sizes from the manifest are 10 / 21 / 23 / 28 (the plan's draft said 22 for batch 4;
the manifest has 28 items from 2025-10-24 on, six of them phase 1 sources).

## Batch 1 (pilot)

Ran 2026-10-23, as planned: digest in parallel, merge in sequence, verify independently,
fix once. Ten sources (seven Zero to Hero lectures, three READMEs), about 133k raw words.

| Step | How | Result |
|---|---|---|
| Digest | 8 parallel agents (one per lecture, one for the three READMEs), read-only on `wiki/` | 10 digests in `staging/digests/`, 34k words; every quote string-checked against raw |
| Reconcile | by hand, before merging: `staging/batch-1-merge-map.md` | digests proposed ~60 topics, ~50 claims, 17 methods; map fixed 20 topics, 22 claims, 8 methods, 5 artifacts |
| Merge | 3 sequential agents (A1: micrograd, makemore 1–2; A2: makemore 3–4; B: makemore 5, GPT lecture, three READMEs), lint after every source | 64 new pages, 20 existing pages extended; 30 → 94 pages |
| Verify | 3 parallel fresh readers, one per merge group, read-only; reports in `staging/verify/` | 21 findings: 0 wrong, 6 overstated, 5 mis-cited, 10 minor; all 12 + 5 + 6 claim quotes verbatim at the cited block |
| Fix | 1 agent, all 21 findings, one `correction` entry in `log.md` | 23 pages changed; lint 0 findings; 94 tests pass |

Pages after batch 1: 16 sources, 29 topics, 28 claims, 6 artifacts, 11 methods, 1 timeline.
Index is 110 lines (split threshold is 200; expect it after batch 2).

### What the verification caught (the kind of error lint cannot see)

- Purpose invented: "overfits a single batch to check the training loop"; he develops on
  five words for speed and only observes the overfitting.
- Fact-of-the-matter title: "the variance mismatch is a bug" where he hedges ("I basically
  consider this to be a bug"); title now says he considers it one.
- Attribution: the biased/unbiased variance choice is the BatchNorm paper's, which PyTorch
  follows; two pages had called it PyTorch's.
- Garbled caption numbers (2.2 → 2.16) presented as his; replaced by his clean summary.
- A `supports` line that connected two lectures he never connects; now says so.
- The wiki's own label ("RLHF") presented as his word.

Three of the five fixes the phase 1 review demanded (overstated wording, mismatched
citations, invented links) recurred here at a lower rate: 21 findings over ~600 cited
sentences, none "wrong". Verification by a reader who did not write the pages remains the
step that finds them.

### Decisions made while building

- **Reconcile before merge.** Parallel digests do not see each other, so the same idea came
  back under three names (batch-normalization / batchnorm-pitfalls / batchnorm-backward-pass).
  A hand-written merge map between digest and merge fixed the canonical slugs; merge agents
  were told to create only mapped pages. This step is now part of the method for batches 2–4.
- **Coarser topics than the digests proposed.** Sub-steps of one idea (query/key/value,
  scaled attention, causal masking) are sections of `self-attention`, not pages; a page is
  created for an idea he explains, and a lecture explains a handful.
- **Claim relations kept minimal.** One `supports` pair (variance bug → avoid batchnorm) in
  the whole batch; cross-claim connections are labelled **Note:** lines. No `extends` or
  `contradicts`, so no new timeline. The 2025–2026 phase 1 claims are unrelated to 2022
  lecture material and were not forced into relations.
- **`makemore` artifact created from the lectures** before its README was merged (group B
  added the README). `repo_url` came from the manifest.
- **`tokenization` first_seen is 2023-01-08** (minGPT README mentions `bpe.py`) rather than
  the GPT lecture date.
- **Verify reports are per merge group**, not one per batch as validation.md said;
  `scripts/batches.py` reads every file in `staging/verify/`, so the count is the same.
  Side effect: the nanoGPT README (batch 4, a phase 1 source) shows as "verified" because
  a group B fix cited it and the report names it.

### Deviations from the plan

- Batch sizes 10 / 21 / 23 / 28, not 10 / 21 / 23 / 22 (the plan's draft miscounted
  batch 4).
- Digests were not strictly one agent per source: the three short READMEs shared one.
- The merge was three groups of 2–5 digests, not groups of "about five": group A1 created
  most of the shared topic pages and was the heaviest step (35 pages).
- Lint was not changed; the index split has not happened yet.

### Cost

About 2.4M agent tokens for batch 1 (digest ≈ 0.9M, merge ≈ 0.65M, verify ≈ 0.6M,
fix ≈ 0.1M), plus the coordinating session. Batches 2–4 together hold about 2.6× the words
of batch 1.

## Pilot gate

Batch 1 stopped for the user's review in Obsidian (decision 3). On 2026-10-24 the user
said "start batch 2" without reviewing, so decision 3 was waived for this phase. An early
question check on 2026-10-23 (`staging/phase-3-question-validation.md`) found the
backpropagation question answerable, and the agents and tokenization questions only
partly answerable until batch 2 is compiled. Batches 2–4 run with a merge map step added
for each.

## Batch 2

Ran 2026-10-24. 21 sources, May 2023 to July 2024, about 150k raw words: CS25, State of
GPT, Intro to LLMs, the tokenizer lecture, Sequoia 2024, the GPT-2 reproduction, the
Berkeley keynote, seven llm.c Discussions and seven short READMEs and posts.

| Step | How | Result |
|---|---|---|
| Index split | between batches, before any batch 2 merge | `wiki/index.md` links one file per type in `wiki/index/`; lint checks each page is in its type's file; 4 new tests (98 total) |
| Digest | 9 agents, 8 in parallel then 1; shared brief `staging/digest-brief.md` | 18 digests (52k words) |
| Reconcile | `staging/batch-2-merge-map.md`, written while the last digest ran | ~30 proposed topics and ~80 claims reduced to 11 new topics, 36 claims, 4 methods, 6 artifacts, 2 timelines |
| Merge | 4 sequential groups (C1 2023, C2 early 2024, C3 llm.c + llama2.c, C4 GPT-2 + Berkeley); shared brief `staging/merge-brief.md` | 94 → 182 pages |
| Verify | 4 fresh readers, each started as soon as its group was committed, in parallel with the next merge; shared brief `staging/verify-brief.md` | 31 findings: 3 wrong, 6 overstated, 7 mis-cited, 15 minor |
| Fix | 1 agent for all four reports, then a wiki-wide search for one class of error | 30 fixed, 1 left as is (the report asked for no change); 14 interval phrases replaced by dates |

Pages after batch 2: 37 sources, 40 topics, 64 claims, 12 artifacts, 15 methods,
3 timelines. Lint 0 findings; 98 tests pass; 45 raw files left (batches 3–4).

### What the verification caught

- **Published date is not when he said it.** CS25 was given around January 2023 and
  published in May, so "four months later" and "a week later" between sources were wrong.
  This is a schema issue, not a one-off: CLAUDE.md §2 now forbids intervals or orderings
  between sources computed from published dates, the merge and verify briefs carry the
  rule, and a search after the fix pass replaced 14 such phrases across batch 1 and 2
  pages (logged as a correction).
- **Order inside one source.** A failure he raises only at the end of the tokenizer
  lecture had been put into his opening list.
- **Hedges dropped.** "end of text token I think" written as fact; the GPT-2 run's 1.7
  hours was his projection at launch, not the measured time.
- **Invented purpose or connection.** TinyStories presented as his evidence for small
  models (the README cites the paper); the calorie app called a personal project outside
  his AI work (the README does not say so); both sides of the llm.c cross-check described
  with flags only one side used.

No verifier found a number that did not match its raw file, a quote that was not his, or
a host's words attributed to him.

### Decisions made while building

- **The index was split between batches**, not mid-merge, so merge agents saw one layout.
  The top `index.md` lists no pages and carries no counts, so ingest never has to update it.
- **Shared briefs.** Digest, merge and verify instructions live in `staging/*-brief.md`;
  each agent prompt names its sources and the few things specific to them. Prompts got
  shorter and the rules stayed the same across agents.
- **Verify overlaps merge.** Each group's verifier starts when that group is committed,
  while the next group merges; it checks only sentences citing its own sources. The fix
  pass runs once, after all groups. This cut wall-clock without two writers on `wiki/`.
- **A rule found mid-batch is pushed to running agents.** The published-date rule was sent
  to the C2 merge agent while it was writing the agents timeline.
- **Two timelines** (`llm-agents-over-time`, `llm-os-over-time`) record dated statements
  without asserting a change of view; their closing Notes say where views only
  accumulated. No `extends` or `contradicts` link was found in batch 2.
- **Profile README** (five words) is cited once as `context` on `nn-zero-to-hero` with a
  labelled Note, so its source page is not an orphan.
- **`llm101n` deferred to batch 3**, where its README is.

### Deviations

- The map left four methods without a group; groups were assigned after C1.
- Two claims assigned to C3 were stated only in C4 sources and moved to C4.
- Raw word count for the batch was ~150k; digests were 52k words, about a third.

### Cost

About 4.2M agent tokens for batch 2 (digest ≈ 1.3M, merge ≈ 1.1M, verify ≈ 0.8M,
fix ≈ 0.15M), plus the coordinating session.

### Gate questions after batch 2

The early check on 2026-10-23 found the agents and tokenization questions only partly
answerable. Batch 2 compiled the tokenizer lecture (with his failure list on
`tokenization` and `a-lot-of-llm-oddness-traces-back-to-tokenization`) and the 2023–2024
agent statements (`llm-agents-over-time`). The gate itself is re-run at the end of the phase.
