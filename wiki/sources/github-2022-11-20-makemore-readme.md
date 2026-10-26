---
type: source
raw_path: raw/github/karpathy__makemore.md
published: 2022-11-20
medium: github
summary: "README of makemore, his one-file, PyTorch-only character-level language model that learns from a list of lines and generates more like them, with models from a bigram table to a Transformer."
url: https://github.com/karpathy/makemore
title: makemore README
---
# makemore README
Raw: [[raw/github/karpathy__makemore]] · Original: https://github.com/karpathy/makemore

Dated by the README's last commit (988aa59); the repo itself is older.

## Summary
makemore takes a text file in which each line is one training example and generates more lines like it; underneath it is an autoregressive character-level language model, with a choice of models from bigrams up to a GPT-style Transformer (§intro). He gives names, company names and Scrabble words as example inputs (§intro). He frames it as deliberately not a heavyweight library: one hackable file, mostly for education, with PyTorch as the only dependency (§intro). The implementations follow a short list of papers, one per model family, from Bengio et al. 2003 for the MLP to Vaswani et al. 2017 for the Transformer, with the WaveNet-style CNN marked as in progress (§intro). The usage section walks through training the default 200K-parameter Transformer on a 32K-name dataset from ssa.gov, notes that it runs on his MacBook Air without special hardware, and shows sampled made-up names (§Usage).

## Key points
- What makemore is, what it generates and the paper lineage of its models → [[makemore]]
- Character-level, line-per-example language modelling as the framing → [[character-level-language-modeling]]
- One hackable file, educational purpose, single dependency → [[small-hackable-educational-code]]

## Fed pages
- [[makemore]]
- [[character-level-language-modeling]]
- [[small-hackable-educational-code]]
