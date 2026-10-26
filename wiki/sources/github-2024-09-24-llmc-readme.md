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

Dated by its commit (315b8d1). Headings are lowercase in the raw and cited as written; text before the first heading is `§intro`.

## Summary
The README presents llm.c as LLMs in simple, pure C/CUDA without PyTorch or cPython, currently focused on pretraining and on reproducing the GPT-2 and GPT-3 miniseries, with a parallel PyTorch reference in `train_gpt2.py`, which he says is a slightly tweaked nanoGPT; he puts llm.c at about 7% faster than PyTorch Nightly (§intro). Besides the mainline `train_gpt2.cu` there is a ~1,000-line CPU fp32 reference in `train_gpt2.c` and frozen fp32 CUDA files for learners; reproducing GPT-2 (124M) via Discussion #481 is the recommended introduction (§intro, §quick start, §quick start (1 GPU, fp32 only)). A unit test checks that the C and CUDA code match the PyTorch reference on logits, loss and ten training steps (§test). In §repo he says he wants llm.c to be a place for education, with a hand-written, documented kernel library in `dev/cuda`, and also fast enough to reproduce the GPT-2 (1.6B) run, using cuBLAS, cuDNN and similar libraries as an expert upper bound; but the root folder must stay simple and readable, and he may reject a PR that buys 2% speed with 500 lines of complex code (§repo). The rest covers datasets, a layernorm tutorial, cuDNN flash attention, multi-GPU and three multi-node launch methods, a learning-rate sweep example, and a long list of ports by others (§datasets, §tutorial, §multi-GPU training, §multi-node training, §experiments / sweeps, §notable forks).

## Key points
- Pure C/CUDA, pretraining, GPT-2/GPT-3 miniseries, C and CUDA only in this repo, ports elsewhere, coordination channels, a four-GPU learning-rate sweep → [[llm-c]]
- About 7% faster than PyTorch Nightly, no baseline given → [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- `train_gpt2.py` is a slightly tweaked nanoGPT → [[nanogpt]]
- Unit test against the PyTorch reference: logits, loss, ten Adam steps, fp32 and mixed-precision GPU paths; library kernels as a unit of measurement → [[verify-against-a-reference-implementation]], [[port-a-pytorch-model-to-c-and-cuda]]
- A layernorm tutorial for implementing a layer in C → [[port-a-pytorch-model-to-c-and-cuda]]
- Quick start is reproducing GPT-2 (124M); other GPT-2 and GPT-3 models in both llm.c and PyTorch → [[reproduce-a-published-model]]
- Education and speed, but the root folder stays simple; reject a 2% gain that costs 500 lines; cuBLAS as default is a no-brainer → [[small-hackable-educational-code]]
- Fast library kernels; cuDNN flash attention off by default for compile time; multi-GPU and multi-node → [[compute-efficiency]]
- `#llmc` on the Zero to Hero Discord as a coordination channel → [[nn-zero-to-hero]]

## Fed pages
- [[llm-c]]
- [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- [[nanogpt]]
- [[verify-against-a-reference-implementation]]
- [[reproduce-a-published-model]]
- [[small-hackable-educational-code]]
- [[compute-efficiency]]
- [[nn-zero-to-hero]]
- [[port-a-pytorch-model-to-c-and-cuda]]
- [[cut-complexity-that-does-not-pay-for-itself]]
