---
type: source
raw_path: raw/youtube/P6sfmUTpUmc.md
published: 2022-10-04
medium: youtube
summary: "Makemore lecture 3 diagnoses a badly initialised MLP (confident logits, saturated tanh), derives Kaiming initialisation, implements batch normalization and introduces his activation, gradient and update-ratio diagnostic plots."
url: https://www.youtube.com/watch?v=P6sfmUTpUmc
title: "Building makemore Part 3: Activations & Gradients, BatchNorm"
---
# Building makemore Part 3: Activations & Gradients, BatchNorm
Raw: [[raw/youtube/P6sfmUTpUmc]] · Original: https://www.youtube.com/watch?v=P6sfmUTpUmc

## Summary
Continuing the makemore character-level MLP, he says the point of staying at the MLP level is to build intuition for activations and the gradients flowing backwards before moving to RNNs, which he says are hard to optimise for exactly these reasons (@00:33, @01:06). He first shows the network is misconfigured at initialisation: the initial loss of 27 is far above the roughly 3.29 expected from a uniform distribution over 27 characters, because the output layer is confidently wrong; shrinking the output weights removes the hockey-stick loss curve and improves the final loss (@04:28, @05:38, @11:44, @12:19). He then shows the tanh hidden layer is saturated, explains why tanh outputs near ±1 kill the gradient, defines dead neurons for tanh and ReLU, and fixes it by scaling the first layer (@14:00, @16:17, @19:12, @21:26, @25:57). To replace the hand-tuned scales he derives dividing by the square root of fan-in, introduces the Kaiming paper and its gain, and notes that residual connections, normalization layers and better optimisers have made precise initialisation less important (@30:21, @31:30, @34:50, @35:55, @36:26). He implements batch normalization from the paper, including scale and shift, running statistics for inference, epsilon and the redundant bias, and argues that its coupling of examples in a batch is both an accidental regulariser and a source of bugs he tells viewers to avoid (@41:25, @45:52, @50:23, @52:04, @56:29, @1:17:07). A bonus section rewrites the code as PyTorch-style modules and introduces his diagnostic plots: activation and gradient histograms per layer, weight gradient-to-data ratios, and the update-to-data ratio over time with a rough target of 1e-3 on a log scale (@1:18:47, @1:27:05, @1:31:03, @1:37:41, @1:42:06).

## Key points
- A rough expected initial loss can be computed from the problem; a far higher one means the logits are too extreme and the net is confidently wrong → [[weight-initialization]], [[loss-functions]] (@04:28, @05:38)
- Fixing the initial loss removes the hockey-stick loss curve and slightly improves the final result because training stops wasting steps on squashing weights → [[the-hockey-stick-loss-means-training-is-wasting-steps]] (@11:11, @12:19)
- tanh outputs near ±1 multiply the gradient by (1 - t²) ≈ 0 and stop backpropagation; a neuron that is saturated for every example is dead → [[activation-functions]] (@16:17, @19:12)
- Dividing weights by the square root of fan-in preserves unit standard deviation; Kaiming init adds a gain per nonlinearity (√2 for ReLU, 5/3 for tanh) → [[weight-initialization]] (@30:21, @34:50)
- He calls Kaiming normal probably the most common initialisation now → [[modern-innovations-make-precise-initialization-less-important]] (@33:45)
- Residual connections, normalization layers and optimisers like Adam make exact initialisation less important → [[modern-innovations-make-precise-initialization-less-important]] (@36:26)
- Batch normalization standardises pre-activations over the batch, adds a learned gain and bias, and keeps running mean and variance for inference → [[batch-normalization]] (@41:25, @45:52, @55:54)
- Its coupling of examples acts as a regulariser as a side effect, which has made it hard to remove → [[avoid-batch-normalization-where-possible]], [[overfitting-and-generalization]] (@52:04, @52:38)
- The same coupling causes bugs; he says to avoid the layer where possible → [[avoid-batch-normalization-where-possible]] (@1:17:07)
- A bias in a layer followed by batchnorm is subtracted out and never trains → [[avoid-batch-normalization-where-possible]], [[batch-normalization]] (@1:01:31)
- PyTorch-style Linear, BatchNorm1d and Tanh modules; `kaiming_normal`, `nn.Linear` defaults and `BatchNorm1d` arguments → [[pytorch]] (@1:09:55, @1:11:34, @1:18:47)
- Diagnostic plots: activation histograms and saturation, gradient histograms, weight grad-to-data and update-to-data ratios over time → [[training-diagnostics]] (@1:27:05, @1:31:03, @1:37:41)
- The update-to-data ratio should sit around 1e-3 on a log10 scale; far below means the learning rate is too low → [[training-diagnostics]], [[gradient-descent]] (@1:42:06, @1:43:12)
- Without normalisation a deep linear-tanh sandwich needs a precisely calibrated gain, like balancing a pencil; a stack of linear layers collapses to one linear function → [[weight-initialization]], [[multilayer-perceptron]] (@1:34:54, @1:45:56)
- The makemore MLP is now limited by its three-character context, not by optimisation → [[makemore]] (@1:53:45)
- Initialisation and backpropagation are still active research, not solved → [[modern-innovations-make-precise-initialization-less-important]] (@1:55:22)
- The lecture is part 3 of the makemore series → [[makemore]] (@00:00)
- He suspects the three-character MLP is bottlenecked by context length, not optimisation → [[wavenet-hierarchical-model]] (@1:53:45, @1:54:17)

## Fed pages
- [[weight-initialization]]
- [[batch-normalization]]
- [[the-hockey-stick-loss-means-training-is-wasting-steps]]
- [[modern-innovations-make-precise-initialization-less-important]]
- [[avoid-batch-normalization-where-possible]]
- [[batchnorm-train-test-variance-mismatch-is-a-bug]]
- [[training-diagnostics]]
- [[activation-functions]]
- [[gradient-descent]]
- [[pytorch]]
- [[loss-functions]]
- [[overfitting-and-generalization]]
- [[multilayer-perceptron]]
- [[makemore]]
- [[wavenet-hierarchical-model]]
