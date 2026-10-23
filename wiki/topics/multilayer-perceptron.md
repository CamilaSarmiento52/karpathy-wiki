---
type: topic
aliases: [Multilayer perceptron, MLP, MLP language model, Bengio et al. 2003]
first_seen: 2022-08-16
last_updated: 2022-11-21
sources: ["[[youtube-2022-08-16-micrograd]]", "[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2022-10-04-makemore-3-activations-batchnorm]]", "[[youtube-2022-11-21-makemore-5-wavenet]]"]
related: ["[[micrograd]]", "[[backpropagation]]", "[[activation-functions]]", "[[gradient-descent]]", "[[weight-initialization]]", "[[batch-normalization]]"]
---
# Multilayer perceptron
A multilayer perceptron is a net of two or more layers whose neurons are fully connected to the previous layer ([[youtube-2022-08-16-micrograd]] @52:50, @1:47:47).

## What he says
A neuron multiplies each input by a synaptic weight, sums them, adds a bias he describes as the neuron's trigger happiness, and passes the result through a squashing activation such as sigmoid or tanh ([[youtube-2022-08-16-micrograd]] @53:23, @53:54, @55:02). He backpropagates by hand through a two-input tanh neuron, finding that w2's gradient is zero because x2 is zero ([[youtube-2022-08-16-micrograd]] @55:34, @1:07:18, @1:08:27).

In micrograd, `Neuron` initialises weights uniformly in [-1, 1] and a bias, and `__call__` returns tanh of the dot product plus bias ([[youtube-2022-08-16-micrograd]] @1:44:58, @1:46:41, @1:47:13). A layer is a list of independent neurons evaluated independently; an MLP is a list of layers applied sequentially, built from a list of layer sizes ([[youtube-2022-08-16-micrograd]] @1:48:20, @1:49:24). His example net has 3 inputs, two hidden layers of 4 and one output, 41 parameters in total ([[youtube-2022-08-16-micrograd]] @1:49:24, @2:01:02). `parameters()` on neuron, layer and MLP collects all weights and biases, matching PyTorch's nn.Module API ([[youtube-2022-08-16-micrograd]] @1:58:14, @1:59:22, @2:18:12). Gradients also exist on the input data but are not useful because the data is fixed ([[youtube-2022-08-16-micrograd]] @1:57:07, @1:57:40). A trained MLP over four examples plus the loss is a very large graph, and backprop still works through all of it ([[youtube-2022-08-16-micrograd]] @1:50:32, @1:56:36).

He says networks with hundreds of billions of parameters, such as GPT predicting the next word, train on the same principles with a different update and a cross-entropy loss ([[youtube-2022-08-16-micrograd]] @2:15:28, @2:16:00, @2:16:34).

Opening the second makemore lecture, he notes that the bigram model only looks at one previous character and that its predictions were not very name-like ([[youtube-2022-09-12-makemore-2-mlp]] @00:33). Taking more context with a count table grows the table exponentially: 27 contexts for one character, 729 for two, about 20,000 for three, leaving too few counts per row ([[youtube-2022-09-12-makemore-2-mlp]] @01:06, @01:40). His MLP language model follows Bengio et al. 2003, which he says is not the first MLP language-model paper but a very influential and readable one ([[youtube-2022-09-12-makemore-2-mlp]] @01:40, @02:13). The paper is word-level with a 17,000-word vocabulary; he keeps the same approach at the character level, and training maximises the log likelihood of the training data as in the bigram model ([[youtube-2022-09-12-makemore-2-mlp]] @02:46, @03:54). Each token is embedded through a shared lookup table C; the hidden layer size is a hyperparameter, followed by a tanh non-linearity and an output layer of one logit per vocabulary item, which he calls the expensive layer ([[youtube-2022-09-12-makemore-2-mlp]] @06:08, @06:42, @07:15, @07:49). The parameters are the output weights and biases, the hidden weights and biases, and the embedding table C ([[youtube-2022-09-12-makemore-2-mlp]] @08:21). Block size is the context length; he uses three characters to predict the fourth and pads with dots as a rolling window ([[youtube-2022-09-12-makemore-2-mlp]] @09:28, @11:07).

His implementation uses 27 characters embedded in 2 dimensions, a 100-neuron hidden layer and about 3,400 parameters ([[youtube-2022-09-12-makemore-2-mlp]] @12:13, @18:51, @32:10). Scaling the hidden layer to 300 gives about 10,000 parameters; 10-dimensional embeddings with 200 hidden neurons give about 11,000 ([[youtube-2022-09-12-makemore-2-mlp]] @1:00:52, @1:07:41). Samples from the trained model are much more name-like than the bigram samples, though still improvable, and the best validation loss he reaches is 2.17 ([[youtube-2022-09-12-makemore-2-mlp]] @1:11:38, @1:14:24). Knobs he leaves to the viewer: hidden size, embedding dimension, context length, optimisation details and batch size ([[youtube-2022-09-12-makemore-2-mlp]] @1:12:12, @1:12:44).

In the third makemore lecture he stays at the MLP level deliberately, to build intuition for the activations and the gradients flowing backwards before moving to RNNs, which he says are hard to optimise for exactly these reasons ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @00:33, @01:06). The starting MLP has about 11,000 parameters, trained 200,000 steps at batch size 32 to a train and validation loss of about 2.16 ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @02:12). A one-hidden-layer MLP is forgiving of bad initialisation, but with 50-layer networks the problems stack up and a network can fail to train at all ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @27:02, @27:35). In the bonus section he builds a six-layer MLP of about 46,000 parameters from PyTorch-style `Linear`, `BatchNorm1d` and `Tanh` modules ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:18:47, @1:25:25, @1:25:58). A stack of linear layers collapses to a single linear function in the forward pass, though its training dynamics differ; the nonlinearities are what make the net a universal approximator ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:34:54, @1:35:28, @1:36:02). He suspects that by the end of the lecture the three-character MLP is bottlenecked by its context length rather than by optimisation, and that RNNs and Transformers are needed to push further ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:53:45, @1:54:17).

The fifth lecture names the limit: feeding all the context characters into one hidden layer squashes too much information too quickly, so he wants a deeper model that fuses context progressively ([[youtube-2022-11-21-makemore-5-wavenet]] @00:33, @19:56). Still, after building it he says it is not obvious that a large enough one-hidden-layer network could not beat the hierarchical one ([[youtube-2022-11-21-makemore-5-wavenet]] @55:40).

## Claims
- [[gradient-based-models-scale-where-count-tables-do-not]]
- [[neural-networks-are-just-mathematical-expressions]]
- [[micrograd-is-all-you-need-everything-else-is-efficiency]]

## Related
- [[micrograd]] — the toy MLP library
- [[backpropagation]]
- [[activation-functions]]
- [[gradient-descent]]
- [[pytorch]]
- [[embeddings]] — the lookup table C
- [[bigram-language-model]] — the model it replaces
- [[overfitting-and-generalization]], [[diagnose-under-or-overfitting]], [[learning-rate-sweep]]
- [[weight-initialization]], [[batch-normalization]], [[training-diagnostics]] — what goes wrong inside a deeper MLP and how he reads it
- [[wavenet-hierarchical-model]] — the deeper model that replaces the single squashing layer
- [[makemore]]
