---
type: source
raw_path: raw/github/karpathy__minbpe__discussion-98.md
published: 2025-08-08
medium: github
summary: "A minbpe Discussion where he posts his best-guess configuration for training a GPT-4-style BPE tokenizer with the Hugging Face Tokenizers library, unsure it is correct."
url: https://github.com/karpathy/minbpe/discussions/98
title: Train a GPT-4 tokenizer using huggingface Tokenizers
---
# Train a GPT-4 tokenizer using huggingface Tokenizers
Raw: [[raw/github/karpathy__minbpe__discussion-98]] · Original: https://github.com/karpathy/minbpe/discussions/98

No headings: prose is `§intro`, and comments inside the posted code, also his words, are `§intro (code)`.

## Summary
In a Discussion on the [[minbpe]] repo he posts how he believes one could train a GPT-4 tokenizer on one's own documents with the Hugging Face Tokenizers library, after about an hour with its documentation and code, for future reference and comparison (§intro). The example trains a 32,768-token vocabulary with one special document-delimiter token on 1 billion characters of FineWeb-edu (§intro). He says he is not fully confident the configuration is correct (§intro). The code sets a BPE model with byte fallback, no normalizer, a pre-tokenizer that splits on the GPT-4 regex and then maps to bytes, a matching byte-level decoder, no post-processor, and a BPE trainer with no minimum frequency seeded with the byte-level alphabet (§intro (code)).

## Key points
- His HF Tokenizers recipe for a GPT-4-style tokenizer, posted on minbpe → [[minbpe]]
- The pieces of a GPT-4-style tokenizer as a library configures them: GPT-4 split regex, byte-level mapping, BPE training → [[tokenization]]

## Fed pages
- [[minbpe]]
- [[tokenization]]
