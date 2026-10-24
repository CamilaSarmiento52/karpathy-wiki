---
type: source
raw_path: raw/talks/XfpMkf4rD6E.md
published: 2023-05-19
medium: talk
summary: Guest lecture opening Stanford's CS25 in which he traces how AI converged on the Transformer, explains attention as data-dependent message passing on a directed graph, walks through nanoGPT, and argues the Transformer is a general-purpose, efficient, optimizable computer capable of in-context learning.
url: https://www.youtube.com/watch?v=XfpMkf4rD6E
title: "Stanford CS25: V2 I Introduction to Transformers w/ Andrej Karpathy"
---
# Stanford CS25: V2 I Introduction to Transformers w/ Andrej Karpathy
Raw: [[raw/talks/XfpMkf4rD6E]] · Original: https://www.youtube.com/watch?v=XfpMkf4rD6E

The course instructors speak for the first ten minutes; his part starts inside the @10:05 block. Published 2023-05-19; the lecture itself was given earlier, in the winter 2023 quarter, and he says he had worked on nanoGPT "over the last few days" (@31:02).

## Summary
The course instructors introduce CS25 and an attention timeline for the first ten minutes; his part starts at @10:05. He describes AI around 2011 as separate fields with their own feature pipelines and vocabularies, then neural nets spreading after 2012 and, since 2017, every field copy-pasting one architecture, the Transformer (@11:12, @12:50, @13:56). He traces the architecture's history from the 2003 neural language model through sequence-to-sequence, the encoder bottleneck and the 2014 soft-search attention paper, including an email from its first author on where attention came from, to "Attention Is All You Need" (@15:00, @16:39, @18:17, @19:57). He explains attention as the communication phase of the Transformer, a data-dependent message passing scheme on directed graphs, then steps through nanoGPT's decoder-only implementation (@22:45, @24:58, @31:02, @38:49). He covers how Transformers are applied to images, speech, RL and multi-sensor inputs by chopping inputs into pieces (@52:43, @54:23), names in-context learning as what makes them special (@55:30, @56:34), and argues the architecture is expressive, optimizable and efficient, a general-purpose computer (@58:12, @59:18, @59:51). Audience Q&A covers autoregression versus diffusion, inductive biases and a scratchpad for extending memory (@50:15, @1:06:28, @1:08:47).

## Key points
- AI fields that once had separate methods and vocabularies converged on neural nets after 2012 and on one architecture after 2017 → [[ai-has-converged-on-one-architecture]]
- The path to the Transformer: neural LM 2003, seq2seq 2014, the encoder bottleneck, soft-search attention 2014, then 2017 → [[transformer-architecture]]
- The 2017 architecture has barely changed; pre-norm LayerNorm is the main change that stuck → [[transformer-architecture]], [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]
- Attention is the communication phase: data-dependent message passing on a directed graph; the MLP is the compute phase → [[attention-is-a-communication-mechanism]], [[self-attention]]
- Heads are copies in parallel, layers copies in series; self- and cross-attention differ only in where keys and values come from → [[self-attention]]
- Encoder, decoder and encoder-decoder models differ in connectivity: delete the mask line for an encoder, add a cross-attention line for encoder-decoder → [[transformer-architecture]]
- nanoGPT walk-through: integer-encoded text, B×T batches, token plus position embeddings, blocks, LM head, cross-entropy → [[nanogpt]], [[tokenization]], [[embeddings]], [[character-level-language-modeling]]
- Generation feeds each sampled character back and crops the context at the block size → [[sampling-from-language-models]]
- Images, speech, RL trajectories and extra sensor inputs are chopped up and fed in as a set → [[transformer-architecture]]
- In-context learning is what makes Transformers special; there may be something like gradient descent in the activations → [[prompting-llms]]
- Expressive, optimizable and efficient at once: a general-purpose efficient optimizable computer → [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]
- GPT runs natural-language programs given as prompts → [[gpt-is-a-general-purpose-computer-running-natural-language-programs]], [[english-is-the-new-programming-language]]
- With enough data, encode less inductive bias; biases live in connectivity and positional encodings → [[with-enough-data-encode-less-inductive-bias]]
- He does not love autoregressive sampling and finds diffusion more appealing → [[he-does-not-love-autoregressive-sampling]], [[sampling-from-language-models]]

## Fed pages
- [[transformer-architecture]]
- [[self-attention]]
- [[attention-is-a-communication-mechanism]]
- [[nanogpt]]
- [[tokenization]]
- [[embeddings]]
- [[character-level-language-modeling]]
- [[prompting-llms]]
- [[sampling-from-language-models]]
- [[ai-has-converged-on-one-architecture]]
- [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]
- [[gpt-is-a-general-purpose-computer-running-natural-language-programs]]
- [[english-is-the-new-programming-language]]
- [[with-enough-data-encode-less-inductive-bias]]
- [[he-does-not-love-autoregressive-sampling]]
- [[the-transformer-is-probably-not-the-final-architecture]]
