---
type: topic
aliases: [Activation functions, tanh, ReLU, dead neurons, saturation]
first_seen: 2022-08-16
last_updated: 2022-09-12
sources: ["[[youtube-2022-08-16-micrograd]]", "[[youtube-2022-09-12-makemore-2-mlp]]"]
related: ["[[multilayer-perceptron]]", "[[backpropagation]]", "[[micrograd]]"]
---
# Activation functions
The activation is usually a squashing function such as sigmoid or tanh applied to a neuron's weighted sum plus bias; tanh maps zero to zero and caps smoothly at 1 and -1 ([[youtube-2022-08-16-micrograd]] @53:54, @54:28, @55:02).

## What he says
tanh cannot be built from plus and times alone because it needs exponentiation, so in micrograd he implements it as a single composite op whose local derivative is 1 - tanh² ([[youtube-2022-08-16-micrograd]] @57:16, @1:03:23, @1:03:56). Later he breaks tanh into exp, addition, subtraction and division and gets identical forward and backward results ([[youtube-2022-08-16-micrograd]] @1:27:18, @1:37:47, @1:38:22).

micrograd as of recording ships ReLU rather than tanh; he says ReLU, tanh and sigmoid are all roughly equivalent for MLPs and chose tanh in the video because it is smoother and stresses the local-gradient work more ([[youtube-2022-08-16-micrograd]] @2:17:07, @2:17:40).

The makemore MLP's hidden layer uses tanh before the output layer ([[youtube-2022-09-12-makemore-2-mlp]] @06:42). When arguing for `F.cross_entropy`, he recalls that tanh's backward in micrograd was simply 1 - t² as an example of an analytically simpler backward pass ([[youtube-2022-09-12-makemore-2-mlp]] @33:49, @34:23).

## Claims
- [[micrograd-is-all-you-need-everything-else-is-efficiency]] — tanh as atomic op or composite gives the same gradients

## Related
- [[multilayer-perceptron]]
- [[backpropagation]]
- [[micrograd]]
- [[multilayer-perceptron]]
- [[makemore]]
