---
type: source
raw_path: raw/github/karpathy__autoresearch__discussion-43.md
published: 2026-03-08
medium: github
summary: "An automated session report written and posted by an autoresearch agent (Claude) on his behalf: 126 five-minute training experiments on one H100 over about 10.5 hours, with a kept/discarded log that the agent reports lowering val_bpb from 0.9979 to 0.9697."
url: https://github.com/karpathy/autoresearch/discussions/43
title: "Session report: 0.9979 → 0.9697 in 126 experiments — weight decay on everything + init scaling"
---
# Session report: 0.9979 → 0.9697 in 126 experiments — weight decay on everything + init scaling
Raw: [[raw/github/karpathy__autoresearch__discussion-43]] · Original: https://github.com/karpathy/autoresearch/discussions/43

Locations: `§intro` (text before `## Highlights`), `§Highlights`, `§Full experiment log`, `§Metadata`, `§How this report was generated`.

## Summary
**This post was written by an agent, not by him.** It calls itself an automated post from an autoresearch agent running on his behalf, and its Metadata names the agent as Claude (Anthropic) (§intro, §Metadata); the raw's author field is the account it was posted under. Nothing in it, title, highlights, interpretations or the closing instructions to other agents, is his wording or opinion, and no claim page cites it. It is the agent's report of one overnight session on the repo's training script: starting from wins reported in an earlier discussion, #32 (not in raw/), it ran 126 experiments on one H100 in about 10.5 hours of wall time, kept 23 changes, discarded 102 and had 1 crash, and reports val_bpb falling from 0.997900 to 0.969686 (§intro, §Metadata, §Highlights). Every experiment is listed with its val_bpb, its delta against the best so far, and keep or discard (§Full experiment log). The report says weight decay on embeddings and value embeddings stacked for about 0.0028 of improvement, but the kept weight-decay rows in its own log sum to about 0.0017; the mismatch is the report's, and is not reconciled here (§Highlights, §Full experiment log).

## Key points
- What an autoresearch session produces, as the agent reports it: a keep/discard log against one metric → [[autoresearch]]

## Fed pages
- [[autoresearch]]
