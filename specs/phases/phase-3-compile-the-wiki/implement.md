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

## Pilot gate (open)

Batch 1 stops here for the user's review in Obsidian (decision 3). Batches 2–4 run after
that review, with the merge map step added for each.
