---
type: artifact
repo_url: https://github.com/karpathy/nanoGPT
language: Python
status: superseded
sources: ["[[github-2025-11-12-nanogpt-readme]]", "[[github-2026-07-03-nanochat-readme]]", "[[youtube-2025-06-19-software-is-changing]]"]
aliases: [nanoGPT]
---
# nanoGPT
His earlier repo for training and finetuning medium-sized GPTs, a rewrite of minGPT that he says prioritises "teeth over education" ([[github-2025-11-12-nanogpt-readme]] §intro).

## What it demonstrates
- Plain, readable code: a roughly 300-line training loop and a roughly 300-line GPT model that can load OpenAI's GPT-2 weights ([[github-2025-11-12-nanogpt-readme]] §intro).
- Reproducing GPT-2 (124M) on OpenWebText in about four days on one 8×A100 node ([[github-2025-11-12-nanogpt-readme]] §intro).
- A beginner path: train a character-level GPT on Shakespeare first ([[github-2025-11-12-nanogpt-readme]] §quick start).
- Finetuning is the same as training, starting from a pretrained checkpoint with a smaller learning rate ([[github-2025-11-12-nanogpt-readme]] §finetuning).
- Deprecated since November 2025 in favour of nanochat, and kept up for posterity ([[github-2025-11-12-nanogpt-readme]] §intro).
- nanochat takes its name from it and describes it as covering pretraining only, in contrast to nanochat's full chat pipeline ([[github-2026-07-03-nanochat-readme]] §Acknowledgements).
- In the YC talk he uses it as an example of a repo with a human-only GitHub interface, which gitingest or DeepWiki make readable to an LLM ([[youtube-2025-06-19-software-is-changing]] @36:40).

## Related
- [[nanochat]]
- [[building-for-agents]]
