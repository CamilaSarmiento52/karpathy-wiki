---
type: source
raw_path: raw/youtube/kCc8FmEb1nY.md
published: 2023-01-17
medium: youtube
summary: "Two-hour lecture that builds a decoder-only Transformer on tiny Shakespeare from an empty file, deriving self-attention step by step, scaling it to a nanoGPT-shaped model, and closing with how ChatGPT's pretraining and finetuning stages relate to it."
url: https://www.youtube.com/watch?v=kCc8FmEb1nY
title: "Let's build GPT: from scratch, in code, spelled out."
---
# Let's build GPT: from scratch, in code, spelled out.
Raw: [[raw/youtube/kCc8FmEb1nY]] · Original: https://www.youtube.com/watch?v=kCc8FmEb1nY

## Summary
A 1h56m coding lecture that writes a character-level Transformer language model from an empty file, training on the 1 MB tiny Shakespeare text (@03:23, @06:45). He starts with a character-level tokenizer and contrasts it with sub-word schemes such as SentencePiece and tiktoken (@09:31, @11:10), then builds a bigram baseline, checks its initial loss against the value expected from the vocabulary size, and gets it generating (@21:57, @28:03). The core of the video derives self-attention: first averaging past tokens with a lower-triangular matrix multiply, then making the weights data-dependent with queries, keys and values, adding scaling, causal masking, multiple heads and a feed-forward layer (@42:09, @1:01:54, @1:22:01). He adds residual connections, pre-norm LayerNorm and dropout, scales the model up to reach a validation loss of 1.48 in about 15 minutes on an A100, and walks through how nanoGPT's `model.py` matches what was built (@1:28:36, @1:40:21, @1:46:28). He ends by explaining why the model is decoder-only and how ChatGPT adds a finetuning stage of supervised data, a reward model and PPO on top of pretraining (@1:42:35, @1:48:42, @1:53:43).

## Key points
- Tokenization trades vocabulary size against sequence length; he keeps characters for simplicity → [[tokenization]]
- A bigram model predicts the next character from the current one alone and is the baseline → [[bigram-language-model]]
- Check the loss at initialization against what the vocabulary size predicts; average over batches; mind eval mode → [[training-diagnostics]]
- Build up incrementally from a bigram script, reading validation loss after each addition → [[spelled-out-build-from-scratch]]
- Averaging past tokens is a weighted aggregation done with a lower-triangular matrix multiply; queries, keys and values make the weights data-dependent; scaling, causal masking and multiple heads → [[self-attention]]
- Attention is a communication mechanism between nodes in a directed graph, with no notion of space; the triangular mask is what makes it a decoder → [[attention-is-a-communication-mechanism]]
- Attention has no notion of space, so positions must be added → [[embeddings]]
- A block interleaves communication (attention) with computation (feed-forward); residual connections, pre-norm LayerNorm, decoder-only → [[transformer-architecture]]
- Dropout as regularization before scaling up → [[regularization]]
- nanoGPT's model.py is the same model with heads batched; the lecture code is released with its git log → [[nanogpt]], [[ng-video-lecture]]
- Pretraining yields a document completer; finetuning aligns it into an assistant; GPT-3 is the same architecture far larger; the finetuning stage is harder to replicate → [[pretraining-and-finetuning]], [[pretraining-gives-a-document-completer]]

## Fed pages
- [[tokenization]]
- [[bigram-language-model]]
- [[training-diagnostics]]
- [[spelled-out-build-from-scratch]]
- [[self-attention]]
- [[attention-is-a-communication-mechanism]]
- [[embeddings]]
- [[transformer-architecture]]
- [[regularization]]
- [[nanogpt]]
- [[ng-video-lecture]]
- [[pretraining-and-finetuning]]
- [[pretraining-gives-a-document-completer]]
