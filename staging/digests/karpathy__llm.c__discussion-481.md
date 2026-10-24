# Digest: Reproducing GPT-2 (124M) in llm.c in 90 minutes for $20
- raw: raw/github/karpathy__llm.c__discussion-481.md · published: 2024-05-28 · medium: github · words: 3250
- source slug: github-2024-05-28-llmc-gpt-2-124m

## Source page
```
---
type: source
raw_path: raw/github/karpathy__llm.c__discussion-481.md
published: 2024-05-28
medium: github
summary: "His walkthrough of training GPT-2 (124M) from scratch in llm.c on 10B FineWeb tokens in about 90 minutes and $20 on one 8×A100 node, with every flag explained, how to read the training log, how he evaluates against OpenAI's checkpoint, a 350M run, and an FAQ on why GPT-2."
url: https://github.com/karpathy/llm.c/discussions/481
title: Reproducing GPT-2 (124M) in llm.c in 90 minutes for $20
---
# Reproducing GPT-2 (124M) in llm.c in 90 minutes for $20
Raw: [[raw/github/karpathy__llm.c__discussion-481]] · Original: https://github.com/karpathy/llm.c/discussions/481

## Summary
He reproduces GPT-2 (124M), the smallest model OpenAI released in 2019, in llm.c (about 4,000 lines of C/CUDA): on one 8×A100 80GB node at up to ~60% model flops utilisation it takes about 90 minutes, about $20 at ~$14/hour, training on 10B tokens of FineWeb (§intro). His run beats OpenAI's checkpoint on FineWeb validation loss, which he says is not a fair comparison because GPT-2 was trained on different data, and reaches 29.9 on HellaSwag against GPT-2 (124M)'s 29.4 and the GPT-3 paper's 33.7 for a 124M model trained on 300B tokens (§intro). He gives the full setup and explains each flag, most following the GPT-3 paper because it is more detailed than GPT-2's, then explains how to read a log line: MFU, tokens per second, loss as perplexity, and gradient norm with clipping at 1.0 (§intro). He covers tokenizer generation, very hacky sampling, the code's layout, and an overnight 350M run on 30B tokens for about $200 (§intro). The FAQ says the model is pretraining only, not chat, that llm.c is C/CUDA only, and that he cares about GPT-2 because it was the first recognisably modern LLM stack with released weights (§intro).

## Key points
- 124M in ~90 min / ~$20 on 8×A100, 350M in 14 h / ~$200, code layout, FAQ → [[llm-c]]
- FineWeb val vs HellaSwag, why val loss against OpenAI's checkpoint is unfair, HellaSwag favouring web-like data → [[llm-evaluation]]
- Hyperparameters from the GPT-3 paper: 0.5M-token batch, LR 6e-4, 700-step warmup, decay to 0, weight decay 0.1 on 2-D weights, clipping at 1.0 → [[gradient-descent]]
- Reading a log line: loss as perplexity, gradient norm spikes, MFU → [[training-diagnostics]]
- exp(loss) as the number of tokens the model is effectively guessing among → [[loss-functions]]
- MFU, memory-bound training, GELU recompute, ZeRO-1 → [[gpu-training-efficiency]]
- 6ND compute estimates, 10X compute and cost per model step → [[training-compute-budget]]
- GPT-2 as the grand-daddy of LLMs; GPT-3 and Llama 3 differences → [[gpt-2-is-the-first-recognizably-modern-llm-stack]], [[transformer-architecture]]
- His 124M beats OpenAI's 124M on HellaSwag with 10B tokens → [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- Pretraining only, no chat finetuning; CPU users can finetune OpenAI's weights → [[pretraining-and-finetuning]]
- `train_gpt2.py` as a parallel reference for error checking, without full parity → [[pytorch]], [[verify-gradients-against-pytorch]]
- Started as 1,000 clean lines of C, now ~3,500; plans to rebuild it piece by piece → [[small-hackable-educational-code]]

## Fed pages
- [[llm-c]]
- [[llm-evaluation]]
- [[gradient-descent]]
- [[training-diagnostics]]
- [[loss-functions]]
- [[gpu-training-efficiency]]
- [[training-compute-budget]]
- [[transformer-architecture]]
- [[gpt-2-is-the-first-recognizably-modern-llm-stack]]
- [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- [[pretraining-and-finetuning]]
- [[pytorch]]
- [[verify-gradients-against-pytorch]]
- [[small-hackable-educational-code]]
```

## Candidates
### artifact: llm-c
- existing: no
- statements:
  - llm.c is about 4,000 lines of C/CUDA (§intro). [his count, 2024-05-28]
  - GPT-2 (124M), 12 layers, 12 heads, 768 dimensions, trained from scratch on 10B FineWeb tokens on one 8×A100 80GB SXM node in about 90 minutes, about $20 at ~$14/hour on Lambda; one GPU takes proportionally longer, roughly 4–24 hours depending on the GPU (§intro). [his result]
  - He expects significant improvements: llm.c still has pending optimisations and nobody has tuned training in the style of "cramming" (§intro). [expectation]
  - With ~0.5M tokens per step and 10B tokens the run is 18,865 steps, because one shard is held out for validation and the batch is exactly 524,288 (§intro).
  - Code layout: 95% of the work is in `train_gpt2.cu`, now about 3,500 lines after starting as about 1,000 clean lines of C, plus four support files; roughly 500 lines of MPI/NCCL/cuDNN/cuBLAS setup, 1,500 of layer forward and backward kernels (developed in `dev/cuda`), 1,000 for the `gpt2` model's forward and backward, and 1,000 of `main` with the training loop, argument parsing and resume logic (§intro).
  - 350M reproduced overnight: 10B tokens was not enough, so he trained ~30B tokens, 60K steps at 820 ms/step, 14 hours, about $200 (§intro). [his result; he adds the plot suggests slightly less might have sufficed]
  - Coming next: 740M and then the 1558M "GPT-2"; by rough napkin math 1558M would take about a week and ~$2.5K on his one node (§intro). [estimate; see digest 677 for the actual run]
  - He wants to make the code cleaner and better tested and add multi-node support, and to rebuild the whole thing from scratch piece by piece, "coming soon" (§intro).
  - FAQ: sampling is possible but inefficient and odd; no chat (pretraining only); multi-node works in principle via a slurm PR for up to 50 nodes he has not tried; not yet bitwise deterministic (one kernel left); no fp8 yet; NVIDIA/CUDA only, forks for other hardware welcome; CPU users can finetune OpenAI's GPT-2 in `train_gpt2.c` (§intro).
  - Sampling: he hacked conditional generation by writing prompt tokens into `gen_tokens` and moving the loop start; conditional generation was not really supported (§intro).
  - Tokenizer: running `train_gpt2.py` on TinyShakespeare writes `gpt2_tokenizer.bin`, which the C code needs to decode samples (§intro).

### topic: llm-evaluation
- existing: no (no eval topic in `wiki/index/topics.md`; [[loss-functions]] and [[overfitting-and-generalization]] cover train/val loss, not benchmark evals)
- aliases: [evals, evaluation, HellaSwag, validation loss comparison, benchmark comparison]
- statements:
  - He plots validation loss on held-out FineWeb, where his run beats OpenAI's checkpoint, but says it is not the ideal metric: GPT-2 was trained on the unreleased WebText and the internet's statistics may have changed in five years (§intro).
  - So he also plots HellaSwag accuracy, a common benchmark he calls nice, smooth and well-behaved; he would mostly look at HellaSwag and treat FineWeb val as confirmation (§intro).
  - HellaSwag has no math or code, so it slightly favours their common-crawl-like training data (§intro).
  - Reference points he cites: GPT-3 paper Appendix H gives 33.7 for GPT-3 Small (124M); his run gets 29.9, above GPT-2 (124M) at 29.4; GPT-3 models were trained on 300B tokens against his 10B (§intro).
  - `-h 1` evaluates HellaSwag, which he chose as something comparable across papers (§intro).

### topic: gradient-descent
- existing: yes
- statements:
  - Many hyperparameters follow the GPT-3 paper rather than GPT-2's because it was much more detailed (§intro).
  - Total batch ~0.5M tokens per update, from the GPT-3 paper's table for this size (GPT-2's batch size is unknown); the code computes the gradient-accumulation inner loop to reach it, 1 on 8 GPUs, 8 on one GPU (§intro).
  - Weight decay 0.1 applied only to 2-D weights, as in GPT-2; maximum LR 6e-4; linear warmup over 700 iterations (350M tokens); LR decayed to 0 over training (§intro).
  - Gradient clipping at 1.0 is standard and llm.c uses it to mitigate exploding gradients (§intro).
- note: the decay-to-zero setting is revised in 580 and 677 (decay to 10%).

### method: training-diagnostics
- existing: yes
- proposed step: Read loss, gradient norm, MFU and tokens/s from every log line
- statements:
  - He walks through a log line: step time, MFU, tokens per second, loss and gradient norm (§intro).
  - Loss 7.577 at step 80 means the model is as confused as guessing among exp(7.577) ≈ 2K tokens out of 50,257; by the end ~3.29, about 27 tokens (§intro).
  - A spiking gradient norm means the gradient is exploding, which is very bad; later in training the norm usually calms down (§intro).
  - Visualise `main.log` with the `dev/vislog.ipynb` notebook (§intro).

### topic: loss-functions
- existing: yes
- statements:
  - He reads the loss through perplexity: exp(loss) is how many tokens the model is effectively guessing uniformly among (§intro).

### topic: gpu-training-efficiency
- existing: no
- statements:
  - MFU is model flops utilisation: count the FLOPs done, divide by time, compare with the A100's claimed 312 TFLOPS; that peak is hard to reach because training is memory-bound and the tensor cores cannot be fed (§intro).
  - About 49% MFU on an A100 40GB PCIe, about 60% on the A100 80GB SXM with more bandwidth and power; the figure is in A100 fp16 units and meaningless on other GPUs (§intro). [his measurement]
  - `-r 1` recomputes the GELU activations: slightly slower but saves enough memory to raise the batch size for a net throughput gain (§intro).
  - ZeRO-1 on more than one GPU is a no-brainer and a no-op on one (§intro).
  - Out of memory: turn on `-r 1`, then halve `-b` until it runs, then try `-r 0` again (§intro).

### topic: training-compute-budget (optional; merge to decide)
- existing: no
- aliases: [6ND, training FLOPs, compute budget, cost of training]
- statements:
  - He estimates training compute with the 6ND approximation: 124M on 10B tokens ≈ 7e18 FLOPs, 350M on ~30B tokens ≈ 7e19, about 10X (§intro).
  - Cost scales with it: about $20 for 124M and $200 for 350M, 10X (§intro). [his result]
- note: thin topic; could instead be sentences on [[llm-c]]. The parallel lecture digest may have a related candidate.

### claim: gpt-2-is-the-first-recognizably-modern-llm-stack
- existing: no
- title: GPT-2 was the first time the modern LLM stack came together in recognisable form
- confidence: stated
- stated_on: 2024-05-28
- quote: "GPT-2 is the grand-daddy of LLMs" (§intro)
- context: in the FAQ "Why do you care so much about GPT-2?": first time the modern stack came together in recognisably modern form, and OpenAI released the parameters; GPT-3 changed little in the model (he thinks context 1024 → 2048 is it); GPT-4 details were never published; many LLMs resemble GPT-2, e.g. Llama 3 architecturally differs by an MLP non-linearity change and RoPE (§intro).
- topic: [[transformer-architecture]]
- relation: supports [[gpt-is-not-a-complicated-model]] only loosely (both treat the GPT model as small and stable); merge may prefer a **Note:** link rather than `supports`. Otherwise none.

### topic: transformer-architecture
- existing: yes
- statements:
  - GPT-3 changed little about the model relative to GPT-2: he thinks only the context size, 1024 → 2048 (§intro).
  - Llama 3, architecturally, differs from GPT-2 by a change of MLP non-linearity and the addition of RoPE relative positional encoding (§intro).

### claim: his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag
- existing: no
- title: His llm.c GPT-2 reproductions matched or beat OpenAI's checkpoints of the same size on HellaSwag with fewer tokens
- confidence: stated
- stated_on: 2024-05-28 (first instance; 580 and 677 repeat it with his uncertainty about why)
- quote (this file): "This is not the ideal metric because the data distribution of GPT-2 was different" is a caveat, not the claim; the claim quote is better from 580 ("we somewhat unexpectedly outperform both GPT-2 and GPT-3 very quickly").
- statements: 29.9 vs GPT-2 (124M) 29.4 on HellaSwag after 10B tokens; GPT-3 Small reported at 33.7 after 300B (§intro). [29.9 is his measured result; 29.4 and 33.7 are comparison numbers]
- relation to existing claims: none.

### topic: pretraining-and-finetuning
- existing: yes
- statements:
  - llm.c is currently pretraining only, not chat finetuning, so you cannot chat with the model (§intro).
  - Without a GPU you can still finetune OpenAI's GPT-2 weights on other data such as TinyShakespeare or TinyStories on CPU with `train_gpt2.c` (§intro).

### topic: pytorch
- existing: yes
- statements:
  - `train_gpt2.py` is a parallel PyTorch implementation used for error checking and unit tests, without full feature parity (e.g. no sharded data loading); he would accept PRs bringing it closer to llm.c's loop (§intro).

### method: verify-gradients-against-pytorch
- existing: yes
- statements:
  - The PyTorch script is a parallel implementation kept for error checking and unit tests (§intro).

### method: small-hackable-educational-code
- existing: yes
- statements:
  - `train_gpt2.cu` started as a nice clean 1,000 lines of C and grew to about 3,500 (§intro).
  - He still wants to build the whole thing again from scratch, piece by piece (§intro).

## Quotes
- "This is not the ideal metric because the data distribution of GPT-2 was different" (§intro)
- "I'd mostly look at HellaSwag, but FineWeb val is a nice confirmation." (§intro)
- "That said, HellaSwag has no math/code so it slightly favors our setting" (§intro)
- "When this number spikes, the gradient is exploding and this is very bad." (§intro)
- "GPT-2 is the grand-daddy of LLMs" (§intro)
- "the modern LLM stack came together in a recognizably modern form" (§intro)
- "I found that 10B tokens was not enough for the 350M model" (§intro)
- "No but we are very close, one more kernel to patch." (§intro)
- "no, this is currently only pretraining, not chat finetuning." (§intro)

## Notes for merge
- No markdown headings: bold labels (Args guide, Training, Visualization, Tokenizer, Sampling, Code, 350M model, Coming up, FAQ, Acknowledgements). Everything is `§intro`; append the label for precision if wanted.
- **Measured vs comparison numbers.** His measured results: ~90 min, ~$20, ~60% MFU on A100 80GB SXM, 49% / ~178K tok/s on A100 40GB PCIe, 18,865 steps, final loss ~3.29, HellaSwag 29.9; 350M: 820 ms/step, 60K steps, 14 h, ~$200. Comparisons/third-party: GPT-2 (124M) HellaSwag 29.4; GPT-3 Small 33.7 (from GPT-3 paper Appendix H); GPT-3 trained on 300B tokens; A100's claimed 312 TFLOPS. Estimates/targets: 4–24 h on one GPU; 1558M at ~1 week and ~$2.5K.
- The "740M" in the Coming up paragraph is his wording; the next Discussion (580) reproduces the 774M. Treat 740M as a slip; do not quote it as a model size.
- Mentions that are not explanations: "cramming" (linked paper), Lambda as sponsor, the slurm multi-node PR (someone else's), RoPE and Llama 3 (only named).
- **Lecture link:** "I want to build the whole thing again, from scratch and piece by piece, coming to you soon" (links an X post) is the promise that the June 2024 GPT-2 reproduction lecture (`youtube-2024-06-09-reproduce-gpt-2`, being digested in parallel, not yet in the wiki) appears to fulfil. The Discussion does not name the lecture; merge may connect them with a **Note:** only after the lecture page exists.
- nanoGPT is not mentioned in any of these Discussions. **Note:** for merge, the [[nanogpt]] page says nanoGPT reproduced GPT-2 (124M) in about four days on 8×A100 ([[github-2025-11-12-nanogpt-readme]] §intro); any comparison with llm.c's ~90 minutes is a Note citing both, not his statement (different data and settings).
- The two sampled completions about llm.c are model output, not his words; do not quote them as him.
- No replies by other people in the raw file.
