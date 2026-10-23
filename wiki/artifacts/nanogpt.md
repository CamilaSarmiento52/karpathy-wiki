---
type: artifact
repo_url: https://github.com/karpathy/nanoGPT
language: Python
status: superseded
sources: ["[[github-2023-01-08-mingpt-readme]]", "[[youtube-2023-01-17-gpt-from-scratch]]", "[[github-2023-01-31-ng-video-lecture-readme]]", "[[github-2025-11-12-nanogpt-readme]]", "[[github-2026-07-03-nanochat-readme]]", "[[youtube-2025-06-19-software-is-changing]]"]
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

- The minGPT side of the handover, two years earlier: in January 2023 he marked minGPT semi-archived and pointed to nanoGPT as his rewrite, because minGPT's wide adoption in notebooks, blogs, courses and books made large changes harder, and because he wanted code that stays simple and hackable but has teeth, reproducing medium-sized industry benchmarks and accepting some tradeoffs for runtime efficiency ([[github-2023-01-08-mingpt-readme]] §intro).
- In January 2023 he describes nanoGPT as two files of about 300 lines each, one defining the GPT model and one training it on any text; trained on OpenWebText it reproduces GPT-2's smallest, 124M model, which proves the codebase is arranged correctly and can load OpenAI's weights ([[youtube-2023-01-17-gpt-from-scratch]] @05:36, @06:12). The GPT lecture's goal is to write this repository from scratch ([[youtube-2023-01-17-gpt-from-scratch]] @06:45).
- `train.py` adds checkpointing, pretrained weights, learning-rate decay, model compilation and distributed training; `model.py` is almost identical to the lecture code, with the heads batched in one causal self-attention module, GELU instead of ReLU so OpenAI checkpoints load, and parameters split into weight-decayed and not ([[youtube-2023-01-17-gpt-from-scratch]] @1:46:28, @1:47:01, @1:47:36, @1:48:10).
- nanoGPT focuses on the pretraining stage; the finetuning stage that makes an assistant is much harder to replicate ([[youtube-2023-01-17-gpt-from-scratch]] @1:54:16).
- Two weeks after the lecture, the ng-video-lecture README points to the `# init all weights` comment and the `_init_weights` function in nanoGPT's `model.py` as the proper weight initialisation the lecture code lacks ([[github-2023-01-31-ng-video-lecture-readme]] §intro).

## Related
- [[weight-initialization]]
- [[ng-video-lecture]] — the lecture code that builds toward it
- [[self-attention]], [[transformer-architecture]], [[pretraining-and-finetuning]]
- [[mingpt]] — the predecessor it rewrote
- [[small-hackable-educational-code]]
- [[nanochat]]
- [[building-for-agents]]
