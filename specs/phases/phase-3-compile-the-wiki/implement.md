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
| Digest | 9 agents, 8 in parallel then 1; shared brief `staging/digest-brief.md` | 21 digests (52k words) |
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

## Batch 3

Ran 2026-10-24 and 2026-10-25 (paused overnight at the account usage limit, during the
last verification). 23 sources, August 2024 to October 2025; 2 were phase 1 sources, so 21
were compiled, about 133k raw words: No Priors, the CUDA keynote, Deep Dive, How I use
LLMs, Dwarkesh, the 2025 blog posts, the nanochat launch, LLM101n, llm.c README, rendergit.

| Step | Result |
|---|---|
| Digest | 8 agents in parallel, 21 digests |
| Reconcile | `staging/batch-3-merge-map.md`: 13 new topics, ~45 claims, 9 methods, 2 artifacts, 1 new timeline; many digest claims folded into existing pages (cognitive core, gym, ghosts, march of nines each became a second source) |
| Merge | 4 sequential groups (D1 Aug–Oct 2024, D2 Feb–Mar 2025, D3 Apr–Aug 2025, D4 Oct 2025); 182 → 265 pages |
| Verify | 4 fresh readers, each overlapping the next merge: 32 findings, 0 wrong, 9 overstated, 3 mis-cited, 20 minor |
| Fix | 1 agent; all 32 fixed; 33 pages changed; date-interval search found none computed between sources |

Pages after batch 3: 58 sources, 49 topics, 105 claims, 14 artifacts, 24 methods,
4 timelines. Lint 0 findings; 98 tests pass; 24 raw files left (batch 4).

### What the verification caught

- **Relations stronger than the texts.** The first `extends` links in the wiki were set
  from Deep Dive (2025) to two 2023 claims. One was the wrong relation: a 2023 statement of
  a then-current limitation is not broadened by a 2025 description of models that did not
  exist then (now a Note). The other was true but `supports` is weaker (CLAUDE.md: weakest
  true link). The self-improvement timeline now claims no more change than "hints" and
  "primordial" allow. The vibe-coding `extends` (deploying is harder than writing) was
  confirmed by its verifier.
- **Host's words as his.** No Priors: "he worked on the Tesla humanoid" was a host's
  question; "first course" was a host's phrase, and the interview never names LLM101n.
- **Numbers loosened.** "Gamed within tens of steps" for his "10 or 20 steps, not 100 or
  1,000"; the GPT-2 size he corrected himself on (1.5B, not 1.6B).
- **Reasons moved.** The broadcast-reward reason given for why RL beats imitation; he gives
  it for why RL is terrible.
- **Practice invented.** A How I use LLMs method said he uses text-to-speech; he does not
  say so.

### Decisions made while building

- The X post on Sutton is the blog body word for word: cited as a second location of one
  text, never as independent evidence.
- The Dwarkesh transcript has no speaker labels; spans the digest marked unclear were not
  attributed to him. His own figures win over the host's restatements (cognitive-core
  horizon: 20 years, not 10).
- Personal posts (calculator, digital hygiene, sleep tracker, grocery) got source pages,
  one recurring topic (user-hostile-technology), claims only where he takes a position,
  and methods for procedures he follows (digital-hygiene-checklist, append-and-review-note).
- A rule found mid-batch was again pushed to a running merge agent (D4 was told not to
  build on the self-improvement `extends` links the verifier had flagged).

### Cost

About 4.5M agent tokens (digest ≈ 1.4M, merge ≈ 1.2M, verify ≈ 0.95M, fix ≈ 0.25M).

## Batch 4

Ran 2026-10-25. 28 sources, October 2025 to August 2026; 4 were phase 1 sources, so 24
were compiled, about 60k raw words: the nanochat Discussions, verifiability, space of minds,
reader3, llm-council, hn-time-capsule, chemical hygiene, rustbpe, microgpt, autoresearch,
jobs, Skill Issue, the llm-wiki gist, Sequoia Ascent 2026, the 2026 micrograd README.

| Step | Result |
|---|---|
| Digest | 7 agents in parallel, 24 digests |
| Reconcile | `staging/batch-4-merge-map.md`: 3 new topics, 30 claims, 2 methods, 7 artifacts; timelines extended only |
| Merge | 4 groups (E1 Oct–Nov 2025, E2 Dec 2025–Feb 2026, E3 Mar 2026, E4 Apr–Aug 2026); 265 → 331 pages; backlog 0 |
| Verify | 4 fresh readers: 28 findings, 0 wrong, 5 overstated, 1 mis-cited, 22 minor |
| Fix | all 28 fixed; then `scripts/quote_check.py` (new) found 21 suspect inline quotes: 7 misquotes made verbatim, 7 non-quotes unquoted, 1 method step reworded, 6 already verbatim; then 2 prompt strings made verbatim |

### Schema changes

- **AI-written text is never his** (CLAUDE.md §3, 2026-10-25). Autoresearch Discussion #43
  was written by the agent; most of the Sequoia Ascent 2026 post was written by Codex,
  with only the intro his. Those parts are described as what they are and never cited as
  his view; the talk itself is cited for what he said. Merge and verify briefs carry the
  rule. No earlier source was found to contain AI-written text, so no migration.
- **No new date rule violations.** Searches after batches 3 and 4 found only intervals he
  states himself.

### The first real change of view

He states it himself in Skill Issue (2026-03-20): in December something flipped, and he
went from writing most of his code to delegating most of it to agents. The Dwarkesh
interview (2025-10-17) had autocomplete as his sweet spot "for now". Per invariant 6 the
old claim stays, the new dated claim `he-now-delegates-most-coding-to-agents` `extends`
it, and `vibe-coding-over-time` says that entries up to the 2025-12-19 review accumulated
and that this one records a change he states. The Sequoia Ascent talk is its second
source. Two more `extends` links (agentic engineering after weekend projects; neural nets
as host process after the LLM kernel) were confirmed by their verifier.

## Phase totals

| | Batch 1 | Batch 2 | Batch 3 | Batch 4 | Total |
|---|---|---|---|---|---|
| Sources compiled | 10 | 21 | 21 | 24 | 76 (+6 from phase 1) |
| Pages after batch | 94 | 182 | 265 | 331 | 331 |
| Verification findings | 21 | 31 | 32 | 28 | 112 |
| of which wrong | 0 | 3 | 0 | 0 | 3 |
| Agent tokens (approx.) | 2.4M | 4.2M | 4.5M | 3.9M | 15M |

Final wiki: 82 sources, 52 topics, 135 claims, 21 artifacts, 26 methods, 4 timelines.
Lint 0 findings, 0 raw files uncompiled; 342 inline quotes verbatim against their cited
raw; 101 tests pass. One ingest entry per source in `log.md`; 10 correction entries.

What the method found across the phase: verification by a reader who did not write the
pages caught ~1 issue per 20 sentences, almost all overstatement, mis-citation, or a
host's or paper's words given to him; none was a number not in the source. Three classes
of error recurred across batches and became rules or tools rather than one-off fixes:
intervals computed from published dates (CLAUDE.md §2), AI-written text in his sources
(§3), and inline quotes lint could not see (`quote_check.py`).

## Query answer format (2026-10-26)

After batch 4 the user found query answers unhelpful: a fresh session answered the
backprop question as a bullet inventory with a citation on every line, which tells you
where things are written rather than explaining them. That was the old Query procedure
doing what it said ("answer with citations to wiki source pages", with invariant 3's
sentence-level citations). CLAUDE.md §7 Query now asks for a plain-language explanation
first, in short paragraphs, citations at the end of each paragraph or in a Sources list,
and a closing "More detail" line linking the wiki pages. Wiki pages are unchanged; the
evidence rules (invariants 7–9) still apply to every statement in an answer. A fresh-reader
test of two gate questions under the new procedure produced readable explanations; it also
wrote "December 2025" where he says only "December", so the procedure now says never to add
a year he did not give. The fuller teaching voice (his style, built up from scratch) is
still phase 4.
