# Digest: minbpe README
- raw: raw/github/karpathy__minbpe.md · published: 2024-04-22 · medium: github · words: 1316
- source slug: github-2024-04-22-minbpe-readme

## Source page
```
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

Dated by the README's last commit (45a0c2f).

## Summary
minbpe is minimal, clean code for byte-level Byte Pair Encoding, the algorithm he says all modern LLMs use to train their tokenizers, popularised for LLMs by GPT-2 (§intro). It has two tokenizers that each train a vocabulary and merges, encode text to tokens and decode tokens to text: `BasicTokenizer`, which runs BPE directly on text, and `RegexTokenizer`, which first splits text by category with a regex so no merge crosses a category boundary and which handles special tokens; a `GPT4Tokenizer` wrapper reproduces GPT-4's tiktoken tokenization exactly (§intro, §inference: GPT-4 comparison). The quick start reproduces Wikipedia's BPE example, with the twist that minbpe always reserves the 256 bytes as the first tokens (§quick start). Unlike tiktoken it can train, and he believes a `RegexTokenizer` trained on a large dataset at 100K vocabulary would reproduce the GPT-4 tokenizer (§training). He stresses that he kept the code clean, readable and hackable, and points to an exercise progression and to the lecture in which he built it (§training, §exercise, §lecture).

## Key points
- What the repo contains, its tests, todos and community port → [[minbpe]]
- Byte-level BPE, the regex pre-split, the 256 byte tokens, special tokens and their footgun → [[tokenization]]
- Clean, readable, hackable files with usage examples, an exercise progression and a lecture → [[small-hackable-educational-code]]
- Built in a lecture, with a step-by-step exercise for building your own → [[spelled-out-build-from-scratch]]
- Verifying parity against tiktoken's GPT-4 encoding → [[verify-against-a-reference-implementation]]

## Fed pages
- [[minbpe]]
- [[tokenization]]
- [[small-hackable-educational-code]]
- [[spelled-out-build-from-scratch]]
- [[verify-against-a-reference-implementation]]
```

## Candidates
### artifact: minbpe
- existing: no
- aliases: [minBPE, minbpe]
- frontmatter: repo_url https://github.com/karpathy/minbpe · language Python · status active
- statements:
  - Minimal, clean code for the byte-level BPE algorithm used in LLM tokenization; "byte-level" because it runs on UTF-8 encoded strings (§intro)
  - Files: `base.py` (the `Tokenizer` base class with train/encode/decode stubs, save/load and utilities, meant to be inherited), `basic.py` (`BasicTokenizer`), `regex.py` (`RegexTokenizer`, with special tokens), `gpt4.py` (`GPT4Tokenizer`, a light wrapper reproducing GPT-4's tiktoken tokenization, handling recovery of the exact merges and some 1-byte token permutations he calls unfortunate and likely historical) (§intro)
  - `train.py` trains both tokenizers on the Wikipedia entry for Taylor Swift and saves the vocab for visualisation, in about 25 seconds on his M1 MacBook (§intro)
  - All files are very short, thoroughly commented, and end with a usage example (§intro)
  - `save` writes a `.model` file for loading and a `.vocab` file for viewing (§quick start, §training)
  - Tests use pytest in `tests/` (§tests); a Rust port, minbpe-rs, is listed as a community extension (§community extensions)
  - Built in a YouTube lecture, also available as text in `lecture.md`; `exercise.md` gives an advised progression for building your own minbpe step by step (§exercise, §lecture)
  - Todos at snapshot time: a faster Python version for large files and vocabularies, a C or Rust version, generalising GPT4Tokenizer to GPT-2/3/3.5, and a LlamaTokenizer attempting a sentencepiece equivalent (§todos)

### topic: tokenization
- existing: yes
- aliases to add: byte-level BPE, regex pre-tokenization, special tokens, tiktoken
- statements:
  - BPE was popularised for LLMs by the GPT-2 paper and code release; Sennrich et al. 2015 is cited as the original NLP reference; he says all modern LLMs (e.g. GPT, Llama, Mistral) use it to train their tokenizers (§intro)
  - A tokenizer's three primary functions: train the vocabulary and merges on text, encode text to tokens, decode tokens to text (§intro)
  - The regex pre-split breaks input text into categories (letters, numbers, punctuation) so no merges happen across category boundaries; introduced in GPT-2 and still in use as of GPT-4 (§intro)
  - minbpe always allocates the 256 individual bytes as tokens and merges from there, so in the Wikipedia example the first merge becomes token 256 (§quick start)
  - As in tiktoken, you must explicitly allow special tokens when encoding; otherwise it can become a major footgun, unintentionally tokenizing attacker-controlled data such as user prompts with special tokens (§inference: GPT-4 comparison)
  - Two paths for training: `BasicTokenizer` if you do not want regex splitting or special tokens, or `RegexTokenizer` (GPT-4 pattern by default) to follow OpenAI's approach; vocabulary size should vary with dataset size (§training)
  - Special tokens are registered after the merges; with vocab_size 32768 the first special token has id exactly 32768 (§training)
- relation: extends the existing page's character-versus-sub-word material ([[youtube-2023-01-17-gpt-from-scratch]] @10:35) and minGPT's `bpe.py` ([[github-2023-01-08-mingpt-readme]] §intro) with how BPE is actually implemented and trained.

### method: small-hackable-educational-code
- existing: yes
- statements:
  - He says he tried hard to keep the code clean, readable and hackable, and that you should not be scared to read it (§training)
  - Every file is very short, thoroughly commented, with a usage example at the bottom; tests double as usage examples (§intro, §training)
  - He provides an exercise progression for building your own minbpe step by step (§exercise)

### method: spelled-out-build-from-scratch
- existing: yes
- statements:
  - He built the repo's code in a YouTube lecture, with a text version of the lecture in the repo (§lecture)

### method: verify-against-a-reference-implementation
- existing: no (closest: [[verify-gradients-against-pytorch]], which is gradient-specific)
- aliases: [parity check, reproduce the reference output]
- steps (from this source): encode the same text with the reference (tiktoken `cl100k_base`) and with yours; compare token ids; repeat with special tokens allowed (§inference: GPT-4 comparison)
- note: parallel digests overlap: the llm.c state-of-the-union digest proposes `benchmark-against-pytorch`, and [[verify-gradients-against-pytorch]] exists. Merge should pick one general parity method ("check your implementation against a reference") rather than three. The llama2.c digest has the same move (C and Python forward passes checked against a known-good output, §tests; PyTorch `sample.py` gives the same results as `run.c`, §training). Merge could instead widen [[verify-gradients-against-pytorch]] into a general parity method; I lean to one new method or to folding into the existing one, not both.

## Quotes
- "Minimal, clean code for the (byte-level) Byte Pair Encoding (BPE) algorithm" (§intro)
- "all modern LLMs (e.g. GPT, Llama, Mistral) use this algorithm to train their tokenizers" (§intro)
- "This ensures that no merges will happen across category boundaries." (§intro)
- "minbpe always allocates the 256 individual bytes as tokens" (§quick start)
- "Otherwise this can become a major footgun" (§inference: GPT-4 comparison)
- "you would reproduce the GPT-4 tokenizer" (§training)
- "I tried hard to keep the code itself clean, readable and hackable." (§training)

## Notes for merge
- Locations: text under the `# minbpe` H1 is `§intro`; other headings are lowercase in the raw (`§quick start`, `§inference: GPT-4 comparison`, `§training`, `§tests`, `§community extensions`, `§exercise`, `§lecture`, `§todos`).
- "you would reproduce the GPT-4 tokenizer" is hedged in the raw: "In principle and to my knowledge"; keep the hedge in any paraphrase.
- The lecture link (zduSFxRajkE) is Zero to Hero Lecture 8; its digest is in this batch (`zduSFxRajkE.md`, slug `youtube-2024-02-20-gpt-tokenizer`), which also proposes the `minbpe` artifact. Link the two source pages via the artifact.
- Raw typos: "You should not have feel scared", "follow along with OpenAI did"; avoid quoting them.
- The Taylor Swift training text is a joke ("kek"); fine to mention as the sample file, not as a claim.
- No claim candidates: the README is descriptive. "All modern LLMs use BPE" is a factual statement he makes in passing; keep it as a topic sentence, not a claim page. The tokenization claim is in the nn-zero-to-hero digest.
