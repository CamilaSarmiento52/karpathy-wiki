---
type: source
raw_path: raw/github/karpathy__llama2.c.md
published: 2024-05-29
medium: github
summary: "README of llama2.c, his minimal train-in-PyTorch, inference-in-one-C-file repo for the Llama 2 architecture: tiny TinyStories models, Meta checkpoints, int8 quantization, custom tokenizers, a training guide and a contributing policy that puts simplicity first."
url: https://github.com/karpathy/llama2.c
title: llama2.c README
---
# llama2.c README
Raw: [[raw/github/karpathy__llama2.c]] · Original: https://github.com/karpathy/llama2.c

Dated by the README's last commit (350e04f); much of the text reads as written earlier ("started recently"), so the weekend project is not dated from this file. Text under the `## llama2.c` heading is cited as `§intro`; the other headings are lowercase in the raw except `§Meta's Llama 2 models`.

## Summary
llama2.c trains the Llama 2 architecture in PyTorch and runs inference with one simple, roughly 700-line C file, a "fullstack" solution focused on minimalism and simplicity; he argues very small LLMs can perform surprisingly well in a narrow enough domain, citing the TinyStories paper (§intro). It began as a weekend project in which he adapted nanoGPT to Llama 2 and wrote the C inference engine, choosing, unlike llama.cpp, to hard-code the architecture in pure C with no dependencies (§intro). The README walks through running his TinyStories models, loading Meta's Llama 2 and Code Llama checkpoints, int8 quantization that cut checkpoint size 4X and ran 3X faster, training your own model with a short hyperparameter guide, and training a custom tokenizer (§feel the magic, §Meta's Llama 2 models, §int8 quantization, §training, §custom tokenizers). He expects strong interest in custom micro-LLMs deployed near the edge and wants the repo to stay the simplest, most hackable reference implementation that people fork, not a full-featured or maximally efficient framework (§contributing).

## Key points
- The repo, its models, platforms, tests and forks → [[llama2c]]
- Started from nanoGPT, retuned to Llama 2 → [[nanogpt]]
- Very small LLMs can be strong in a narrow domain; he expects interest in custom micro-LLMs at the edge → [[small-llms-can-be-strong-in-narrow-domains]]
- How Llama differs from GPT-1/2: RoPE, SwiGLU, RMSNorm, no biases, optional multiquery → [[transformer-architecture]]
- int8 weight and activation quantization, why RMSNorm parameters stay float32, CPU compile flags and threads → [[compute-efficiency]]
- Temperature versus top-p, and his recommended defaults → [[sampling-from-language-models]]
- Small custom vocabularies for small applications → [[tokenization]]
- His brief training guide: size, context, batch, accumulation, learning rate, iterations → [[gradient-descent]]
- Dropout 0.1 usually helps a bit at medium size → [[regularization]]
- Simple, readable, portable reference code you fork; what PRs he will merge → [[small-hackable-educational-code]]
- C and Python forward passes checked against known-good output → [[verify-against-a-reference-implementation]]

## Fed pages
- [[llama2c]]
- [[nanogpt]]
- [[small-llms-can-be-strong-in-narrow-domains]]
- [[transformer-architecture]]
- [[compute-efficiency]]
- [[sampling-from-language-models]]
- [[tokenization]]
- [[gradient-descent]]
- [[regularization]]
- [[small-hackable-educational-code]]
- [[verify-against-a-reference-implementation]]
- [[a-cognitive-core-could-be-a-billion-parameters-or-less]]
- [[cut-complexity-that-does-not-pay-for-itself]]
