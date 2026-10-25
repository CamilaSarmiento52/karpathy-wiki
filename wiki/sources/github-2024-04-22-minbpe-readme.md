---
type: source
raw_path: raw/github/karpathy__minbpe.md
published: 2024-04-22
medium: github
summary: "README of minbpe, his minimal, clean implementation of byte-level Byte Pair Encoding for LLM tokenizers: a basic and a regex tokenizer that train, encode and decode, plus a wrapper that reproduces GPT-4's tokenization."
url: https://github.com/karpathy/minbpe
title: minbpe README
---
# minbpe README
Raw: [[raw/github/karpathy__minbpe]] · Original: https://github.com/karpathy/minbpe

Dated by the README's last commit (45a0c2f). Text under the `# minbpe` heading is cited as `§intro`; the other headings are lowercase in the raw.

## Summary
minbpe is minimal, clean code for byte-level Byte Pair Encoding, the algorithm he says all modern LLMs use to train their tokenizers, popularised for LLMs by GPT-2 (§intro). It has two tokenizers that each train a vocabulary and merges, encode text to tokens and decode tokens to text: `BasicTokenizer`, which runs BPE directly on text, and `RegexTokenizer`, which first splits text by category with a regex so no merge crosses a category boundary and which handles special tokens; a `GPT4Tokenizer` wrapper reproduces GPT-4's tiktoken tokenization exactly (§intro, §inference: GPT-4 comparison). The quick start reproduces Wikipedia's BPE example, with the twist that minbpe always reserves the 256 bytes as the first tokens (§quick start). Unlike tiktoken it can train, and, in principle and to his knowledge, a `RegexTokenizer` trained on a large dataset at 100K vocabulary would reproduce the GPT-4 tokenizer (§training). He stresses that he kept the code clean, readable and hackable, and points to an exercise progression and to the lecture in which he built it (§training, §exercise, §lecture).

## Key points
- What the repo contains, its tests, todos and community port → [[minbpe]]
- Byte-level BPE, the regex pre-split, the 256 byte tokens, special tokens and their footgun → [[tokenization]]
- Clean, readable, hackable files with usage examples, an exercise progression and a lecture → [[small-hackable-educational-code]]
- Built in a lecture, with a step-by-step exercise for building your own → [[spelled-out-build-from-scratch]]
- Verifying parity against tiktoken's GPT-4 encoding, special tokens included → [[verify-against-a-reference-implementation]]

## Fed pages
- [[rustbpe]]
- [[minbpe]]
- [[tokenization]]
- [[small-hackable-educational-code]]
- [[spelled-out-build-from-scratch]]
- [[verify-against-a-reference-implementation]]
