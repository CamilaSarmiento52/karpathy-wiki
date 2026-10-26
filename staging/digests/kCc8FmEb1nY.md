# Digest: Let's build GPT: from scratch, in code, spelled out.
- raw: raw/youtube/kCc8FmEb1nY.md · published: 2023-01-17 · medium: youtube · words: 21238
- source slug: youtube-2023-01-17-gpt-from-scratch

## Source page

```
---
type: source
raw_path: raw/youtube/kCc8FmEb1nY.md
published: 2023-01-17
medium: youtube
summary: Two-hour lecture that builds a decoder-only Transformer on tiny Shakespeare from an empty file, deriving self-attention step by step, scaling it to a nanoGPT-shaped model, and closing with how ChatGPT's pretraining and finetuning stages relate to it.
url: https://www.youtube.com/watch?v=kCc8FmEb1nY
title: "Let's build GPT: from scratch, in code, spelled out."
---
# Let's build GPT: from scratch, in code, spelled out.
Raw: [[raw/youtube/kCc8FmEb1nY]] · Original: https://www.youtube.com/watch?v=kCc8FmEb1nY

## Summary
A 1h56m coding lecture that writes a character-level Transformer language model from an empty
file, training on the 1 MB tiny Shakespeare text (@03:23, @06:45). He starts with a
character-level tokenizer and contrasts it with sub-word schemes such as SentencePiece and
tiktoken (@09:31, @11:10), then builds a bigram baseline, checks its initial loss against the
value expected from the vocabulary size, and gets it generating (@21:57, @28:03). The core of
the video derives self-attention: first averaging past tokens with a lower-triangular matrix
multiply, then making the weights data-dependent with queries, keys and values, adding
scaling, causal masking, multiple heads and a feed-forward layer (@42:09, @1:01:54, @1:22:01).
He adds residual connections, pre-norm LayerNorm and dropout, scales the model up to reach a
validation loss of 1.48 in about 15 minutes on an A100, and walks through how nanoGPT's
`model.py` matches what was built (@1:28:36, @1:40:21, @1:46:28). He ends by explaining why
the model is decoder-only and how ChatGPT adds a finetuning stage of supervised data, a
reward model and PPO on top of pretraining (@1:42:35, @1:48:42, @1:53:43).

## Key points
- Tokenization trades vocabulary size against sequence length; he keeps characters for simplicity → [[tokenization]]
- A bigram model predicts the next character from the current one alone and is the baseline → [[bigram-language-model]]
- Check the loss at initialization against what the vocabulary size predicts → [[check-the-loss-at-initialization]]
- Build up incrementally from a bigram script, reading validation loss after each addition → [[build-up-from-a-bigram-baseline]]
- Averaging past tokens is a weighted aggregation done with a lower-triangular matrix multiply → [[lower-triangular-weighted-aggregation]]
- Queries, keys and values make the aggregation weights data-dependent → [[query-key-value]], [[self-attention]]
- Attention is a communication mechanism between nodes in a directed graph → [[attention-is-a-communication-mechanism]]
- Attention has no notion of space, so positions must be added → [[positional-embeddings]], [[attention-has-no-notion-of-space]]
- Dividing by the square root of head size keeps softmax diffuse at initialization → [[scaled-attention]]
- The triangular mask is what makes a block a decoder; encoders delete it → [[causal-masking]], [[the-triangular-mask-is-what-makes-it-a-decoder]]
- Multiple heads are several communication channels in parallel → [[multi-head-attention]]
- A block interleaves communication (attention) with computation (feed-forward) → [[transformer-block]]
- Residual connections give gradients a direct path from loss to input → [[residual-connections]]
- LayerNorm normalizes rows per token; he uses the pre-norm variant → [[layer-norm]]
- Dropout as regularization before scaling up → [[dropout]]
- Decoder-only because there is nothing to condition on; cross-attention is for encoder-decoder → [[decoder-only-transformer]]
- nanoGPT's model.py is the same model with heads batched → [[nanogpt]], [[ng-video-lecture]]
- Pretraining yields a document completer; finetuning aligns it into an assistant → [[pretraining-and-finetuning]], [[pretraining-gives-a-document-completer]]
- GPT-3 is architecturally near-identical to the lecture model but vastly larger → [[gpt3-is-the-same-architecture-far-larger]]
- The finetuning stage is much harder to replicate because the data is internal → [[the-finetuning-stage-is-harder-to-replicate]]

## Fed pages
- [[tokenization]]
- [[bigram-language-model]]
- [[lower-triangular-weighted-aggregation]]
- [[self-attention]]
- [[query-key-value]]
- [[positional-embeddings]]
- [[scaled-attention]]
- [[causal-masking]]
- [[multi-head-attention]]
- [[transformer-block]]
- [[residual-connections]]
- [[layer-norm]]
- [[dropout]]
- [[decoder-only-transformer]]
- [[pretraining-and-finetuning]]
- [[attention-is-a-communication-mechanism]]
- [[attention-has-no-notion-of-space]]
- [[the-triangular-mask-is-what-makes-it-a-decoder]]
- [[pretraining-gives-a-document-completer]]
- [[gpt3-is-the-same-architecture-far-larger]]
- [[the-finetuning-stage-is-harder-to-replicate]]
- [[nanogpt]]
- [[ng-video-lecture]]
- [[build-up-from-a-bigram-baseline]]
- [[check-the-loss-at-initialization]]
```

## Candidates

### topic: tokenization
- existing: no
- aliases: Tokenization, tokenizer, character-level tokenizer, sub-word tokenizer, BPE
- statements:
  - To tokenize is to convert raw text into a sequence of integers according to a vocabulary of possible elements (@09:31).
  - His lecture uses a character-level tokenizer: a lookup table from each of the 65 characters in tiny Shakespeare to an integer and back (@08:59, @10:35).
  - Sub-word tokenizers such as Google's SentencePiece and OpenAI's tiktoken (byte-pair encoding, used by GPT) encode neither whole words nor single characters, and are what is usually adopted in practice (@10:35, @11:10).
  - The GPT-2 encoding has roughly 50,000 tokens, so "hi there" becomes three integers instead of eight (@11:43).
  - You can trade off codebook size against sequence length: small vocabularies give long sequences, large vocabularies give short ones (@11:43, @12:16).
  - He keeps the character-level tokenizer because it is the simplest thing, accepting very long sequences (@12:16).
  - Because OpenAI uses sub-word tokens, the Shakespeare set would be around 300,000 tokens in their vocabulary rather than 1 million characters (@1:49:47).

### topic: bigram-language-model
- existing: no
- aliases: Bigram language model, bigram baseline
- statements:
  - He calls the bigram model the simplest possible neural network for language modeling and starts there, having covered it in the makemore series (@21:57).
  - It is a token embedding table of size vocab by vocab; each input integer plucks out a row that is read as the logits for the next character (@23:04, @23:37).
  - It predicts the next character from the identity of a single token because tokens are not yet talking to each other (@24:12).
  - Loss is negative log likelihood, implemented in PyTorch as cross entropy, which requires reshaping B,T,C logits to B*T,C (@24:44, @26:25, @26:58).
  - Generation samples with softmax and torch.multinomial from the last time step and appends the result (@30:19, @30:54).
  - He writes generate to feed the whole context even though a bigram only needs the last character, so the same function works once history is used (@33:47, @34:20).
  - Trained with AdamW, the bigram model converges to a loss of about 2.5 (@34:53, @37:06, @41:36).

### method: check-the-loss-at-initialization
- existing: no
- aliases: expected loss at init
- statements:
  - With 65 vocabulary elements he expects an initial loss of about -ln(1/65), roughly 4.17 (@28:03).
  - The measured 4.87 tells him the initial predictions are not diffuse and carry some entropy, i.e. the model is guessing wrong at init (@28:37).
  - Related hygiene he shows in the same script: average the loss over many batches with an estimate_loss function because a single batch is a noisy measurement (@39:23, @39:56); switch the model between eval and train mode as good practice even when no layer yet depends on it (@40:31); wrap evaluation in torch.no_grad so PyTorch can save memory (@41:04).
  - Steps (proposed): compute the loss a uniform guess over the vocabulary would give; run the untrained model and compare; investigate if the measured loss is much higher.

### method: build-up-from-a-bigram-baseline
- existing: no (compare [[quick-experiment-loop]], a later nanochat-era loop; this one is pedagogical rather than research)
- aliases: incremental model build-up
- statements:
  - He begins with an empty file and defines the Transformer piece by piece, training on tiny Shakespeare (@06:45).
  - He converts the notebook into a roughly 120-line script (bigram.py) as starter code to iterate on, with hyperparameters at the top, GPU support and a loss estimator (@37:41, @38:15, @41:36).
  - He reads validation loss after each addition: bigram 2.5 (@41:36), one self-attention head 2.4 (@1:21:27), four heads 2.28 (@1:23:41), feed-forward 2.24 (@1:25:52), residuals with 4x inner layer 2.08 (@1:31:57), LayerNorm 2.06 (@1:36:59), scaled-up model 1.48 (@1:40:21).
  - He decreases the learning rate when adding self-attention because attention cannot tolerate very high learning rates, and again when the network gets much bigger (@1:21:27, @1:39:46).
  - When stacking blocks fails to train well he recognizes deep-network optimization issues and borrows residual connections and LayerNorm from the paper rather than tuning (@1:28:02).
  - He adds dropout before scaling up because he is concerned about overfitting (@1:39:13).
  - He releases the code with its git log commits so the build-up can be followed step by step (@1:54:50).
  - Steps (proposed): start from the simplest model; package it as a script with a stable loss estimate; add one component at a time; compare validation loss; adjust learning rate as the model grows; scale up last.

### topic: lower-triangular-weighted-aggregation
- existing: no
- aliases: the mathematical trick, bag of words averaging, masked softmax aggregation, tril trick
- statements:
  - He introduces a mathematical trick that is at the heart of an efficient self-attention implementation before writing the attention block (@42:09).
  - The fifth token should only communicate with tokens one to four, because information must flow from the past and never from the future it is trying to predict (@43:17).
  - The simplest communication is to average the channels of the current and all preceding tokens into a feature vector that summarizes the token in its history (@43:52).
  - He calls a plain average an extremely weak, lossy form of interaction that discards spatial arrangement, to be fixed later (@44:26).
  - A lower-triangular matrix of ones (torch.tril) multiplied with a matrix sums a variable number of its rows; normalizing the rows to sum to one turns the sums into incremental averages (@47:14, @48:26, @50:05, @50:39).
  - PyTorch broadcasts a T-by-T weight matrix across the batch as a batched matrix multiply, giving the same result as the for loop (@52:20, @52:52).
  - This is a weighted aggregation whose weights sit in a triangular T-by-T array (@53:59).
  - The third form starts weights at zero, masked_fills the upper triangle with negative infinity and applies softmax, which produces the same matrix (@54:33, @55:07, @56:14).
  - He prefers the softmax form because the zeros can be read as affinities, how much of each past token to aggregate, and the minus infinity says the future cannot communicate (@56:46).
  - Preview: the affinities will become data-dependent, with tokens finding each other more or less interesting (@57:21).
  - Long story short: weighted aggregation of past elements is a matrix multiply with a lower-triangular matrix whose entries say how much of each element fuses into a position (@57:53).

### topic: self-attention
- existing: no
- aliases: Self-attention, attention, attention head, single head of self-attention
- statements:
  - He calls the self-attention derivation probably the most important part of the video to understand (@1:01:54).
  - The problem self-attention solves is gathering information from the past in a data-dependent way, e.g. a vowel looking for consonants in its past (@1:03:36).
  - Every token emits a query (what am I looking for) and a key (what do I contain); affinities are the dot products of a token's query with all keys (@1:04:09).
  - Aligned keys and queries interact strongly, so the token learns more about that specific token than others (@1:04:45).
  - Keys and queries are produced in parallel and independently by linear layers with no bias; communication happens only in the query-key matmul, which transposes the last two dimensions to give a B,T,T affinity tensor (@1:05:18, @1:05:52, @1:06:25).
  - The weights are now data-dependent and differ per batch element (@1:06:58, @1:07:31).
  - Raw affinities range over negative and positive values; masking the upper triangle and exponentiating and normalizing gives a distribution summing to one (@1:09:11, @1:09:45).
  - A value vector is also produced; the output aggregates values, not the raw x, so the head output has head-size dimensions (@1:10:20, @1:10:53).
  - He frames x as private information, the query as what I am interested in, the key as what I have, and the value as what I will communicate if you find me interesting (@1:10:53).
  - Elements across the batch never talk to each other; with batch four and block size eight there are four separate pools of eight nodes (@1:13:38).
  - It is self-attention because keys, queries and values all come from the same source x; attention in general is broader (@1:15:55).
  - After adding one head with lowered learning rate, validation loss falls from about 2.5 to 2.4 (@1:21:27).
  - The head module registers tril as a buffer, not a parameter, and crops generation context to block size because of the positional table (@1:19:15, @1:20:55).

### topic: query-key-value
- existing: no (could be merged into [[self-attention]] by merge; listed separately because he explains each role)
- aliases: queries keys and values, Q K V
- statements:
  - Query: roughly, what am I looking for; key: roughly, what do I contain (@1:04:09).
  - A vowel at the eighth position might emit a query for consonants at positions up to four, and a matching key channel gives a high dot product (@1:07:31, @1:08:04).
  - Value: the vector a token communicates for aggregation, distinct from its private x (@1:10:20, @1:10:53).
  - In cross-attention the queries come from x while keys and values come from a separate source such as an encoder (@1:15:55, @1:16:28).

### claim: attention-is-a-communication-mechanism
- existing: no
- title: Attention is a communication mechanism between nodes in a directed graph
- confidence: stated
- quote: "attention is a communication mechanism" (@1:11:26)
- statements:
  - Nodes in a directed graph each hold a vector and aggregate information via a weighted sum from the nodes pointing to them, in a data-dependent way (@1:11:26, @1:11:58).
  - In autoregressive language modeling the first node is pointed to only by itself and the eighth by all previous nodes and itself, but attention applies to any directed graph (@1:11:58, @1:12:32).
  - Attention supports arbitrary connectivity; encoder and decoder blocks differ only in whether the mask line is present (@1:15:19).
- relation: none existing.

### claim: attention-has-no-notion-of-space
- existing: no
- title: Attention has no notion of space, so position must be added explicitly
- confidence: stated
- quote: "attention simply acts over like a set of vectors in this graph" (@1:12:32)
- statements:
  - Nodes do not know where they are, which is why positional encodings are added; this differs from convolution, where filters act over a spatial layout (@1:12:32, @1:13:03).
- relation: supports [[positional-embeddings]] (topic).

### topic: positional-embeddings
- existing: no
- aliases: Positional embeddings, position embedding table, positional encodings
- statements:
  - Beyond token identity he adds a second embedding table of block size by n_embd so each position gets its own vector (@1:00:15).
  - The input x becomes token embeddings plus positional embeddings, broadcast across the batch (@1:00:47, @1:01:20).
  - For a bigram model position is useless because the model is translation invariant; it starts to matter with self-attention (@1:01:20).
  - Because the table only covers block size positions, generation must crop the context to the last block size tokens (@1:20:55).

### topic: scaled-attention
- existing: no
- aliases: Scaled dot-product attention, scaled attention, 1/sqrt(head size)
- statements:
  - The paper divides the query-key dot product by the square root of head size, calling it scaled attention (@1:17:01).
  - With unit-Gaussian k and q the naive weights have variance on the order of head size (16 here); scaling restores variance one (@1:17:34).
  - This matters because the weights feed softmax, which should be fairly diffuse especially at initialization (@1:17:34, @1:18:10).
  - Softmax converges towards one-hot vectors when its inputs take extreme values, as he shows by multiplying a tensor by eight (@1:18:10, @1:18:42).
  - Too-peaky softmax means every node aggregates from a single other node, which is not wanted at initialization; the scaling just controls variance at init (@1:18:42).

### topic: causal-masking
- existing: no
- aliases: Causal masking, triangular mask, decoder block vs encoder block, autoregressive mask
- statements:
  - Future tokens must not communicate with past ones in language modeling, because they would give away the answer (@1:14:11, @1:15:19).
  - For tasks like sentiment analysis you may want all tokens to talk fully; that is an encoder block, which deletes the masking line (@1:14:11, @1:14:45).
  - What he implements is sometimes called a decoder block because of its autoregressive format with the triangular mask (@1:14:45).
  - Both are allowed; attention does not care and supports arbitrary connectivity (@1:15:19).

### claim: the-triangular-mask-is-what-makes-it-a-decoder
- existing: no
- title: Using the triangular mask is what makes the Transformer a decoder
- confidence: stated
- quote: "what makes it a decoder is that we are using the Triangular mask" (@1:43:07)
- statements:
  - The mask gives the autoregressive property that lets you sample from the model, so it can be used for language modeling (@1:43:07).
- relation: supports [[decoder-only-transformer]], [[causal-masking]].

### topic: multi-head-attention
- existing: no
- aliases: Multi-head attention, multi-headed self-attention, heads
- statements:
  - Multi-head attention is just multiple attentions applied in parallel with their results concatenated over the channel dimension (@1:22:01, @1:22:35).
  - Instead of one 32-dimensional channel he runs four 8-dimensional heads whose outputs concatenate back to 32; he compares this to group convolution (@1:22:35, @1:23:08).
  - Four heads bring validation loss to about 2.28 from 2.4 (@1:23:41).
  - Multiple communication channels help because tokens have many different things to look for, such as consonants, vowels, or particular positions (@1:23:41, @1:24:15).
  - The head count is like group size: 32 embedding dimensions with four heads gives head size eight; the scaled model uses 384 dimensions and six heads of 64 (@1:26:59, @1:27:31, @1:39:46).
  - nanoGPT batches all heads inside a single causal self-attention module with a fourth tensor dimension, which is mathematically equivalent but more efficient (@1:47:01, @1:47:36).

### topic: transformer-block
- existing: no
- aliases: Transformer block, communication then computation, feed-forward, MLP
- statements:
  - The paper's feed-forward part is a simple per-position MLP; he adds it because after attention the tokens looked at each other but had no time to think on what they found (@1:24:48, @1:25:20).
  - Self-attention is the communication; the feed-forward, applied to each token independently, is where they think on the gathered data (@1:25:52).
  - A block intersperses communication (multi-head self-attention) with computation (feed-forward); the Transformer groups and replicates these blocks (@1:26:26, @1:26:59).
  - Stacking blocks sequentially without further ideas did not train well, which he attributes to deep-network optimization issues (@1:27:31, @1:28:02).
  - The feed-forward inner layer is four times the embedding dimension, following the paper's 512 to 2048 ratio (@1:31:23, @1:31:57).
  - The scaled model has six layers, 384 embedding dimensions, six heads, block size 256, batch size 64 and dropout 0.2 (@1:39:13, @1:39:46).
  - The result is a decoder-only Transformer with the major pieces of the original paper in place (@1:37:35).

### topic: residual-connections
- existing: no
- aliases: Residual connections, skip connections, residual pathway
- statements:
  - Skip or residual connections come from the 2015 residual learning paper and add transformed data back onto the previous features (@1:28:36).
  - He visualizes a residual pathway from which computation forks off and projects back by addition (@1:28:36, @1:29:11).
  - Because addition distributes gradients equally to both branches, gradients hop through every addition node from the loss to the input, a gradient superhighway (@1:29:11, @1:29:46).
  - Residual blocks are initialized to contribute very little, so at init the pathway is almost unobstructed and blocks come online during optimization (@1:29:46, @1:30:19).
  - Implemented as x = x + sa(x) and x = x + ffwd(x), with a linear projection back into the residual pathway after both (@1:30:19, @1:30:51, @1:31:23).
  - With residuals and the 4x inner layer, validation loss reaches 2.08 and train loss starts to get ahead of validation, a little overfitting (@1:31:57, @1:32:30).

### topic: layer-norm
- existing: no
- aliases: LayerNorm, layer normalization, pre-norm
- statements:
  - LayerNorm is very similar to batch norm, which made each neuron zero-mean unit-variance across the batch (@1:32:30, @1:33:04).
  - Changing the normalization dimension from columns to rows turns his makemore BatchNorm1d into LayerNorm, normalizing each example's vector (@1:33:37, @1:34:10).
  - Because the computation no longer spans examples, running buffers and the train/test distinction go away; gamma and beta remain (@1:34:43).
  - Unlike the original paper's add-and-norm after the transformation, it is now common to apply LayerNorm before, the pre-norm formulation, which he implements as a slight deviation (@1:35:19).
  - Mean and variance are taken over the embedding dimension per token; batch and time act as batch dimensions (@1:36:26).
  - LayerNorm improves validation loss from 2.08 to 2.06; he expects more help in bigger, deeper networks; a final LayerNorm goes before the output linear layer (@1:36:59).

### topic: dropout
- existing: no
- aliases: Dropout
- statements:
  - Dropout can be added right before the connection back into the residual pathway, at the end of multi-head attention, and on the affinities after softmax to randomly prevent some nodes from communicating (@1:38:07).
  - From a 2014 paper; every forward-backward pass shuts off a random subset of neurons, effectively training an ensemble of sub-networks merged at test time (@1:38:40, @1:39:13).
  - He treats it as a regularization technique added because he was about to scale the model and was concerned about overfitting (@1:39:13).
  - The scaled model uses dropout 0.2 (@1:39:46).

### topic: decoder-only-transformer
- existing: no
- aliases: Decoder-only Transformer, encoder-decoder, cross-attention
- statements:
  - The implemented model is decoder-only: no encoder and no cross-attention block; the block has only self-attention and feed-forward (@1:42:35).
  - It is decoder-only because text generation here is unconditioned, just imitating a dataset (@1:43:07, @1:45:55).
  - The original paper used encoder-decoder because it was a machine translation paper, reading French tokens and decoding English between start and end tokens (@1:43:39, @1:44:12).
  - The encoder runs a Transformer with no triangular mask so all tokens talk fully; the decoder adds cross-attention where queries come from x but keys and values come from the encoder output, feeding into every decoder block (@1:44:48, @1:45:22).
  - This is exactly as done in GPT (@1:45:55).
  - Cross-attention is used when there is a separate source of nodes to pull information from (@1:16:28).

### topic: pretraining-and-finetuning
- existing: no (related to [[rlvr]], which is a different, later RL stage; do not merge)
- aliases: Pretraining vs finetuning, ChatGPT training stages, RLHF, alignment stage
- statements:
  - Training ChatGPT has roughly two stages: pretraining and finetuning (@1:48:42).
  - Pretraining trains a decoder-only Transformer on a large chunk of internet to babble text, very similar to the lecture's tiny baby pretraining step (@1:48:42, @1:49:14).
  - His Shakespeare model has about 10 million parameters trained on about 1 million characters, roughly 300,000 tokens in OpenAI's vocabulary (@1:49:14, @1:49:47).
  - GPT-3's largest model has 175 billion parameters trained on 300 billion tokens, about a millionfold more data, and that is not even large by today's standards (@1:50:22, @1:50:56).
  - Training at that scale is a massive infrastructure challenge with thousands of GPUs (@1:50:56).
  - After pretraining you get a document completer that babbles internet, may answer questions with more questions, and is unaligned (@1:51:29, @1:52:02).
  - The finetuning stage aligns it to be an assistant in roughly three steps: supervised finetuning on question-answer documents, perhaps thousands of examples (@1:52:36); raters rank responses to train a reward model (@1:53:08); PPO, a policy-gradient RL optimizer, finetunes the sampling policy to score high reward (@1:53:43).
  - Very large models are very sample efficient during finetuning (@1:53:08).
  - Much of this data is internal to OpenAI and much harder to replicate; nanoGPT focuses on pretraining (@1:54:16).
  - Anything that is not a plain document completer, e.g. task performance, alignment or sentiment, requires further finetuning stages, simple supervised or RLHF-style (@1:55:22, @1:55:55).

### claim: pretraining-gives-a-document-completer
- existing: no
- title: Pretraining alone gives a document completer, not an assistant
- confidence: stated
- quote: "you get a document completer" (@1:51:29)
- statements:
  - It will complete whatever a similar internet document would, giving undefined behaviour on a question (@1:51:29, @1:52:02).
- relation: none existing.

### claim: gpt3-is-the-same-architecture-far-larger
- existing: no
- title: GPT-3 is architecturally nearly identical to the lecture model, only 10,000 to 1,000,000 times bigger
- confidence: stated
- quote: "the architecture is actually like nearly identical to what we implemented ourselves" (@1:50:56)
- statements:
  - GPT-3's hyperparameters (layers, n_embd, heads, head size, batch size, learning rate) should be recognizable from the lecture (@1:50:22, @1:50:56).
  - Models like GPT-3 are between 10,000 and 1 million times bigger depending on how you count (@1:55:22).
- relation: none existing.

### claim: the-finetuning-stage-is-harder-to-replicate
- existing: no
- title: ChatGPT's finetuning stage is much harder to replicate than pretraining
- confidence: stated
- quote: "it's much harder to replicate this stage" (@1:54:16)
- statements:
  - A lot of the alignment data is not public and is internal to OpenAI (@1:54:16).
- relation: none existing.

### artifact: nanogpt
- existing: yes ([[nanogpt]], alias nanoGPT)
- statements:
  - As of January 2023 he describes nanoGPT as two files of about 300 lines each, one defining the GPT model and one training it on any text (@05:36).
  - Trained on OpenWebText it reproduces GPT-2's smallest 124M model, proving the codebase is arranged correctly and can load OpenAI's weights (@06:12).
  - The lecture's goal is to write this repository from scratch (@06:45).
  - train.py adds checkpointing, pretrained weights, learning-rate decay, model compilation and distributed training; model.py is almost identical to the lecture code (@1:46:28, @1:47:01).
  - Differences: heads batched in one causal self-attention module; GELU instead of ReLU so OpenAI checkpoints load; parameters split into weight-decayed and not (@1:47:36, @1:48:10).
  - nanoGPT focuses on the pretraining stage (@1:54:16).
- relation: extends the existing page backwards in time; the existing page's `status: superseded` and 2025 README statements stand. He says GPT-2 is "from 2017 if I recall correctly" (@06:12); do not copy that date into the wiki.

### artifact: ng-video-lecture
- existing: no
- aliases: ng-video-lecture, bigram.py, gpt.py, lecture notebook
- statements:
  - He develops the code in a Google Colab notebook he will share in the video description (@07:50).
  - The intermediate script is about 120 lines and he calls it bigram.py (@41:36).
  - The final training code is roughly 200 lines; he will release the codebase with all git log commits made along the way, plus the notebook (@1:54:50).
- notes: the repository name ng-video-lecture is never spoken in the transcript; merge should take `repo_url` from GitHub (github.com/karpathy/ng-video-lecture), not from this source, and mark it as such.

## Quotes
- "the authors didn't fully anticipate the impact that the Transformer would have" (@02:17)
- "you can trade off the code book size and the sequence lengths" (@11:43)
- "we can actually guess at what the loss should be" (@28:03)
- "a good practice to Think Through what mode your neural network is in" (@40:31)
- "an average is an extremely weak form of interaction" (@44:26)
- "this is probably the most important part of this video to understand" (@1:01:54)
- "the query Vector roughly speaking is what am I looking for" (@1:04:09)
- "attention is a communication mechanism" (@1:11:26)
- "attention simply acts over like a set of vectors in this graph" (@1:12:32)
- "attention supports arbitrary connectivity between nodes" (@1:15:19)
- "the scaling is used just to control the variance at initialization" (@1:18:42)
- "the self attention is the communication" (@1:25:52)
- "you have this gradient Super Highway that goes directly from the supervision" (@1:29:46)
- "what makes it a decoder is that we are using the Triangular mask" (@1:43:07)
- "the architecture is actually like nearly identical to what we implemented ourselves" (@1:50:56)
- "you get a document completer" (@1:51:29)
- "it babbles but it doesn't Babble Shakespeare it babbles internet" (@1:51:29)
- "these very very large models are very sample efficient during their fine-tuning" (@1:53:08)
- "it's much harder to replicate this stage" (@1:54:16)
- "nanog GPT focuses on the pre-training stage" (@1:54:16)

## Notes for merge
- Caption misspellings (copy quotes as written, paraphrase correctly): "Byram"/"byr"/"pyr" = bigram; "nanog GPT"/"N GPT" = nanoGPT; "chpt"/"CH GPT"/"chat jpt" = ChatGPT; "Hau" = haiku; "Trill" = torch.tril; "way"/"wayy"/"we"/"Whey" = wei (the weights tensor); "Expo"/"xbo" = xbow; "nbed"/"nmed"/"n ined"/"n Ed" = n_embd; "ATM W" = AdamW; "Tik token"/"tick token" = tiktoken; "bashor"/"bash Norm" = BatchNorm; "gion"/"gsh"/"gashin" = Gaussian; "Galu" = GELU; "Rel"/"Ru" = ReLU; "po"/"Po" = PPO; "presidual learning" = Deep Residual Learning; "248" = 2048; "lawn" = ln; "microG grad" = micrograd; "b.p" = bigram.py; "prorm" = pre-norm; "incoder" = encoder; "Raiders" = raters; "spous" = spurious; "unineed" = unaligned.
- Factual slip in the source: he says GPT-2 is "from 2017 if I recall correctly" (@06:12). GPT-2 is from 2019. Paraphrase as "an early OpenAI GPT" rather than repeating the year, or flag it.
- Mentioned but not explained (do not make topics): makemore and micrograd series (@07:18, @29:11 implied, @33:47); AdamW vs SGD (@34:53); torch.compile and distributed training (@1:46:28); weight decay parameter groups (@1:48:10); GPT-3 paper table (@1:50:22); OpenAI's ChatGPT blog post (@1:52:02); GitHub Copilot suggesting n_embd=32 (@58:59); tiny Shakespeare dataset details beyond "about 1 MB, all of Shakespeare" (@03:57).
- Hardware claim is hedged: "about 15 minutes on my a100 GPU" with "I want to say" (@1:40:21); he advises not running the scaled config on CPU or a MacBook (@1:40:54).
- The RLHF description (@1:52:36 to @1:53:43) is a 2023 account of ChatGPT's finetuning. It is not RLVR; link [[pretraining-and-finetuning]] to [[rlvr]] only as related/context, not supports or extends, since the 2025 blog describes a different stage. A `training-stages` timeline could later connect them.
- query-key-value could be folded into self-attention if merge prefers fewer pages; the statements above are separable either way.
- The `check-the-loss-at-initialization` method is a short habit shown once; if merge judges a single demonstration too thin for a method page, keep the statements inside [[bigram-language-model]] instead.
- Validation-loss numbers in the build-up are read off his screen as he states them; they are not reproducible to the decimal and should be written as "about".
- Source predates every existing wiki source (2023 vs 2025 to 2026), so `first_seen` on new topics will be 2023-01-17, and [[nanogpt]]'s source list gains its earliest entry.
