---
type: topic
aliases: [Loss functions, cross-entropy, negative log likelihood, NLL, mean squared error]
first_seen: 2022-08-16
last_updated: 2024-05-28
sources: ["[[youtube-2022-08-16-micrograd]]", "[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2022-10-04-makemore-3-activations-batchnorm]]", "[[youtube-2022-10-11-makemore-4-backprop-ninja]]", "[[github-2024-05-28-llmc-gpt-2-124m]]"]
related: ["[[gradient-descent]]", "[[backpropagation]]", "[[micrograd]]", "[[training-diagnostics]]"]
---
# Loss functions
The trick in deep learning, as he puts it, is to compute a single number, the loss, that measures total performance, and then minimise it ([[youtube-2022-08-16-micrograd]] @1:52:10).

## What he says
Mean squared error subtracts prediction from target and squares, so the loss is zero exactly when prediction equals target and grows the further off you are; absolute value would also discard the sign ([[youtube-2022-08-16-micrograd]] @1:52:43, @1:53:49, @1:54:22). Calling `backward` on the loss gives every parameter a gradient saying how it influences the loss ([[youtube-2022-08-16-micrograd]] @1:54:56, @1:55:28). The loss is arranged so that when it is low the network does what you want ([[youtube-2022-08-16-micrograd]] @2:14:22, @2:14:54). He mentions, without explaining, that micrograd's demo uses a max-margin loss, that binary cross-entropy is another option, and that GPT-style models use cross-entropy ([[youtube-2022-08-16-micrograd]] @2:16:00, @2:19:51).

In the first makemore lecture he wants to summarise model quality into a single number, the training loss, as in micrograd ([[youtube-2022-09-07-makemore-1-bigram]] @50:47). With 27 characters a uniform model gives about 4% per bigram, so probabilities above 4% mean the statistics learned something ([[youtube-2022-09-07-makemore-1-bigram]] @52:21). In the maximum-likelihood literature the measure is the likelihood, the product of the probabilities the model assigns to the data; a good model makes it high ([[youtube-2022-09-07-makemore-1-bigram]] @52:54, @53:27). The product is tiny, so people work with the log likelihood: log is monotonic, log(1) is 0, it goes to negative infinity at 0, and the log of a product is a sum of logs ([[youtube-2022-09-07-makemore-1-bigram]] @53:27, @54:00, @55:03). A loss should be low-is-good, so he negates it: negative log likelihood, whose minimum is 0 ([[youtube-2022-09-07-makemore-1-bigram]] @56:44, @57:20). People usually average rather than sum; the training-set loss of the counting bigram model is about 2.45 ([[youtube-2022-09-07-makemore-1-bigram]] @57:20, @57:52, @1:00:02). Maximising likelihood, maximising log likelihood and minimising average negative log likelihood are equivalent optimisation problems ([[youtube-2022-09-07-makemore-1-bigram]] @58:24, @58:57, @59:29). A bigram never seen in training has probability 0, log 0 is minus infinity, so the loss is infinite ([[youtube-2022-09-07-makemore-1-bigram]] @1:00:35, @1:01:09).

For the neural net the loss is again the average negative log likelihood, because this is classification rather than regression; it is computed by indexing `probs[torch.arange(5), ys]`, taking the log, the mean and negating, and matches the hand-computed 3.76 ([[youtube-2022-09-07-makemore-1-bigram]] @1:35:40, @1:37:22, @1:37:56). The same single number lets him compare settings of W and later confirm that the net matches counting ([[youtube-2022-09-07-makemore-1-bigram]] @1:31:47, @1:44:36).

In the second makemore lecture the hand-rolled loss exponentiates logits to fake counts, normalises to probabilities, plucks the correct-class probability and takes the mean negative log ([[youtube-2022-09-12-makemore-2-mlp]] @29:55, @31:03, @31:36). `F.cross_entropy` computes exactly the same loss ([[youtube-2022-09-12-makemore-2-mlp]] @32:44, @33:16). He gives three reasons to prefer it: PyTorch avoids the intermediate tensors and uses fused kernels; the backward pass is simpler analytically, as with tanh in micrograd; and it is numerically stable, since exp of a large positive logit overflows to inf and gives nan while very negative logits are fine ([[youtube-2022-09-12-makemore-2-mlp]] @33:16, @33:49, @34:23, @35:30, @36:02). Logits can be offset by any constant without changing the probabilities, so PyTorch subtracts the maximum logit internally ([[youtube-2022-09-12-makemore-2-mlp]] @36:35, @37:08). `F.softmax` is likewise careful about overflow when sampling ([[youtube-2022-09-12-makemore-2-mlp]] @1:13:50).

The loss also serves as a sanity check before training: he says you almost always have a rough idea of the loss to expect at initialisation from the loss function and the problem setup, and with 27 equally likely characters that is -log(1/27), about 3.29, whereas his network recorded 27 because its logits were extreme and confidently wrong ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @04:28, @05:03, @05:38).

In the backprop lecture he derives the gradient of cross-entropy with respect to the logits: the softmax probabilities with 1 subtracted at the correct label, divided by n for the mean, which is why PyTorch can glue the whole loss into one faster `F.cross_entropy` ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:27:11, @1:30:32, @1:31:36). Each row of that gradient sums to zero; he reads it as a force that pulls the correct probability up and the incorrect ones down in proportion to how wrong the prediction was, and calls that the magic of the cross-entropy loss ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:33:50, @1:35:31, @1:36:04).

**Loss as perplexity (llm.c, 2024-05-28).** Reading a training log, he turns the loss into a count: the perplexity exp(loss) is how many tokens the model is effectively guessing uniformly among, about 2,000 at a loss of 7.577 and about 27 at 3.29, out of a vocabulary of 50,257 ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (Training)).

## Claims
- [[use-cross-entropy-not-a-hand-rolled-loss]]
- [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers]]
- [[weight-regularization-is-equivalent-to-count-smoothing]]
- [[the-hockey-stick-loss-means-training-is-wasting-steps]]

## Related
- [[training-diagnostics]] — the expected loss at initialisation and the plots beyond the single number
- [[weight-initialization]]
- [[gradient-descent]] — minimising the loss
- [[backpropagation]]
- [[micrograd]]
- [[softmax]], [[regularization]], [[bigram-language-model]]
- [[llm-evaluation]] — validation loss beside a benchmark
