---
type: topic
aliases: [Gradient descent, learning rate, minibatch, SGD, optimization]
first_seen: 2022-08-16
last_updated: 2022-10-04
sources: ["[[youtube-2022-08-16-micrograd]]", "[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2022-10-04-makemore-3-activations-batchnorm]]"]
related: ["[[loss-functions]]", "[[backpropagation]]", "[[micrograd]]", "[[training-diagnostics]]"]
---
# Gradient descent
The gradient is a vector pointing in the direction of increasing loss, so parameters are nudged by a small step size times the negative gradient ([[youtube-2022-08-16-micrograd]] @2:02:10, @2:03:19).

## What he says
He first writes the update without the minus sign, reasons through a specific neuron, and adds the negative ([[youtube-2022-08-16-micrograd]] @2:02:44, @2:03:19). Training is forward pass, backward pass, update, repeated; his loss fell from 4.84 to 4.36 to 3.9 and so on ([[youtube-2022-08-16-micrograd]] @2:04:57, @2:05:30, @2:06:02). Too large a step overshoots because only the local dependence of the loss is known; his loss briefly exploded before landing at 7e-9 ([[youtube-2022-08-16-micrograd]] @2:06:35, @2:07:11, @2:07:43).

He calls the learning rate and its tuning "a subtle art": too low converges far too slowly, too high destabilises training and can explode the loss, depending on the loss function ([[youtube-2022-08-16-micrograd]] @2:06:35, @2:07:43). In the lecture 0.01 was too small and 0.1 dangerously high, so he picked in between for 20 steps ([[youtube-2022-08-16-micrograd]] @2:07:43, @2:09:21). A proper training loop zeros the gradients before `backward`, then updates ([[youtube-2022-08-16-micrograd]] @2:11:35, @2:12:09). He mentions, without explaining, batching on large datasets, L2 regularisation and learning-rate decay in micrograd's demo notebook ([[youtube-2022-08-16-micrograd]] @2:19:18, @2:19:51, @2:20:23).

In the bigram net, matrix multiplication evaluates all neurons on all examples in parallel; element (3, 13) is the dot product of input 3 with column 13 of W ([[youtube-2022-09-07-makemore-1-bigram]] @1:15:34, @1:17:16, @1:17:50). Reseeding W and checking the loss is guess and check, which he calls amateur hour and "not how you optimize a neural net"; instead, commit to a random start and minimise the differentiable loss with gradients ([[youtube-2022-09-07-makemore-1-bigram]] @1:31:15, @1:31:47, @1:32:20, @1:32:54). The loop mirrors micrograd: forward pass, loss, zero the gradients, `loss.backward()`, nudge parameters against the gradient ([[youtube-2022-09-07-makemore-1-bigram]] @1:33:26, @1:34:33, @1:35:05). Setting `.grad` to None is a more efficient way to zero it, and W needs `requires_grad=True` ([[youtube-2022-09-07-makemore-1-bigram]] @1:38:29, @1:39:03). A positive gradient means increasing that weight increases the loss ([[youtube-2022-09-07-makemore-1-bigram]] @1:40:09, @1:40:43). The update is `W.data += -0.1 * W.grad`, and the loss falls 3.76, 3.74, 3.72 ([[youtube-2022-09-07-makemore-1-bigram]] @1:41:15, @1:42:21). Scaling from 5 to 228,000 bigrams needs no code change, and a much larger learning rate (even 50) works on this simple problem, reaching about 2.47 ([[youtube-2022-09-07-makemore-1-bigram]] @1:43:27, @1:44:00, @1:44:36).

Minibatches arrive in the second makemore lecture: forwarding and backwarding all 228,000 examples each step is too slow, so in practice people update on a randomly selected minibatch, and he uses `torch.randint` to pick 32 indices into X and Y ([[youtube-2022-09-12-makemore-2-mlp]] @41:35, @42:07, @42:42, @43:16). With minibatches the gradient quality is lower and the direction less reliable, but good enough on 32 examples to be useful; he says it is much better to have an approximate gradient and take more steps than an exact gradient with fewer ([[youtube-2022-09-12-makemore-2-mlp]] @43:50, @44:24). The minibatch loss is noisy, so he evaluates on the full training set to judge progress ([[youtube-2022-09-12-makemore-2-mlp]] @44:24, @44:56). The loss curve is thick because of minibatch noise; a larger batch size would give a more correct gradient and less thrashing, and plotting log10 of the loss squashes the hockey-stick shape ([[youtube-2022-09-12-makemore-2-mlp]] @1:01:57, @1:02:30, @1:08:14).

On the learning rate, his initial 0.1 was a guess, and he cannot tell from the loss alone whether steps are too slow or too fast ([[youtube-2022-09-12-makemore-2-mlp]] @44:56, @45:28). A rate of 1 minimises the loss but is unstable and 10 does not optimise at all, so the right value is between 0.001 and 1; stepping linearly between rates does not make sense, so he steps linearly in the exponent ([[youtube-2022-09-12-makemore-2-mlp]] @46:34, @47:07, @47:42). The loss-versus-exponent plot shows nothing happening at low rates, a valley, then instability; around exponent -1, that is 0.1, is a good setting ([[youtube-2022-09-12-makemore-2-mlp]] @49:52, @50:25, @50:59). Learning-rate decay means lowering the rate by 10x in the late stages of training once the loss plateaus ([[youtube-2022-09-12-makemore-2-mlp]] @51:32, @52:04). His rough recipe is to find a decent rate, train a while, then decay by a factor of 10 and take a few more steps, which he calls janky and not production practice ([[youtube-2022-09-12-makemore-2-mlp]] @52:37). He admits his decay is done at random and the optimisation is suspect; in production you would turn these into hyperparameters and run many experiments ([[youtube-2022-09-12-makemore-2-mlp]] @1:09:20, @1:09:55). His final run uses 0.1 for 100,000 steps and then 0.01 for 100,000 ([[youtube-2022-09-12-makemore-2-mlp]] @1:11:38).

The third makemore lecture adds a way to judge the learning rate from the updates themselves. He tracks, per weight tensor, the update-to-data ratio, the standard deviation of learning rate times gradient divided by the standard deviation of the parameter, and plots its log10 over time ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:40:26, @1:41:00). He calls -3 on that scale, updates about a thousandth of the tensor's magnitude, a rough guide: well below it usually means parameters train too slowly, and with learning rate 0.001 the updates were 10,000× too small ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:42:06, @1:43:12, @1:43:45). Dead neurons can arise during training when a high learning rate knocks a neuron off the data manifold ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @21:58, @22:33). Changing the activation scale changes the update scale: with batch normalization and no fan-in scaling the ratio fell well below -3 and he raised the learning rate 10× to 1.0, and he admits he did not fully explain why a different gain needs a different learning rate ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:49:50, @1:50:24, @1:51:00, @1:54:48). He also mentions the earlier learning-rate finding mechanism and says the field has not settled the best update rule ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:53:45, @1:55:22).

## Claims
- [[approximate-gradient-with-more-steps-beats-exact-gradient]]
- [[counting-and-gradient-bigram-models-are-the-same-model]]
- [[gradient-based-models-scale-where-count-tables-do-not]]
- [[forgetting-to-zero-grad-is-a-common-neural-net-bug]]
- [[a-buggy-neural-net-can-still-train-on-a-simple-problem]]

## Related
- [[loss-functions]] — what is being minimised
- [[backpropagation]] — where the gradient comes from
- [[micrograd]]
- [[makemore]]
- [[learning-rate-sweep]] — how he picks the rate
- [[training-diagnostics]] — the update-to-data ratio plot that checks it
- [[batch-normalization]] — why the rate had to be retuned
- [[overfitting-and-generalization]]
