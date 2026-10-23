---
type: topic
aliases: [Backpropagation, backprop, chain rule, autograd, expression graph]
first_seen: 2022-08-16
last_updated: 2022-09-07
sources: ["[[youtube-2022-08-16-micrograd]]", "[[youtube-2022-09-07-makemore-1-bigram]]"]
related: ["[[micrograd]]", "[[gradient-descent]]", "[[multilayer-perceptron]]", "[[pytorch]]"]
---
# Backpropagation
Backpropagation is an algorithm that efficiently evaluates the gradient of a loss function with respect to the weights of a neural network, so the weights can be tuned iteratively to minimise the loss ([[youtube-2022-08-16-micrograd]] @00:32, @01:05). He describes it as a recursive application of the chain rule backwards through an expression graph, starting at the output node and working back to every internal node and input ([[youtube-2022-08-16-micrograd]] @03:14, @50:37).

## What he says
He does not take the symbolic approach, because nobody writes out the derivative of a neural net, which would have tens of thousands of terms ([[youtube-2022-08-16-micrograd]] @09:45, @10:18). He defines the derivative as the limit of (f(x+h) - f(x))/h as h goes to zero: how the function responds, and with what sensitivity, when the input is nudged slightly ([[youtube-2022-08-16-micrograd]] @10:52). He estimates it numerically with a small h such as 0.001, as rise over run, noting that too small an h gives wrong answers because of finite floating-point precision ([[youtube-2022-08-16-micrograd]] @11:26, @12:35).

Because neural nets are massive expressions, a data structure is needed to maintain them; that is the purpose of micrograd's `Value` object ([[youtube-2022-08-16-micrograd]] @19:11). Each `Value` keeps `_prev`, the children that produced it, and `_op`, the operation, so every node knows how it came to be ([[youtube-2022-08-16-micrograd]] @22:29, @23:02, @24:08). The forward pass reads `.data` at the output; calling `backward` on the output fills `.grad` on every node ([[youtube-2022-08-16-micrograd]] @02:42, @03:14). He visualises graphs with graphviz through a `draw_dot` helper, adding fake op nodes so the picture reads nicely ([[youtube-2022-08-16-micrograd]] @25:13, @25:46, @26:18).

He states the chain rule as: if z depends on y and y depends on x, then dz/dx is dz/dy times dy/dx, and he prefers this formulation to the one he was taught, which he found confusing ([[youtube-2022-08-16-micrograd]] @41:47, @42:20). He borrows Wikipedia's intuition: if a car is twice as fast as a bicycle and the bicycle four times as fast as a walker, the car is eight times as fast as the walker ([[youtube-2022-08-16-micrograd]] @42:53, @43:27). Each node knows only its local derivative; the chain rule multiplies that local derivative onto the gradient of the output with respect to the node's output ([[youtube-2022-08-16-micrograd]] @40:39, @44:33, @50:37). A plus node routes the gradient unchanged to both children because its local derivatives are one, and he calls it "a plus is just a distributor of gradient"; a times node gives each input the other input's value times the incoming gradient ([[youtube-2022-08-16-micrograd]] @45:05, @1:04:28, @48:24, @1:06:42). He describes the gradient signal as flowing backwards through the graph ([[youtube-2022-08-16-micrograd]] @46:11).

Each `Value` carries a `grad` initialised to zero, meaning no effect on the output, and the base case is that the derivative of the output with respect to itself is one ([[youtube-2022-08-16-micrograd]] @30:39, @31:12, @32:18, @1:02:15). In the neural-net setting one wants the derivative of the loss with respect to the weights; derivatives with respect to the data are usually not used because the data is fixed ([[youtube-2022-08-16-micrograd]] @30:07, @30:39). Backpropagation is implemented by storing a `_backward` closure on each node that applies its piece of the chain rule; leaf nodes get an empty function ([[youtube-2022-08-16-micrograd]] @1:09:34, @1:10:08). Nodes must be processed so that everything after a node is done before it; this ordering is a topological sort of the DAG, and `backward` calls each node's `_backward` in reverse topological order ([[youtube-2022-08-16-micrograd]] @1:17:50, @1:18:24, @1:20:41). Gradients must be accumulated with `+=` rather than set, because a variable used more than once receives contributions from several paths; this follows from the multivariate chain rule ([[youtube-2022-08-16-micrograd]] @1:22:57, @1:24:33, @1:25:05).

The gradient tells you how to nudge inputs to make the output go up; nudging the leaves in the direction of the gradient raised the output from -8 to -7, which he presents as one step of optimisation ([[youtube-2022-08-16-micrograd]] @51:10, @52:18).

In PyTorch the computational graph is built during the forward pass, and `backward` fills in `W.grad` ([[youtube-2022-09-07-makemore-1-bigram]] @1:39:36, @1:40:09). Every step of the bigram net's forward pass (multiply, add, exp, sum, divide) is differentiable, so the whole thing can be backpropagated through ([[youtube-2022-09-07-makemore-1-bigram]] @1:24:35, @1:28:29).

## Claims
- [[neural-networks-are-just-mathematical-expressions]]
- [[backpropagation-is-more-general-than-neural-networks]]
- [[micrograd-is-all-you-need-everything-else-is-efficiency]]
- [[forgetting-to-zero-grad-is-a-common-neural-net-bug]]

## Related
- [[micrograd]] — the scalar autograd engine that implements it
- [[verify-gradients-against-pytorch]] — how he checks hand-derived gradients
- [[gradient-descent]] — what the gradients are used for
- [[multilayer-perceptron]]
- [[activation-functions]]
- [[pytorch]]
