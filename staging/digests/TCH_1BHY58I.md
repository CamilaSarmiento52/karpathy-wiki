# Digest: Building makemore Part 2: MLP
- raw: raw/youtube/TCH_1BHY58I.md · published: 2022-09-12 · medium: youtube · words: 12891
- source slug: youtube-2022-09-12-makemore-2-mlp

## Source page

```
---
type: source
raw_path: raw/youtube/TCH_1BHY58I.md
published: 2022-09-12
medium: youtube
summary: Second makemore lecture; he builds the Bengio et al. 2003 MLP character model in PyTorch, then teaches minibatches, learning-rate search, train/dev/test splits and how to read under- versus over-fitting.
url: https://www.youtube.com/watch?v=TCH_1BHY58I
title: "Building makemore Part 2: MLP"
---

# Building makemore Part 2: MLP
Raw: [[raw/youtube/TCH_1BHY58I]] · Original: https://www.youtube.com/watch?v=TCH_1BHY58I

## Summary
He opens by showing why the bigram count table cannot take more context: the number of rows grows exponentially with context length, and the counts per row collapse (@01:06, @01:40). He then walks through the Bengio et al. 2003 model, in which each token is embedded through a shared lookup table C, the embeddings are concatenated, passed through a tanh hidden layer and a softmax output, and everything including C is trained by backpropagation (@02:46, @06:08, @08:21). Implementing it in PyTorch, he shows that indexing an embedding table is the same operation as a linear layer on one-hot inputs (@15:30), that `.view` reshapes without touching memory while `torch.cat` allocates (@24:24, @27:10), and that `F.cross_entropy` should replace a hand-rolled softmax loss for efficiency and numerical stability (@33:16, @37:08). Training the full 228,000-example set is slow, so he introduces minibatches and argues that an approximate gradient with more steps beats an exact one with fewer (@42:07, @44:24). He demonstrates a learning-rate sweep on an exponential grid, picks 0.1 from the loss-versus-exponent plot, then trains and decays by 10x (@47:07, @50:25, @52:37). Finally he explains the 80/10/10 train/dev/test split, reads equal train and dev loss as under-fitting, scales the hidden layer and embedding size, visualises the learned 2D character embeddings, and reaches a best validation loss of 2.17 (@54:49, @1:00:20, @1:06:02, @1:11:38).

## Key points
- Count-based n-gram tables blow up exponentially with context length, which motivates the MLP → [[mlp-language-model]] (@01:06)
- The Bengio 2003 architecture: shared embedding table C, tanh hidden layer, softmax over the vocabulary, all trained by backprop → [[mlp-language-model]] (@06:08, @08:21)
- Embeddings let the model generalise to unseen contexts because similar tokens land near each other → [[embeddings]] (@05:01)
- Indexing a lookup table equals a linear layer applied to one-hot inputs; he indexes because it is faster → [[embedding-index-equals-one-hot-linear-layer]] (@15:30, @16:02)
- `.view` manipulates storage offset, strides and shape without copying; `torch.cat` creates new memory → [[pytorch-tensor-views]], [[view-is-free-cat-copies]] (@24:24, @27:10)
- Use `F.cross_entropy` instead of rolling your own: fused kernels, simpler backward, and max-subtraction avoids overflow → [[cross-entropy-loss]], [[use-cross-entropy-not-a-hand-rolled-loss]] (@33:16, @34:56, @37:08)
- Overfit a single small batch first to check the training loop; loss cannot reach zero where one context has several labels → [[overfit-a-single-batch]] (@39:23, @40:28)
- Minibatches trade gradient quality for speed; more approximate steps beat fewer exact ones → [[minibatch-training]], [[approximate-gradient-with-more-steps-beats-exact-gradient]] (@43:50, @44:24)
- Find a learning rate by sweeping exponents from -3 to 0 over 1,000 steps and plotting loss against exponent → [[learning-rate-sweep]], [[learning-rate]] (@47:07, @50:25)
- Rough recipe: find a decent rate, train a while, decay by 10x at the end → [[learning-rate]] (@52:37)
- A lower training loss does not by itself mean a better model; bigger nets can memorise the training set → [[lower-training-loss-alone-does-not-mean-a-better-model]], [[overfitting-and-underfitting]] (@53:10, @53:42)
- Split data roughly 80/10/10 into train, dev and test; dev tunes hyperparameters, test is touched very few times → [[train-dev-test-splits]], [[test-set-evaluated-very-few-times]] (@54:49, @55:22, @55:54)
- Train loss roughly equal to dev loss means under-fitting; scale the network up → [[diagnose-under-or-overfitting]], [[equal-train-and-dev-loss-means-underfitting]] (@1:00:20)
- Trained 2D character embeddings cluster the vowels together and isolate q and the dot → [[embeddings]] (@1:06:02, @1:06:35)
- makemore is the artifact being built; a Colab link lets viewers run it with no install → [[makemore]] (@00:00, @1:14:57)

## Fed pages
- [[mlp-language-model]]
- [[embeddings]]
- [[pytorch-tensor-views]]
- [[cross-entropy-loss]]
- [[minibatch-training]]
- [[learning-rate]]
- [[train-dev-test-splits]]
- [[overfitting-and-underfitting]]
- [[makemore]]
- [[learning-rate-sweep]]
- [[overfit-a-single-batch]]
- [[diagnose-under-or-overfitting]]
- [[embedding-index-equals-one-hot-linear-layer]]
- [[view-is-free-cat-copies]]
- [[use-cross-entropy-not-a-hand-rolled-loss]]
- [[approximate-gradient-with-more-steps-beats-exact-gradient]]
- [[lower-training-loss-alone-does-not-mean-a-better-model]]
- [[test-set-evaluated-very-few-times]]
- [[equal-train-and-dev-loss-means-underfitting]]
```

## Candidates

### topic: mlp-language-model
- existing: no
- aliases: Bengio et al. 2003, neural probabilistic language model, multilayer perceptron language model, MLP character model
- statements:
  - The bigram model only looks at one previous character, and its predictions were not very name-like (@00:33)
  - Taking more context with a count table grows the table exponentially: 27 contexts for one character, 729 for two, about 20,000 for three, leaving too few counts per row (@01:06, @01:40)
  - The modelling approach follows Bengio et al. 2003, which he says is not the first MLP language-model paper but a very influential and readable one (@01:40, @02:13)
  - The paper is word-level with a 17,000-word vocabulary; he keeps the same approach at the character level (@02:46)
  - Each word gets a roughly 30-dimensional feature vector, initialised randomly and tuned by backpropagation (@02:46, @03:21)
  - Training maximises the log likelihood of the training data, as in the bigram model (@03:54)
  - The lookup table C is a 17,000-by-30 matrix shared across all input positions; each index plucks out a row (@06:08, @06:42)
  - The hidden layer size is a hyperparameter, followed by a tanh non-linearity and an output layer of one logit per vocabulary item; the output layer is the expensive one (@06:42, @07:15, @07:49)
  - The parameters are the output weights and biases, hidden weights and biases, and the embedding table C (@08:21)
  - Block size is the context length; he uses three characters to predict the fourth and pads with dots as a rolling window (@09:28, @11:07)
  - His implementation uses 27 characters embedded in 2 dimensions, a 100-neuron hidden layer and about 3,400 parameters (@12:13, @18:51, @32:10)
  - Scaling the hidden layer to 300 gives about 10,000 parameters; 10-dimensional embeddings with 200 hidden neurons give about 11,000 (@1:00:52, @1:07:41)
  - Sampling: start from dots, embed the context, get logits, apply F.softmax, draw with torch.multinomial, shift the window (@1:13:16, @1:13:50)
  - Samples from the trained model are much more name-like than the bigram samples, though still improvable (@1:14:24)
  - Knobs left to the viewer: hidden size, embedding dimension, context length, optimisation details, batch size (@1:12:12, @1:12:44)

### topic: embeddings
- existing: no
- aliases: embedding table, lookup table, lookup table C, feature vectors
- statements:
  - Words are embedded as points in a small space; similar words or synonyms may end up near each other after training (@03:21, @03:54)
  - Embeddings let the model handle an out-of-distribution phrase by transferring knowledge from nearby embeddings, e.g. "a" and "the", or cats and dogs (@04:27, @05:01, @05:34)
  - Indexing into C with a one-hot vector times C gives the same result as indexing the row, because the zeros mask out every other row (@13:19, @14:58)
  - The embedding can be read either as a lookup or as the first linear layer of the network with weight matrix C; he indexes because it is much faster (@15:30, @16:02)
  - PyTorch can index C with a list, a tensor, or a multi-dimensional tensor of integers, so C[X] embeds all 32-by-3 integers at once (@16:34, @17:07, @18:16)
  - After training with 2D embeddings, the vowels a e i o u cluster together, q and the dot are outliers, and the structure is not random (@1:06:02, @1:06:35)
  - He suspects two dimensions are the bottleneck and raises the embedding size to 10; the lower loss afterwards suggests the embedding size was holding the model back (@1:04:25, @1:07:08, @1:11:05)

### topic: pytorch-tensor-views
- existing: no
- aliases: torch.view, storage and strides, PyTorch internals, torch.cat vs view, broadcasting
- statements:
  - Torch is a very large library and there are usually many ways to implement something, some faster or shorter (@19:58)
  - torch.cat concatenates a sequence of tensors along a dimension; indexing each position by hand does not generalise to other block sizes (@20:31, @22:10)
  - torch.unbind returns the slices along a dimension, which makes the concatenation generalise (@22:10, @22:43)
  - A tensor's storage is always a one-dimensional vector; `.view` changes storage offset, strides and shape so no memory is copied, moved or created (@24:24, @24:57)
  - He points to Edward Yang's "PyTorch Internals" blog post and may make a video on tensor internals (@24:57, @25:29)
  - Passing -1 to view lets PyTorch infer the dimension (@27:10)
  - Concatenation creates a whole new tensor with new storage, so it is less efficient than view (@27:10, @27:43)
  - Broadcasting a 100-vector bias onto a 32-by-100 matrix aligns on the right, adds a fake dimension, and copies the row; he says to always check broadcasting (@28:16, @28:49)

### topic: cross-entropy-loss
- existing: no
- aliases: F.cross_entropy, torch.nn.functional.cross_entropy, negative log likelihood, softmax numerical stability
- statements:
  - The hand-rolled loss exponentiates logits to fake counts, normalises to probabilities, plucks the correct-class probability and takes the mean negative log (@29:55, @31:03, @31:36)
  - F.cross_entropy computes exactly the same loss (@32:44, @33:16)
  - Reason one: PyTorch avoids the intermediate tensors and uses fused kernels (@33:16, @33:49)
  - Reason two: the backward pass is simpler analytically, as with tanh in micrograd where the derivative is 1 - t squared (@33:49, @34:23)
  - Reason three: numerical stability; exp of a large positive logit overflows to inf and gives nan, while very negative logits are fine (@35:30, @36:02)
  - Logits can be offset by any constant without changing the probabilities, so PyTorch subtracts the maximum logit internally (@36:35, @37:08)
  - F.softmax is likewise careful about overflow when sampling (@1:13:50)

### topic: minibatch-training
- existing: no
- aliases: minibatches, mini batch, batch size, stochastic gradient descent
- statements:
  - Forwarding and backwarding all 228,000 examples each step is too slow (@41:35, @42:07)
  - In practice people update on a randomly selected minibatch; he uses torch.randint to pick 32 indices into X and Y (@42:07, @42:42, @43:16)
  - With minibatches the gradient quality is lower and the direction less reliable, but good enough to be useful on 32 examples (@43:50)
  - It is much better to have an approximate gradient and take more steps than an exact gradient with fewer steps (@44:24)
  - The minibatch loss is noisy, so he evaluates on the full training set to judge progress (@44:24, @44:56)
  - The loss curve is thick because of minibatch noise; a larger batch size would give a more correct gradient and less thrashing (@1:01:57, @1:02:30)
  - Plotting log10 of the loss squashes the hockey-stick shape (@1:08:14)

### topic: learning-rate
- existing: no
- aliases: learning rate, step size, learning rate decay
- statements:
  - His initial 0.1 was a guess, and he cannot tell from the loss alone whether steps are too slow or too fast (@44:56, @45:28)
  - A learning rate of 1 minimises the loss but is unstable, 10 does not optimise at all, so the right value is between 0.001 and 1 (@46:34, @47:07)
  - Stepping linearly between rates does not make sense; he steps linearly in the exponent so the candidates are spaced exponentially (@47:07, @47:42)
  - The loss-versus-exponent plot shows nothing happening at low rates, a valley, then instability; around exponent -1, i.e. 0.1, is a good setting (@49:52, @50:25, @50:59)
  - Learning-rate decay means lowering the rate by 10x in the late stages of training once the loss plateaus (@51:32, @52:04)
  - The rough recipe: find a decent rate, train a while, then decay by a factor of 10 and take a few more steps; he calls this janky and not production practice (@52:37)
  - He admits his decay is done at random and the optimisation is suspect; in production you would turn these into hyperparameters and run many experiments (@1:09:20, @1:09:55)
  - A final run uses 0.1 for 100,000 steps then 0.01 for 100,000 (@1:11:38)

### topic: train-dev-test-splits
- existing: no
- aliases: train/dev/test, validation split, held-out data, hyperparameters
- statements:
  - The standard in the field is three splits: training, dev or validation, and test, typically about 80/10/10 (@54:15, @54:49)
  - The training split optimises parameters by gradient descent; the dev split is for development over hyperparameters such as hidden size, embedding size and regularisation strength (@54:49, @55:22)
  - The test split evaluates the model at the end and is used very sparingly, because every time you learn from the test loss you start training on it (@55:22, @55:54)
  - He shuffles the words and splits at 80% and 90%, giving about 25,000 training words and about 3,000 words each for dev and test (@56:26, @57:01, @57:33)
  - Once hyperparameters are chosen by dev performance, the test set is evaluated a single time and that is the number you report (@1:10:30)

### topic: overfitting-and-underfitting
- existing: no
- aliases: overfitting, underfitting, memorisation, model capacity
- statements:
  - With 3,400 parameters and 32 examples the network overfits a single batch and reaches a very low loss (@39:23)
  - Loss cannot reach exactly zero because the same context (dots) has several possible next characters in the data (@40:28, @41:03)
  - A lower training loss does not prove a better model: as capacity grows, the model can memorise the training set verbatim, samples repeat the training data, and held-out loss can be very high (@53:10, @53:42, @54:15)
  - Equal training and dev loss means the model is not overfitting but under-fitting; the network is too small and should be scaled up (@1:00:20)
  - After scaling, training and validation loss start to slowly depart, which he reads as the start of overfitting (@1:09:55)
  - A hidden-layer bottleneck versus an embedding bottleneck: making the tanh layer bigger did not help much, so the 2D embeddings were suspected (@1:03:52, @1:04:25)

### artifact: makemore
- existing: no
- aliases: makemore
- statements:
  - makemore is the character-level name generator he is building across lectures; part 1 was the bigram model with counts and a one-layer net (@00:00)
  - The dataset is about 32,000 names, giving 228,000 three-character examples (@08:55, @41:35)
  - This lecture implements the MLP step of the makemore plan (@01:40)
  - He shares a Google Colab so the notebook runs in the browser with no installation (@1:14:57, @1:15:30)
- note: the raw gives no repo URL; `repo_url` for the artifact page must come from elsewhere (likely github.com/karpathy/makemore). `language`: Python.

### method: learning-rate-sweep
- existing: no
- aliases: learning rate search, LR range test
- steps: reset parameters → try a few rates by hand to bracket too-slow and exploding → build 1,000 exponents with torch.linspace from -3 to 0 and take 10 to the power → run 1,000 steps using lrs[i] at step i, recording rate and loss → plot loss against exponent → pick a value in the valley before instability
- statements:
  - Reset parameters and print the loss every step for a short run to find a reasonable search range (@45:28, @46:01)
  - A very low rate barely decreases the loss; around 1 it is unstable; 10 does not work (@46:01, @46:34)
  - Use torch.linspace on exponents from -3 to 0 with 1,000 steps and raise 10 to them, so the candidates are exponentially spaced (@47:07, @47:42)
  - Index the learning rate by the step number, starting very low and ending at 1, tracking the rate and loss used (@48:14, @48:47)
  - Plot losses against the exponent rather than the raw rate; the good setting is in the valley, around exponent -1 (@49:52, @50:25)
  - This gave confidence that 0.1 was a fairly good rate (@50:59)
- seen in: this source

### method: overfit-a-single-batch
- existing: no
- aliases: overfit one batch, sanity-check the training loop
- steps: build the dataset from a handful of words → run the full forward/backward/update loop → confirm the loss falls to near zero → check argmax predictions against labels → then switch to the full dataset
- statements:
  - He develops on the first five words, 32 examples, for efficiency and plans to erase that later (@10:02)
  - Running 1,000 steps on 32 examples gives a very low loss because there are 3,400 parameters for so few examples (@38:50, @39:23)
  - He inspects the max logits and their indices against the labels to see where they differ (@39:56, @40:28)
  - Loss cannot be exactly zero where one input has several labels; it is correct where input to output is unique (@40:28, @41:03)
  - Then he reads in the full dataset and optimises (@41:03, @41:35)
- seen in: this source

### method: diagnose-under-or-overfitting
- existing: no
- aliases: compare train and dev loss, reading train vs dev loss
- steps: evaluate loss on train and on dev → if roughly equal, the model is under-fitting, so scale it up → if dev departs above train, the model is starting to overfit → report test loss once at the end
- statements:
  - After training only on the train split he evaluates on dev and gets about 2.3, then compares to the training loss (@59:12, @59:47)
  - Train and dev loss about equal means not overfitting but under-fitting, so he expects gains from scaling the network (@1:00:20)
  - He increases the hidden layer to 300 neurons and later the embedding to 10 dimensions (@1:00:52, @1:07:08)
  - When train and validation performance slowly depart, the parameters may be large enough to start overfitting (@1:09:55)
  - Hyperparameters are tuned on dev performance across many experiments; the test set is evaluated a single time (@1:10:30)
- seen in: this source

### claim: embedding-index-equals-one-hot-linear-layer
- existing: no
- title: Indexing an embedding table is the same as a linear layer on one-hot inputs
- confidence: stated
- quote: "So those are two equivalent ways of doing the same thing." (@16:02)
- statements:
  - A one-hot vector times C masks out all but the fifth row, giving the same result as indexing (@14:58)
  - The embedding can be seen as a first layer of linear neurons with weight matrix C fed one-hot inputs (@15:30)
  - He indexes because it is much faster and discards the one-hot interpretation (@16:02)
- relation: none in index

### claim: view-is-free-cat-copies
- existing: no
- title: `.view` costs no memory while `torch.cat` allocates new storage
- confidence: stated
- quote: "And in PyTorch, this operation calling dot view is extremely efficient." (@23:49)
- statements:
  - view manipulates storage offset, strides and shape; no memory is changed, copied, moved or created (@24:24, @24:57)
  - Concatenation creates a whole new tensor with new storage because there is no way to concatenate by manipulating view attributes (@27:10, @27:43)
- relation: none in index

### claim: use-cross-entropy-not-a-hand-rolled-loss
- existing: no
- title: Call F.cross_entropy rather than rolling your own softmax and log-likelihood
- confidence: stated
- quote: "I did this for educational reasons, but you'd never use this in practice." (@33:16)
- statements:
  - The forward pass is more efficient via fused kernels, the backward pass is simpler analytically, and the result is numerically well-behaved (@33:16, @34:56, @37:41)
  - Large positive logits overflow exp to inf; PyTorch subtracts the maximum logit to avoid this (@36:02, @37:08)
- relation: none in index

### claim: approximate-gradient-with-more-steps-beats-exact-gradient
- existing: no
- title: An approximate minibatch gradient with more steps is better than an exact gradient with fewer steps
- confidence: stated
- quote: "It's not the actual gradient direction." (@43:50) — short; the full statement at @44:24 is 25 words and must be paraphrased
- statements:
  - Minibatch gradient quality is lower and the direction less reliable, but good enough on 32 examples to be useful (@43:50)
  - It is much better to have an approximate gradient and make more steps than to evaluate the exact gradient and take fewer (@44:24)
- relation: none in index

### claim: lower-training-loss-alone-does-not-mean-a-better-model
- existing: no
- title: A lower training loss does not by itself mean a better model
- confidence: stated
- quote: "But all that the model is doing is memorizing your training set verbatim." (@53:42)
- statements:
  - He says calling the MLP better than the bigram model because 2.3 beats 2.45 is not exactly true (@53:10)
  - As capacity grows the training loss can go to zero while the model memorises; samples repeat training data and held-out loss can be very high (@53:42, @54:15)
- relation: none in index

### claim: test-set-evaluated-very-few-times
- existing: no
- title: The test split should be evaluated very few times because each look trains on it
- confidence: stated
- quote: "Otherwise, you risk overfitting to it as well as you experiment on your model." (@55:54)
- statements:
  - Every time you evaluate the test loss and learn from it you start training on the test split (@55:54)
  - At the end you evaluate the test set a single time and report that number (@1:10:30)
- relation: none in index

### claim: equal-train-and-dev-loss-means-underfitting
- existing: no
- title: Train loss roughly equal to dev loss means the model is under-fitting and should be scaled up
- confidence: stated
- quote: "And so, we see that the training and the dev loss are about equal." (@1:00:20)
- statements:
  - Equal losses mean the model is not powerful enough to memorise and is under-fitting; the network is tiny and improvements are expected from scaling (@1:00:20)
- relation: none in index

## Quotes
- "This is the expensive layer." (@07:49)
- "So this is kind of like a rolling window of context." (@11:07)
- "So those are two equivalent ways of doing the same thing." (@16:02)
- "Luckily, PyTorch indexing is fairly flexible and quite powerful." (@16:34)
- "So, basically, long story short, PyTorch indexing is awesome." (@18:16)
- "And in PyTorch, this operation calling dot view is extremely efficient." (@23:49)
- "I did this for educational reasons, but you'd never use this in practice." (@33:16)
- "And so, there's many good reasons to call cross entropy." (@37:41)
- "It's not the actual gradient direction." (@43:50)
- "Um so, this point one, I just guessed it." (@45:28)
- "But, it doesn't really make sense to step between these linearly." (@47:07)
- "So we've already surpassed the bigram model." (@52:04)
- "But all that the model is doing is memorizing your training set verbatim." (@53:42)
- "This is used to train the hyper parameters." (@55:22)
- "Otherwise, you risk overfitting to it as well as you experiment on your model." (@55:54)
- "Training a neural network can take a while." (@58:40)
- "And so, we see that the training and the dev loss are about equal." (@1:00:20)
- "No installation necessary." (@1:15:30)

## Notes for merge
- Captions in this raw file are punctuated and capitalised (not lowercase), with filler words ("uh", "um") and stutters ("we we", "it is is"); quotes above are copied exactly, including leading "So," / "And so," / "Um so,".
- Caption transcription quirks: "tan h" for tanh (@15:30); "after cross entropy" means F.cross_entropy (@34:56, @37:41); "lrs of I" / "LRE at I" are variable names lrs[i], lre[i] (@48:14, @49:52); "20 each one" is a stumble (@12:46); "over- fitting" is split across a hyphen (@1:00:20); "I'm converting this to be a function" refers to `build_dataset` (@56:26); "N2 to be 90% of the weight of the words" is a slip for "of the words" (@57:01); "0.2 2.48" is a stumble before "2.48" (@51:32). The "26-dimensional vector" at @13:52 is a slip for 27-dimensional.
- The blog post he cites is "PyTorch Internals" by "Eric" in the captions (@24:57); the author of that post is Edward Z. Yang — the digest statement names him, but the raw says only "Eric". Merge should either keep "Eric" or label the correction as a Note.
- The Bengio et al. 2003 paper is explained at length (@01:40–@08:55) but no title or URL is given beyond "Bengio et al. 2003". He also leaves dashed arrows (direct input-to-output connections) unexplained (@08:21).
- Mentioned only, not explained: micrograd and its tanh backward (@34:23); regularisation as a hyperparameter not yet used (@55:22); "launch a bunch of jobs and wait" production training (@58:40); the paper's ideas for improvements (@1:12:44); Google Colab link in the description (@1:14:57).
- Numbers: 32,000 names (@08:55); 228,000 examples, also said as 220,000 and 200,000 in passing (@41:35, @42:07, @43:16); bigram loss 2.45 (@52:04); best validation loss 2.17 (@1:11:38); final train/dev readings 2.16/2.19 (@1:11:05).
- The raw does not give a repo URL for makemore; the artifact page's `repo_url` needs a non-raw source or the GitHub README once ingested. Part 1 (bigram lecture) is referenced throughout as "the previous video" but is not in index.md yet, so cross-lecture links wait for that ingest.
- Quote for the minibatch claim is weak (6 words); the real argument at @44:24 is too long to quote under the 15-word rule and is paraphrased instead.
- Nothing here contradicts or extends any existing claim in index.md; all candidates are new.
