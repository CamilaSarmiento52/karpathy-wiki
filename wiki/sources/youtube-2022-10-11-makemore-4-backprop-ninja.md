---
type: source
raw_path: raw/youtube/q8SA3rM6ckI.md
published: 2022-10-11
medium: youtube
summary: "He removes loss.backward() from the makemore MLP and hand-derives every gradient at the tensor level, checking each against PyTorch, then collapses cross-entropy and batchnorm backward into closed-form expressions."
url: https://www.youtube.com/watch?v=q8SA3rM6ckI
title: "Building makemore Part 4: Becoming a Backprop Ninja"
---
# Building makemore Part 4: Becoming a Backprop Ninja
Raw: [[raw/youtube/q8SA3rM6ckI]] · Original: https://www.youtube.com/watch?v=q8SA3rM6ckI

## Summary
He pauses the makemore series for one lecture to replace PyTorch's `loss.backward()` with a backward pass written by hand at the level of tensors, because he regards backpropagation as a leaky abstraction that will fail or underperform if you do not understand its internals (@00:31, @01:05). He frames the exercise historically: ten years earlier everyone wrote their backward pass by hand, in MATLAB or numpy, and checked it with a gradient checker (@03:16, @06:41). Exercise one backpropagates through every atomic operation of the two-layer MLP with batchnorm, from log-probabilities back to the embedding table, checking each intermediate gradient against PyTorch with an exact/approximate/max-difference comparison (@07:46, @17:46, @1:26:06). Along the way he teaches the duality between a sum in the forward pass and a broadcast in the backward pass, and his trick of deriving matrix-multiply gradients by making the shapes work out rather than remembering formulas (@50:01, @1:09:12). Exercises two and three derive the gradient of cross-entropy (softmax minus one-hot, scaled by 1/n) and of the whole batchnorm layer analytically on paper (@1:30:32, @1:38:18), and exercise four trains the network with only the manual gradients, reaching the same loss as before (@1:50:31, @1:53:18). He also departs from the batchnorm paper by using the unbiased (n-1) variance and calls the paper's train/test variance mismatch, which PyTorch follows, a bug (@1:05:16, @1:05:49, @1:07:31, @1:08:05).

## Key points
- Backprop is a leaky abstraction: stacking differentiable blocks and calling backward does not guarantee things work, and you need the internals to debug; autograd is no reason to ignore how it works → [[understand-backprop-even-with-autograd]] (@01:05, @02:43)
- Writing a backward pass by hand is no longer recommended outside exercises, but around 2010–2014 it was standard, with numerical gradient checkers → [[backpropagation]] (@03:16, @06:41)
- micrograd covered only scalars, which he does not think is enough, so this lecture does it on tensors → [[micrograd]], [[backpropagation]] (@02:43)
- Small random (not zero) initialisation of biases is used so that zeros do not mask an incorrect gradient; the `cmp` utility reports exact equality, `allclose` and the maximum absolute difference → [[verify-gradients-against-pytorch]] (@08:20, @17:46, @18:19)
- A variable used in several places accumulates gradient by summing; broadcasting is replication plus the operation, so its backward pass is a sum over the replicated dimension; a forward sum becomes a backward replication → [[broadcasting]], [[backpropagation]] (@23:19, @25:34, @30:39, @31:11)
- The gradient on the max-subtraction used for softmax stability comes out at roughly 1e-9, reflecting that it does not affect the loss → [[backpropagation]] (@36:44, @37:17)
- The backward pass of a matrix multiply is a matrix multiply with the other operand transposed; the bias gradient is a sum over examples; the shapes admit only one valid arrangement → [[backpropagation]], [[verify-gradients-against-pytorch]] (@48:57, @49:29, @50:01, @50:37)
- He scrutinises the shapes first; a reduction in the forward shape signals a broadcast in the backward → [[check-shapes-and-broadcasting]], [[broadcasting]] (@1:08:38, @1:09:12, @1:09:47)
- The backward of tanh is 1 minus the output squared; `view` is re-viewed; the embedding lookup routes rows back with `+=` → [[activation-functions]], [[backpropagation]], [[pytorch]] (@54:03, @1:21:06, @1:23:52)
- The batchnorm paper uses biased 1/n variance in training and unbiased 1/(n-1) at inference; he treats this train/test mismatch as a bug and uses n-1 throughout → [[batchnorm-train-test-variance-mismatch-is-a-bug]], [[batch-normalization]], [[avoid-batch-normalization-where-possible]] (@1:05:49, @1:08:05)
- The gradient of cross-entropy with respect to the logits is the softmax probabilities with 1 subtracted at the correct label, divided by n; each row sums to zero and acts like a force → [[backpropagation]], [[loss-functions]] (@1:30:32, @1:31:36, @1:33:50)
- Batchnorm backward derived analytically on paper in the order x-hat, sigma-squared, mu, x; the final one line must broadcast across 64 neurons, which he calls highly non-trivial → [[backpropagation]], [[batch-normalization]] (@1:39:25, @1:43:17, @1:48:50)
- The MLP trains to the same loss with about 20 lines of manual backward code and no autograd → [[makemore]] (@1:51:04, @1:53:18)

## Fed pages
- [[backpropagation]]
- [[broadcasting]]
- [[batch-normalization]]
- [[loss-functions]]
- [[activation-functions]]
- [[pytorch]]
- [[understand-backprop-even-with-autograd]]
- [[batchnorm-train-test-variance-mismatch-is-a-bug]]
- [[avoid-batch-normalization-where-possible]]
- [[verify-gradients-against-pytorch]]
- [[check-shapes-and-broadcasting]]
- [[makemore]]
- [[micrograd]]
