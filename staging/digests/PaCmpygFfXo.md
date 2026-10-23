# Digest: The spelled-out intro to language modeling: building makemore
- raw: raw/youtube/PaCmpygFfXo.md · published: 2022-09-07 · medium: youtube · words: 19658
- source slug: youtube-2022-09-07-makemore-1-bigram

## Source page

```
---
type: source
raw_path: raw/youtube/PaCmpygFfXo.md
published: 2022-09-07
medium: youtube
summary: First makemore lecture: a bigram character-level language model built twice, once by counting and normalising, once as a one-layer neural net trained on negative log likelihood, ending in the same model.
url: https://www.youtube.com/watch?v=PaCmpygFfXo
title: "The spelled-out intro to language modeling: building makemore"
---

# The spelled-out intro to language modeling: building makemore
Raw: [[raw/youtube/PaCmpygFfXo]] · Original: https://www.youtube.com/watch?v=PaCmpygFfXo

## Summary
He introduces makemore, a character-level language model trained on a file of about 32,000 names, and announces a series that will go from bigrams through MLPs and RNNs to a GPT-2-equivalent transformer (@00:00, @01:06, @02:13). The first model is a bigram model built by counting how often each character follows each other character into a 27×27 PyTorch tensor, normalising rows into probabilities, and sampling names with `torch.multinomial` and a seeded generator (@05:31, @17:40, @26:26, @32:02). Along the way he spends several minutes on PyTorch broadcasting, showing that dropping `keepdim=True` silently normalises columns instead of rows and urging viewers to treat broadcasting with respect (@42:01, @46:21, @49:08). He then evaluates the model with one number, the average negative log likelihood, derives it from likelihood and log likelihood, and fixes the infinite loss on unseen bigrams with model smoothing (@50:47, @53:27, @56:44, @1:01:43). In the second half he recasts the same model as a neural net: one-hot inputs, a single 27×27 linear layer producing logits, exponentiate and normalise (softmax), negative log likelihood loss, and gradient descent, reaching about the same loss as counting (@1:10:35, @1:16:08, @1:20:38, @1:27:22, @1:44:36). He closes by showing that the trained weights are the log counts of the counting model, that L2 regularisation plays the role of smoothing, and that only the forward pass will change as the series moves toward transformers (@1:48:58, @1:51:45, @1:46:46).

## Key points
- makemore is a character-level language model: each name is a sequence of characters and the model predicts the next character (@01:06, @01:39) → [[makemore]], [[character-level-language-modeling]]
- A single word packs many training examples, including the fact that the word ends (@04:24, @04:58) → [[character-level-language-modeling]]
- A bigram model looks only at the previous character; he calls it simple and weak but a great place to start (@05:31, @06:03) → [[bigram-language-model]]
- Counts go in a 2D tensor indexed by character; one special `.` token at index 0 replaces separate start and end tokens, which wasted a row and a column (@12:43, @20:56, @22:03) → [[bigram-language-model]]
- Sampling: take the row for the current character, normalise, draw with `torch.multinomial` under a seeded generator, stop at `.`; a uniform model shows the bigram samples are at least better than nothing (@25:21, @26:59, @32:02, @35:24) → [[sampling-from-a-language-model]]
- Broadcasting rules: align shapes from the right; each dimension must be equal, one, or missing; `keepdim=False` turns a 27×1 column into a 1×27 row and normalises the wrong axis (@42:01, @46:21, @47:29, @48:36) → [[broadcasting-semantics]], [[check-broadcasting-carefully]]
- Model quality is summarised as one number: likelihood → log likelihood → negative log likelihood → average, giving about 2.45 on the training set (@50:47, @53:27, @57:52, @1:00:02) → [[negative-log-likelihood]], [[evaluate-with-a-single-loss-number]]
- Unseen bigrams give infinite loss; adding fake counts (model smoothing) removes the zeros and makes the model more uniform (@1:00:35, @1:01:43, @1:02:16) → [[model-smoothing-and-regularization]]
- Integers cannot be fed into neurons, so inputs are one-hot encoded and cast to float (@1:10:02, @1:10:35, @1:13:18) → [[one-hot-encoding]]
- Prefer `torch.tensor` to `torch.Tensor`, and expect to read documentation and threads because frameworks are not always well documented (@1:07:47, @1:08:55, @1:09:28) → [[pytorch-tensor-basics]]
- The 27 outputs are interpreted as log counts (logits); exponentiate to get counts, normalise rows to get probabilities; the last two steps are the softmax (@1:20:38, @1:22:56, @1:27:22) → [[softmax]]
- Resampling W by hand and checking loss is "amateur hour"; the loss is differentiable, so use gradients: zero grad, `loss.backward()`, nudge W against the gradient (@1:32:20, @1:32:54, @1:38:29, @1:41:15) → [[gradient-based-optimization]], [[guess-and-check-is-not-how-you-optimize-a-neural-net]]
- Trained on all 228,000 bigrams the net reaches about 2.46, the same vicinity as counting (@1:43:27, @1:44:36, @1:45:08) → [[counting-and-gradient-bigram-models-are-the-same-model]]
- A one-hot vector times W plucks out a row of W, so `W.exp()` is the counts array arrived at by a different route (@1:47:52, @1:48:58, @1:49:31) → [[counting-and-gradient-bigram-models-are-the-same-model]]
- The gradient approach is more flexible and scalable; tables blow up with more context characters (@1:45:39, @1:46:46, @1:47:19) → [[gradient-based-approach-is-more-flexible-than-counting]], [[bigram-count-tables-do-not-scale-to-longer-contexts]]
- Pushing W toward zero (a squared-weight regularization term) is equivalent to smoothing; its strength plays the role of the added count (@1:51:13, @1:51:45, @1:52:52, @1:53:26) → [[model-smoothing-and-regularization]], [[weight-regularization-is-equivalent-to-count-smoothing]]
- Sampling from the neural net gives exactly the same names as the counting model (@1:54:33, @1:55:39) → [[counting-and-gradient-bigram-models-are-the-same-model]]
- Only the forward pass will change on the way to transformers; logits, softmax, NLL and gradient descent stay (@1:46:12, @1:46:46, @1:57:19) → [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers]]
- Teaching method: a blank notebook, spell everything out, seeded generators so viewers reproduce his numbers, build the explicit version first and then the neural-net version (@00:00, @02:45, @26:59, @1:03:22) → [[spell-it-out-step-by-step]], [[explicit-baseline-then-neural-net]]

## Fed pages
- [[makemore]]
- [[character-level-language-modeling]]
- [[bigram-language-model]]
- [[sampling-from-a-language-model]]
- [[broadcasting-semantics]]
- [[negative-log-likelihood]]
- [[model-smoothing-and-regularization]]
- [[one-hot-encoding]]
- [[softmax]]
- [[gradient-based-optimization]]
- [[pytorch-tensor-basics]]
- [[counting-and-gradient-bigram-models-are-the-same-model]]
- [[gradient-based-approach-is-more-flexible-than-counting]]
- [[bigram-count-tables-do-not-scale-to-longer-contexts]]
- [[weight-regularization-is-equivalent-to-count-smoothing]]
- [[treat-broadcasting-with-respect]]
- [[guess-and-check-is-not-how-you-optimize-a-neural-net]]
- [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers]]
- [[explicit-baseline-then-neural-net]]
- [[check-broadcasting-carefully]]
- [[evaluate-with-a-single-loss-number]]
- [[spell-it-out-step-by-step]]
```

## Candidates

### artifact: makemore
- existing: no
- aliases: make more
- repo_url: https://github.com/karpathy/makemore · language: Python · status: active (as of this source; later snapshots may change it)
- statements:
  - makemore is a repository on his GitHub that, like micrograd before it, he builds out step by step in the video series (@00:00)
  - It "makes more of things that you give it"; the example dataset names.txt holds about 32,000 names he found on a government website (@00:00, @00:34)
  - Trained on names it generates unique name-like strings such as Dontal, Irot, Zendy (@01:06)
  - Under the hood it is a character-level language model (@01:06)
  - The series will implement bigram and bag-of-words models, MLPs, RNNs and a transformer he says is basically equivalent to GPT-2 (@02:13)
  - Possible later extensions: word level, then images and image-text networks such as DALL-E and Stable Diffusion (@02:13, @02:45)
- relation: **Note:** candidate `related` link to [[nanogpt]] (the series' endpoint is a GPT-2-grade transformer; nanoGPT is his later repo for that) — a connection, not something the source says.

### topic: character-level-language-modeling
- existing: no
- aliases: character-level language model, char-level LM
- statements:
  - A character-level language model treats each line as an example and each example as a sequence of characters, and predicts the next character given the ones before (@01:06, @01:39, @04:24)
  - One word like Isabella contains many examples: which character comes first, which follows each prefix, and that the word is likely to end after the last letter (@04:24, @04:58)
  - With 32,000 words there is a lot of statistical structure to model (@05:31)
  - The dataset's shortest word has 2 characters, the longest 15 (@03:52)

### topic: bigram-language-model
- existing: no
- aliases: bigram model, bigrams
- statements:
  - A bigram model works with two characters at a time, predicting the next from only the previous one; he calls it very simple and weak but a great place to start (@05:31, @06:03)
  - Bigrams are collected with `zip(w, w[1:])` over a word wrapped with special start and end tokens (@06:36, @07:09, @08:15)
  - The simplest way to learn the statistics is counting how often each pair occurs, first in a Python dictionary, then in a 2D PyTorch tensor with rows = first character and columns = second (@09:20, @12:43)
  - Two special tokens waste an all-zero row and column, so he switches to a single `.` token at index 0 and offsets letters to start at 1, giving a 27×27 array (@20:56, @22:03, @22:36)
  - Row 0 of the counts is then the counts of first letters; column 0 is ending characters (@23:09)
  - The normalised rows of the counts matrix P are the parameters of the bigram model (@50:13)
  - Trained by counting, the model's average negative log likelihood on the training set is about 2.45 (@1:00:02)
  - He stared at the samples for a few minutes to convince himself they were right; they are bad because the model does not know whether an H is the first letter or has a history (@33:46, @34:17, @34:52)

### topic: sampling-from-a-language-model
- existing: no
- aliases: sampling, torch.multinomial, autoregressive sampling
- statements:
  - To sample, start at the `.` token, take that row of counts, convert to float and normalise to a probability vector, then draw an index (@24:17, @25:21, @25:52)
  - `torch.multinomial` takes probabilities and returns integers sampled according to them; `replacement=True` must be set because it defaults to false (@26:26, @28:05, @28:37)
  - He uses a seeded `torch.Generator` so viewers get exactly the same results as he does (@26:59, @27:32)
  - The loop feeds each sampled character back in as the row for the next draw and stops when index 0 (the end token) is sampled (@31:26, @32:02, @32:35)
  - Comparing against a uniform distribution over 27 characters shows the trained bigram model is more name-like than an untrained one, though still bad (@35:24, @35:58)
  - Re-normalising a row on every step is wasteful; he precomputes a probability matrix P once, also as practice for tensor manipulation (@36:30, @37:03)
  - The same sampling loop works for the neural net by replacing the row lookup with one-hot → W → exp → normalise (@1:54:33, @1:55:05)

### topic: broadcasting-semantics
- existing: no
- aliases: broadcasting, PyTorch broadcasting, keepdim
- statements:
  - `torch.sum` with `dim` sums along one dimension; `keepdim=True` keeps that dimension as size 1, `keepdim=False` squeezes it out (@38:43, @39:16, @39:50)
  - For the bigram counts, row sums and column sums happen to be identical, which hides which axis you summed (@40:55)
  - Broadcasting rules: each tensor has at least one dimension; align shapes from the trailing dimension; each pair must be equal, one of them 1, or one missing (@42:01, @42:32)
  - Dividing 27×27 by 27×1 stretches the column vector across 27 columns and divides element-wise, normalising rows (@43:05, @43:37)
  - Dividing 27×27 by a bare 27 also broadcasts: the 27 becomes 1×27, a row vector, which is replicated vertically, so columns get normalised instead of rows; P[0].sum() is 7, not 1 (@45:47, @46:21, @47:29, @48:02)
  - The issue comes from the silent adding of a dimension on the left (@48:02, @48:36)
  - He encourages viewers to read the broadcasting semantics, treat them with respect, practice, and check which direction things broadcast, because the bugs are subtle and hard to find (@44:10, @49:08, @49:40)
  - In-place operations such as `/=` avoid allocating a new tensor and can be faster (@49:40)

### topic: negative-log-likelihood
- existing: no
- aliases: NLL, likelihood, log likelihood, maximum likelihood estimation, loss function
- statements:
  - He wants to summarise model quality into a single number, the training loss, as in micrograd (@50:47)
  - With 27 characters, a uniform model gives about 4% per bigram, so probabilities above 4% mean the statistics learned something (@52:21)
  - In the maximum-likelihood literature the measure is the likelihood, the product of the probabilities the model assigns to the data; a good model makes it high (@52:54, @53:27)
  - The product is tiny, so people work with the log likelihood; log is monotonic, log(1)=0 and it goes to negative infinity at 0, and log of a product is a sum of logs (@53:27, @54:00, @55:03)
  - A loss function should be low-is-good, so negate it: negative log likelihood, whose minimum is 0 (@56:44, @57:20)
  - People usually average rather than sum; the training-set loss of the counting model is about 2.4 (2.45 over the whole set) (@57:20, @57:52, @1:00:02)
  - Maximising likelihood, maximising log likelihood and minimising (average) negative log likelihood are equivalent optimisation problems (@58:24, @58:57, @59:29)
  - The model parameters are the probabilities in the table now, but will later be computed by a neural network (@58:24, @58:57)
  - A bigram never seen in training (JQ in "andrejq") has probability 0, log 0 is minus infinity, so the loss is infinite (@1:00:35, @1:01:09)
  - For the neural net the loss is the average negative log likelihood because this is classification, not regression; it is computed by indexing `probs[torch.arange(5), ys]`, taking log, mean, and negating, and matches the hand-computed 3.76 (@1:35:40, @1:37:22, @1:37:56)

### topic: model-smoothing-and-regularization
- existing: no
- aliases: model smoothing, label smoothing, add-one smoothing, regularization, regularization loss, L2 regularization
- statements:
  - Model smoothing adds fake counts (e.g. 1) to every entry before normalising so no probability is zero; more added counts give a more uniform model, fewer a more peaked one (@1:01:43, @1:02:16)
  - After smoothing JQ gets a very small but nonzero probability, and the loss is no longer infinite (@1:02:16, @1:02:49)
  - Adding a huge count (he says a million) pushes every row toward the uniform distribution (@1:50:40)
  - In the gradient framework, W all zeros gives logits all zero, counts all one, probabilities exactly uniform, so pushing W toward zero is equivalent to smoothing (@1:51:13, @1:51:45)
  - Regularization augments the loss with a term such as `(W**2).mean()` times a strength like 0.01; it is zero only when W is zero, acting like a spring or gravity force (@1:51:45, @1:52:19, @1:52:52, @1:53:26)
  - The regularization strength controls the same thing as the number of added counts; strong enough and predictions become uniform (@1:53:26, @1:54:00)

### topic: one-hot-encoding
- existing: no
- aliases: one-hot, F.one_hot
- statements:
  - Integer indices cannot simply be plugged into neurons, whose weights act multiplicatively on inputs (@1:10:02)
  - One-hot encoding turns an integer like 13 into a vector of zeros with a 1 at position 13 (@1:10:35)
  - `torch.nn.functional.one_hot` takes integer tensors and `num_classes`; passing 27 explicitly avoids it guessing too small a size (@1:11:07, @1:11:40)
  - Its output is int64 and it has no dtype argument, so he casts to float, since neural nets want floating-point inputs (@1:12:44, @1:13:18)
  - Multiplying a one-hot vector by W plucks out one row of W, which is the same lookup the counting model did (@1:47:52, @1:48:25, @1:48:58)

### topic: softmax
- existing: no
- aliases: logits, log counts, exponentiate and normalise
- statements:
  - A single linear layer of 27 neurons on 27 one-hot inputs (`xenc @ W`, no bias, no nonlinearity) is the whole network (@1:16:08, @1:18:26, @1:19:01)
  - Raw outputs are positive and negative, so they cannot be probabilities (positive, sum to one) or counts (positive integers) (@1:19:33, @1:20:06)
  - He interprets the outputs as log counts, also called logits; exponentiating gives positive count-like numbers, normalising rows gives probabilities (@1:20:38, @1:21:44, @1:22:56, @1:23:28)
  - The exponentiate-and-normalise steps are the softmax, a layer that turns any linear layer's outputs into a probability distribution (@1:27:22, @1:27:56)
  - Every step (multiply, add, exp, sum, divide) is differentiable, so the whole forward pass can be backpropagated through (@1:24:35, @1:28:29)

### topic: gradient-based-optimization
- existing: no
- aliases: gradient descent, backpropagation in PyTorch, training loop
- statements:
  - Matrix multiplication evaluates all neurons on all examples in parallel; element (3,13) is the dot product of input 3 with column 13 of W (@1:15:34, @1:17:16, @1:17:50)
  - The loop mirrors micrograd: forward pass, loss, zero the gradients, `loss.backward()`, nudge parameters against the gradient (@1:33:26, @1:34:33, @1:35:05)
  - Setting `.grad` to None is a more efficient way to zero it; W needs `requires_grad=True` (@1:38:29, @1:39:03)
  - PyTorch builds the computational graph during the forward pass, and `backward` fills in `W.grad`; a positive gradient means increasing that weight increases the loss (@1:39:36, @1:40:09, @1:40:43)
  - Update `W.data += -0.1 * W.grad`; loss falls 3.76 → 3.74 → 3.72 (@1:41:15, @1:42:21)
  - Scaling from 5 to 228,000 bigrams needs no code change; a much larger learning rate (even 50) works on this simple problem, reaching about 2.47 (@1:43:27, @1:44:00, @1:44:36)

### topic: pytorch-tensor-basics
- existing: no
- aliases: torch.tensor vs torch.Tensor, dtype, tensor indexing
- statements:
  - `torch.zeros((3,5))` defaults to float32; counts use `dtype=torch.int32`; indexing is zero-based `a[1,3]` (@13:48, @14:20)
  - Indexing a tensor returns a tensor; `.item()` pops out the Python number (@20:23, @30:18)
  - `N[0, :]` and `N[0]` both grab a row (@24:48, @25:21)
  - `torch.tensor` infers dtype while `torch.Tensor` returns a float tensor; he recommends the lowercase one and says the docs are unclear (@1:07:47, @1:08:55, @1:09:28)
  - He wants viewers to get used to reading documentation and Q&A threads because some of this is not well documented (@1:09:28)
  - `torch.randn` draws from a normal distribution; most values near zero, few above 3 in magnitude (@1:13:53, @1:14:27)

### claim: counting-and-gradient-bigram-models-are-the-same-model
- existing: no
- title: The counting bigram model and the one-layer neural net are the same model
- confidence: stated
- quote: "So logits literally becomes the uh the the appropriate row of W." (@1:48:58)
- statements:
  - Casting the bigram model as a neural net ends up in a very similar position by a very different route (@1:03:22, @1:03:55)
  - Gradient training on all bigrams reaches roughly 2.45–2.47, the same vicinity as counting, because no extra information is used (@1:44:36, @1:45:08)
  - The explicit counting approach happens to optimise the loss very well without gradients because the bigram setup is so simple (@1:45:39)
  - `W.exp()` is the counts array; counting filled it in directly while gradient descent arrived at it piece by piece following the loss (@1:49:31, @1:50:05)
  - Sampling from the net gives the exact same names as sampling from P (@1:55:39, @1:56:11)
- topic: [[bigram-language-model]]
- relation to existing pages: none in index.

### claim: gradient-based-approach-is-more-flexible-than-counting
- existing: no
- title: The gradient-based approach is more flexible than counting
- confidence: stated
- quote: "But the gradient-based approach is significantly more flexible." (@1:45:39)
- statements:
  - Counting works here only because bigrams are so simple that probabilities can be estimated directly in a table (@1:45:39)
  - The gain is that the approach can be expanded and the neural net complexified with more previous characters (@1:45:39, @1:46:12)
- relation: supports [[bigram-count-tables-do-not-scale-to-longer-contexts]].

### claim: bigram-count-tables-do-not-scale-to-longer-contexts
- existing: no
- title: Count tables do not scale past one character of context
- confidence: stated
- quote: "So this is fundamentally an unscalable approach" (@1:47:19) — clause of a longer sentence; the full sentence continues "and the neural network approach is significantly more scalable"
- statements:
  - It is not obvious how to extend the counting approach to many input characters because the tables get too large for all combinations (@1:46:46, @1:47:19)
  - With the last 10 characters as input you cannot keep everything in a table; the neural approach is more scalable and improvable (@1:47:19)
- relation: supported by [[gradient-based-approach-is-more-flexible-than-counting]].

### claim: weight-regularization-is-equivalent-to-count-smoothing
- existing: no
- title: Pushing weights toward zero is equivalent to count smoothing
- confidence: stated
- quote: "trying to incentivize W to be near zero is basically equivalent to label smoothing." (@1:51:45)
- statements:
  - Zero weights give uniform probabilities, as adding huge counts does (@1:50:40, @1:51:13)
  - The regularization strength controls the amount of counts you add (@1:53:26, @1:54:00)
- topic: [[model-smoothing-and-regularization]]

### claim: treat-broadcasting-with-respect
- existing: no
- title: Broadcasting deserves respect, not fast-and-loose use
- confidence: stated
- quote: "And it's not something to play fast and loose with." (@44:10)
- statements:
  - He strongly encourages reading the broadcasting semantics, practising, and checking the direction of broadcasting, because mistakes produce very subtle, hard-to-find bugs (@44:10, @49:08, @49:40)
- topic: [[broadcasting-semantics]]

### claim: guess-and-check-is-not-how-you-optimize-a-neural-net
- existing: no
- title: Randomly resampling parameters is not how you optimise a neural net
- confidence: stated
- quote: "That's not how you optimize a neural net." (@1:32:20)
- statements:
  - Reseeding W and checking the loss (3.76, 3.37, worse, terrible) is guess and check, which he calls amateur hour (@1:31:15, @1:31:47, @1:32:20)
  - Instead, commit to a random start and minimise the differentiable loss with gradients (@1:32:20, @1:32:54)
- topic: [[gradient-based-optimization]]

### claim: the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers
- existing: no
- title: Only the forward pass changes on the way to transformers
- confidence: stated
- quote: "None of this will fundamentally change." (@1:46:46)
- statements:
  - Future nets will take more previous characters and be more complex, but will still output logits that go through softmax, negative log likelihood and gradient descent (@1:46:12, @1:46:46)
  - The only change is how the forward pass computes logits from previous characters (@1:46:46, @1:57:19)
- topic: [[softmax]]

### method: explicit-baseline-then-neural-net
- existing: no
- aliases: counts first, then neural net
- steps: build the explicit solution by counting; evaluate it with one loss number; recast the problem as a neural net with the same loss; train with gradients; check that loss and samples match
- statements:
  - He first arrives at the model by doing something that felt sensible, counting and normalising, then takes an alternative neural-net approach that should land in a very similar spot (@1:03:22, @1:03:55)
  - The expected loss for the net is whatever counting achieved, about 2.45–2.47, used as the target to confirm the net is right (@1:44:36, @1:45:08)
  - He confirms the equivalence by comparing samples and by showing W.exp() equals the counts (@1:49:31, @1:55:39)
- seen in: [[makemore]]

### method: check-broadcasting-carefully
- existing: no
- aliases: respect broadcasting
- steps: write down both shapes; align from the right and apply the three rules; keep `keepdim=True` when summing for normalisation; verify a row sums to one; check the result against a known answer
- statements:
  - He walks the shapes 27×27 vs 27×1 through the rules before dividing (@42:32, @43:05)
  - He checks `P[0].sum()` equals 1 and that the samples are identical to the earlier loop (@43:37, @44:10)
  - He deliberately removes `keepdim` to show the result is garbage even though broadcasting allows it, and suggests pausing to work out why (@45:15, @46:21, @46:57)
- seen in: [[makemore]]

### method: evaluate-with-a-single-loss-number
- existing: no
- aliases: single-number evaluation, training loss
- steps: assign a probability to every training example; combine into average negative log likelihood; read one number; lower is better; use it as the objective for training
- statements:
  - He wants to summarise the model's quality in a single number, as with micrograd's loss (@50:47)
  - The number is the average negative log likelihood, about 2.45 for the counting model; the job of training is to find parameters that minimise it (@57:52, @1:00:02)
  - The same number lets him compare settings of W (3.76 vs 3.37) and later confirm the net matches counting (@1:31:47, @1:44:36)
- seen in: [[makemore]]; **Note:** related to the existing [[quick-experiment-loop]] (also judged by reading the same loss plots) — a connection across sources, not stated here.

### method: spell-it-out-step-by-step
- existing: no
- aliases: spelled-out lectures
- steps: start from a blank Jupyter notebook; build the simplest version first; spell out every operation; seed randomness so viewers reproduce the numbers; show a bug on purpose and invite a pause to think
- statements:
  - As with micrograd he builds the repo step by step, spelling everything out slowly and together (@00:00)
  - He starts from a completely blank notebook (@02:45)
  - He uses a seeded generator so viewers get exactly the same results on their computer (@26:59, @1:26:13)
  - He invites viewers to pause and think about why the keepdim bug happens before explaining it (@46:57)
  - He cautions viewers about framework APIs and tells them to get used to reading docs and threads (@1:07:47, @1:09:28)
- seen in: [[makemore]]

## Quotes
- "So, under the hood, make more is a character-level language model." (@01:06)
- "It's just um bigram is so terrible, and we have to do better." (@35:58)
- "And I encourage you to treat this with respect." (@44:10)
- "And it's not something to play fast and loose with." (@44:10)
- "This needs to be keepdims equals true in this case." (@49:08)
- "We prefer to use in-place operations if possible." (@49:40)
- "We'd like to somehow summarize the quality of this model into a single number." (@50:47)
- "And the lower it is, the better off we are." (@57:52)
- "I would recommend stick to torch.lower case tensor." (@1:08:55)
- "We always want to be careful with data types." (@1:12:44)
- "So everything here is differentiable operation and we can back propagate through." (@1:28:29)
- "That's not how you optimize a neural net." (@1:32:20)
- "But the gradient-based approach is significantly more flexible." (@1:45:39)
- "None of this will fundamentally change." (@1:46:46)
- "So logits literally becomes the uh the the appropriate row of W." (@1:48:58)
- "trying to incentivize W to be near zero is basically equivalent to label smoothing." (@1:51:45)

## Notes for merge
- Captions in this raw file are mostly punctuated and capitalised (not the usual lowercase stream), except a stretch from about @46:21 to @47:29 which is lowercase and unpunctuated. Quotes above are copied as they appear.
- Caption misspellings: "make more" for makemore throughout; "keep them"/"keep dims" for keepdim (@46:57, @47:29); "S2I"/"S 2 I" for stoi, "I2S"/"I 2 S" for itos; "X inc"/"X_enc" for xenc; "torch.lower case tensor" for torch.tensor; "Andre"/"Andre Q" for andrej/andrejq (@1:00:35); "MP" for np (@1:37:22); "climatic" for climactic (@1:55:39); "label smoothing" at @1:51:45 where he had earlier called the same thing "model smoothing" (@1:01:43) — the claim title uses the smoothing/regularization framing, not "label smoothing".
- The quote at @1:51:45 begins mid-sentence: the raw has "So," at the end of the @1:51:13 block and the rest after the marker.
- The quote for the claim bigram-count-tables-do-not-scale-to-longer-contexts is a clause, not a full sentence; the full sentence is over 15 words. Merge may prefer paraphrase only.
- Mentioned but not explained: micrograd (predecessor repo and lecture, referenced for backprop and the training loop at @00:00, @1:10:02, @1:33:26); bag-of-words models, MLPs, RNNs, transformers, GPT-2, DALL-E, Stable Diffusion (@02:13, @02:45); Matplotlib plotting code (@18:13); mean squared error as micrograd's loss (@1:34:00). None of these are topic candidates from this source.
- Numbers to carry carefully: ~32,000 names (@00:34); 228,000 bigrams (@1:43:27); loss 2.45 unsmoothed over the full set (@1:00:02), 2.47 after smoothing (@1:44:36, stated in retrospect); net reaches about 2.46–2.47 (@1:44:36, @1:45:08); Emma-only loss 3.76 (@1:31:15).
- He says M starts about 2,500 of 32,000 words, "a bit less than 10%" (@30:53); fine as paraphrase.
- No existing index page covers any of these topics; all candidate slugs are new. No `extends`/`contradicts` relations, so no timeline is needed from this source alone. The next makemore videos will likely feed the same topic pages (softmax, NLL, gradient-based-optimization), so keep those slugs general rather than bigram-specific.
- Artifact status for makemore is set to `active` from this 2022 source; a later GitHub README snapshot should decide the real status.
