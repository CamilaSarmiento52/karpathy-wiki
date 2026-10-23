---
type: topic
aliases: [Softmax, logits, one-hot encoding]
first_seen: 2022-09-07
last_updated: 2022-09-12
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]"]
related: ["[[loss-functions]]", "[[bigram-language-model]]", "[[character-level-language-modeling]]"]
---
# Softmax
The softmax is the exponentiate-and-normalise step that turns any linear layer's outputs into a probability distribution ([[youtube-2022-09-07-makemore-1-bigram]] @1:27:22, @1:27:56).

## What he says
The raw outputs of the bigram net are positive and negative, so they cannot be probabilities (positive, summing to one) or counts (positive integers) ([[youtube-2022-09-07-makemore-1-bigram]] @1:19:33, @1:20:06). He interprets the outputs as log counts, also called logits; exponentiating gives positive count-like numbers, and normalising rows gives probabilities ([[youtube-2022-09-07-makemore-1-bigram]] @1:20:38, @1:21:44, @1:22:56, @1:23:28). Every step (multiply, add, exp, sum, divide) is differentiable, so the whole forward pass can be backpropagated through ([[youtube-2022-09-07-makemore-1-bigram]] @1:24:35, @1:28:29).

On the input side, integer indices cannot simply be plugged into neurons, whose weights act multiplicatively on inputs ([[youtube-2022-09-07-makemore-1-bigram]] @1:10:02). One-hot encoding turns an integer like 13 into a vector of zeros with a 1 at position 13 ([[youtube-2022-09-07-makemore-1-bigram]] @1:10:35). `torch.nn.functional.one_hot` takes integer tensors and `num_classes`; passing 27 explicitly avoids it guessing too small a size ([[youtube-2022-09-07-makemore-1-bigram]] @1:11:07, @1:11:40). Its output is int64 and it has no dtype argument, so he casts to float, since neural nets want floating-point inputs ([[youtube-2022-09-07-makemore-1-bigram]] @1:12:44, @1:13:18). Multiplying a one-hot vector by W plucks out one row of W, which is the same lookup the counting model did ([[youtube-2022-09-07-makemore-1-bigram]] @1:47:52, @1:48:25, @1:48:58).

In the MLP lecture he reuses the one-hot reading: a one-hot vector times the embedding table C gives the same row as indexing, so the lookup can be seen as a first linear layer on one-hot inputs, and he indexes because it is much faster ([[youtube-2022-09-12-makemore-2-mlp]] @14:58, @15:30, @16:02). The hand-rolled softmax loss is replaced by `F.cross_entropy`, partly because exponentiating large logits overflows, and `F.softmax` is likewise careful about overflow when sampling ([[youtube-2022-09-12-makemore-2-mlp]] @33:16, @36:02, @1:13:50).

## Claims
- [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers]]
- [[counting-and-gradient-bigram-models-are-the-same-model]]

## Related
- [[loss-functions]] — negative log likelihood on the softmax output
- [[bigram-language-model]]
- [[character-level-language-modeling]] — sampling from the distribution
- [[embeddings]] — the other reading of a one-hot linear layer
- [[use-cross-entropy-not-a-hand-rolled-loss]]
