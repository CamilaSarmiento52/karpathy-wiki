# Digest: Building makemore Part 3: Activations & Gradients, BatchNorm
- raw: raw/youtube/P6sfmUTpUmc.md · published: 2022-10-04 · medium: youtube · words: ~21,600
- source slug: youtube-2022-10-04-makemore-3-activations-batchnorm

## Source page

```
---
type: source
raw_path: raw/youtube/P6sfmUTpUmc.md
published: 2022-10-04
medium: youtube
summary: Makemore lecture 3 diagnoses a badly initialised MLP (confident logits, saturated tanh), derives Kaiming initialisation, implements batch normalization and introduces his activation, gradient and update-ratio diagnostic plots.
url: https://www.youtube.com/watch?v=P6sfmUTpUmc
title: "Building makemore Part 3: Activations & Gradients, BatchNorm"
---
# Building makemore Part 3: Activations & Gradients, BatchNorm
Raw: [[raw/youtube/P6sfmUTpUmc]] · Original: https://www.youtube.com/watch?v=P6sfmUTpUmc

## Summary
Continuing the makemore character-level MLP, he says the point of staying at the MLP level is to build intuition for activations and the gradients flowing backwards before moving to RNNs, which he says are hard to optimise for exactly these reasons (@00:33, @01:06). He first shows the network is misconfigured at initialisation: the initial loss of 27 is far above the roughly 3.29 expected from a uniform distribution over 27 characters, because the output layer is "confidently wrong"; shrinking the output weights removes the hockey-stick loss curve and improves the final loss (@04:28, @05:38, @11:44, @12:19). He then shows the tanh hidden layer is saturated, explains why tanh outputs near ±1 kill the gradient, defines dead neurons for tanh and ReLU, and fixes it by scaling the first layer (@14:00, @16:17, @19:12, @21:26, @25:57). To replace the hand-tuned scales he derives dividing by the square root of fan-in, introduces the Kaiming paper and its gain, and notes that residual connections, normalization layers and better optimisers have made precise initialisation less important (@30:21, @31:30, @34:50, @35:55, @36:26). He implements batch normalization from the paper, including scale and shift, running statistics for inference, epsilon and the redundant bias, and argues that its coupling of examples in a batch is both an accidental regulariser and a source of bugs he tells viewers to avoid (@41:25, @45:52, @50:23, @52:04, @56:29, @1:17:07). A bonus section rewrites the code as PyTorch-style modules and introduces his diagnostic plots: activation and gradient histograms per layer, weight gradient-to-data ratios, and the update-to-data ratio over time with a rough target of 1e-3 on a log scale (@1:18:47, @1:27:05, @1:31:03, @1:37:41, @1:42:06).

## Key points
- A rough expected initial loss can be computed from the problem; a far higher one means the logits are too extreme and the net is confidently wrong → [[weight-initialization]]
- Fixing the initial loss removes the hockey-stick loss curve and slightly improves the final result because training stops wasting steps on squashing weights → [[the-hockey-stick-loss-means-training-is-wasting-steps-on-shrinking-weights]]
- Tanh outputs near ±1 multiply the gradient by (1 - t²) ≈ 0 and stop backpropagation; a neuron that is saturated for every example is dead → [[saturated-tanh-and-dead-neurons]]
- Dividing weights by the square root of fan-in preserves unit standard deviation; Kaiming init adds a gain per nonlinearity (√2 for ReLU, 5/3 for tanh) → [[kaiming-initialization]]
- He calls Kaiming normal probably the most common initialisation now → [[kaiming-init-is-probably-the-most-common-initialization]]
- Residual connections, normalization layers and optimisers like Adam make exact initialisation less important → [[modern-innovations-make-precise-initialization-less-important]]
- Batch normalization standardises pre-activations over the batch, adds a learned gain and bias, and keeps running mean and variance for inference → [[batch-normalization]]
- Its coupling of examples acts as a regulariser as a side effect, which has made it hard to remove → [[batchnorm-regularizes-as-a-side-effect-of-coupling-examples]]
- The same coupling causes bugs; he says to avoid the layer where possible → [[avoid-batch-normalization-where-possible]]
- A bias in a layer followed by batchnorm is subtracted out and never trains → [[a-bias-before-batchnorm-is-useless]]
- Diagnostic plots: activation histograms and saturation, gradient histograms, weight grad-to-data and update-to-data ratios over time → [[training-diagnostics-plots]]
- The update-to-data ratio should sit around 1e-3 on a log10 scale; far below means the learning rate is too low → [[update-to-data-ratio-should-be-around-1e-3]]
- Without normalisation a deep linear-tanh sandwich needs a precisely calibrated gain, like balancing a pencil → [[weight-initialization]]
- The makemore MLP is now limited by its three-character context, not by optimisation → [[makemore-mlp-is-bottlenecked-by-context-length-not-optimization]]
- Initialisation and backpropagation are still active research, not solved → [[initialization-and-backpropagation-are-not-solved]]
- The lecture is part 3 of the makemore series → [[makemore]]

## Fed pages
- [[weight-initialization]]
- [[saturated-tanh-and-dead-neurons]]
- [[kaiming-initialization]]
- [[batch-normalization]]
- [[the-hockey-stick-loss-means-training-is-wasting-steps-on-shrinking-weights]]
- [[kaiming-init-is-probably-the-most-common-initialization]]
- [[modern-innovations-make-precise-initialization-less-important]]
- [[batchnorm-regularizes-as-a-side-effect-of-coupling-examples]]
- [[avoid-batch-normalization-where-possible]]
- [[a-bias-before-batchnorm-is-useless]]
- [[update-to-data-ratio-should-be-around-1e-3]]
- [[makemore-mlp-is-bottlenecked-by-context-length-not-optimization]]
- [[initialization-and-backpropagation-are-not-solved]]
- [[makemore]]
- [[training-diagnostics-plots]]
```

## Candidates

### topic: weight-initialization
- existing: no
- aliases: [Weight initialization, initialization, initial loss, expected loss at initialization]
- statements:
  - He says you almost always have a rough idea of the loss to expect at initialisation from the loss function and problem setup (@04:28).
  - With 27 possible characters and no reason to prefer any, the expected initial loss is -log(1/27) ≈ 3.29, not the 27 recorded (@05:03, @05:38).
  - The high loss comes from logits taking extreme values so the network is confidently wrong; he wants logits roughly zero (or at least equal) at initialisation (@05:38, @07:51, @08:25).
  - He zeroes the output bias and scales the output weights by 0.01 rather than exactly zero, keeping a little entropy for symmetry breaking (@09:33, @10:39, @11:11).
  - He prefers not to set weights to exactly zero and says he is nervous about doing so, though for the output layer in this case he thinks it would be fine (@10:39).
  - For the hidden layer he sometimes multiplies biases by 0.01 for a little diversity and finds in practice that can help optimisation a little (@24:15).
  - Validation loss moved from 2.17 to 2.13 by fixing the softmax, then to 2.10 by fixing tanh saturation (@25:57).
  - A one-hidden-layer MLP is forgiving of bad initialisation, but with 50-layer networks the problems stack up and a network can fail to train at all (@27:02, @27:35).
  - In a sandwich of linear layers alone the right gain is 1; with 5/3 the activations diffuse and the gradients shrink with depth, an asymmetry that is bad for deep nets (@1:32:09, @1:32:43, @1:33:16).
  - Before normalization layers, Adam and residual connections, training deep nets was a balancing act and very deep networks were basically impossible to train (@1:33:49, @1:34:21).
  - A stack of linear layers collapses to a single linear function in the forward pass, though its training dynamics differ; nonlinearities make it a universal approximator (@1:34:54, @1:35:28, @1:36:02).
  - Calibrating gains in a linear-tanh sandwich feels like balancing a pencil on your finger (@1:45:56).

### topic: saturated-tanh-and-dead-neurons
- existing: no
- aliases: [Saturated tanh, dead neurons, vanishing gradient through tanh, dead ReLU]
- statements:
  - After fixing the logits, the hidden tanh activations are mostly -1 or 1 because the pre-activations spread between roughly -5 and 15 (@13:26, @14:00, @14:34).
  - In backprop the local gradient of tanh is 1 - t², so an output near ±1 multiplies the incoming gradient by about zero and stops it; the gradient through tanh can only decrease (@15:41, @16:17, @17:28).
  - He visualises |h| > 0.99 as a boolean image; a fully white column would be a dead neuron that no example activates and that never learns (@18:36, @19:12, @19:44).
  - Sigmoid has the same issue; ReLU zeroes the gradient exactly in its flat region, so a ReLU that never activates is dead (@20:17, @20:53, @21:26).
  - Dead neurons can arise at initialisation or during training when a high learning rate knocks a neuron off the data manifold, which he likens to permanent brain damage (@21:58, @22:33).
  - Leaky ReLU does not suffer as much because it has no flat tails; ELU has flat parts and may (@23:06).
  - Scaling the first-layer weights to about 0.2 brings pre-activations to roughly ±1.5 with no saturated neurons (@24:48, @25:22).
  - In the deeper experiments he reports percent saturation as |t| > 0.97, and finds roughly 5% saturation and standard deviation about 0.65 a good range for the tanh sandwich with gain 5/3 (@1:27:05, @1:28:12, @1:30:30).

### topic: kaiming-initialization
- existing: no
- aliases: [Kaiming initialization, He initialization, Kaiming normal, fan-in scaling]
- statements:
  - Multiplying a unit-Gaussian input by Gaussian weights expands the standard deviation (to about 3 with fan-in 10); he wants roughly unit-Gaussian activations throughout the net (@29:15, @29:48).
  - Dividing the weights by the square root of fan-in preserves unit standard deviation (@30:21, @30:58).
  - He points to "Delving deep into rectifiers" (He et al.), which studies ReLU in conv nets and adds a factor √2 because ReLU discards half the distribution (@31:30, @32:04, @32:36).
  - The paper finds that initialising the forward pass well also roughly initialises the backward pass, and that the fan-in versus fan-out choice does not matter much (@33:10, @33:45, @34:18).
  - PyTorch's kaiming_normal takes a mode and a nonlinearity, with gain 1 for linear, √2 for ReLU and 5/3 for tanh (@33:45, @34:50).
  - The gain compensates for tanh and ReLU being contractive, squeezing the distribution (@35:23).
  - In practice he just normalises weights by the square root of fan-in; the exact version is std = gain / √fan_in (@37:00).
  - For his W1 the fan-in is 30 (embedding 10 × block size 3), giving a scale of about 0.3 versus the 0.2 he found by eye; the result is the same 2.10 without magic numbers (@38:43, @39:16, @39:47, @40:19).
  - PyTorch's nn.Linear defaults to uniform init in ±1/√fan_in with gain 1 (@1:09:55, @1:10:28).
  - He does not know where the 5/3 tanh gain in PyTorch comes from; he searched briefly and found nothing, but empirically it stabilises the linear-tanh sandwich (@1:29:56, @1:30:30).
  - Gain 1 with tanh layers shrinks activations towards zero over depth; gain 3 saturates them; the gradients also distort when the gain is too small or too large (@1:28:47, @1:29:56, @1:31:03, @1:31:35).

### topic: batch-normalization
- existing: no
- aliases: [Batch normalization, batchnorm, BatchNorm, BatchNorm1d]
- statements:
  - Batch normalization came out in 2015 from a team at Google and made training very deep nets reliable (@40:52).
  - The insight is that if you want roughly Gaussian hidden states you can just normalise them over the batch, because standardising is differentiable (@41:25, @41:58).
  - He computes mean and standard deviation over the batch dimension (shape 1×200) and standardises the pre-activations before tanh (@42:33, @43:06, @44:13).
  - Forcing unit Gaussian always gives poor results, so the paper adds a learned scale (gain, initialised to 1) and shift (bias, initialised to 0) that backprop can move (@45:19, @45:52, @46:27).
  - With one hidden layer, batchnorm gives the same 2.10 because the scale could already be set by hand; it pays off in deep nets with many layer types where tuning scales becomes intractable (@48:06, @48:41, @49:16).
  - It is customary to append a batchnorm layer after linear or convolutional layers to control activation scale throughout the network (@49:16, @49:49).
  - The cost is that examples in a batch become mathematically coupled in the forward and backward pass, so one example's hidden states jitter depending on the others (@49:49, @50:23, @50:57, @51:31).
  - This jitter acts as a regulariser, a kind of data augmentation, which is one reason it has been hard to replace (@51:31, @52:04, @52:38).
  - People have tried to move to layer, instance or group normalization, which do not couple examples (@53:11, @53:44).
  - For inference the paper proposes calibrating mean and std once over the training set after training; he implements this and gets the same loss while being able to forward a single example (@54:16, @54:50, @55:22).
  - Instead, running mean and std are kept during training with a momentum update (0.999/0.001 here), outside gradient descent and under torch.no_grad; they come out close to the calibrated values (@55:54, @57:35, @58:09, @59:48, @1:00:26).
  - Epsilon (default 1e-5) prevents division by zero when batch variance is zero (@1:00:58).
  - A bias before batchnorm is subtracted out, gets zero gradient and is wasteful; the batchnorm bias takes over, which is why ResNet convs use bias=False (@1:01:31, @1:02:04, @1:02:37, @1:07:40, @1:08:13).
  - Summary: parameters are gain and bias (trained by backprop); buffers are running mean and std (updated by running mean); it standardises over the batch, then scales and shifts (@1:03:09, @1:03:44, @1:04:19).
  - The ResNet bottleneck block repeats the motif weight layer, normalization, nonlinearity (conv, batchnorm, ReLU) (@1:06:34, @1:07:07).
  - PyTorch BatchNorm1d takes num_features, eps, momentum (default 0.1), affine and track_running_stats; with batch size 32 a momentum of 0.1 may thrash and 0.001 is safer (@1:11:34, @1:12:06, @1:12:39, @1:13:13).
  - His module keeps a `training` flag like PyTorch, uses batch statistics when training and running statistics otherwise, and follows the paper in tracking variance rather than std (@1:21:35, @1:22:08, @1:23:15).
  - He places batchnorm after the linear layer and before the nonlinearity, says placing it after the nonlinearity gives similar results, and that it can also go before the loss, in which case gamma rather than the weight makes the softmax less confident (@1:46:30, @1:47:04).
  - With batchnorm the activations are homogeneous regardless of the linear gain, and even without fan-in scaling, but the update scale changes so the learning rate may need retuning (here about 10×) (@1:47:37, @1:48:44, @1:49:18, @1:49:50, @1:50:24, @1:51:00).
  - Training a batchnorm version with his learning-rate finder gave very similar results, because performance is no longer bottlenecked by optimisation (@1:53:45).

### claim: the-hockey-stick-loss-means-training-is-wasting-steps-on-shrinking-weights
- existing: no
- title: A hockey-stick loss curve means the first iterations are just squashing down overconfident weights
- confidence: stated
- quote: "the plot of the loss uh now doesn't have this hockey shape appearance" (@11:11)
- statements:
  - After fixing the output scale the loss no longer has the hockey-stick shape, because the easy early gains from shrinking the logits are gone (@11:11, @11:44).
  - He says this is true for any neural net you might train and is something to look out for (@12:19).
  - The final loss improved slightly (about 2.2 to 2.16 in that run) because more cycles went to real training (@12:19, @12:52).
  - In the closing summary he ties hockey-stick losses to confident mispredictions from messed-up activations at the last layer (@1:14:18).
- topic: weight-initialization

### claim: kaiming-init-is-probably-the-most-common-initialization
- existing: no
- title: Kaiming normal is probably the most common way to initialise neural networks (as of 2022)
- confidence: stated
- quote: "this is probably the most common way of initializing neural networks" (@33:45)
- statements:
  - He says Kaiming init is implemented in PyTorch as kaiming_normal and that in his opinion it is probably the most common initialisation now (@33:45).
  - He also says that in practice he himself just normalises by the square root of fan-in (@37:00).
- topic: kaiming-initialization

### claim: modern-innovations-make-precise-initialization-less-important
- existing: no
- title: Residual connections, normalization layers and better optimisers make exact initialisation less important
- confidence: stated
- quote: "it's become less important to initialize these networks exactly right" (@36:26)
- statements:
  - About seven years before the lecture you had to be extremely careful with activation and gradient ranges and gains, and everything was finicky and fragile (@35:55).
  - He names three innovations: residual connections, normalization layers (batch, layer, group), and better optimisers such as RMSprop and especially Adam (@36:26, @37:00).
  - He skips the Kaiming paper details intentionally for this reason (@35:55).
  - He nonetheless says initialisation and backprop are not solved (@1:55:22), see the claim below.
- topic: weight-initialization

### claim: batchnorm-regularizes-as-a-side-effect-of-coupling-examples
- existing: no
- title: Batch normalization's coupling of examples acts as a regulariser as a side effect
- confidence: stated
- quote: "deceivingly as a second order effect uh this is actually a regularizer" (@52:38)
- statements:
  - One example's hidden states jitter depending on which other examples are in the batch (@50:57, @51:31).
  - He says this pads out examples like a form of data augmentation, making overfitting harder (@52:04).
  - This regularising effect is one reason it has been hard to remove batchnorm in favour of other normalizations (@52:38, @53:44).
- topic: batch-normalization
- relation: supports [[avoid-batch-normalization-where-possible]] in the sense that both describe the same coupling; they are not in conflict.

### claim: avoid-batch-normalization-where-possible
- existing: no
- title: He tells learners to avoid batch normalization as much as possible because coupling examples causes bugs
- confidence: stated
- quote: "so basically try to avoid it as much as possible" (@1:17:07)
- statements:
  - He says the stability of batchnorm comes at a terrible cost: examples are coupled in the forward and backward pass (@49:49, @50:23).
  - He says no one likes this property, it leads to strange results and a lot of bugs, and people have tried to deprecate it for layer, instance or group normalization (@52:38, @53:11).
  - He says he has shot himself in the foot with this layer over and over and does not want viewers to suffer the same (@1:17:07).
  - He still credits it as very influential in 2015 for making deep nets trainable (@1:17:40).
- topic: batch-normalization

### claim: a-bias-before-batchnorm-is-useless
- existing: no
- title: A bias in a layer followed by batch normalization is subtracted out and never learns
- confidence: stated
- quote: "these biases now are actually useless" (@1:01:31)
- statements:
  - The batchnorm mean subtraction removes whatever bias was added, so b1.grad is zero (@1:01:31, @1:02:04).
  - He recommends no bias in linear or conv layers followed by batchnorm; the batchnorm bias does the job (@1:02:04, @1:02:37).
  - PyTorch's ResNet uses bias=False on its convolutions for exactly this reason (@1:07:40, @1:08:13).
  - It is not catastrophic, only wasteful (@1:02:37, @1:08:13).
- topic: batch-normalization

### claim: update-to-data-ratio-should-be-around-1e-3
- existing: no
- title: The update-to-data ratio should sit around 1e-3 (log10 ≈ -3) over training
- confidence: stated
- quote: "it should be like roughly one3" (@1:42:06)
- statements:
  - The update-to-data ratio is the std of (learning rate × gradient) divided by the std of the parameter, tracked per weight tensor each iteration and plotted as log10 (@1:40:26, @1:41:00).
  - He calls -3 a rough guide: updates about a thousandth of the tensor's magnitude (@1:42:06).
  - Below -3 usually means parameters train too slowly; with learning rate 0.001 the plot shows updates 10,000× too small (@1:43:12, @1:43:45).
  - His run sits around -2.5, a little high but stabilising, which he calls a decent learning rate (@1:44:17).
  - Without fan-in normalisation and with batchnorm the ratio fell well below -3 and he 10× the learning rate to 1.0 (@1:50:24, @1:51:00).
  - In the final summary he calls -3 on the log scale a good rough heuristic (@1:53:12).
- topic: training-diagnostics-plots (method)

### claim: makemore-mlp-is-bottlenecked-by-context-length-not-optimization
- existing: no
- title: His three-character makemore MLP is bottlenecked by context length, not optimisation
- confidence: stated (he says "I suspect")
- quote: "our performance now is not bottlenecked by the optimization" (@1:53:45)
- statements:
  - Training a batchnorm version with his learning-rate finder gave very similar results (@1:53:45).
  - He suspects the bottleneck is taking three characters to predict the fourth, and that RNNs and Transformers are needed to push further (@1:54:17).
- artifact: makemore

### claim: initialization-and-backpropagation-are-not-solved
- existing: no
- title: Initialisation and backpropagation are still active research, not solved
- confidence: stated
- quote: "we certainly haven't I would say soled initialization and we haven't soled back propagation" (@1:55:22)
- statements:
  - He says he did not fully explain why changing the gain requires a different learning rate, which would need the backward pass of each layer (@1:54:48).
  - He says the field is still working out the best initialisation and update rule, but at least there are tools to tell whether training is on track (@1:55:22).
- relation: extends [[modern-innovations-make-precise-initialization-less-important]] — same lecture; modern tools reduce the need for exactness but the underlying problem is unsolved. No contradiction.

### artifact: makemore
- existing: no
- aliases: [makemore]
- statements:
  - makemore is his character-level language model series; part 2 implemented an MLP along the lines of Bengio et al. 2003 and this part scrutinises its activations and gradients (@00:00, @00:33).
  - The dataset is about 32,000 names, a 27-token vocabulary with a special dot, split into train, dev and test (@01:06, @01:39).
  - The starting MLP has about 11,000 parameters, trained 200,000 steps with batch size 32, reaching train and val loss about 2.16 (@02:12).
  - He uses @torch.no_grad for evaluation to skip gradient bookkeeping (@02:45, @03:20).
  - The bonus section rewrites it into Linear, BatchNorm1d and Tanh modules with the same API as torch.nn, a six-layer MLP with about 46,000 parameters (@1:18:47, @1:25:25, @1:25:58, @1:52:07).
  - He says prepending nn. to his layers would make the code work with PyTorch (@1:52:07).
  - Validation loss moved from 2.17 to 2.13 to 2.10 across the fixes (@25:57).
- notes: repo_url and language are not stated in this source (the code is PyTorch); merge should take repo_url from a GitHub raw file if one exists, otherwise leave as PyTorch notebook with status active.

### method: training-diagnostics-plots
- existing: no (related to [[quick-experiment-loop]] which judges nanochat runs by fixed plots; this is a different, lower-level set of plots for a single training run)
- aliases: [Activation and gradient statistics, update-to-data ratio, training diagnostics]
- steps (proposed):
  - Compute the expected loss at initialisation and compare with the first recorded loss (@04:28, @05:38)
  - Plot the loss curve and check for a hockey stick (@11:11, @12:19)
  - Histogram the tanh activations per layer and report mean, std and percent saturation (|t| > 0.97) (@13:26, @14:00, @1:27:05, @1:27:38)
  - Visualise |h| > 0.99 as a boolean image and look for all-white columns (dead neurons) (@18:36, @19:44)
  - Histogram the gradients at each tanh layer and check they are similar across layers, neither shrinking nor exploding (@1:30:30, @1:31:03)
  - For each weight tensor, plot gradient mean, std, histogram and gradient-to-data ratio (@1:36:35, @1:37:07, @1:37:41)
  - Track the update-to-data ratio (log10 of std(lr × grad)/std(param)) per weight every iteration and plot it over time against -3 (@1:39:52, @1:40:26, @1:41:33, @1:42:06)
  - Use the update-ratio plot to set the learning rate: well below -3 means too slow, well above means too fast (@1:43:12, @1:43:45, @1:53:12)
- statements:
  - He says understanding activation and gradient statistics becomes increasingly important as networks get bigger and deeper (@1:14:18).
  - He adds a `.out` attribute to his modules, which PyTorch does not have, so he can gather statistics for plotting (@1:23:48).
  - The gradient-to-data ratio is less informative than the update-to-data ratio because the update is what actually changes the data (@1:39:52).
  - The output layer is an outlier: its weights were shrunk by 0.1, so it has 10× larger gradients and a high update ratio at first, which stabilises after about 1,000 steps (@1:38:15, @1:38:47, @1:39:20, @1:42:39).
  - People look at these ratios over time rather than as a single snapshot (@1:52:40, @1:53:12).
  - He demonstrates that forgetting fan-in normalisation shows up at once in saturation, gradient and update-ratio plots (@1:44:49, @1:45:22).
  - He mentions a learning-rate finding mechanism "described before" (earlier lecture) (@1:53:45).

## Quotes
- "the network is very confidently wrong" (@05:38)
- "we want the loges to be roughly zero" (@07:51)
- "the plot of the loss uh now doesn't have this hockey shape appearance" (@11:11)
- "you are looking at your distribution of 10h activations here and you are sweating" (@15:07)
- "we are killing the gradient" (@16:17)
- "that's kind of like a permanent brain damage" (@22:33)
- "you are supposed to divide by the square root of the fan in" (@30:21)
- "this is probably the most common way of initializing neural networks" (@33:45)
- "everything was very finicky and very fragile" (@35:55)
- "it's become less important to initialize these networks exactly right" (@36:26)
- "I basically just uh normalize my weights by the square root of the Fanon" (@37:00)
- "when I first read it my mind was blown" (@41:58)
- "the stability offered by bash normalization actually comes at a terrible cost" (@49:49)
- "we are coupling these examples mathematically" (@50:23)
- "deceivingly as a second order effect uh this is actually a regularizer" (@52:38)
- "no one likes this layer it causes a huge amount of bugs" (@1:17:07)
- "I've shot myself in the foot with this layer over and over again" (@1:17:07)
- "so basically try to avoid it as much as possible" (@1:17:07)
- "honestly I have no idea where 5 over3 came from in pytorch" (@1:29:56)
- "it's like a total Balancing Act" (@1:33:49)
- "it was it was basically impossible to train very deep networks" (@1:34:21)
- "it should be like roughly one3" (@1:42:06)
- "it definitely feels a little bit like balancing of a pencil on your finger" (@1:45:56)
- "our performance now is not bottlenecked by the optimization" (@1:53:45)
- "we certainly haven't I would say soled initialization and we haven't soled back propagation" (@1:55:22)

## Notes for merge
- Caption misspellings, consistent throughout: "10h"/"10"/"10 H"/"tanh" = tanh; "bash normalization"/"bat normalization"/"bachor"/"borm"/"Bator"/"bachom" = batch normalization; "Fanon" = fan-in; "loges"/"loits"/"lits"/"loges"/"log jits" = logits; "gion"/"gsan"/"Gan"/"caution"/"goshan" = Gaussian; "reu"/"re" = ReLU; "leyu" = leaky ReLU; "King hatal"/"climing"/"coming"/"timing" init = Kaiming (He et al.); "soled" = solved; "one3"/"onean neg3"/"ne3" = 1e-3 / -3 on the log scale; "5 over3" = 5/3; "neurs"/"neurals"/"neural nut(s)" = neural nets; "microad"/"microgr" = micrograd; "benj 2003" = Bengio et al. 2003; "ARS prop" = RMSprop; "adom" = Adam; "make more" = makemore; "resonet"/"reset" = ResNet; "Aline"/"aine" = affine; "PCH"/"pyto"/"pych" = PyTorch.
- Quotes "it should be like roughly one3" and "we certainly haven't I would say soled initialization..." are verbatim with caption garble; a reviewer may prefer paraphrase on the claim page and keep these only in the digest.
- Mentioned but not explained (do not make topics): residual connections (promised for later, @36:26, @1:07:07), layer/instance/group normalization (@53:11, @1:15:27), RNNs/GRU/LSTM and Transformers (@00:00, @1:18:14, @1:54:17), convolutions (@1:06:00), data augmentation (@52:04), RMSprop and Adam (@36:26), the learning-rate finder (@1:53:45), infinitely-deep linear network papers (@1:35:28), half precision (@1:13:45).
- Timestamps in this raw are 30-second blocks; several statements span the boundary of two blocks, so the cited block is the one where the sentence starts.
- He frames the 1e-3 update-ratio target as a "rough guide" and "rough heuristic", not a rule; keep that hedge on the claim page.
- The claim about Kaiming being the most common initialisation is dated 2022 ("now"); title it with the date or "as of 2022".
- No GitHub raw for makemore exists yet in the index; the artifact page's repo_url cannot be filled from this source.
- Nothing here contradicts existing wiki pages; [[quick-experiment-loop]] is a plausible `related` link from the new method page (both are about reading fixed plots), labelled as a Note.
