---
type: source
raw_path: raw/youtube/VMj-3S1tku0.md
published: 2022-08-16
medium: youtube
summary: A 2.5-hour lecture that builds micrograd from a blank notebook to show that neural-net training is backpropagation (recursive chain rule) over a scalar expression graph, then trains a tiny MLP with gradient descent.
url: https://www.youtube.com/watch?v=VMj-3S1tku0
title: "The spelled-out intro to neural networks and backpropagation: building micrograd"
---
# The spelled-out intro to neural networks and backpropagation: building micrograd
Raw: [[raw/youtube/VMj-3S1tku0]] · Original: https://www.youtube.com/watch?v=VMj-3S1tku0

## Summary
He starts from a blank Jupyter notebook and rebuilds micrograd, the scalar-valued autograd engine he had released on GitHub about two years earlier, commenting on every piece (@00:00, @00:32). He first builds intuition for a derivative as the numerical slope f(x+h)-f(x) over h, then wraps scalars in a `Value` object that records its children and the operation that produced it, forming an expression graph he visualises with graphviz (@10:52, @22:29, @25:13). Backpropagation is then done by hand on a small expression and on a single tanh neuron, each step checked numerically, before being automated with per-node `_backward` closures and a topological sort; along the way he hits and fixes the bug where gradients must be accumulated rather than overwritten (@33:57, @50:37, @1:17:50, @1:25:05). He shows the same computation in PyTorch, agreeing to the digit, then builds `Neuron`, `Layer` and `MLP` classes mirroring the PyTorch API, defines a mean-squared-error loss over four examples, and trains with gradient descent (@1:42:48, @1:44:26, @1:52:43, @2:05:30). He leaves in a bug he made on camera, forgetting to zero the gradients before `backward`, and explains why it still trained (@2:10:28, @2:12:42). He closes by walking the real micrograd repo, locating the tanh backward kernel deep inside PyTorch, and stating that networks of billions of parameters train on the same principles (@2:16:34, @2:21:33, @2:15:28).

## Key points
- Neural networks are just a class of mathematical expressions taking data and weights as inputs; backpropagation is more general and does not care about neural nets (@04:19, @04:51) → [[neural-networks-are-just-mathematical-expressions]], [[backpropagation-is-more-general-than-neural-networks]]
- micrograd is a ~100-line scalar autograd engine plus a ~50-line neural-net library; tensors change efficiency, not the math (@05:24, @07:03, @07:35) → [[micrograd]], [[micrograd-is-all-you-need-everything-else-is-efficiency]]
- A derivative is the sensitivity of the output to a small nudge of an input, estimated numerically as rise over run; nobody derives the symbolic derivative of a neural net (@10:52, @11:59, @09:45) → [[backpropagation]]
- A `Value` wraps a scalar and keeps `_prev` (children) and `_op`, so the full expression graph is available for the forward and backward pass (@22:29, @24:08) → [[backpropagation]]
- Backpropagation is a recursive application of the chain rule backwards through the graph: each node multiplies its local derivative onto the gradient flowing in from the output (@41:14, @50:37) → [[backpropagation]]
- A plus node routes the gradient unchanged to its children; a times node scales it by the other operand; tanh's local derivative is 1 - tanh^2 (@45:05, @47:50, @1:03:23) → [[backpropagation]], [[activation-functions]]
- Any operation, atomic or composite, can be a node as long as you can write its local derivative; the granularity is up to you (@58:24, @1:38:22) → [[micrograd-is-all-you-need-everything-else-is-efficiency]]
- Gradients must be accumulated with `+=` because a variable used more than once receives contributions from several paths (@1:24:33, @1:25:05) → [[backpropagation]]
- A neuron is tanh(sum of w_i x_i + b); a layer is independent neurons; an MLP is layers in sequence, with `parameters()` gathering all weights and biases as in PyTorch's nn.Module (@53:23, @1:48:20, @1:49:24, @1:58:14) → [[multilayer-perceptron]], [[activation-functions]]
- The loss is a single number measuring performance; mean squared error is zero only when prediction equals target (@1:52:10, @1:53:49) → [[loss-functions]]
- Gradient descent: forward, backward, nudge each parameter by a small step against the gradient, repeat; the learning rate is a subtle art and too large a step can blow up the loss (@2:02:10, @2:03:19, @2:06:35, @2:07:43) → [[gradient-descent]]
- Forgetting to zero the gradients before `backward` is a common, subtle bug he made on camera; the simple problem still trained because accumulated grads acted as a huge step size (@2:10:28, @2:11:01, @2:12:42) → [[forgetting-to-zero-grad-is-a-common-neural-net-bug]], [[a-buggy-neural-net-can-still-train-on-a-simple-problem]]
- He builds live from a blank notebook, derives everything by hand first, picks inputs so the numbers come out nice, and leaves his own errors in (@00:00, @1:01:09, @1:15:05) → [[spelled-out-build-from-scratch]]
- Every manually derived gradient is checked by bumping the input by h and reading the change in the output, and the same expression is run in PyTorch to confirm forward and gradients agree (@37:50, @46:45, @1:39:28, @1:42:48) → [[verify-gradients-against-pytorch]], [[pytorch]]
- Production libraries like PyTorch are meant to be used, not inspected: he spent about 15 minutes searching PyTorch for tanh's backward without finding it, and only reached the kernel through a pointer in a thread (@2:21:33, @2:22:07) → [[pytorch]], [[micrograd-is-all-you-need-everything-else-is-efficiency]]

## Fed pages
- [[backpropagation]]
- [[multilayer-perceptron]]
- [[activation-functions]]
- [[loss-functions]]
- [[gradient-descent]]
- [[pytorch]]
- [[micrograd]]
- [[spelled-out-build-from-scratch]]
- [[verify-gradients-against-pytorch]]
- [[neural-networks-are-just-mathematical-expressions]]
- [[backpropagation-is-more-general-than-neural-networks]]
- [[micrograd-is-all-you-need-everything-else-is-efficiency]]
- [[forgetting-to-zero-grad-is-a-common-neural-net-bug]]
- [[a-buggy-neural-net-can-still-train-on-a-simple-problem]]
- [[neural-net-training-should-not-be-complicated]]
