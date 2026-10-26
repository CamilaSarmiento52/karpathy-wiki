# Digest: The spelled-out intro to neural networks and backpropagation: building micrograd
- raw: raw/youtube/VMj-3S1tku0.md · published: 2022-08-16 · medium: youtube · words: 24644
- source slug: youtube-2022-08-16-micrograd

## Source page

```
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
- A derivative is the sensitivity of the output to a small nudge of an input, estimated numerically as rise over run; nobody derives the symbolic derivative of a neural net (@10:52, @11:59, @09:45) → [[derivatives]]
- A `Value` wraps a scalar and keeps `_prev` (children) and `_op`, so the full expression graph is available for the forward and backward pass (@22:29, @24:08) → [[expression-graphs]]
- Backpropagation is a recursive application of the chain rule backwards through the graph: each node multiplies its local derivative onto the gradient flowing in from the output (@41:14, @50:37) → [[backpropagation]], [[chain-rule]]
- A plus node routes the gradient unchanged to its children; a times node scales it by the other operand; tanh's local derivative is 1 - tanh^2 (@45:05, @47:50, @1:03:23) → [[backpropagation]], [[activation-functions]]
- Any operation, atomic or composite, can be a node as long as you can write its local derivative; the granularity is up to you (@58:24, @1:38:22) → [[operation-granularity-in-autograd-is-up-to-you]]
- Gradients must be accumulated with `+=` because a variable used more than once receives contributions from several paths (@1:24:33, @1:25:05) → [[backpropagation]]
- A neuron is tanh(sum of w_i x_i + b); a layer is independent neurons; an MLP is layers in sequence, with `parameters()` gathering all weights and biases as in PyTorch's nn.Module (@53:23, @1:48:20, @1:49:24, @1:58:14) → [[multi-layer-perceptron]], [[activation-functions]]
- The loss is a single number measuring performance; mean squared error is zero only when prediction equals target (@1:52:10, @1:53:49) → [[loss-functions]]
- Gradient descent: forward, backward, nudge each parameter by a small step against the gradient, repeat; the learning rate is a subtle art and too large a step can blow up the loss (@2:02:10, @2:03:19, @2:06:35, @2:07:43) → [[gradient-descent]], [[learning-rate-tuning-is-a-subtle-art]]
- Forgetting to zero the gradients before `backward` is a common, subtle bug he made on camera; the simple problem still trained because accumulated grads acted as a huge step size (@2:10:28, @2:11:01, @2:12:42) → [[forgetting-to-zero-grad-is-a-common-neural-net-bug]], [[a-buggy-neural-net-can-still-train-on-a-simple-problem]]
- He builds live from a blank notebook, derives everything by hand first, picks inputs so the numbers come out nice, and leaves his own errors in (@00:00, @1:01:09, @1:15:05) → [[spelled-out-build-from-scratch]]
- Every manually derived gradient is checked by bumping the input by h and reading the change in the output (@37:50, @46:45, @50:03) → [[inline-gradient-check]]
- The same expression is run in PyTorch to confirm forward and gradients agree, and micrograd's API is deliberately modelled on PyTorch (@1:39:28, @1:42:48, @1:44:26, @2:18:12) → [[verify-against-pytorch]], [[pytorch]]
- Production libraries like PyTorch are meant to be used, not inspected: it took him 15 minutes to find the tanh backward kernel (@2:21:33, @2:22:07) → [[production-libraries-are-meant-to-be-used-not-inspected]]

## Fed pages
- [[backpropagation]]
- [[chain-rule]]
- [[derivatives]]
- [[expression-graphs]]
- [[multi-layer-perceptron]]
- [[activation-functions]]
- [[loss-functions]]
- [[gradient-descent]]
- [[pytorch]]
- [[micrograd]]
- [[spelled-out-build-from-scratch]]
- [[inline-gradient-check]]
- [[verify-against-pytorch]]
- [[neural-networks-are-just-mathematical-expressions]]
- [[backpropagation-is-more-general-than-neural-networks]]
- [[micrograd-is-all-you-need-everything-else-is-efficiency]]
- [[operation-granularity-in-autograd-is-up-to-you]]
- [[learning-rate-tuning-is-a-subtle-art]]
- [[forgetting-to-zero-grad-is-a-common-neural-net-bug]]
- [[a-buggy-neural-net-can-still-train-on-a-simple-problem]]
- [[production-libraries-are-meant-to-be-used-not-inspected]]
```

## Candidates

### topic: backpropagation
- existing: no
- aliases: backprop, back propagation, backward pass, autograd, automatic gradient
- statements:
  - Backpropagation is an algorithm that efficiently evaluates the gradient of a loss function with respect to the weights of a neural network, so the weights can be tuned iteratively to minimise the loss (@00:32, @01:05).
  - It sits at the mathematical core of any modern deep-learning library such as PyTorch or JAX (@01:05).
  - Calling `backward` on the output node starts at that node and goes backwards through the expression graph, recursively applying the chain rule to get the derivative of the output with respect to every internal node and input (@03:14).
  - In the neural-net setting one wants the derivative of the loss with respect to the weights; derivatives with respect to the data are usually not used because the data is fixed (@30:07, @30:39).
  - Each `Value` carries a `grad`, initialised to zero, meaning "no effect" on the output (@30:39, @31:12).
  - The base case is that the derivative of the output with respect to itself is one (@32:18, @1:02:15).
  - Each node knows only its local derivative; the chain rule multiplies that local derivative onto the gradient of the output with respect to the node's output (@40:39, @44:33, @50:37).
  - A plus node routes the gradient unchanged to both children because its local derivatives are one (@45:05, @45:37, @1:04:28).
  - A times node gives each input the other input's value times the incoming gradient (@48:24, @1:06:42).
  - Backpropagation is implemented by storing a `_backward` closure on each node that applies its piece of the chain rule; leaf nodes get an empty function (@1:09:34, @1:10:08).
  - Nodes must be processed so that everything after a node is done before it; this ordering is a topological sort of the DAG, and `backward` calls each node's `_backward` in reverse topological order (@1:17:50, @1:18:24, @1:20:41).
  - Gradients must be accumulated with `+=` rather than set, because a variable used more than once receives contributions from several paths; this follows from the multivariate chain rule (@1:22:57, @1:24:33, @1:25:05).
  - He describes the gradient signal as flowing backwards through the graph (@46:11).

### topic: chain-rule
- existing: no
- aliases: chain rule of calculus
- statements:
  - If z depends on y which depends on x, then dz/dx = dz/dy times dy/dx; differentiating through a composition means multiplying the derivatives (@41:47, @42:20).
  - He prefers this formulation to the one he was taught, which he found confusing (@41:47).
  - He uses the Wikipedia intuition: if a car is twice as fast as a bicycle and the bicycle four times as fast as a walker, the car is eight times as fast as the walker (@42:53, @43:27).
  - Backpropagation is just recursive application of the chain rule backwards through the computation graph (@50:37).

### topic: derivatives
- existing: no
- aliases: derivative, slope, numerical gradient, numerical derivative
- statements:
  - He does not take the symbolic approach because nobody writes out the derivative of a neural net, which would have tens of thousands of terms (@09:45, @10:18).
  - The derivative is the limit as h goes to zero of (f(x+h) - f(x))/h: how the function responds, and with what sensitivity, when the input is nudged slightly (@10:52).
  - He estimates it numerically with a small h such as 0.001, as rise over run; too small an h gives wrong answers because of finite floating-point precision (@11:26, @12:35).
  - He checks the numerical slope of 3x^2 - 4x + 5 at x=3 (14), at x=-3 (negative) and near 2/3 (zero) against the analytic derivative (@12:35, @13:10, @13:43).
  - For d = a*b + c, dd/da is b, dd/db is a and dd/dc is 1, and he reasons about the sign intuitively before computing (@17:03, @17:35, @18:08, @18:39).
  - The gradient tells you how to nudge inputs to make the output go up; nudging leaves in the direction of the gradient raised l from -8 to -7, one step of optimisation (@51:10, @52:18).

### topic: expression-graphs
- existing: no
- aliases: expression graph, computational graph, computation graph, DAG, Value object
- statements:
  - micrograd lets you build mathematical expressions out of `Value` objects that wrap numbers and support add, multiply, power, negate, divide and so on; it builds the whole expression graph in the background (@01:37, @02:11).
  - The forward pass reads `.data` at the output; `backward` on the output fills `.grad` on every node (@02:42, @03:14).
  - Because neural nets are massive expressions, a data structure is needed to maintain them; that is the purpose of `Value` (@19:11).
  - `Value` implements `__add__` and `__mul__` via Python's dunder methods, returning new `Value`s (@20:17, @21:24).
  - Each `Value` keeps `_prev` (the set of children that produced it) and `_op` (the operation string), so every node knows how it came to be (@22:29, @23:02, @24:08).
  - He visualises graphs with graphviz through a `draw_dot` helper, adding fake op nodes so the picture reads nicely (@25:13, @25:46, @26:18).
  - A trained MLP over four examples plus the loss is a very large graph, and backprop still works through all of it (@1:50:32, @1:56:36).

### topic: multi-layer-perceptron
- existing: no
- aliases: MLP, neuron, layer, neural network, artificial neuron
- statements:
  - An MLP is a two-layer-or-more net of hidden layers whose neurons are fully connected to the previous layer (@52:50, @1:47:47).
  - A neuron multiplies each input by a synaptic weight, sums them, adds a bias he calls the neuron's "trigger happiness", and passes the result through a squashing activation such as sigmoid or tanh (@53:23, @53:54, @55:02).
  - He backpropagates by hand through a two-input tanh neuron, finding w2's gradient is zero because x2 is zero (@55:34, @1:07:18, @1:08:27).
  - `Neuron` initialises weights uniformly in [-1, 1] and a bias, and `__call__` returns tanh of the dot product plus bias, written with `zip` and `sum(..., start=self.b)` (@1:44:58, @1:46:41, @1:47:13).
  - A layer is a list of independent neurons evaluated independently; an MLP is a list of layers applied sequentially, built from a list of layer sizes (@1:48:20, @1:49:24).
  - The example net has 3 inputs, two hidden layers of 4 and one output, 41 parameters in total (@1:49:24, @2:01:02).
  - `parameters()` on neuron, layer and MLP collects all weights and biases, matching PyTorch's nn.Module API (@1:58:14, @1:59:22, @2:18:12).
  - Gradients also exist on the input data but are not useful because the data is fixed (@1:57:07, @1:57:40).
  - He says networks with hundreds of billions of parameters, such as GPT predicting the next word, train on the same principles with a different update and a cross-entropy loss (@2:15:28, @2:16:00, @2:16:34).

### topic: activation-functions
- existing: no
- aliases: non-linearity, nonlinearity, tanh, relu, sigmoid, squashing function
- statements:
  - The activation is usually a squashing function such as sigmoid or tanh; tanh maps zero to zero and caps smoothly at 1 and -1 (@53:54, @54:28, @55:02).
  - tanh cannot be built from plus and times alone because it needs exponentiation, so he implements it as a single composite op whose local derivative is 1 - tanh^2 (@57:16, @1:03:23, @1:03:56).
  - Later he breaks tanh into exp, addition, subtraction and division and gets identical forward and backward results (@1:27:18, @1:37:47, @1:38:22).
  - micrograd as of recording ships relu, not tanh; he says relu, tanh and sigmoid are all roughly equivalent for MLPs and chose tanh in the video because it is smoother and stresses the local-gradient work more (@2:17:07, @2:17:40).

### topic: loss-functions
- existing: no
- aliases: loss, mean squared error, MSE, cross-entropy
- statements:
  - The trick in deep learning is to compute a single number, the loss, that measures total performance, and then minimise it (@1:52:10).
  - Mean squared error subtracts prediction from target and squares, so the loss is zero exactly when prediction equals target and grows the further off you are; absolute value would also discard the sign (@1:52:43, @1:53:49, @1:54:22).
  - Calling `backward` on the loss gives every parameter a gradient saying how it influences the loss (@1:54:56, @1:55:28).
  - The loss is arranged so that when it is low the network does what you want (@2:14:22, @2:14:54).
  - Mentioned, not explained: the demo uses a max-margin loss, binary cross-entropy is another option, and GPT-style models use cross-entropy (@2:16:00, @2:19:51).

### topic: gradient-descent
- existing: no
- aliases: training loop, SGD, stochastic gradient descent, learning rate, step size
- statements:
  - The gradient is a vector pointing in the direction of increasing loss, so parameters are nudged by a small step size times the negative gradient (@2:02:10, @2:03:19).
  - He first writes the update without the minus sign, reasons through a specific neuron, and adds the negative (@2:02:44, @2:03:19).
  - Training is forward pass, backward pass, update, repeated; the loss fell 4.84 to 4.36 to 3.9 and so on (@2:04:57, @2:05:30, @2:06:02).
  - Too large a step overshoots because only the local dependence of the loss is known; his loss briefly exploded before landing at 7e-9 (@2:06:35, @2:07:11, @2:07:43).
  - The learning rate must be neither too low (slow) nor too high (unstable); 0.01 was too small and 0.1 dangerously high, so he picked in between for 20 steps (@2:07:43, @2:09:21).
  - A proper training loop zeros the gradients before `backward`, then updates (@2:11:35, @2:12:09).
  - Mentioned, not explained: batching on large datasets, L2 regularisation, learning-rate decay in the demo notebook (@2:19:18, @2:19:51, @2:20:23).

### topic: pytorch
- existing: no
- aliases: PyTorch, torch
- statements:
  - micrograd is roughly modelled on PyTorch, which is what you would use in production (@1:39:28).
  - In PyTorch everything is a tensor (n-dimensional array of scalars); he makes single-element tensors, casts to double to match Python's float64, and sets `requires_grad=True` because leaf tensors default to no gradient for efficiency (@1:40:01, @1:41:08, @1:41:43).
  - Tensors have `.data`, `.grad` and `.backward()` like micrograd; `.item()` strips the single element out (@1:42:15, @1:43:20).
  - micrograd's `Neuron`, `Layer`, `MLP`, `parameters()`, `Module` and `zero_grad` deliberately match the nn.Module API (@1:44:26, @1:58:14, @2:18:12).
  - He spent about 15 minutes and could not find tanh's backward in PyTorch's source (2,800 results in 406 files); it lives in a CPU kernel and a CUDA kernel inside binary-ops code (@2:21:33, @2:22:07, @2:22:40, @2:23:11).
  - New ops can be registered as a `torch.autograd.Function` subclass with a forward and a backward, becoming a Lego block in the larger library (@2:23:43, @2:24:15).

### artifact: micrograd
- existing: no
- aliases: micrograd, micrograd autograd engine
- repo_url: https://github.com/karpathy/micrograd · language: Python · status: active (he says he intends to keep developing it, @2:16:34)
- statements:
  - micrograd is a scalar-valued autograd engine he released on GitHub about two years before the lecture, originally source-only (@00:00, @00:32, @05:24).
  - It has two files: `engine.py`, the ~100-line autograd engine, and `nn.py`, the neural-net library defining neuron, layer and MLP; roughly 150 lines in total (@07:03, @07:35).
  - It works on individual scalars for pedagogical reasons; you would never do this in production (@05:24, @05:56).
  - As of recording, `engine.py` has data, grad, `_backward`, `_prev`, `_op`, add, mul, pow and relu (not tanh, which he intends to add); `nn.py` has a `Module` parent class with `zero_grad`, mirroring PyTorch (@2:17:07, @2:18:12).
  - The repo includes a test comparing forward and backward against PyTorch, and `demo.ipynb`, a larger 2-D binary classifier with batching, max-margin loss, L2 regularisation and learning-rate decay (@2:18:45, @2:19:18, @2:19:51, @2:20:23).
  - In the lecture he uses `_prev` as a set built from a `_children` tuple, which he believes was for efficiency (@23:02).

### method: spelled-out-build-from-scratch
- existing: no
- aliases: build from a blank notebook, spelled-out lecture
- statements:
  - Start with a blank Jupyter notebook and build the whole thing step by step, commenting on every piece (@00:00, @00:32).
  - Work at the level of individual scalars so the math is visible, deferring tensors as pure efficiency (@05:24, @05:56, @06:30).
  - Build intuition first (what a derivative measures) before writing the data structure (@08:07, @10:18).
  - Do the backward pass fully by hand on a small expression and on a neuron, then codify what you saw into code (@31:45, @1:08:59).
  - Copy-paste the "slightly scary" plumbing (graphviz drawing) and explain it briefly rather than typing it live (@24:40, @25:13).
  - Choose inputs so intermediate numbers come out nice, e.g. a bias of 6.88 so tanh's local derivative is exactly 0.5 (@1:01:09, @1:03:56).
  - Pause-the-video exercises for the reader to derive a local gradient (@1:30:38, @1:33:56).
  - Leave your own errors in the recording when they are instructive, including a bug done "for the 20th time" (@1:15:05, @2:10:28).
  - Finish by walking the real repo and the production library to connect the toy to the real thing (@2:16:34, @2:20:56).
- Steps (ordered): start blank; build intuition numerically; wrap scalars in a graph node; backprop by hand; verify numerically; automate; compare to PyTorch; build the net; define a loss; train; show the real code.

### method: inline-gradient-check
- existing: no
- aliases: gradient check, numerical gradient check
- statements:
  - After deriving a gradient by hand, verify it by bumping the input by a small h in a scoped function and printing (l2 - l1)/h (@32:18, @32:51, @33:25).
  - He names this an inline gradient check: deriving backprop for the intermediates and estimating the derivative numerically with a small step (@37:50).
  - He applies it to every node in the manual example (d, f, c, e, a, b), accepting small float differences (@36:47, @37:18, @46:45, @50:03).
- Steps: fix inputs; compute output; bump one input by h; recompute; divide the change by h; compare to the hand-derived gradient.

### method: verify-against-pytorch
- existing: no
- aliases: compare to PyTorch, PyTorch parity check
- statements:
  - Reproduce the same expression in PyTorch and check that forward output (0.707) and all gradients (0.5, 0, -1.5, 1) agree (@1:39:28, @1:42:48).
  - Design the toy library to match PyTorch's API on both the autograd side and the nn.Module side (@1:44:26, @2:18:12).
  - The repo's test file does this systematically for simple and more complicated expressions (@2:18:45).
- Steps: build the expression in micrograd; rebuild it in PyTorch with double, single-element, requires_grad tensors; run forward and backward; compare values and grads.

### claim: neural-networks-are-just-mathematical-expressions
- existing: no
- title: Neural networks are just a class of mathematical expressions
- confidence: stated
- quote: "neural networks are just mathematical expressions just like this one" (@04:19)
- statements:
  - A neural net takes the data and the weights as inputs and outputs predictions or the loss; it is a certain class of mathematical expression, slightly less crazy than his made-up example (@04:19, @04:51).
  - He repeats it in the summary: an MLP is a fairly simple expression for the forward pass followed by a loss (@2:13:49, @2:14:22).
- relation: none existing.

### claim: backpropagation-is-more-general-than-neural-networks
- existing: no
- title: Backpropagation does not care about neural networks; it works on arbitrary expressions
- confidence: stated
- quote: "back propagation is actually significantly more general" (@04:51)
- statements:
  - Backprop only tells you about arbitrary mathematical expressions; neural nets happen to use that machinery (@04:51).
- relation: supports [[neural-networks-are-just-mathematical-expressions]] (same passage, same framing).

### claim: micrograd-is-all-you-need-everything-else-is-efficiency
- existing: no
- title: micrograd is all you need to train neural nets; everything else is efficiency
- confidence: stated
- quote: "micrograd is what you need to train your networks" (@06:30)
- statements:
  - Tensors package scalars into arrays to exploit parallelism; none of the math changes (@05:56, @06:30).
  - About 150 lines of code is all you need to understand neural-net training; there is a lot to efficiency, but that is all that is fundamentally happening (@07:35).
  - He says it is not pedagogically useful to deal with tensors from scratch (@06:30).
- relation: supports [[neural-networks-are-just-mathematical-expressions]].

### claim: operation-granularity-in-autograd-is-up-to-you
- existing: no
- title: The granularity of autograd operations is up to you, as long as you know each local derivative
- confidence: stated
- quote: "the level at which you implement your operations is totally up to you" (@1:38:22)
- statements:
  - You can implement backward for a single plus or for a composite like tanh; all that matters is a forward pass and a known local derivative (@58:24, @1:38:54).
  - He demonstrates it by implementing tanh atomically and then from exp, getting identical gradients (@1:37:47, @1:38:22).
  - PyTorch's `torch.autograd.Function` registration is the same idea (@2:23:43, @2:24:15).
- relation: none existing.

### claim: learning-rate-tuning-is-a-subtle-art
- existing: no
- title: Setting the learning rate in vanilla gradient descent is a subtle art
- confidence: stated
- quote: "this learning rate and the tuning of it is a subtle art" (@2:07:43)
- statements:
  - Too low converges far too slowly; too high destabilises training and can explode the loss, depending on the loss function (@2:06:35, @2:07:43).
- relation: none existing.

### claim: forgetting-to-zero-grad-is-a-common-neural-net-bug
- existing: no
- title: Forgetting to zero the gradients before backward is a common, subtle neural-net bug
- confidence: stated
- quote: "you forgot to zero grad before that backward" (@2:11:01)
- statements:
  - He made the bug on camera, says it is very common, and that it is number three on a list of most common neural-net mistakes he tweeted long ago (@2:10:28, @2:11:01).
  - Because every `_backward` does `+=`, grads accumulate across iterations unless reset; the fix is to set every parameter's grad to zero before `backward`, as PyTorch's `zero_grad` does (@2:11:35, @2:12:09).
- relation: supports [[a-buggy-neural-net-can-still-train-on-a-simple-problem]].

### claim: a-buggy-neural-net-can-still-train-on-a-simple-problem
- existing: no
- title: A buggy neural net can still appear to train when the problem is simple enough
- confidence: stated
- quote: "your network might actually work" (@2:13:16)
- statements:
  - The un-zeroed grads effectively gave a massive step size that happened to converge fast on this four-example problem; on a harder problem the bug would have prevented good optimisation (@2:12:42, @2:13:49).
- relation: supported by [[forgetting-to-zero-grad-is-a-common-neural-net-bug]].

### claim: production-libraries-are-meant-to-be-used-not-inspected
- existing: no
- title: Production libraries like PyTorch grow in size and entropy and are meant to be used, not inspected
- confidence: stated
- quote: "these libraries are quite complex they're meant to be used not really inspected" (@2:22:07)
- statements:
  - He searched PyTorch for tanh, got 2,800 results in 406 files, and spent 15 minutes before finding the backward kernel via a GitHub issue (@2:21:33, @2:22:07).
  - Finding the real code for what micrograd does in a few lines is difficult (@2:23:11).
- relation: supports [[micrograd-is-all-you-need-everything-else-is-efficiency]] (weakly; the simplicity contrast is his point).

## Quotes
- "autograd is short for automatic gradient" (@00:32)
- "neural networks are just mathematical expressions just like this one" (@04:19)
- "back propagation is actually significantly more general" (@04:51)
- "none of the math changes this is done purely for efficiency" (@06:30)
- "i don't think that it's pedagogically useful to be dealing with tensors from scratch" (@06:30)
- "micrograd is what you need to train your networks" (@06:30)
- "there's a lot of power that comes from only 150 lines of code" (@07:35)
- "no one in neural networks actually writes out the expression for the neural net" (@09:45)
- "a plus is just a distributor of gradient" (@1:04:28)
- "pluses are my favorite uh operations to back propagate through" (@1:05:37)
- "just a recursive application of chain rule backwards through the computation graph" (@50:37)
- "doing the back propagation manually is obviously ridiculous" (@1:08:59)
- "we have to accumulate these gradients these gradients add" (@1:25:05)
- "if you can write the local gradients you can chain the gradient" (@1:38:54)
- "the level at which you implement your operations is totally up to you" (@1:38:22)
- "pi torch agrees with us" (@1:42:48)
- "this learning rate and the tuning of it is a subtle art" (@2:07:43)
- "i can't believe i've done it for the 20th time in my life" (@2:10:28)
- "you forgot to zero grad before that backward" (@2:11:01)
- "your network might actually work" (@2:13:16)
- "we just have a blob of neural stuff" (@2:14:54)
- "these libraries are quite complex they're meant to be used not really inspected" (@2:22:07)

## Notes for merge
- Captions are auto-generated, lowercase and unpunctuated. Misspellings: "andre" (Andrej), "micrograph" / "microgrant" / "micrograb" / "microgradlend" / "microcraft" / "micro crab" (micrograd), "jupiter" (Jupyter), "10h" / "10 h" / "tanhd" (tanh), "pi torch" / "fighters" / "by torch" (PyTorch), "jaxx" (JAX), "graphless" / "graphis" (graphviz), "nn.pi" / "init.pi" / "engine.pi" (nn.py, __init__.py, engine.py), "demo.ipymb" (demo.ipynb), "r mold" / "our mole" / "armel" (`__rmul__`), "wrapper function" (`__repr__`), "pop" / "up" (`_op`), "pref" / "prep" (`_prev`), "sell dot backward" (`self._backward`), "storage.org that function" (`torch.autograd.Function`), "gender polynomial 3" (Legendre polynomial), "kuda" (CUDA), "white red" / "wipe red" / "why pred" (ypred), "multilateral perceptrons" (multilayer), "neural nuts" / "neurologic training" (neural nets / neural net training), "kapedia" (Wikipedia). The line "it happens to be 138" and "645" are grad values 138 and 645 as stated.
- Quotes with the misspelling "pi torch" are copied as-is per the verbatim rule; a merge should keep the misspelling inside the quotation marks.
- The transcript's last two blocks (@2:24:47 onward, "now here's the problem ... micro crab ... i know what happened there") are outtakes/bloopers appended after the sign-off, not content.
- Mentioned but not explained (do not make topics): JAX; relu/sigmoid equivalence (one sentence); batching; max-margin loss; binary cross-entropy; L2 regularisation; learning-rate decay; cross-entropy for next-token prediction; GPT as a next-word predictor with hundreds of billions of parameters; his old tweet of most common neural-net mistakes (he does not list the others); the discussion forum and possible follow-up video.
- The 150-lines figure is his rough count (@07:35); the "100 lines" for the engine is also approximate (@07:03). "About two years ago" for the micrograd release is relative to August 2022.
- "Status: active" for micrograd rests only on his stated intent to keep developing it (@2:16:34, @2:17:07); a later GitHub snapshot should decide the real status.
- Possible cross-links for merge (Note: sentences, not evidence): [[nanogpt]] and [[nanochat]] as later from-scratch training repos; the spelled-out method is the same teaching stance as the later "Zero to Hero" videos (not in the wiki yet). This video is the earliest source so far (2022); `first_seen` on every new topic will be 2022-08-16.
- He attributes the chain-rule phrasing and the car/bicycle intuition to Wikipedia (@41:47, @42:53); do not credit the analogy to him.
- The four-example training numbers (loss 7.12, 4.84, 4.36, 3.9, 3.66, 3.47, 0.31, 0.04, 7e-9) come from a re-initialised network partway through (@2:00:28), so values before and after that point are from different random inits.
