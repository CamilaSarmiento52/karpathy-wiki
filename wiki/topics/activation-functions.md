---
type: topic
aliases: [Activation functions, tanh, ReLU, dead neurons, saturation]
first_seen: 2022-08-16
last_updated: 2022-10-11
sources: ["[[youtube-2022-08-16-micrograd]]", "[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2022-10-04-makemore-3-activations-batchnorm]]", "[[youtube-2022-10-11-makemore-4-backprop-ninja]]"]
related: ["[[multilayer-perceptron]]", "[[backpropagation]]", "[[micrograd]]", "[[weight-initialization]]", "[[batch-normalization]]"]
---
# Activation functions
The activation is usually a squashing function such as sigmoid or tanh applied to a neuron's weighted sum plus bias; tanh maps zero to zero and caps smoothly at 1 and -1 ([[youtube-2022-08-16-micrograd]] @53:54, @54:28, @55:02).

## What he says
tanh cannot be built from plus and times alone because it needs exponentiation, so in micrograd he implements it as a single composite op whose local derivative is 1 - tanh² ([[youtube-2022-08-16-micrograd]] @57:16, @1:03:23, @1:03:56). Later he breaks tanh into exp, addition, subtraction and division and gets identical forward and backward results ([[youtube-2022-08-16-micrograd]] @1:27:18, @1:37:47, @1:38:22).

micrograd as of recording ships ReLU rather than tanh; he says ReLU, tanh and sigmoid are all roughly equivalent for MLPs and chose tanh in the video because it is smoother and stresses the local-gradient work more ([[youtube-2022-08-16-micrograd]] @2:17:07, @2:17:40).

The makemore MLP's hidden layer uses tanh before the output layer ([[youtube-2022-09-12-makemore-2-mlp]] @06:42). When arguing for `F.cross_entropy`, he recalls that tanh's backward in micrograd was simply 1 - t² as an example of an analytically simpler backward pass ([[youtube-2022-09-12-makemore-2-mlp]] @33:49, @34:23).

The third makemore lecture is about what goes wrong with tanh. After fixing the output logits, the hidden tanh activations are mostly -1 or 1 because the pre-activations spread between roughly -5 and 15 ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @13:26, @14:00, @14:34). In backprop the local gradient of tanh is 1 - t², so an output near ±1 multiplies the incoming gradient by about zero and stops it; he says the gradient through tanh can only decrease ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @15:41, @16:17, @17:28). He visualises |h| > 0.99 as a boolean image; a fully white column would be a dead neuron that no example activates and that never learns ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @18:36, @19:12, @19:44). Sigmoid has the same issue; ReLU zeroes the gradient exactly in its flat region, so a ReLU that never activates is dead ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @20:17, @20:53, @21:26). Dead neurons can arise at initialisation or during training when a high learning rate knocks a neuron off the data manifold, which he likens to permanent brain damage ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @21:58, @22:33). Leaky ReLU does not suffer as much because it has no flat tails; ELU has flat parts and may ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @23:06). Scaling the first-layer weights by 0.1 brought the pre-activations to roughly ±1.5 with no saturated neurons; he then relaxed the scale to 0.2 as a nicer distribution ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @24:48, @25:22). In the deeper experiments he reports percent saturation as |t| > 0.97, and finds roughly 5% saturation and standard deviation about 0.65 a good range for a tanh sandwich with gain 5/3 ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:27:05, @1:28:12, @1:30:30). The gain compensates for tanh and ReLU being contractive, squeezing the distribution ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @35:23).

In the hand-written tensor backward pass, the backward of tanh is again 1 minus the output squared, expressed in terms of the output rather than the input; he lists saturating nonlinearities killing gradients and dead neurons among the ways backprop leaks ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @01:37, @54:03, @54:35).

## Claims
- [[micrograd-is-all-you-need-everything-else-is-efficiency]] — tanh as atomic op or composite gives the same gradients
- [[modern-innovations-make-precise-initialization-less-important]] — why saturation is less fatal than it was

## Related
- [[multilayer-perceptron]]
- [[backpropagation]]
- [[micrograd]]
- [[weight-initialization]] — scaling weights to keep tanh out of saturation
- [[batch-normalization]] — normalising pre-activations instead
- [[training-diagnostics]] — the saturation plots
- [[makemore]]
