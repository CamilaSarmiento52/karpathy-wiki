# Digest: Building makemore Part 4: Becoming a Backprop Ninja
- raw: raw/youtube/q8SA3rM6ckI.md · published: 2022-10-11 · medium: youtube · words: 20983
- source slug: youtube-2022-10-11-makemore-4-backprop-ninja

## Source page

```markdown
---
type: source
raw_path: raw/youtube/q8SA3rM6ckI.md
published: 2022-10-11
medium: youtube
summary: He removes loss.backward() from the makemore MLP and hand-derives every gradient at the tensor level, checking each against PyTorch, then collapses cross-entropy and batchnorm backward into closed-form expressions.
url: https://www.youtube.com/watch?v=q8SA3rM6ckI
title: "Building makemore Part 4: Becoming a Backprop Ninja"
---

# Building makemore Part 4: Becoming a Backprop Ninja
Raw: [[raw/youtube/q8SA3rM6ckI]] · Original: https://www.youtube.com/watch?v=q8SA3rM6ckI

## Summary
He pauses the makemore series for one lecture to replace PyTorch's `loss.backward()` with a backward pass written by hand at the level of tensors, because he regards backpropagation as a leaky abstraction that will fail or underperform if you do not understand its internals (@00:31, @01:05). He frames the exercise historically: ten years earlier everyone wrote their backward pass by hand, in MATLAB or numpy, and checked it with a gradient checker (@03:16, @06:41). Exercise one backpropagates through every atomic operation of the two-layer MLP with batchnorm, from log-probabilities back to the embedding table, checking each intermediate gradient against PyTorch with an exact/approximate/max-difference comparison (@07:46, @17:46, @1:26:06). Along the way he teaches the duality between a sum in the forward pass and a broadcast in the backward pass, and his trick of deriving matrix-multiply gradients by making the shapes work out rather than remembering formulas (@50:01, @1:09:12). Exercises two and three derive the gradient of cross-entropy (softmax minus one-hot, scaled by 1/n) and of the whole batchnorm layer analytically on paper (@1:30:32, @1:38:18), and exercise four trains the network with only the manual gradients, reaching the same loss as before (@1:50:31, @1:53:18). He also departs from the batchnorm paper by using the unbiased (n-1) variance and calls PyTorch's train/test variance mismatch a bug (@1:05:16, @1:08:05).

## Key points
- Backprop is a leaky abstraction: stacking differentiable blocks and calling backward does not guarantee things work, and you need the internals to debug (@01:05) → [[backprop-is-a-leaky-abstraction]]
- Frameworks offering autograd is not a reason to ignore how backprop works; micrograd covered only scalars, so this lecture does it on tensors (@02:43) → [[understand-backprop-despite-autograd]]
- Writing a backward pass by hand is no longer recommended outside exercises, but around 2010–2014 it was standard, with numerical gradient checkers (@03:16, @06:41) → [[backpropagation]]
- Small random (not zero) initialisation of biases is used so that zeros do not mask an incorrect gradient (@08:20) → [[check-manual-gradients-against-pytorch]]
- The `cmp` utility reports exact equality, `allclose` approximate equality, and the maximum absolute difference against PyTorch's `.grad` (@17:46, @18:19) → [[check-manual-gradients-against-pytorch]]
- A variable used in several places accumulates gradient by summing; broadcasting is replication plus the operation, so its backward pass is a sum over the replicated dimension (@23:19, @25:34) → [[broadcasting-and-its-backward-pass]]
- Addition routes the incoming gradient equally to all its inputs; a forward sum becomes a backward replication (@30:39, @31:11) → [[broadcasting-and-its-backward-pass]]
- The gradient on the max-subtraction used for softmax stability comes out at roughly 1e-9, reflecting that it does not affect the loss (@36:44, @37:17) → [[backpropagation]]
- The backward pass of a matrix multiply is a matrix multiply with the other operand transposed; the bias gradient is a sum over examples (@48:57, @49:29) → [[backpropagation]]
- He does not remember the matmul backward formulas; the shapes admit only one valid arrangement, and that is the correct one (@50:01, @50:37) → [[derive-gradients-by-shape-matching]]
- Deriving a gradient: write out a tiny concrete example on paper, differentiate the multiplies and adds, then generalise the pattern (@42:50, @43:23) → [[derive-gradients-by-shape-matching]]
- Duality: a sum in the forward pass becomes a replication/broadcast in the backward pass along the same dimension, and vice versa (@1:09:12, @1:09:47) → [[broadcasting-and-its-backward-pass]]
- Batchnorm paper uses biased 1/n variance in training and unbiased 1/(n-1) at inference; he treats this train/test mismatch as a bug and uses n-1 throughout (@1:05:49, @1:08:05) → [[batchnorm-train-test-variance-mismatch-is-a-bug]], [[batch-normalization]]
- The gradient of cross-entropy with respect to logits is the softmax probabilities with 1 subtracted at the correct label, divided by n (@1:30:32, @1:31:36) → [[cross-entropy-gradient]]
- Each row of that gradient sums to zero and acts like a force pulling the correct probability up and incorrect ones down, proportional to how wrong the prediction is (@1:33:50, @1:35:31) → [[cross-entropy-gradient]]
- Batchnorm backward derived analytically on paper in the order x-hat, sigma-squared, mu, x; the d(sigma^2)/d(mu) term vanishes because mu is the mean (@1:39:25, @1:43:17) → [[batchnorm-backward-pass]]
- The final batchnorm backward is one line of code that must also broadcast across 64 neurons, which he calls highly non-trivial (@1:48:50, @1:49:24) → [[batchnorm-backward-pass]]
- The MLP trains to the same loss with about 20 lines of manual backward code and no autograd (@1:51:04, @1:53:18) → [[makemore]]

## Fed pages
- [[backpropagation]]
- [[broadcasting-and-its-backward-pass]]
- [[cross-entropy-gradient]]
- [[batchnorm-backward-pass]]
- [[batch-normalization]]
- [[backprop-is-a-leaky-abstraction]]
- [[understand-backprop-despite-autograd]]
- [[batchnorm-train-test-variance-mismatch-is-a-bug]]
- [[makemore]]
- [[micrograd]]
- [[derive-gradients-by-shape-matching]]
- [[check-manual-gradients-against-pytorch]]
```

## Candidates

### topic: backpropagation
- existing: no
- aliases: backprop, backward pass, manual backpropagation, tensor-level backprop
- statements:
  - He wants to remove `loss.backward()` and write the backward pass manually at the level of tensors (@00:31).
  - He has a blog post on backprop as a leaky abstraction; examples of what goes wrong include saturated tanh tails killing gradients, dead neurons, and exploding or vanishing gradients in RNNs (@00:31, @01:37).
  - A code snippet from the wild tried to clip the loss when the author meant to clip gradients, which silently zeroed outlier gradients; he reads this as the author not understanding backprop (@02:11).
  - micrograd was an autograd engine at the level of individual scalars, which he does not think is enough (@02:43).
  - He says the exercise makes you better at debugging neural networks and makes everything fully explicit (@03:16).
  - Writing the backward pass by hand is not recommended today and nobody does it except as an exercise, but about ten years earlier it was standard and pervasive, including for him (@03:16, @03:49).
  - His 2010 RBM library was in MATLAB and used contrastive divergence; his 2014 fragment-embeddings code in numpy implemented the cost and backward pass by hand and used a gradient checker (@04:26, @05:34, @06:08, @06:41).
  - In the backward pass each tensor gets a `d`-prefixed counterpart holding the derivative of the loss with respect to it, always of the same shape (@09:58, @13:13).
  - The gradient of the mean-of-negative-log-probs loss is -1/n at the plucked-out positions and zero everywhere else (@15:35, @16:07).
  - Backprop through log multiplies by 1/probs, which boosts the gradient of examples currently assigned low probability (@19:27, @20:31).
  - He uses `**-1` instead of division because he found something wrong with PyTorch's backward for division (@21:38).
  - A node used in two branches of the graph receives the sum of both contributions, implemented with `+=`, and an intermediate check is expected to fail until the second branch is done (@27:18, @31:45, @1:03:34).
  - Subtracting the per-row max for softmax stability does not change the loss, so its gradient should be zero; it comes out at about 1e-9 due to floating point (@36:44, @37:17).
  - `max` returns indices as well as values; the backward pass scatters the gradient to those indices, which he implements with `F.one_hot` (@38:55, @40:03).
  - Written out on paper, a 2x2 matmul-plus-bias is just multiplies and adds; dL/dA = dL/dD @ B^T, dL/dB = A^T @ dL/dD, and dL/dC is a sum over columns (@44:29, @47:49, @48:22, @48:57).
  - The backward of tanh is 1 minus the output squared, expressed in terms of the output not the input (@54:03, @54:35).
  - The backward of `view` is just re-viewing the gradient into the original shape (@1:21:06).
  - The backward of embedding lookup routes each gradient row back into the row of C it came from, adding when a row was used several times; he uses a Python for-loop and invites a vectorised version (@1:23:52, @1:24:24).
  - Training with the manual gradients gives the same loss and samples as before, with full visibility into what happens under the hood (@1:50:31, @1:53:18).
  - He says that in practice you probably do not want to derive these yourself and should use PyTorch's autograd, but should have the intuition (@1:54:25).

### topic: broadcasting-and-its-backward-pass
- existing: no
- aliases: broadcasting, sum-broadcast duality, variable reuse in backprop
- statements:
  - A broadcasted multiply like `counts * counts_sum_inv` is really two operations: replication of the column across 27 columns, then the element-wise multiply (@23:19, @23:54).
  - Replication means one variable is reused many times, so, as in micrograd, the gradients from all uses sum; the backward pass is a `sum(1, keepdim=True)` so the gradient keeps the variable's shape (@25:02, @25:34, @26:07).
  - Addition is a router of gradient: whatever gradient arrives is routed equally to every element that participated (@30:39).
  - A forward `sum` over rows becomes a backward replication, which he implements as `torch.ones_like(counts) * dcounts_sum` to let broadcasting do the replication (@31:11, @31:45).
  - A bias vector of 27 is padded to a row vector and replicated vertically 32 times in the forward pass, so its gradient is a sum over dimension 0 (@42:18, @52:17).
  - Batchnorm gain and bias are 1x64 while the activations are 32x64, so their gradients need a sum over the examples with `keepdim=True` (@55:43, @56:49, @57:21).
  - He states the duality explicitly: a sum in the forward pass turns into replication or broadcasting in the backward pass along the same dimension, and a broadcast in the forward pass indicates variable reuse and turns into a sum over that dimension (@1:09:12, @1:09:47).
  - Shapes alone hint at the backward structure: seeing a 32x64 reduced to 1x64 tells him there will be a broadcast in the backward pass (@1:09:12, @1:14:15).

### topic: cross-entropy-gradient
- existing: no
- aliases: dlogits, gradient of cross-entropy, softmax backward, push and pull
- statements:
  - Exercise one backpropagated through far too many atomic pieces; if you differentiate the mathematical expression for the loss on paper, many terms cancel and the result is much shorter and faster to implement (@1:26:39, @1:27:11).
  - PyTorch glues the whole thing into `F.cross_entropy`, which gives the same loss and is faster in both forward and backward (@1:27:11).
  - For one example the loss is -log of the softmax probability at the label; differentiating with respect to logit i splits into the case i equals the label and i does not (@1:28:50, @1:30:32).
  - The result is p_i, or p_i - 1 at the label; in a batch this is softmax of the logits, minus 1 at the label column, divided by n for the mean (@1:30:32, @1:31:36, @1:32:09).
  - This matches PyTorch to about 5e-9, approximate rather than bitwise equality (@1:32:09).
  - Visualised, dlogits is the probability matrix with the correct positions reduced by 1; each row sums to zero (@1:32:44, @1:33:50).
  - He reads each gradient cell as a force: pulling down the probabilities of incorrect characters and pulling up the correct one, with push and pull exactly balanced (@1:33:50, @1:34:24).
  - He pictures the network as a pulley system where tension at the logits translates into tugs on the weights and biases; parameters slowly give in to the tug (@1:34:24, @1:34:57).
  - The force is proportional to the probabilities from the forward pass: a perfectly correct prediction gives a row of zeros and no push or pull, a confidently wrong one gets pulled down heavily (@1:35:31, @1:36:04).

### topic: batchnorm-backward-pass
- existing: no
- aliases: batch normalization backward, analytic batchnorm gradient
- statements:
  - Exercise one breaks batchnorm into mean, diff, diff squared, variance, inverse std and raw pieces and backpropagates through each line, using the power rule for the -0.5 exponent (@59:38, @1:00:11, @1:04:07).
  - bndiff feeds two branches (through bnraw and through the variance), so its gradient is incomplete and fails the check until the second branch is added (@1:03:34, @1:13:39).
  - Likewise hprebn receives gradient both directly and via the mean, and the direct-only check is expected to be wrong (@1:16:31, @1:17:03).
  - Exercise three treats batchnorm as one glued expression and derives dhprebn from dhpreact on two sheets of paper, ignoring gamma and beta because their gradients are simple (@1:36:36, @1:37:42, @1:38:18).
  - He warns that x, x-hat and y are vectors of many nodes while mu and sigma-squared are single scalars, and recommends backpropagating in the order x-hat, sigma-squared, mu, x like a topological sort (@1:38:50, @1:39:25).
  - Because sigma-squared fans out into all the x-hats, dL/dsigma-squared is a sum over i of the global times local gradient (@1:41:03, @1:41:36).
  - mu has 32 arrows to the x-hats plus one to sigma-squared; the d(sigma-squared)/d(mu) term vanishes exactly when mu is the mean of the x's, which cancels the whole second term (@1:42:09, @1:43:17).
  - Each x_i has three arrows (to mu, sigma-squared and its own x-hat); the final chain-rule sum requires renaming the summation index from i to j to avoid clashing with the x_i being differentiated (@1:44:23, @1:46:37).
  - Terms refactor so that (sigma-squared + eps)^(-3/2) splits into three factors and some terms collapse into x-hats, leaving an expression that uses only dL/dy and the x-hats from the forward pass (@1:47:11, @1:47:45, @1:48:17).
  - The one-line implementation matches PyTorch with a tiny max diff, but writing it was not trivial because the per-neuron formula must run in parallel over all 64 columns and every sum must broadcast correctly (@1:48:17, @1:48:50, @1:49:24).
  - He calls the batchnorm backward pass the notable exception to the rest of the backward pass being about three lines per layer (@1:53:52).

### topic: batch-normalization
- existing: no
- aliases: batchnorm, BatchNorm1d, Bessel's correction in batchnorm
- statements:
  - The lecture normalises the variance by 1/(n-1) rather than the paper's 1/m, deliberately, which is Bessel's correction (@1:00:11, @1:00:43, @1:05:16).
  - He says the paper uses the biased 1/n estimate during training but the unbiased n-1 estimate when calibrating running statistics for inference, which he finds extremely confusing (@1:05:49, @1:06:22).
  - He says 1/n almost always underestimates the variance, matters when samples are small as with mini-batches, and the unbiased version is advised (@1:06:22, @1:06:57).
  - `torch.var` takes an `unbiased` flag whose default he believes is true but which the docs do not state; the BatchNorm1d docs say biased but the implementation uses the unbiased version for the running std, which others have flagged in issues (@1:06:57, @1:07:31).
  - BatchNorm does not take a keyword to choose the variance estimator consistently in train and test, so in his view anyone using it has a bit of a bug; this matters less with larger batch sizes (@1:08:05, @1:08:38).
  - Note: this source covers only the variance-estimator issue and the backward derivation; the layer itself is explained in the previous makemore lecture (not yet in the wiki). If a batch-normalization topic exists by merge time, add these as sources; otherwise this page may be thin and could be folded into [[batchnorm-backward-pass]] with the claim below.

### claim: backprop-is-a-leaky-abstraction
- existing: no
- title: Backpropagation is a leaky abstraction that will fail silently if you do not understand it
- confidence: stated
- quote: "I'd like to call back propagation a leaky abstraction" (@00:31)
- statements:
  - Backprop does not make neural networks work magically; you cannot stack arbitrary differentiable Lego blocks and cross your fingers (@01:05).
  - If you do not understand its internals it will not work or not work optimally, and you need the internals to debug it (@01:05).
  - Examples he has covered: saturating nonlinearities killing gradients, dead neurons, exploding or vanishing gradients in RNNs, and a loss-clipping bug found in a random codebase (@01:37, @02:11).
  - He has a blog post on this topic (not named in captions; "a while ago") (@00:31, @01:37).
- relation: supports [[understand-backprop-despite-autograd]] (the leak is the reason to understand it).

### claim: understand-backprop-despite-autograd
- existing: no
- title: Autograd being available is not a reason to ignore how backprop works
- confidence: stated
- quote: "now everyone just calls lost that backward uh we've lost something" (@03:49)
- statements:
  - He does not think it is okay to ignore how backprop works because PyTorch or other frameworks offer autograd (@02:43).
  - The exercise makes you better at debugging, makes everything explicit, and leaves you stronger (@03:16).
  - He acknowledges that writing a backward pass by hand is not recommended today and nobody does it outside exercises (@03:16).
  - In practice you probably do not want to derive gradients yourself and should use PyTorch autograd, but should have the intuition for how gradients flow (@1:54:25).
- relation: supported by [[backprop-is-a-leaky-abstraction]].
- Note: the inverted phrase "it is okay for us to ignore how it works" (@02:43) is in the raw as part of "I don't think it's the case that ... it is okay"; do not quote it alone.

### claim: batchnorm-train-test-variance-mismatch-is-a-bug
- existing: no
- title: Using the biased variance in training and the unbiased one at test time is a bug in batchnorm
- confidence: stated
- quote: "I basically consider this to be a bug" (@1:08:05)
- statements:
  - The batchnorm paper trains with the 1/n variance and calibrates running variance with 1/(n-1); PyTorch follows the paper (@1:05:49, @1:07:31).
  - He is not a fan of train/test discrepancies, sees no good reason given in the paper, and prefers Bessel's correction consistently in his own work (@1:07:31, @1:08:05, @1:08:38).
  - In his view anyone using batch normalization has a bit of a bug in the code, less of a problem with larger mini-batches (@1:08:05, @1:08:38).
  - He hedges: "maybe someone can explain why this is okay" (@1:08:38).
- relation: none existing. topic: [[batch-normalization]].

### artifact: makemore
- existing: no
- aliases: make more
- statements:
  - makemore is the character-level name model built across the lecture series; this lecture continues the two-layer MLP with batchnorm from the previous one (@00:00, @07:13).
  - The notebook for this lecture is on GitHub and Google Colab; he recommends attempting each gradient yourself before watching him (@12:10, @12:41).
  - Starter code expands the forward pass into many intermediate tensors and retains their grads so each manual gradient can be checked (@09:26, @09:58).
  - Exercise four trains the MLP with only manual gradients, `torch.no_grad`, and a zip of parameters and gradients for the update, reaching a similar loss and name-like samples (@1:52:13, @1:52:46, @1:53:18).
  - The next lecture moves to RNNs and LSTMs (@1:54:58).
- Note: repo_url, language and status are not in this source; merge should fill them from a GitHub raw if one exists (`karpathy/makemore`, Python) or leave a placeholder.

### artifact: micrograd
- existing: no
- aliases: micrograd
- statements:
  - micrograd was an autograd engine only at the level of individual scalars, which he does not think is enough on its own (@02:43).
  - He refers back to micrograd for the rule that gradients from multiple uses of a node sum, for the tanh backward, and for topological-order backprop (@25:02, @53:30, @1:39:25).
- Note: mentioned as prior work, not explained here. Use as `context` only unless a micrograd source exists.

### method: derive-gradients-by-shape-matching
- existing: no
- aliases: shape matching, make the shapes work out, toy-example derivation
- statements:
  - Before each line he scrutinises the shapes of every tensor involved and writes them out (@22:12, @1:08:38, @1:18:48).
  - He picks a small concrete example (2x2 or 3x3), writes out the operation element by element, differentiates the multiplies and adds as in micrograd, and generalises the pattern (@14:26, @42:50, @43:23, @45:02).
  - He never remembers the matmul backward formulas; dX must have the shape of X and must be a matmul of the incoming gradient and the other operand, with a transpose placed so the shapes work out, and there is only one way to do that (@49:29, @50:01, @50:37, @51:44).
  - For a bias, the shape tells him which axis to sum over (@52:17, @52:54).
  - A reduction in the forward shape signals a broadcast in the backward, and vice versa (@1:09:12, @1:09:47).
  - For a glued expression (batchnorm) he does the same on paper with symbols: draw the compute graph, mark which nodes are vectors and which scalars, and backprop in topological order (@1:38:50, @1:39:25).
- steps (proposed): check and write out the shapes; write out a tiny concrete example; differentiate the multiplies and adds; arrange the result so the gradient has the variable's shape (transpose or sum as needed); sum where a variable was replicated; verify against PyTorch.

### method: check-manual-gradients-against-pytorch
- existing: no
- aliases: cmp, gradient checking
- statements:
  - A `cmp` utility compares the manual gradient to `tensor.grad`: exact equality, `torch.allclose` for floating-point wiggle, and the maximum absolute difference (@07:46, @17:46, @18:19).
  - He initialises biases to small random numbers rather than zero because zeros can mask an incorrect gradient implementation (@07:46, @08:20).
  - He keeps a bias before batchnorm, although unnecessary, to have one more gradient to check (@08:52).
  - He breaks the forward pass into many intermediate tensors and calls `retain_grad` on them so every intermediate gradient is checkable (@09:26, @09:58).
  - An expected failure on a half-finished branch shows the checker can detect wrong gradients and does not just say yes (@1:03:34, @1:16:31).
  - Analytic shortcuts (cross-entropy, batchnorm) match only approximately, at about 5e-9 or 1e-9, and he does not know exactly where the differences come from (@1:32:09, @1:51:37).
  - In the full training loop he runs 100 iterations and breaks to check gradients against PyTorch before disabling autograd (@1:51:04, @1:51:37).
  - Historically the equivalent was a numerical gradient checker against the hand-written backward pass (@06:41).
- steps (proposed): expand the forward pass into intermediates and retain their grads; initialise with small non-zero values; write each manual gradient; compare exact, approximate and max difference to PyTorch; expect failures on unfinished branches; only then remove `loss.backward()`.

## Quotes
- "I'd like to call back propagation a leaky abstraction" (@00:31)
- "things don't just work automatically it is a leaky abstraction" (@01:05)
- "you're going to become better at debugging neural networks" (@03:16)
- "writing your backward pass by hand and manually is not recommended" (@03:16)
- "now everyone just calls lost that backward uh we've lost something" (@03:49)
- "I'm trying to unmask those potential errors in these calculations" (@08:20)
- "I always like to work with simpler examples" (@14:26)
- "an addition is a router of gradient" (@30:39)
- "the backward Paths of a matrix multiply is a matrix multiply" (@48:57)
- "the reason this works is because the dimensions have to work out" (@50:01)
- "there is only a single way to make the shape work out" (@50:37)
- "it can in fact detect when your gradient is not correct" (@1:03:34)
- "I basically consider this to be a bug" (@1:08:05)
- "I like to scrutinize the shapes first" (@1:08:38)
- "anytime you have a sum in the forward pass that turns into a replication" (@1:09:12)
- "you should think of these uh gradients here at each cell as like a force" (@1:33:50)
- "that's basically the magic of the cross-entropy loss" (@1:36:04)
- "it's just that we have full visibility on exactly what goes on under the hood" (@1:50:31)
- "we don't need it anymore it feels amazing" (@1:51:37)

## Notes for merge
- Caption misspellings: "lost that backward" / "lost up backward" / "lost of backward" = loss.backward(); "make more" = makemore; "montalia perceptrons" / "multilio perceptron" = multilayer perceptron; "lock props" / "log probs" / "block probes" = logprobs; "bathroom" / "bachelor" / "bastionalization" / "pastoralization" = batchnorm / batch normalization; "bezels correction" = Bessel's correction; "deluggets" / "deloaches" / "delojits" = dlogits; "from alpha" = Wolfram Alpha; "Russell selectinov" = Ruslan Salakhutdinov; "restricted bolstery machines" = restricted Boltzmann machines; "Patrick's" / "pythonograd" = PyTorch's / PyTorch autograd; "MCAT" = embcat; "hpbn" / "hpvn" = hprebn; "doji's" = Doges (the buff Doge meme at the end).
- The "lost that backward" quote at @03:49 carries a caption error; a reviewer may prefer paraphrase, but the raw string is exact.
- The leaky-abstraction blog post is referenced but not named in captions (it is his 2016 Medium post "Yes you should understand backprop"; the captions do not say so, so do not cite the title to this source).
- Only mentioned, not explained: RNNs/LSTMs (next lecture), his 2006 Hinton/Salakhutdinov RBM reference, his 2014 fragment-embeddings paper, CLIP, contrastive divergence, `torch.no_grad`. The leaky-abstraction examples (saturated tanh, dead neurons, vanishing gradients) are listed as previously covered, not re-explained.
- The previous makemore lecture (Part 3, batchnorm) and micrograd lecture are referenced throughout; neither has a source page yet. If they are ingested later, [[batch-normalization]] and [[micrograd]] gain their primary sources there.
- Audio timestamps: several sentences straddle a marker boundary (e.g. "I'm not a fan of trained test / discrepancies" at 1:07:31–1:08:05; "anyone using batch normalization basically in / my view has a bit of a bug" at 1:08:05–1:08:38). Quotes above were chosen to sit inside a single block.
- His hedges to preserve: "I believe unbiased by default is true I'm not sure" (@1:06:57); "maybe someone can explain why this is okay" (@1:08:38); "I don't exactly know where they're coming from" about ~1e-9 gradient differences (@1:51:37); "maybe someone has a better way" about the embedding for-loop (@1:24:24).
- Possible new claim not proposed as a page: "the backward pass of a matmul is a matmul" (@48:57) is kept as a statement in [[backpropagation]] since it is a derivation result rather than a position.
