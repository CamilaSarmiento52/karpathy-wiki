# Digest: makemore README
- raw: raw/github/karpathy__makemore.md · published: 2022-11-20 · medium: github · words: 448
- source slug: github-2022-11-20-makemore-readme

## Source page
```
---
type: source
raw_path: raw/github/karpathy__makemore.md
published: 2022-11-20
medium: github
summary: README of makemore, his one-file, PyTorch-only character-level language model that learns from a list of lines and generates more like them, with models from a bigram table to a Transformer.
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
```

## Candidates
### artifact: makemore
- existing: no
- aliases: [makemore]
- frontmatter: repo_url https://github.com/karpathy/makemore · language Python · status active (the README gives no deprecation notice; merge may prefer `archived` if a later snapshot says so)
- statements:
  - makemore reads a text file with one training example per line and generates more examples like it (§intro)
  - Under the hood it is an autoregressive character-level language model, with models ranging from a bigram count table to a Transformer as in GPT (§intro)
  - He suggests feeding it names to get name-like baby names that do not already exist, company names, or valid Scrabble words for English-like babble (§intro)
  - It is one hackable file, mostly intended for education, and PyTorch is its only requirement (§intro)
  - The implementations follow specific papers: bigram (lookup table of counts), MLP after Bengio et al. 2003, CNN after WaveNet 2016 (marked in progress), RNN after Mikolov et al. 2010, LSTM after Graves et al. 2014, GRU after Cho et al. 2014, Transformer after Vaswani et al. 2017 (§intro)
  - The bundled `names.txt` is the 32K most common names from ssa.gov for 2018 (§Usage)
  - The default model is a roughly 200K-parameter Transformer; other configurations are reachable via argparse and reading the code (§Usage)
  - Training needs no special hardware and runs on his MacBook Air, faster with a GPU; a `--sample-only` flag samples from the best model so far (§Usage)
  - The default settings reach a test log-probability of about 1.92, and he says lower is achievable with hyperparameter tuning (§Usage)
  - Licence MIT (§License)
- relation to existing pages: **Note:** link to [[nanogpt]] as a sibling educational repo (nanoGPT is the later "teeth" rewrite of minGPT; makemore is the smaller char-level predecessor). Future link to the lecture source `youtube-2022-09-07-makemore-1-bigram` and its siblings once ingested; not in index yet.

### topic: character-level-language-modeling
- existing: no
- aliases: [Character-level language modeling, char-level LM, autoregressive character model]
- statements:
  - A character-level language model treats each line of a text file as one training example and learns to generate more lines like it, one character at a time (§intro)
  - The simplest version is a bigram model, where one character predicts the next from a lookup table of counts; the same task can be solved with an MLP, RNN, LSTM, GRU, CNN or Transformer (§intro)
  - Example uses: names, company names, Scrabble words (§intro)
- context sources to add later: minGPT's `projects/chargpt` trains a GPT as a character-level model (minGPT §intro, mention only); the nanoGPT Shakespeare quick start already on [[nanogpt]].

### method: small-hackable-educational-code
- existing: no (no matching slug or alias in index; the nanoGPT page describes the contrast "teeth over education" but there is no method page)
- aliases: [One hackable file, minimal educational re-implementation]
- steps (proposed): keep the whole thing in one (or very few) readable files; keep dependencies to PyTorch; expose configuration through the code and argparse rather than switches; publish so people can hack it
- statements:
  - makemore is explicitly not meant to be a heavyweight library with many switches and knobs; it is one hackable file, mostly for educational purposes (§intro)
  - PyTorch is the only requirement (§intro)
  - He points users to the argparse and the code itself for further training configurations (§Usage)
- also fed by: minGPT README (small, clean, interpretable, educational, ~300 lines) and ng-video-lecture README (publishing lecture code as a repo so people can hack it and read the git log). Merge may split or rename; see minGPT digest.

## Quotes
- "It is one hackable file, and is mostly intended for educational purposes." (§intro) — 12 words
- "This is not meant to be too heavyweight library with a billion switches and knobs." (§intro) — 14 words, verbatim including the missing "a"

## Notes for merge
- Read at commit 988aa59e4d8fefa526d06f3b453ad116258398d4 (2022-11-20). The repo predates the commit; the makemore lecture series on YouTube began in September 2022, so this README postdates the first lectures. Date the artifact's `first seen` by the source, not the repo's creation.
- Headings in the raw file are H3 (`### Usage`, `### License`); the body before `### Usage` is cited as §intro.
- The CNN/WaveNet model is marked "(in progress...)" in this snapshot; do not write that makemore implements a CNN without that qualifier.
- The `names.txt` description reads "most common 32K names takes from ssa.gov" (typo "takes" for "taken") in the raw; paraphrased, not quoted.
- Expected inbound links: [[nanogpt]] (Related), the future lecture source pages. Until a lecture source exists, the artifact's only inbound content link may be from [[character-level-language-modeling]] and [[small-hackable-educational-code]]; that satisfies the no-orphans invariant.
