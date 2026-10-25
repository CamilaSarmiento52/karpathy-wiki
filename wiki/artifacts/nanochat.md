---
type: artifact
repo_url: https://github.com/karpathy/nanochat
language: Python
status: active
sources: ["[[github-2026-07-03-nanochat-readme]]", "[[blog-2025-12-19-year-in-review-2025]]", "[[github-2025-10-13-nanochat-discussion-introducing]]", "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]", "[[github-2025-10-24-nanochat-strawberry-guide]]", "[[github-2025-11-20-nanochat-d34-model]]"]
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

**Teaching d32 to count letters (2025-10-24).** He taught nanochat d32 to count the r's in "strawberry" as an example of how any arbitrary computing capability can be added, with a new `SpellingBee` task under `tasks/` and a simpler `SimpleSpelling` task mixed into midtraining and SFT; the procedure is [[teach-a-capability-with-synthetic-tasks]] ([[github-2025-10-24-nanochat-strawberry-guide]] §intro, §Spelling). The d32 deployed on nanochat.karpathy.ai can count letters now, he says ([[github-2025-10-24-nanochat-strawberry-guide]] §Summary). This post gives no size or cost for d32 ([[github-2025-10-24-nanochat-strawberry-guide]] §intro).

**The d34 model (2025-11-20).** He trained d34 and uploaded it to Hugging Face as `karpathy/nanochat-d34` ([[github-2025-11-20-nanochat-d34-model]] §intro). It was pretrained with `--depth=34 --device_batch_size=4 --target_param_data_ratio=40` (settings) on an 8×H100 node for about 100 hours, about 4 days (measured, approximate), at a cost of about $2,500 (his rounded cost; no hourly rate is given in the post) ([[github-2025-11-20-nanochat-d34-model]] §intro). The base model reaches CORE 0.3382 (measured), against d32 at 0.3168, the d20 speedrun at 0.22 and GPT-2 at 0.25 (comparison); he calls d32 a "$1000 run" (comparison, no time given) ([[github-2025-11-20-nanochat-d34-model]] §intro). ChatCORE rose from d32's 0.27 to 0.41 (measured); see [[llm-evaluation]] ([[github-2025-11-20-nanochat-d34-model]] §intro). d34 is now deployed live on nanochat.karpathy.ai ([[github-2025-11-20-nanochat-d34-model]] §intro). **Note:** this post gives the cost of a model past GPT-2 on CORE, not a time-to-GPT-2 figure; each cost and time on this page is given with its own source and date, with no order between them ([[github-2025-11-20-nanochat-d34-model]] §intro; [[github-2025-10-13-nanochat-discussion-introducing]] §Report card). The GPT-2 CORE is 0.25 here and 0.26 for GPT-2 xl in the launch post, likely rounding of nearby figures, not reconciled ([[github-2025-11-20-nanochat-d34-model]] §intro; [[github-2025-10-13-nanochat-discussion-introducing]] §Pretraining).

## Related
- [[nanogpt]] — its predecessor, now deprecated in its favour
- [[pretraining-and-finetuning]] — the stages it runs, midtraining included
- [[llm-evaluation]] — CORE, bits per byte and ChatCORE
- [[quick-experiment-loop]]
- [[teach-a-capability-with-synthetic-tasks]] — adding an ability with a synthetic task
- [[vibe-coding]]
- [[building-for-agents]]
