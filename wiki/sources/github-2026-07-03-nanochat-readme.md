---
type: source
raw_path: raw/github/karpathy__nanochat.md
published: 2026-07-03
medium: github
summary: README of nanochat, a minimal single-node harness that trains a GPT-2-grade chat model end to end, controlled by one depth dial.
url: https://github.com/karpathy/nanochat
title: nanochat README
---
# nanochat README
Raw: [[raw/github/karpathy__nanochat]] · Original: https://github.com/karpathy/nanochat

Dated by the README's last commit (the repo was created 2025-10-13).

## Summary
nanochat trains a GPT-2-capability model on one 8×H100 node for about $48 and lets you chat
with it from a CLI (§intro). Every hyperparameter is derived from a single `--depth` dial
(§Research). A "time to GPT-2" leaderboard drives pretraining speedups (§Leaderboard). The
README describes his quick experiment loop on a d12 model (§Research), states a goal of
low cognitive complexity with no configuration monsters (§Contributing), asks contributors to
disclose LLM-written code (§Contributing), and points readers to DeepWiki for questions (§intro).

## Key points
- What the repo is and how it is built → [[nanochat]]
- Lineage from nanoGPT → [[nanogpt]]
- Change one thing, rerun d12, read the plots → [[quick-experiment-loop]]
- Recommends DeepWiki, an LLM-generated view of the repo → [[building-for-agents]]

## Fed pages
- [[microgpt]]
- [[small-scale-tuning-does-not-always-transfer]]
- [[nanochat]]
- [[nanogpt]]
- [[quick-experiment-loop]]
- [[building-for-agents]]
