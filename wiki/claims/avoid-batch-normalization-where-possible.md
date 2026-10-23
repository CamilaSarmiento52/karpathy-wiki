---
type: claim
stated_on: 2022-10-04
confidence: stated
sources: ["[[youtube-2022-10-04-makemore-3-activations-batchnorm]]", "[[youtube-2022-10-11-makemore-4-backprop-ninja]]", "[[youtube-2022-11-21-makemore-5-wavenet]]"]
topic: "[[batch-normalization]]"
supports: ["[[batchnorm-train-test-variance-mismatch-is-a-bug]]"]
---
# He tells learners to avoid batch normalization as much as possible because coupling examples causes bugs
> "so basically try to avoid it as much as possible" — [[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:17:07

## Context
He says the stability offered by batch normalization comes at a terrible cost: the examples in a batch are coupled mathematically in the forward and backward pass ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @49:49, @50:23). Deceivingly, he says, this coupling is a second-order regulariser: one example's hidden states jitter depending on which other examples share the batch, which pads out the examples like a form of data augmentation and makes overfitting harder, and that is one reason it has been hard to remove in favour of other normalizations ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @50:57, @52:04, @52:38, @53:44). He says no one likes this property, it leads to strange results and a lot of bugs, and people have tried to deprecate it for layer, instance or group normalization ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @52:38, @53:11). He says he has shot himself in the foot with this layer over and over and does not want viewers to suffer the same ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:17:07). He still credits it as very influential in 2015 for making deep nets trainable ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:17:40).

A smaller pitfall of the same layer: a bias in the linear or conv layer before batchnorm is subtracted out by the mean subtraction, so `b1.grad` is zero and the bias never learns; he recommends `bias=False` there, as PyTorch's ResNet does, and calls it wasteful rather than catastrophic ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:01:31, @1:02:04, @1:02:37, @1:07:40, @1:08:13).

The WaveNet lecture adds the state argument: the running statistics and train/eval flag have to be managed, and he says there is state in the layer, state is harmful, and it introduces bugs when you forget the mode ([[youtube-2022-11-21-makemore-5-wavenet]] @03:52, @04:25). That lecture hits two such bugs on camera: NaN from training mode on a single example, and wrong reduction dimensions on a 3-D input ([[youtube-2022-11-21-makemore-5-wavenet]] @16:03, @40:32).

## Related claims
- supports [[batchnorm-train-test-variance-mismatch-is-a-bug]]: the following lecture names one of the bugs, PyTorch's biased-in-training, unbiased-at-inference variance, which he says gives anyone using the layer a bit of a bug ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:17:07; [[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:08:05).
- **Note:** [[modern-innovations-make-precise-initialization-less-important]] names normalization layers among the innovations that made deep nets easier to train; this claim is his caveat on the most common of them ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @36:26, @1:17:07).
