---
type: topic
aliases: [Overfitting, underfitting, train/dev/test split, validation loss, generalization]
first_seen: 2022-09-12
last_updated: 2022-10-04
sources: ["[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2022-10-04-makemore-3-activations-batchnorm]]"]
related: ["[[diagnose-under-or-overfitting]]", "[[regularization]]", "[[gradient-descent]]", "[[embeddings]]", "[[batch-normalization]]"]
---
# Overfitting and generalization
A lower training loss does not by itself prove a better model: as capacity grows, a model can memorise the training set verbatim, its samples repeat the training data, and the loss on held-out data can be very high ([[youtube-2022-09-12-makemore-2-mlp]] @53:10, @53:42, @54:15).

## What he says
The standard in the field is three splits, training, dev (or validation) and test, typically about 80/10/10 ([[youtube-2022-09-12-makemore-2-mlp]] @54:15, @54:49). The training split optimises parameters by gradient descent; the dev split is for development over hyperparameters such as hidden size, embedding size and regularisation strength ([[youtube-2022-09-12-makemore-2-mlp]] @54:49, @55:22). The test split evaluates the model at the end and is used very sparingly, because every time you learn from the test loss you start training on it ([[youtube-2022-09-12-makemore-2-mlp]] @55:22, @55:54). He shuffles the words and splits at 80% and 90%, giving about 25,000 training words and about 3,000 words each for dev and test ([[youtube-2022-09-12-makemore-2-mlp]] @56:26, @57:01, @57:33). Once hyperparameters are chosen by dev performance, the test set is evaluated a single time and that is the number you report ([[youtube-2022-09-12-makemore-2-mlp]] @1:10:30).

With 3,400 parameters and 32 examples the network overfits a single batch and reaches a very low loss ([[youtube-2022-09-12-makemore-2-mlp]] @39:23). The loss cannot reach exactly zero because the same context (dots) has several possible next characters in the data ([[youtube-2022-09-12-makemore-2-mlp]] @40:28, @41:03). He says calling the MLP better than the bigram model because 2.3 beats 2.45 is not exactly true ([[youtube-2022-09-12-makemore-2-mlp]] @53:10). Equal training and dev loss means the model is not overfitting but under-fitting: the network is too small and should be scaled up ([[youtube-2022-09-12-makemore-2-mlp]] @1:00:20). After scaling, training and validation loss start to slowly depart, which he reads as the start of overfitting ([[youtube-2022-09-12-makemore-2-mlp]] @1:09:55). Making the tanh layer bigger did not help much, so he suspected the 2D embeddings as the bottleneck instead ([[youtube-2022-09-12-makemore-2-mlp]] @1:03:52, @1:04:25).

In the third lecture he notes an accidental regulariser: batch normalization couples the examples in a batch, so each example's hidden states jitter depending on the others, which he says pads out the examples like a form of data augmentation and makes overfitting harder ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @50:57, @51:31, @52:04).

## Claims
- [[approximate-gradient-with-more-steps-beats-exact-gradient]] — the minibatch loss is noisy, so progress is read on the full set
- [[avoid-batch-normalization-where-possible]] — the regularising side effect is one reason the layer has been hard to remove

## Related
- [[batch-normalization]] — the accidental regulariser
- [[diagnose-under-or-overfitting]] — how he reads train against dev loss
- [[regularization]] — a hyperparameter tuned on dev
- [[gradient-descent]]
- [[embeddings]] — the bottleneck he found
- [[makemore]]
