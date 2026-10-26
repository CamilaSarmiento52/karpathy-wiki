---
type: topic
aliases: [WaveNet, hierarchical model, progressive fusion, dilated causal convolution, context length, block size, convolutions as efficiency]
first_seen: 2022-10-04
last_updated: 2022-11-21
sources: ["[[youtube-2022-10-04-makemore-3-activations-batchnorm]]", "[[youtube-2022-11-21-makemore-5-wavenet]]"]
related: ["[[multilayer-perceptron]]", "[[makemore]]", "[[batch-normalization]]", "[[pytorch]]", "[[embeddings]]"]
---
# WaveNet-style hierarchical model
A deeper character-level model that takes more context than the MLP's three characters and fuses it progressively, two consecutive elements per level, rather than feeding every character into one hidden layer; making the MLP more complex this way arrives, he says, at something very much like WaveNet, a 2016 autoregressive audio model with the same modelling setup and a tree-like architecture ([[youtube-2022-11-21-makemore-5-wavenet]] @00:33, @01:05, @19:22).

## What he says
The motivation comes from the end of the third lecture: he suspects the three-character MLP is bottlenecked by its context length rather than by optimisation, and that RNNs and Transformers would be needed to push further ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:53:45, @1:54:17). In part 5 he wants more input characters and a deeper model, because squashing everything into one hidden layer crushes too much information too fast ([[youtube-2022-11-21-makemore-5-wavenet]] @00:33, @19:56).

Longer context alone helps: changing the block size from 3 to 8 means predicting the ninth character from eight of context and grows the first Linear layer by about 10,000 parameters, and the flat model's validation loss improves from 2.10 to 2.02 with qualitatively better samples ([[youtube-2022-11-21-makemore-5-wavenet]] @19:22, @19:56, @20:29, @21:01). He calls this a rough baseline with a lot of hyperparameter optimisation left on the table ([[youtube-2022-11-21-makemore-5-wavenet]] @21:01).

In WaveNet, two characters are fused into a bigram representation, bigrams into four-character chunks, and so on, so context is fused slowly as the network deepens; the dilated causal convolution framing sounds scary, he says, but the idea is simple and the convolution is an implementation detail for speed ([[youtube-2022-11-21-makemore-5-wavenet]] @18:13, @18:49). At each level the network fuses only two consecutive elements: two characters, then two bigrams, then two four-grams ([[youtube-2022-11-21-makemore-5-wavenet]] @19:22).

The hierarchy is a reshape plus the same Linear layer, because PyTorch's matrix multiply works on the last dimension and treats all leading dimensions as batch dimensions: a (4, 5, 80) input through an 80-by-200 weight gives (4, 5, 200) ([[youtube-2022-11-21-makemore-5-wavenet]] @24:52, @25:27). He uses this to process the four bigram groups of each example in parallel as an extra batch dimension, so the flatten layer should output (4, 4, 20) rather than (4, 80) and the first Linear should expect 20 inputs ([[youtube-2022-11-21-makemore-5-wavenet]] @26:01, @27:11, @27:46). Explicitly concatenating even and odd positions gives the same result as calling view with the desired shape ([[youtube-2022-11-21-makemore-5-wavenet]] @28:51, @30:03, @30:36). He writes a `FlattenConsecutive(n)` module that views (B, T, C) as (B, T//n, C*n) and squeezes out a spurious dimension of size one, named differently from `torch.flatten` because the APIs differ ([[youtube-2022-11-21-makemore-5-wavenet]] @31:42, @32:15, @33:23). With `FlattenConsecutive(2)` and three Linear-BatchNorm-Tanh blocks the shapes go (4,8,10) → (4,4,20) → (4,4,200) → (4,2,400) → (4,200) → (4,400) → logits ([[youtube-2022-11-21-makemore-5-wavenet]] @35:38, @36:10, @36:42). The three-layer network implements the WaveNet tree for a receptive field of 8; the paper's diagram has four layers and 16 ([[youtube-2022-11-21-makemore-5-wavenet]] @37:15). He did not implement WaveNet's gated linear units, residual connections or skip connections, only the structure ([[youtube-2022-11-21-makemore-5-wavenet]] @47:13).

Controlling for parameters, the hierarchy did not beat the flat model at first: with 22,000 parameters in both, validation loss was 2.029 against 2.027, which he reads as not giving anything yet, with the caveats that the architecture was his first guess with no hyperparameter search and that BatchNorm1d might still have a bug ([[youtube-2022-11-21-makemore-5-wavenet]] @37:47, @38:20). It did: his BatchNorm1d kept per-position statistics on the 3-D input, and the fix moved validation loss to 2.022, an improvement he says may not be statistically significant ([[youtube-2022-11-21-makemore-5-wavenet]] @40:32, @45:01, @45:35). Bumping embeddings to 24 and the hidden units up gives 76,000 parameters and a validation loss of 1.993 ([[youtube-2022-11-21-makemore-5-wavenet]] @46:08). He closes by saying it is not obvious that a large enough one-hidden-layer network could not beat the hierarchical one, which would be embarrassing ([[youtube-2022-11-21-makemore-5-wavenet]] @55:40).

The use of convolutions in WaveNet, he says, is strictly for efficiency and does not change the model implemented here ([[youtube-2022-11-21-makemore-5-wavenet]] @47:46). A seven-letter name like DeAndre is eight independent examples; forwarding them is eight separate model calls, or a Python for-loop, and a convolution hides that loop inside CUDA kernels, sliding a linear filter over a one-dimensional input sequence ([[youtube-2022-11-21-makemore-5-wavenet]] @47:46, @48:20, @48:53, @49:27). The WaveNet diagram's black tree is what he implemented for one output; a convolution slides that tree to compute all outputs at once ([[youtube-2022-11-21-makemore-5-wavenet]] @49:27, @50:01). The second efficiency is variable reuse: an intermediate node is the right child of one parent and the left child of another, so it is computed once rather than twice ([[youtube-2022-11-21-makemore-5-wavenet]] @50:34, @51:08). He plans a future video converting the network to dilated causal convolutional layers ([[youtube-2022-11-21-makemore-5-wavenet]] @51:08, @53:57).

## Claims
- [[deep-learning-is-largely-shape-gymnastics]] — the reshapes that make the hierarchy work
- [[avoid-batch-normalization-where-possible]] — the 3-D BatchNorm bug that hid the hierarchy's gain

## Related
- [[multilayer-perceptron]] — the flat model it deepens
- [[makemore]] — part 5 of the series
- [[batch-normalization]] — the 3-D input bug and channels-last convention
- [[pytorch]] — matmul over leading batch dimensions, Flatten and Sequential
- [[embeddings]] — the (B, T, C) embedding output the hierarchy reshapes
- [[diagnose-under-or-overfitting]] — the parameter-matched comparison
- [[check-shapes-and-broadcasting]] — printing every layer's output shape
