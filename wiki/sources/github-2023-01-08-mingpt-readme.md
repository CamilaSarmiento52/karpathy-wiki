---
type: source
raw_path: raw/github/karpathy__minGPT.md
published: 2023-01-08
medium: github
summary: "README of minGPT, his roughly 300-line PyTorch re-implementation of GPT training and inference, built to be small, clean and educational, and marked semi-archived in January 2023 in favour of its rewrite nanoGPT."
url: https://github.com/karpathy/minGPT
title: minGPT README
---
# minGPT README
Raw: [[raw/github/karpathy__minGPT]] · Original: https://github.com/karpathy/minGPT

Dated by the README's last commit (37baab7); the repo itself is older.

## Summary
minGPT is a PyTorch re-implementation of GPT covering both training and inference, written to be small, clean, interpretable and educational because he found existing implementations sprawling (§intro). He states that GPT is not a complicated model: a sequence of indices goes into a Transformer and a probability distribution over the next index comes out, with most of the complexity in batching for efficiency, and the model fits in about 300 lines (§intro). A January 2023 note declares the repo semi-archived and points to his rewrite nanoGPT; being referenced widely in notebooks, blogs, courses and books made him less willing to make large changes, and he also wanted to move from a sole focus on education to code that stays simple and hackable but has "teeth" (§intro). The library is three files, model, BPE tokenizer and a GPT-independent trainer, plus demo projects such as an adder trained from scratch and a character-level model (§intro). The README shows how to instantiate and train a GPT-2 (124M) configuration (§Usage), lists open todos (§todos), and ends with reference code and his own condensed implementation notes from the GPT-1, GPT-2, GPT-3 and Image GPT papers (§References).

## Key points
- What minGPT is, its three-file layout, demos and semi-archived status → [[mingpt]]
- minGPT superseded by his rewrite nanoGPT, and why → [[nanogpt]]
- GPT as indices in, next-index distribution out; paper-by-paper architecture and training notes → [[transformer-architecture]]
- "GPT is not a complicated model" → [[gpt-is-not-a-complicated-model]]
- Small, clean, interpretable, educational as the design goal → [[small-hackable-educational-code]]
- `bpe.py`, a Byte Pair Encoder matching OpenAI's GPT → [[tokenization]]

## Fed pages
- [[mingpt]]
- [[nanogpt]]
- [[transformer-architecture]]
- [[gpt-is-not-a-complicated-model]]
- [[small-hackable-educational-code]]
- [[tokenization]]
