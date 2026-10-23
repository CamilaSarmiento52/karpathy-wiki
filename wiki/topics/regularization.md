---
type: topic
aliases: [Regularization, smoothing, label smoothing, weight decay, dropout]
first_seen: 2022-09-07
last_updated: 2022-09-12
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]"]
related: ["[[loss-functions]]", "[[bigram-language-model]]", "[[gradient-descent]]"]
---
# Regularization
Model smoothing adds fake counts (for example 1) to every entry of a count table before normalising so that no probability is zero; more added counts give a more uniform model, fewer a more peaked one ([[youtube-2022-09-07-makemore-1-bigram]] @1:01:43, @1:02:16).

## What he says
After smoothing, the unseen bigram JQ gets a very small but nonzero probability, and the loss is no longer infinite ([[youtube-2022-09-07-makemore-1-bigram]] @1:02:16, @1:02:49). Adding a huge count (he says a million) pushes every row toward the uniform distribution ([[youtube-2022-09-07-makemore-1-bigram]] @1:50:40).

In the gradient framework, W all zeros gives logits all zero, counts all one and probabilities exactly uniform, so pushing W toward zero is equivalent to smoothing ([[youtube-2022-09-07-makemore-1-bigram]] @1:51:13, @1:51:45). Regularization augments the loss with a term such as `(W**2).mean()` times a strength like 0.01; it is zero only when W is zero, acting like a spring or gravity force ([[youtube-2022-09-07-makemore-1-bigram]] @1:51:45, @1:52:19, @1:52:52, @1:53:26). The regularization strength controls the same thing as the number of added counts; strong enough and predictions become uniform ([[youtube-2022-09-07-makemore-1-bigram]] @1:53:26, @1:54:00). He calls the technique model smoothing early in the lecture and label smoothing when he returns to it ([[youtube-2022-09-07-makemore-1-bigram]] @1:01:43, @1:51:45).

In the second makemore lecture he lists regularisation strength among the hyperparameters tuned on the dev split, alongside hidden size and embedding size, without yet using it ([[youtube-2022-09-12-makemore-2-mlp]] @55:22).

## Claims
- [[weight-regularization-is-equivalent-to-count-smoothing]]

## Related
- [[loss-functions]] — the regularization term is added to the loss
- [[bigram-language-model]]
- [[gradient-descent]]
- [[overfitting-and-generalization]] — what regularisation is tuned against
