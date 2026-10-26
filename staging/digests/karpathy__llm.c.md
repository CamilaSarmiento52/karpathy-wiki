# Digest: llm.c README
- raw: raw/github/karpathy__llm.c.md · published: 2024-09-24 · medium: github · words: 2278
- source slug: github-2024-09-24-llmc-readme
- commit: 315b8d1f626885db31a895510cb299cb282616cc

## Source page
```
---
type: source
raw_path: raw/github/karpathy__llm.c.md
published: 2024-09-24
medium: github
summary: "The llm.c README as of 2024-09-24: LLM pretraining in simple, pure C/CUDA with a parallel PyTorch reference, about 7% faster than PyTorch Nightly, with quick starts for GPU, fp32 and CPU, unit tests against PyTorch, multi-GPU and multi-node instructions, and his policy of education plus speed while keeping the root folder simple."
url: https://github.com/karpathy/llm.c
title: "llm.c README"
---
# llm.c README
Raw: [[raw/github/karpathy__llm.c]] · Original: https://github.com/karpathy/llm.c

## Summary
The README presents llm.c as LLMs in simple, pure C/CUDA without PyTorch or cPython, currently focused on pretraining and on reproducing the GPT-2 and GPT-3 miniseries, with a parallel PyTorch reference in `train_gpt2.py`, which he says is a slightly tweaked nanoGPT; he puts llm.c at about 7% faster than PyTorch Nightly (§intro). Besides the mainline `train_gpt2.cu` there is a ~1,000-line CPU fp32 reference in `train_gpt2.c` and frozen fp32 CUDA files for learners; reproducing GPT-2 (124M) via Discussion #481 is the recommended introduction (§intro, §quick start, §quick start (1 GPU, fp32 only)). A unit test checks that the C and CUDA code match the PyTorch reference on logits, loss and ten training steps (§test). In §repo he says he wants llm.c to be a place for education, with a hand-written, documented kernel library in `dev/cuda`, and also fast enough to reproduce the GPT-2 (1.6B) run, using cuBLAS, cuDNN and similar libraries as an expert upper bound; but the root folder must stay simple and readable, and he may reject a PR that buys 2% speed with 500 lines of complex code (§repo). The rest covers datasets, a layernorm tutorial, cuDNN flash attention, multi-GPU and three multi-node launch methods, a learning-rate sweep example, and a long list of ports by others (§datasets, §tutorial, §multi-GPU training, §multi-node training, §experiments / sweeps, §notable forks).

## Key points
- Pure C/CUDA, pretraining, GPT-2/GPT-3 miniseries, C and CUDA only in this repo, ports elsewhere, coordination channels → [[llm-c]]
- About 7% faster than PyTorch Nightly → [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- `train_gpt2.py` is a slightly tweaked nanoGPT → [[nanogpt]], [[llm-c]]
- Unit test against the PyTorch reference: logits, loss, ten Adam steps, fp32 and mixed-precision GPU paths → [[verify-against-a-reference-implementation]]
- Quick start is reproducing GPT-2 (124M); other GPT-2 and GPT-3 models in both llm.c and PyTorch → [[reproduce-a-published-model]]
- Education and speed, but the root folder stays simple; reject a 2% gain that costs 500 lines; cuBLAS as default is a no-brainer → [[small-hackable-educational-code]], [[neural-net-training-should-not-be-complicated]]
- Fast library kernels as an expert upper bound and unit of measurement for hand-written kernels; cuDNN flash attention off by default for compile time; multi-GPU and multi-node → [[compute-efficiency]]
- `#llmc` on the Zero to Hero Discord as a coordination channel → [[nn-zero-to-hero]]
- Learning-rate sweep across 4 GPUs with screen sessions → [[learning-rate-sweep]]

## Fed pages
- [[llm-c]]
- [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- [[nanogpt]]
- [[verify-against-a-reference-implementation]]
- [[reproduce-a-published-model]]
- [[small-hackable-educational-code]]
- [[neural-net-training-should-not-be-complicated]]
- [[compute-efficiency]]
- [[nn-zero-to-hero]]
- [[learning-rate-sweep]]
```

## Candidates
### artifact: llm-c
- existing: yes (built from seven Discussions in batch 2, plus the GPT-2 lecture)
- status: still `active` (current focus, ongoing contributions invited; nothing says archived)
- statements (new relative to the existing page):
  - He describes llm.c as LLMs in simple, pure C/CUDA with no need for 245MB of PyTorch or 107MB of cPython (§intro).
  - Current focus is pretraining, in particular reproducing the GPT-2 and GPT-3 miniseries, alongside a parallel PyTorch reference implementation in `train_gpt2.py`, which he says readers will recognise as a slightly tweaked nanoGPT, an earlier project of his (§intro).
  - Besides the bleeding-edge mainline `train_gpt2.cu`, there is a simple reference CPU fp32 implementation in about 1,000 lines of clean code in one file, `train_gpt2.c` (§intro).
  - He wants the repo to maintain only C and CUDA code; ports to other languages are welcome in separate repos and he will link them under notable forks (§intro).
  - Coordination happens in Discussions and on Discord, in `#llmc` on the Zero to Hero server or `#llmdotc` on the GPU MODE server (§intro); §discussions splits it: Issues for concrete problems, PRs for code, Discussions for chat and questions, Discord for something faster (§discussions).
  - The best introduction "today" is reproducing GPT-2 (124M), stepped through in Discussion #481; other GPT-2 and GPT-3 models can be reproduced in both llm.c and the PyTorch implementation, with a scripts README (§quick start).
  - Debugging tip: replace `-O3` with `-g` in `make` to step through the code in an IDE (§quick start).
  - The fp32 CUDA files are "legacy", checkpointed early in the project's history and frozen; he says they are simpler, more portable and possibly easier to understand, for single-GPU users who want to learn CUDA (§quick start (1 GPU, fp32 only)).
  - The starter pack downloads the GPT-2 124M weights in fp32 and bfloat16, a debug state for unit tests (a small batch with target activations and gradients), the GPT-2 tokenizer and tokenized tinyshakespeare; the same files can be regenerated with `dev/data/tinyshakespeare.py` and `train_gpt2.py` (§quick start (1 GPU, fp32 only)).
  - The CPU version is an even earlier checkpoint, from when llm.c was a simple C reference; it finetunes GPT-2 (124M) on tinyshakespeare for 40 steps with AdamW (batch 4, context 64), evaluates validation loss and samples; he says that without a beefy CPU you will not get far, but it may be a good demo/reference; example output is from his MacBook Pro M3 Max (§quick start (CPU)).
  - Dataset scripts in `dev/data` download, tokenize and save tokens as `.bin` files: a 1024-byte header then uint16 GPT-2 token ids, easily read from C (§datasets).
  - `doc/layernorm/layernorm.md` is a small step-by-step tutorial implementing one GPT-2 layer, layernorm, as a starting point for how layers are implemented in C (§tutorial).
  - Since 2024-05-01 llm.c uses cuDNN's flash attention, disabled by default because it bloats compile time from a few seconds to about a minute and the path is very new; enable with `USE_CUDNN=1` (§tutorial).
  - Multi-GPU uses MPI and NCCL via `mpirun`; multi-node supports three ways to initialise NCCL (OpenMPI, a shared file system, TCP sockets), and he says none is superior (§multi-GPU training, §multi-node training).
  - Repo philosophy (§repo): a place for education, e.g. `dev/cuda` as a library of hand-written, well-documented kernels from very simple to faster; but also very fast, practically useful, e.g. reproducing the big GPT-2 (1.6B) run, which requires the fastest kernels including cuBLAS, cuBLASLt, CUTLASS and cuDNN; mainline root folder kept simple and readable; `dev/` is scratch space where code may be locally complex.
  - Notable forks: about twenty ports by others, including AMD (@anthonix), C#, CUDA C++ with CCCL (covered in a GPU MODE lecture), C++/CUDA with Eigen, WebGPU C++ (gpu.cpp), C++, Go, Java, Metal, Mojo, OpenCL, Rust, Swift, Zig, Habana Gaudi2 and Nim (§notable forks).
  - License MIT (§license).

### claim: llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements
- existing: yes
- statements:
  - The README says llm.c is currently a bit faster than PyTorch Nightly, by about 7% (§intro). [no setting, model size or date of measurement given in this README; the 2024-05-03 report's ~7% was GPT-2 (124M) on one A100 40GB]
- relation: supports (same claim, new source). **Note:** the README's 7% gives no baseline details; do not merge it with the 1.6B figures (29% memory, 19% speed).
- quote: "Currently, llm.c is a bit faster than PyTorch Nightly (by about 7%)." (§intro)

### artifact: nanogpt
- existing: yes
- statements:
  - The llm.c PyTorch reference `train_gpt2.py` is, he says, a slightly tweaked nanoGPT, "an earlier project of mine" (§intro).
- note: batch 2 rule was that the Discussions never mention nanoGPT; this README does, so it can be cited on [[nanogpt]].

### method: verify-against-a-reference-implementation
- existing: yes
- statements:
  - `test_gpt2` loads `gpt2_124M_debug_state.bin` written by `train_gpt2.py`, runs a forward pass, compares logits and loss with the PyTorch reference, then runs 10 iterations of training with Adam and checks the losses match PyTorch (§test).
  - The GPU tests cover both the fp32 path and the mixed-precision cuDNN path, and should print `overall okay: 1` (§test).
  - In §repo, library kernels such as cuBLAS serve as an expert upper bound and a unit of measurement, so you can say hand-written kernels reach, e.g., 80% of cuBLAS speed (§repo). [this is a speed reference, matching the existing "benchmark against the reference" step]

### method: reproduce-a-published-model
- existing: yes
- statements:
  - The README calls reproducing GPT-2 (124M) the best introduction to the repo, pointing to Discussion #481, and says other GPT-2 and GPT-3 series models can be reproduced in both llm.c and the parallel PyTorch implementation (§quick start).
  - Reproducing the big GPT-2 (1.6B) run is given as the first concrete target for making llm.c practically useful (§repo).

### method: small-hackable-educational-code
- existing: yes
- statements:
  - He keeps the mainline root folder simple and readable: a PR that improves performance by 2% but costs 500 lines of complex C and maybe an exotic dependency may be rejected because the complexity is not worth it (§repo).
  - His concrete counterexample: making cuBLAS the default for matmuls in the root loop is a no-brainer, because it is much faster, one line of interpretable code and a very common dependency; hand-written competitors live in `dev/cuda` (§repo).
  - He will be much more sensitive to complexity in the root folder, while `dev/` is a scratch space where code may be locally complex (§repo).
  - The fp32 and CPU files are frozen early checkpoints kept because they are simpler and easier to understand (§quick start (1 GPU, fp32 only), §quick start (CPU)).
  - Only C and CUDA in the repo; ports go to separate repos and are linked (§intro).
- relation: same policy as the llama2.c contributing rules already on the page (step 11); this adds the explicit 2%/500-lines trade and the root vs `dev/` split.

### claim: neural-net-training-should-not-be-complicated
- existing: yes
- statements:
  - "LLMs in simple, pure C/CUDA" with no PyTorch or cPython (§intro), and the root-folder complexity policy (§repo).
- relation: weak support only; the README does not restate that training is simple arithmetic. Merge may prefer to cite it on the artifact and method pages and leave this claim alone. If cited, put it in `context`.

### topic: compute-efficiency
- existing: yes
- statements:
  - To be fast, llm.c incorporates the fastest kernels, including cuBLAS, cuBLASLt, CUTLASS and cuDNN; he says this also serves education by setting an expert upper bound and unit of measurement for hand-written kernels, and lets users choose a fast run or "drag and drop" their own kernels (§repo).
  - cuDNN flash attention is used since May 1, 2024 but disabled by default because it raises compile time from seconds to about a minute (§tutorial).
  - Multi-GPU with MPI and NCCL; multi-node with three NCCL initialisation methods for different environments, e.g. slurm without PMIx (§multi-GPU training, §multi-node training).

### artifact: nn-zero-to-hero
- existing: yes
- statements:
  - Developer coordination for llm.c happens partly in a `#llmc` channel he created on his Zero to Hero Discord (§intro, §discussions).
- note: a mention, not an explanation of the course; `context` may be the right field.

### method: learning-rate-sweep
- existing: yes
- statements:
  - His example sweep runs four learning rates (3e-5, 1e-4, 3e-4, 1e-3) on TinyStories, one per GPU in separate `screen` sessions, writing loss logs to plot in Python, e.g. with `dev/vislog.ipynb` (§experiments / sweeps).
- note: the existing method is about the exponential-rate valley sweep from makemore; this is a grid of four runs. Merge may decide it is a separate idea and put it on [[llm-c]] instead.

### claims (new)
- none proposed. The 2%/500-lines policy could be a claim ("he rejects small speedups that cost a lot of complexity"), but it is a project policy and fits as a step on [[small-hackable-educational-code]]; the keynote states the same trade (see that digest).

## Quotes
- "LLMs in simple, pure C/CUDA with no need for 245MB of PyTorch" (§intro)
- "Currently, llm.c is a bit faster than PyTorch Nightly (by about 7%)." (§intro)
- "I'd like this repo to only maintain C and CUDA code." (§intro)
- "First, I want `llm.c` to be a place for education." (§repo)
- "I also want `llm.c` to be very fast too" (§repo)
- "establish an expert upper bound, and a unit of measurement" (§repo)
- "I may reject the PR because the complexity is not worth it." (§repo)
- "making cuBLAS for matmuls the default in the root training loop is a no-brainer" (§repo)
- "I will be a lot more sensitive to complexity in the root folder" (§repo)
- "you're not going to get that far on CPU training LLMs" (§quick start (CPU))
- "None of these 3 methods is superior" (§multi-node training)

## Notes for merge
- Headings are lowercase in the raw (`## quick start`, `## repo`, …); cite them as written. Text before the first heading is `§intro`.
- **Numbers.** "about 7%" faster than PyTorch Nightly is stated without baseline (§intro). The CPU file is "~1,000 lines" here; the keynote recalls the single C file at about 2,000 lines "if I remember correctly" and the whole at maybe 3,000 lines; the 2024-07-11 post says ~5,000 lines. Different files and dates; do not reconcile.
- The starter-pack list numbers items 1), 2), 3), 3) and the CPU paragraph jumps (1) to (3); "tineshakespeare" and "trunctated" are typos in the raw. Do not copy.
- The generated "Shakespeare" text block is model output, not his words.
- The README uses "we" for project work and "I" for policy; attribute the §repo policy to him.
- The forks list is other people's work; cite only as "ports by others". The CUDA C++ fork was covered in a GPU MODE lecture (link), not by him.
- The Discord is called "GPU MODE" (discord.gg/gpumode), while the CCCL fork's link says "GPU MODE Discord Server" with discord.gg/cudamode; the keynote's title says "CUDA Mode". Do not assert a rename as fact; at most a **Note:** that the names differ across sources.
- The README is a snapshot at commit 315b8d1; `published` is that commit's date. Later README snapshots would be new sources.
