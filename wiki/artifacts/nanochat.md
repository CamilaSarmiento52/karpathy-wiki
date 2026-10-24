---
type: artifact
repo_url: https://github.com/karpathy/nanochat
language: Python
status: active
sources: ["[[github-2026-07-03-nanochat-readme]]", "[[blog-2025-12-19-year-in-review-2025]]", "[[github-2025-10-13-nanochat-discussion-introducing]]", "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
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

**The launch post (2025-10-13).** The Discussion that introduced nanochat walks through `speedrun.sh`, which aims at "the best ChatGPT that $100 can buy" ($100: target) and runs start to end on a blank 8×H100 box, about $24/hour to rent (comparison) ([[github-2025-10-13-nanochat-discussion-introducing]] §Environment setup, §intro). The tags follow the source page's legend.
- Stages in order: tokenizer training, pretraining, midtraining, SFT, optional RL, then chat by CLI or a web UI ([[github-2025-10-13-nanochat-discussion-introducing]] §Train the tokenizer, §Pretraining, §Midtraining, §Supervised Finetuning (SFT), §Reinforcement Learning (RL)).
- The default model is d20: 20 layers, 1280 channels, 10 heads of dim 128, about 560M parameters (setting) ([[github-2025-10-13-nanochat-discussion-introducing]] §Pretraining).
- The base model reaches CORE 0.22 (measured), a little above GPT-2 large at 0.21 and a little below GPT-2 xl at 0.26 (comparison), for about $72 at three hours of rental (estimate) ([[github-2025-10-13-nanochat-discussion-introducing]] §Pretraining).
- Up to and including SFT the run took 3h51m (measured), $92.4 at $24/hour (estimate from measured time and the rental price); with RL it was closer to 5 hours (measured, approximate), and he notes $8 left for ice cream ([[github-2025-10-13-nanochat-discussion-introducing]] §Report card).
- An auto-generated `report.md` records the run and a stage-by-stage metric table, plus the code size: 8,304 lines in 44 files (measured, of the codebase) ([[github-2025-10-13-nanochat-discussion-introducing]] §Report card).
- Inference uses a custom `Engine` class with a KV cache, prefill and decode, and a Python-interpreter tool ([[github-2025-10-13-nanochat-discussion-introducing]] §Pretraining).
- `--depth` is the single slider: channels, learning rates and the rest follow from it, and he says deeper and longer gives strictly better results; for GPT-2 capability, CORE about 0.25, he suggests trying d26 (target) ([[github-2025-10-13-nanochat-discussion-introducing]] §Your turn).
- He calls the project "nowhere near tuned enough" ([[github-2025-10-13-nanochat-discussion-introducing]] §Supervised Finetuning (SFT)).
- The Rust tokenizer exists because minbpe's Python is too slow and Hugging Face `tokenizers` too bloated and confusing; see [[tokenization]] ([[github-2025-10-13-nanochat-discussion-introducing]] §Environment setup).

**Note:** the 2026 README and this post report different runs and code states: the README's GPT-2-grade CORE in about two hours for about $48, the post's d20 at CORE 0.22 in 3h51m for $92.4 up to SFT; both use $24/hour for the node. They are given with their dates, not as a change ([[github-2026-07-03-nanochat-readme]] §Leaderboard; [[github-2025-10-13-nanochat-discussion-introducing]] §Report card).

**In the Dwarkesh interview (published 2025-10-17).** He calls nanochat the simplest complete repository for the end-to-end pipeline of a ChatGPT clone, released a day or two before the recording in his words, and about 8,000 lines in his spoken figure ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @27:31, @28:09, @28:48). He says he did not necessarily learn anything new building it; it was the mechanical work of making it clean enough to learn from ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @28:09). The chunk-by-chunk building process is missing from the final repo, and he plans to add it, probably as a video ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @29:27). It syncs gradients in its own optimizer step instead of PyTorch's DDP container ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @32:36). He calls it the capstone of LLM101n and a ramp to knowledge ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @2:02:21, @2:03:02).

## Related
- [[nanogpt]] — its predecessor, now deprecated in its favour
- [[pretraining-and-finetuning]] — the stages it runs, midtraining included
- [[llm-evaluation]] — CORE, bits per byte and ChatCORE
- [[quick-experiment-loop]]
- [[vibe-coding]]
- [[building-for-agents]]
