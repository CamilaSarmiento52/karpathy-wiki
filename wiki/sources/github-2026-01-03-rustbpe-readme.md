---
type: source
raw_path: raw/github/karpathy__rustbpe.md
published: 2026-01-03
medium: github
summary: "README of rustbpe, his Rust BPE tokenizer trainer with Python bindings, billed as the missing tiktoken training code: train with rustbpe, export to tiktoken for inference; the Rust was written against his own Python reference with equality tests and significant help from ChatGPT and Claude Code."
url: https://github.com/karpathy/rustbpe
title: rustbpe README
---
# rustbpe README
Raw: [[raw/github/karpathy__rustbpe]] · Original: https://github.com/karpathy/rustbpe

Dated by the README's commit ddf848f; the repo may be older, and nothing here says when or whether it was split out of nanochat. Text under the `# rustbpe` title, before the first `##` heading, is cited `§intro`. The README reports no runs; vocabulary sizes in its examples are settings. The README does not mention nanochat.

## Summary
rustbpe is a lightweight Rust library with Python bindings for training GPT-style BPE tokenizers, which he calls "the missing tiktoken training code" (§intro). He places it against three alternatives: tiktoken is excellent for inference but cannot train, Hugging Face `tokenizers` trains but carries years of accumulated complexity, and his own minbpe does both but only in unoptimised Python (§intro). The intended use is to train with rustbpe and export to tiktoken for fast inference, with GPT-4-style regex pre-tokenization by default, parallel training and batch encoding (§Features, §Usage). The README explains BPE as starting from 256 byte tokens and repeatedly merging the most frequent adjacent pair (§How BPE works). In an LLM-assistance note he says he wrote the Python reference himself, then the Rust against it with equality tests, with significant help from ChatGPT and Claude Code Opus 4.5 because he is not a Rust developer (§LLM Assistance note).

## Key points
- The repo, its API and its gap between tiktoken, HF tokenizers and minbpe → [[rustbpe]]
- Byte-level BPE in four steps; GPT-4 regex pattern by default; tiktoken export → [[tokenization]]
- minbpe trains and infers, but only in Python and slowly → [[minbpe]]
- tiktoken for inference plus training code is the combination it provides → [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]]
- Likely nanochat's Rust tokenizer, though neither source says so → [[nanochat]] (a **Note:** there)
- Python reference first, Rust tested for equality against it → [[verify-against-a-reference-implementation]]
- LLM help in a language he does not know; disclosed in the README → [[coding-models-are-weak-at-code-never-written-before]], [[vibe-coding]]

## Fed pages
- [[rustbpe]]
- [[tokenization]]
- [[minbpe]]
- [[nanochat]]
- [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]]
- [[verify-against-a-reference-implementation]]
- [[coding-models-are-weak-at-code-never-written-before]]
- [[vibe-coding]]
