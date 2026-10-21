---
type: artifact
repo_url: https://github.com/karpathy/nanochat
language: Python
status: active
sources: ["[[github-2026-07-03-nanochat-readme]]", "[[blog-2025-12-19-year-in-review-2025]]"]
aliases: [nanochat]
---
# nanochat
A minimal, hackable harness that trains a ChatGPT-style model end to end on one GPU node, covering tokenization, pretraining, finetuning, evaluation and inference ([[github-2026-07-03-nanochat-readme]] §intro).

## What it demonstrates
- One complexity dial: `--depth` sets every other hyperparameter so each model is compute-optimal ([[github-2026-07-03-nanochat-readme]] §Research).
- A model that beats GPT-2's DCLM CORE score in about two hours on an 8×H100 node, roughly $48 at the README's assumed $24/hour, against about $43,000 to train GPT-2 in 2019 ([[github-2026-07-03-nanochat-readme]] §Leaderboard).
- A "time to GPT-2" leaderboard, borrowed from modded-nanogpt, to drive speedups ([[github-2026-07-03-nanochat-readme]] §Leaderboard, §Acknowledgements).
- Simplicity as a goal: no giant config objects, model factories or if-then-else monsters ([[github-2026-07-03-nanochat-readme]] §Contributing).
- Contributors must disclose substantial LLM-written code ([[github-2026-07-03-nanochat-readme]] §Contributing).
- Its BPE tokenizer in Rust was vibe-coded ([[blog-2025-12-19-year-in-review-2025]] §5).

## Related
- [[nanogpt]] — its predecessor, now deprecated in its favour
- [[quick-experiment-loop]]
- [[vibe-coding]]
- [[building-for-agents]]
