---
type: source
raw_path: raw/x/2031135152349524125.md
published: 2026-03-09
medium: x
summary: "He reports that autoresearch, left tuning nanochat's depth=12 model for about two days, found about 20 changes that transferred to depth=24 and cut the Time to GPT-2 leaderboard figure from 2.02 to 1.80 hours, and predicts that all frontier labs will do this."
url: https://x.com/karpathy/status/2031135152349524125
title: Three days ago I left autoresearch tuning nanochat for ~2 days on depth=12…
---
# Three days ago I left autoresearch tuning nanochat for ~2 days on depth=12…
Raw: [[raw/x/2031135152349524125]] · Original: https://x.com/karpathy/status/2031135152349524125

One post, cited `#1`. His relative dates ("Three days ago", "yesterday", "today") are quoted, not converted. The ~20 and ~700 changes are counts from the agent's run, which he reports; the transfer test and the 2.02 → 1.80 hours are his own measurements.

## Summary
A single X post on the first round of autoresearch on nanochat (#1). He says he left it tuning a depth=12 model for about two days, that it found about 20 changes that improved validation loss, and that when he tested them all were additive and transferred to depth=24; stacked, they took the leaderboard's "Time to GPT-2" from 2.02 to 1.80 hours (#1). He calls it a first for him, after two decades of doing this optimisation by hand, and lists the bigger findings, including oversights in his own code (#1). He says it is not novel research yet but the adjustments are real (#1). He predicts all LLM frontier labs will do this, through swarms of agents tuning small models and promoting ideas to larger scales, and says any metric that is reasonably efficient to evaluate, or has an efficient proxy, can be autoresearched (#1).

## Key points
- The first round of autoresearch on nanochat: ~20 changes, transfer to depth=24, 2.02 → 1.80 hours → [[autoresearch]], [[nanochat]]
- Real improvements, not novel research yet → [[autoresearch-found-real-improvements-to-nanochat]]
- Frontier labs will all do this; swarms of agents, promotion to larger scales → [[all-frontier-labs-will-autoresearch]]
- His manual loop for two decades, and the agent running it end to end → [[quick-experiment-loop]]
- An agent working autonomously through about 700 changes, humans optionally on the edges → [[llm-agents-over-time]], [[llm-self-improvement-over-time]]

## Fed pages
- [[autoresearch]]
- [[nanochat]]
- [[autoresearch-found-real-improvements-to-nanochat]]
- [[all-frontier-labs-will-autoresearch]]
- [[quick-experiment-loop]]
- [[llm-agents-over-time]]
- [[llm-self-improvement-over-time]]
