---
type: topic
aliases: [Bigram model, bigram, count table]
first_seen: 2022-09-07
last_updated: 2022-09-12
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]"]
related: ["[[makemore]]", "[[character-level-language-modeling]]", "[[softmax]]", "[[regularization]]"]
---
# Bigram language model
A bigram model works with two characters at a time, predicting the next character from only the previous one; he calls it very simple and weak but a great place to start ([[youtube-2022-09-07-makemore-1-bigram]] @05:31, @06:03).

## What he says
Bigrams are collected with `zip(w, w[1:])` over a word wrapped with special start and end tokens ([[youtube-2022-09-07-makemore-1-bigram]] @06:36, @07:09, @08:15). The simplest way to learn the statistics is counting how often each pair occurs, first in a Python dictionary, then in a 2D PyTorch tensor with rows for the first character and columns for the second ([[youtube-2022-09-07-makemore-1-bigram]] @09:20, @12:43). Two special tokens waste an all-zero row and column, so he switches to a single `.` token at index 0 and offsets letters to start at 1, giving a 27×27 array ([[youtube-2022-09-07-makemore-1-bigram]] @20:56, @22:03, @22:36). Row 0 of the counts is then the counts of first letters; column 0 holds ending characters ([[youtube-2022-09-07-makemore-1-bigram]] @23:09). The normalised rows of the counts matrix P are the parameters of the bigram model ([[youtube-2022-09-07-makemore-1-bigram]] @50:13). Trained by counting, the model's average negative log likelihood on the training set is about 2.45 ([[youtube-2022-09-07-makemore-1-bigram]] @1:00:02). He stared at the samples for a few minutes to convince himself they were right; they are bad because the model does not know whether an H is the first letter or has a history ([[youtube-2022-09-07-makemore-1-bigram]] @33:46, @34:17, @34:52).

Recast as a neural net, a single linear layer of 27 neurons on 27 one-hot inputs (`xenc @ W`, no bias, no nonlinearity) is the whole network ([[youtube-2022-09-07-makemore-1-bigram]] @1:16:08, @1:18:26, @1:19:01). Trained on all 228,000 bigrams it reaches about 2.46, the same vicinity as counting ([[youtube-2022-09-07-makemore-1-bigram]] @1:43:27, @1:44:36, @1:45:08).

In the next lecture he gives the bigram model's limit: it looks at only one previous character and its predictions were not very name-like, and extending the count table to more context grows it exponentially (27 rows for one character, 729 for two, about 20,000 for three) while the counts per row collapse ([[youtube-2022-09-12-makemore-2-mlp]] @00:33, @01:06, @01:40).

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
