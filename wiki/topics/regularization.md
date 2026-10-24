---
type: topic
aliases: [Regularization, smoothing, label smoothing, weight decay, dropout]
first_seen: 2022-09-07
last_updated: 2024-05-29
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2023-01-17-gpt-from-scratch]]", "[[github-2024-05-29-llama2c-readme]]"]
related: ["[[loss-functions]]", "[[bigram-language-model]]", "[[gradient-descent]]"]
---
# Regularization
Model smoothing adds fake counts (for example 1) to every entry of a count table before normalising so that no probability is zero; more added counts give a more uniform model, fewer a more peaked one ([[youtube-2022-09-07-makemore-1-bigram]] @1:01:43, @1:02:16).

## What he says
After smoothing, the unseen bigram JQ gets a very small but nonzero probability, and the loss is no longer infinite ([[youtube-2022-09-07-makemore-1-bigram]] @1:02:16, @1:02:49). Adding a huge count (he says a million) pushes every row toward the uniform distribution ([[youtube-2022-09-07-makemore-1-bigram]] @1:50:40).

In the gradient framework, W all zeros gives logits all zero, counts all one and probabilities exactly uniform, so pushing W toward zero is equivalent to smoothing ([[youtube-2022-09-07-makemore-1-bigram]] @1:51:13, @1:51:45). Regularization augments the loss with a term such as `(W**2).mean()` times a strength like 0.01; it is zero only when W is zero, acting like a spring or gravity force ([[youtube-2022-09-07-makemore-1-bigram]] @1:51:45, @1:52:19, @1:52:52, @1:53:26). The regularization strength controls the same thing as the number of added counts; strong enough and predictions become uniform ([[youtube-2022-09-07-makemore-1-bigram]] @1:53:26, @1:54:00). He calls the technique model smoothing early in the lecture and label smoothing when he returns to it ([[youtube-2022-09-07-makemore-1-bigram]] @1:01:43, @1:51:45).

In the second makemore lecture he lists regularisation strength among the hyperparameters tuned on the dev split, alongside hidden size and embedding size, without yet using it ([[youtube-2022-09-12-makemore-2-mlp]] @55:22).

In the GPT lecture he adds dropout, from a 2014 paper: every forward-backward pass shuts off a random subset of neurons, effectively training an ensemble of sub-networks merged at test time ([[youtube-2023-01-17-gpt-from-scratch]] @1:38:40, @1:39:13). He places it right before the connection back into the residual pathway, at the end of multi-head attention, and on the affinities after softmax to randomly prevent some nodes from communicating ([[youtube-2023-01-17-gpt-from-scratch]] @1:38:07). He treats it as a regularisation technique added because he was about to scale the model and was concerned about overfitting; the scaled model uses dropout 0.2 ([[youtube-2023-01-17-gpt-from-scratch]] @1:39:13, @1:39:46).

In his llama2.c 110M run he used dropout 0.1, saying it usually helps a bit at medium size ([[github-2024-05-29-llama2c-readme]] §training).

## Claims
- [[weight-regularization-is-equivalent-to-count-smoothing]]

## Related
- [[loss-functions]] — the regularization term is added to the loss
- [[bigram-language-model]]
- [[gradient-descent]]
- [[overfitting-and-generalization]] — what regularisation is tuned against
- [[transformer-architecture]] — where dropout sits in the block
