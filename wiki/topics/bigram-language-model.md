---
type: topic
aliases: [Bigram model, bigram, count table, bigram baseline]
first_seen: 2022-09-07
last_updated: 2023-01-17
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2023-01-17-gpt-from-scratch]]"]
related: ["[[makemore]]", "[[character-level-language-modeling]]", "[[softmax]]", "[[regularization]]"]
---
# Bigram language model
A bigram model works with two characters at a time, predicting the next character from only the previous one; he calls it very simple and weak but a great place to start ([[youtube-2022-09-07-makemore-1-bigram]] @05:31, @06:03).

## What he says
Bigrams are collected with `zip(w, w[1:])` over a word wrapped with special start and end tokens ([[youtube-2022-09-07-makemore-1-bigram]] @06:36, @07:09, @08:15). The simplest way to learn the statistics is counting how often each pair occurs, first in a Python dictionary, then in a 2D PyTorch tensor with rows for the first character and columns for the second ([[youtube-2022-09-07-makemore-1-bigram]] @09:20, @12:43). Two special tokens waste an all-zero row and column, so he switches to a single `.` token at index 0 and offsets letters to start at 1, giving a 27×27 array ([[youtube-2022-09-07-makemore-1-bigram]] @20:56, @22:03, @22:36). Row 0 of the counts is then the counts of first letters; column 0 holds ending characters ([[youtube-2022-09-07-makemore-1-bigram]] @23:09). The normalised rows of the counts matrix P are the parameters of the bigram model ([[youtube-2022-09-07-makemore-1-bigram]] @50:13). Trained by counting, the model's average negative log likelihood on the training set is about 2.45 ([[youtube-2022-09-07-makemore-1-bigram]] @1:00:02). He stared at the samples for a few minutes to convince himself they were right; they are bad because the model does not know whether an H is the first letter or has a history ([[youtube-2022-09-07-makemore-1-bigram]] @33:46, @34:17, @34:52).

Recast as a neural net, a single linear layer of 27 neurons on 27 one-hot inputs (`xenc @ W`, no bias, no nonlinearity) is the whole network ([[youtube-2022-09-07-makemore-1-bigram]] @1:16:08, @1:18:26, @1:19:01). Trained on all 228,000 bigrams it reaches about 2.46, the same vicinity as counting ([[youtube-2022-09-07-makemore-1-bigram]] @1:43:27, @1:44:36, @1:45:08).

In the next lecture he gives the bigram model's limit: it looks at only one previous character and its predictions were not very name-like, and extending the count table to more context grows it exponentially (27 rows for one character, 729 for two, about 20,000 for three) while the counts per row collapse ([[youtube-2022-09-12-makemore-2-mlp]] @00:33, @01:06, @01:40).

The GPT lecture restarts from the same model: he calls the bigram model the simplest possible neural network for language modelling and begins there, having covered it in the makemore series ([[youtube-2023-01-17-gpt-from-scratch]] @21:57). It is a token embedding table of size vocab by vocab; each input integer plucks out a row that is read as the logits for the next character, so it predicts from the identity of a single token because tokens are not yet talking to each other ([[youtube-2023-01-17-gpt-from-scratch]] @23:04, @23:37, @24:12). The loss is negative log likelihood, implemented in PyTorch as cross entropy, which requires reshaping B,T,C logits to B*T,C ([[youtube-2023-01-17-gpt-from-scratch]] @24:44, @26:25, @26:58). Generation samples with softmax and `torch.multinomial` from the last time step and appends the result; he writes `generate` to feed the whole context even though a bigram only needs the last character, so the same function works once history is used ([[youtube-2023-01-17-gpt-from-scratch]] @30:19, @30:54, @33:47, @34:20). Trained with AdamW, the bigram model converges to a loss of about 2.5 ([[youtube-2023-01-17-gpt-from-scratch]] @34:53, @37:06, @41:36). For a bigram model positional embeddings are useless because the model is translation invariant; position starts to matter with self-attention ([[youtube-2023-01-17-gpt-from-scratch]] @1:01:20).

## Claims
- [[counting-and-gradient-bigram-models-are-the-same-model]]
- [[gradient-based-models-scale-where-count-tables-do-not]]
- [[weight-regularization-is-equivalent-to-count-smoothing]]

## Related
- [[makemore]]
- [[character-level-language-modeling]]
- [[softmax]] — the one-layer net's output
- [[regularization]] — smoothing the counts
- [[multilayer-perceptron]] — the next model in the series
- [[self-attention]], [[transformer-architecture]] — what the GPT lecture builds on top of the bigram baseline
- [[spelled-out-build-from-scratch]], [[training-diagnostics]] — the bigram script as starter code, and its loss at initialisation
