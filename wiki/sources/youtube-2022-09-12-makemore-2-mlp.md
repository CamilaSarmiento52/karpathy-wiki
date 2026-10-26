---
type: source
raw_path: raw/youtube/TCH_1BHY58I.md
published: 2022-09-12
medium: youtube
summary: "Second makemore lecture; he builds the Bengio et al. 2003 MLP character model in PyTorch, then teaches minibatches, learning-rate search, train/dev/test splits and how to read under- versus over-fitting."
url: https://www.youtube.com/watch?v=TCH_1BHY58I
title: "Building makemore Part 2: MLP"
---
# Building makemore Part 2: MLP
Raw: [[raw/youtube/TCH_1BHY58I]] · Original: https://www.youtube.com/watch?v=TCH_1BHY58I

## Summary
He opens by showing why the bigram count table cannot take more context: the number of rows grows exponentially with context length, and the counts per row collapse (@01:06, @01:40). He then walks through the Bengio et al. 2003 model, in which each token is embedded through a shared lookup table C, the embeddings are concatenated, passed through a tanh hidden layer and a softmax output, and everything including C is trained by backpropagation (@02:46, @06:08, @08:21). Implementing it in PyTorch, he shows that indexing an embedding table is the same operation as a linear layer on one-hot inputs (@15:30), that `.view` reshapes without touching memory while `torch.cat` allocates (@24:24, @27:10), and that `F.cross_entropy` should replace a hand-rolled softmax loss for efficiency and numerical stability (@33:16, @37:08). Training the full 228,000-example set is slow, so he introduces minibatches and argues that an approximate gradient with more steps beats an exact one with fewer (@42:07, @44:24). He demonstrates a learning-rate sweep on an exponential grid, picks 0.1 from the loss-versus-exponent plot, then trains and decays by 10x (@47:07, @50:25, @52:37). Finally he explains the 80/10/10 train/dev/test split, reads equal train and dev loss as under-fitting, scales the hidden layer and embedding size, visualises the learned 2D character embeddings, and reaches a best validation loss of 2.17 (@54:49, @1:00:20, @1:06:02, @1:11:38).

## Key points
- Count-based n-gram tables blow up exponentially with context length, which motivates the MLP → [[multilayer-perceptron]], [[bigram-language-model]], [[gradient-based-models-scale-where-count-tables-do-not]] (@01:06)
- The Bengio 2003 architecture: shared embedding table C, tanh hidden layer, softmax over the vocabulary, all trained by backprop → [[multilayer-perceptron]], [[activation-functions]] (@06:08, @08:21)
- Embeddings let the model generalise to unseen contexts because similar tokens land near each other → [[embeddings]] (@05:01)
- Indexing a lookup table equals a linear layer applied to one-hot inputs; he indexes because it is faster → [[embeddings]], [[softmax]] (@15:30, @16:02)
- `.view` manipulates storage offset, strides and shape without copying; `torch.cat` creates new memory → [[pytorch]] (@24:24, @27:10)
- A bias broadcast onto a 32×100 matrix is checked against the rules; always check broadcasting → [[broadcasting]], [[check-shapes-and-broadcasting]] (@28:16, @28:49)
- Use `F.cross_entropy` instead of rolling your own: fused kernels, simpler backward, and max-subtraction avoids overflow → [[loss-functions]], [[use-cross-entropy-not-a-hand-rolled-loss]] (@33:16, @34:56, @37:08)
- Developing on 32 examples, he gets a very low loss and names it overfitting a single batch; loss cannot reach zero where one context has several labels → [[diagnose-under-or-overfitting]] (@39:23, @40:28)
- Minibatches trade gradient quality for speed; more approximate steps beat fewer exact ones → [[gradient-descent]], [[approximate-gradient-with-more-steps-beats-exact-gradient]] (@43:50, @44:24)
- Find a learning rate by sweeping exponents from -3 to 0 over 1,000 steps and plotting loss against exponent → [[learning-rate-sweep]], [[gradient-descent]] (@47:07, @50:25)
- Rough recipe: find a decent rate, train a while, decay by 10x at the end → [[gradient-descent]] (@52:37)
- A lower training loss does not by itself mean a better model; bigger nets can memorise the training set → [[overfitting-and-generalization]] (@53:10, @53:42)
- Split data roughly 80/10/10 into train, dev and test; dev tunes hyperparameters including regularisation strength, test is touched very few times → [[overfitting-and-generalization]], [[regularization]] (@54:49, @55:22, @55:54)
- Train loss roughly equal to dev loss means under-fitting; scale the network up → [[diagnose-under-or-overfitting]], [[overfitting-and-generalization]] (@1:00:20)
- Trained 2D character embeddings cluster the vowels together and isolate q and the dot → [[embeddings]] (@1:06:02, @1:06:35)
- Sampling from the MLP: embed the context, logits, `F.softmax`, `torch.multinomial`, shift the window → [[character-level-language-modeling]] (@1:13:16, @1:13:50)
- makemore is the artifact being built; a Colab link lets viewers run it with no install → [[makemore]] (@00:00, @1:14:57)

## Fed pages
- [[multilayer-perceptron]]
- [[bigram-language-model]]
- [[embeddings]]
- [[softmax]]
- [[pytorch]]
- [[broadcasting]]
- [[loss-functions]]
- [[gradient-descent]]
- [[activation-functions]]
- [[regularization]]
- [[overfitting-and-generalization]]
- [[character-level-language-modeling]]
- [[makemore]]
- [[learning-rate-sweep]]
- [[diagnose-under-or-overfitting]]
- [[check-shapes-and-broadcasting]]
- [[use-cross-entropy-not-a-hand-rolled-loss]]
- [[approximate-gradient-with-more-steps-beats-exact-gradient]]
- [[gradient-based-models-scale-where-count-tables-do-not]]
- [[how-he-explains]]
- [[be-careful-with-shapes-and-be-explicit]]
