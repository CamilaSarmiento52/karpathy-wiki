# Digest: Session report: 0.9979 → 0.9697 in 126 experiments — weight decay on everything + init scaling
- raw: raw/github/karpathy__autoresearch__discussion-43.md · published: 2026-03-08 · medium: github · words: 2489 (frontmatter)
- source slug: github-2026-03-08-autoresearch-session-report

**Authorship, read first.** The post opens by saying it is "an automated post from an
autoresearch agent running on behalf of @karpathy" (§intro), and its Metadata names the agent
as "Claude (Anthropic)" (§Metadata). The raw's `author: Andrej Karpathy` is the account it was
posted under. **Nothing in this file is written by him**: not the title, the highlights, the
interpretations ("big deal", "fragile", "load-bearing"), nor the "How this report was
generated" section, which addresses other agents. So this digest proposes **no claims** from
it, and every statement below is attributed to "the report" or "the agent". It can be cited
only for what the agent's run reported, never for his views.

Location scheme: `§intro` (text before `## Highlights`), `§Highlights`, `§Full experiment log`,
`§Metadata`, `§How this report was generated`.

Number tags used below: **[agent-reported]** a result the agent's post reports from its own
run (not checked by him in this source); **[setting]** a configuration value; **[count]** a
tally of experiments or time. No number in this source is measured or stated by him.

## Source page
```
---
type: source
raw_path: raw/github/karpathy__autoresearch__discussion-43.md
published: 2026-03-08
medium: github
summary: "An automated session report written and posted by an autoresearch agent (Claude) on his behalf: 126 five-minute training experiments on one H100 over about 10.5 hours, with a kept/discarded log that lowers val_bpb from 0.9979 to 0.9697."
url: https://github.com/karpathy/autoresearch/discussions/43
title: "Session report: 0.9979 → 0.9697 in 126 experiments — weight decay on everything + init scaling"
---
# Session report: 0.9979 → 0.9697 in 126 experiments — weight decay on everything + init scaling
Raw: [[raw/github/karpathy__autoresearch__discussion-43]] · Original: https://github.com/karpathy/autoresearch/discussions/43

This post was written by an agent, not by him: it calls itself an automated post from an
autoresearch agent running on his behalf, and names the agent as Claude (§intro, §Metadata).
Nothing here is his own wording or opinion.

## Summary
An autoresearch agent's report of one overnight session on the repo's training script,
posted to the repo's Discussions on his behalf (§intro). The agent says it began from wins
reported in an earlier discussion, #32, and then explored new changes (§intro). Over 126
experiments on one H100, about 10.5 hours of wall time, it kept 23 changes, discarded 102
and had 1 crash, and reports validation bits per byte falling from 0.997900 to 0.969686
(§Metadata, §Highlights). The largest single gain it reports is halving the batch size, which
it attributes to fitting more steps into the fixed 5-minute budget; its reported new findings
are small weight decay on embeddings and value embeddings and a reduced initialization
scale (§Highlights). Every experiment is listed with its val_bpb, its delta against the
best-so-far, and keep or discard (§Full experiment log), and the report closes with
instructions for other agents on producing and posting such reports (§How this report was
generated).

## Key points
- What an autoresearch session produces: a keep/discard experiment log against one metric, run and reported by the agent → [[autoresearch]]
- The loop as run by an agent: one change, a fixed 5-minute run, compare val_bpb, keep or discard → [[quick-experiment-loop]]
- The training code tuned is a simplified nanochat; the report tunes its depth, windows, learning rates, weight decay and init → [[nanochat]]

## Fed pages
- [[autoresearch]]
- [[quick-experiment-loop]]
- [[nanochat]]
```

## Candidates

### artifact: autoresearch
- existing: no (new; slug given in the prompt). Built mainly from [[github-2026-03-21-autoresearch-readme]]; this source adds what a session's output looks like.
- aliases: autoresearch
- statements (all attributed to the agent's report):
  - The report says it is an automated post from an autoresearch agent running on his behalf, and names the agent as Claude (Anthropic) (§intro, §Metadata).
  - The session ran on one NVIDIA H100 80GB, on branch `autoresearch/mar8`, for about 10.5 hours of wall time (§Metadata). [setting; ~10.5 h: count]
  - It ran 126 experiments: 23 kept, 102 discarded, 1 crash (§Metadata). [count; the log's rows tally to the same numbers, with the baseline row counted as a keep]
  - The report gives val_bpb going from 0.997900 at baseline to 0.969686 at best, an improvement of 0.0282 (§Highlights). [agent-reported]
  - The agent says it started from changes reported in discussion #32 (batch halving, depth 9, SSSSL window pattern, RoPE base 200K) and then explored new territory (§intro, §Highlights). [#32 is not in raw/]
  - The experiment log is kept in a `results.tsv` file with commit, val_bpb, memory, status and description; each delta is computed against the best val_bpb so far, the most recent keep, and negative means improvement (§How this report was generated).
  - The report gives other agents GitHub GraphQL commands to post a report to Discussions and to read existing discussions for inspiration before a run (§How this report was generated). **Note:** this section is agent-written, addressed to agents; it is not his documentation.
- relation: none to claims.

### method (existing): quick-experiment-loop
- existing: yes (built from [[github-2026-07-03-nanochat-readme]] §Research)
- statements (agent's report, as evidence of what the loop looks like when an agent runs it):
  - Each row of the log is one change, run and judged by val_bpb, then kept or discarded (§Full experiment log).
  - The report attributes its largest gain, halving the batch from 524K to 262K (-0.0119), to fitting more steps into 5 minutes (§Highlights). [agent-reported]
  - It reports that deeper or wider models (depth 10 or 11 with larger dim) lost because they got too few steps in 5 minutes (§Highlights). [agent-reported]
- **Note for merge:** these show the fixed time budget shaping what wins; the README states the budget as a design choice ([[github-2026-03-21-autoresearch-readme]] §Design choices). Cite this source only for what the agent reported.

### artifact (existing): nanochat
- existing: yes
- statements (agent's report):
  - Its reported final config is depth 9, dim 512, batch 262K, SSSSL window, short window 1/8 of context, RoPE base 200K, embedding LR 0.9, unembedding LR 0.005, init scale 0.68x, x0_lambda 0.05, FINAL_LR_FRAC 0.05, warmdown 0.75, value-embedding WD 0.003, embedding WD 0.001, lm_head WD 0.01, Muon momentum warmup 200 steps (§Metadata). [setting, as found by the agent]
  - New findings it reports: tiny weight decay on embeddings (0.001) and on value embeddings (stepped 0.001, 0.002, 0.003) stacked to about 0.0028, with 0.005 on value embeddings regressing; a transformer init scale of 0.68x, with 0.66x and 0.65x regressing; a nonzero final LR fraction of 0.05; WD 0.01 on lm_head; warmdown 0.75 (§Highlights). [agent-reported]
  - Dead ends it reports: weight tying (+2.24 BPB, "completely broken" in its words), parallel attention and MLP (+0.011), multi-query attention with one KV head (+0.008), removing the cautious WD mask (+0.005), zero x0_lambda init (+0.004) (§Highlights). [agent-reported]
  - It reports that two #32 changes did not reproduce, 5% warmup (+0.0008) and seed 137 (+0.0007) (§Highlights). [agent-reported]
- **Note for merge:** this is the autoresearch repo's simplified, single-GPU train.py ([[github-2026-03-21-autoresearch-readme]] §intro), not nanochat itself; whether to put any of it on [[nanochat]] at all is a merge decision. Low priority; the autoresearch page is the natural home.

## Quotes
All three are the agent's words, not his. Use them only with that attribution, or not at all.
- "This is an automated post from an autoresearch agent running on behalf of @karpathy." (§intro)
- "This was the best discovery of the session." (§Highlights)
- "These things are fragile." (§Highlights)

## Notes for merge
- **Authorship.** Agent-written from end to end (§intro, §Metadata). No claim, quote or opinion from this source may be attributed to him. The raw frontmatter's `author` is the account, not the writer.
- **The agent's arithmetic does not reconcile.** §Highlights says weight decay on embeddings and value embeddings "stacked for ~0.0028 total improvement"; the kept WD rows in the log (embedding WD 0.001: -0.000088; VE WD 0.001: -0.000951; 0.002: -0.000403; 0.003: -0.000222) sum to about 0.0017, or about 0.0022 with the embedding-LR-0.9-with-WD and lm_head-WD keeps added. Do not repeat the 0.0028 figure without saying it is the report's own.
- **"Top 7 wins" table** rounds the log's deltas (e.g. -0.011859 → -0.0119); consistent.
- **Not the same run as the X post** [[x-2026-03-09-autoresearch-tuning-nanochat]]: that post describes autoresearch tuning nanochat itself at depth=12 for about 2 days and about 700 changes; this report is 126 experiments in about 10.5 hours on the autoresearch repo's own train.py (the report calls depth 9 an "extra layer", §Highlights). Some findings overlap in kind (value-embedding regularization, init, weight-decay schedule, banded-attention window), but do not write that they are the same run or that one confirms the other.
- Discussion #32, which the agent cites as its starting point, is not in raw/.
- The embedded progress image is not described in the text; nothing to cite from it.
