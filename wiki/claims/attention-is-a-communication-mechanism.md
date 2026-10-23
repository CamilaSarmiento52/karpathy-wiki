---
type: claim
stated_on: 2023-01-17
confidence: stated
sources: ["[[youtube-2023-01-17-gpt-from-scratch]]"]
topic: "[[self-attention]]"
---
# Attention is a communication mechanism between nodes in a directed graph
> "attention is a communication mechanism" — [[youtube-2023-01-17-gpt-from-scratch]] @1:11:26

## Context
Having written one head of self-attention, he steps back: nodes in a directed graph each hold a vector and aggregate information via a weighted sum from the nodes pointing to them, in a data-dependent way ([[youtube-2023-01-17-gpt-from-scratch]] @1:11:26, @1:11:58). In autoregressive language modelling the first node is pointed to only by itself and the eighth by all previous nodes and itself, but attention applies to any directed graph ([[youtube-2023-01-17-gpt-from-scratch]] @1:11:58, @1:12:32). Attention simply acts over a set of vectors in this graph: the nodes have no notion of space and do not know where they are, which is why positional encodings are added, unlike convolution, where filters act over a spatial layout ([[youtube-2023-01-17-gpt-from-scratch]] @1:12:32, @1:13:03). Attention supports arbitrary connectivity; encoder and decoder blocks differ only in whether the masking line is present ([[youtube-2023-01-17-gpt-from-scratch]] @1:15:19). Later he says what makes the model a decoder is the triangular mask, which gives the autoregressive property that lets you sample from it ([[youtube-2023-01-17-gpt-from-scratch]] @1:43:07).

## Related claims
- **Note:** [[gpt-is-not-a-complicated-model]] is the README-side version of the same simplicity: indices in, a Transformer, a distribution out; that page cites the minGPT README ([[youtube-2023-01-17-gpt-from-scratch]] @1:11:26).
