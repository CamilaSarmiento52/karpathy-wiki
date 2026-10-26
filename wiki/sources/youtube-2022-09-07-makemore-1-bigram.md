---
type: source
raw_path: raw/youtube/PaCmpygFfXo.md
published: 2022-09-07
medium: youtube
summary: "First makemore lecture: a bigram character-level language model built twice, once by counting and normalising, once as a one-layer neural net trained on negative log likelihood, ending in the same model."
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
- Sampling: take the row for the current character, normalise, draw with `torch.multinomial` under a seeded generator, stop at `.`; a uniform model shows the bigram samples are at least better than nothing (@25:21, @26:59, @32:02, @35:24) → [[character-level-language-modeling]]
- Broadcasting rules: align shapes from the right; each dimension must be equal, one, or missing; `keepdim=False` turns a 27×1 column into a 1×27 row and normalises the wrong axis (@42:01, @46:21, @47:29, @48:36) → [[broadcasting]], [[check-shapes-and-broadcasting]], [[treat-broadcasting-with-respect]]
- Model quality is summarised as one number: likelihood → log likelihood → negative log likelihood → average, giving about 2.45 on the training set (@50:47, @53:27, @57:52, @1:00:02) → [[loss-functions]]
- Unseen bigrams give infinite loss; adding fake counts (model smoothing) removes the zeros and makes the model more uniform (@1:00:35, @1:01:43, @1:02:16) → [[regularization]]
- Integers cannot be fed into neurons, so inputs are one-hot encoded and cast to float (@1:10:02, @1:10:35, @1:13:18) → [[softmax]]
- Prefer `torch.tensor` to `torch.Tensor`, and expect to read documentation and threads because frameworks are not always well documented (@1:07:47, @1:08:55, @1:09:28) → [[pytorch]]
- The 27 outputs are interpreted as log counts (logits); exponentiate to get counts, normalise rows to get probabilities; the last two steps are the softmax (@1:20:38, @1:22:56, @1:27:22) → [[softmax]]
- Every step of the forward pass is differentiable, and PyTorch builds the graph during the forward pass so `backward` fills `W.grad` (@1:28:29, @1:39:36) → [[backpropagation]]
- Resampling W by hand and checking loss is "amateur hour"; the loss is differentiable, so use gradients: zero grad, `loss.backward()`, nudge W against the gradient (@1:32:20, @1:32:54, @1:38:29, @1:41:15) → [[gradient-descent]]
- Trained on all 228,000 bigrams the net reaches about 2.46, the same vicinity as counting; a one-hot vector times W plucks out a row of W, so `W.exp()` is the counts array; sampling gives exactly the same names (@1:44:36, @1:48:58, @1:55:39) → [[counting-and-gradient-bigram-models-are-the-same-model]]
- The gradient approach is more flexible and scalable; tables blow up with more context characters (@1:45:39, @1:46:46, @1:47:19) → [[gradient-based-models-scale-where-count-tables-do-not]]
- Pushing W toward zero (a squared-weight regularization term) is equivalent to smoothing; its strength plays the role of the added count (@1:51:13, @1:51:45, @1:52:52, @1:53:26) → [[regularization]], [[weight-regularization-is-equivalent-to-count-smoothing]]
- Only the forward pass will change on the way to transformers; logits, softmax, NLL and gradient descent stay (@1:46:12, @1:46:46, @1:57:19) → [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers]]
- Teaching method: a blank notebook, spell everything out, seeded generators so viewers reproduce his numbers, build the explicit version first and then the neural-net version; he points back to micrograd for backprop and the training loop (@00:00, @02:45, @26:59, @1:03:22, @1:33:26) → [[spelled-out-build-from-scratch]], [[micrograd]]

## Fed pages
- [[makemore]]
- [[character-level-language-modeling]]
- [[bigram-language-model]]
- [[broadcasting]]
- [[loss-functions]]
- [[regularization]]
- [[softmax]]
- [[gradient-descent]]
- [[backpropagation]]
- [[pytorch]]
- [[micrograd]]
- [[counting-and-gradient-bigram-models-are-the-same-model]]
- [[gradient-based-models-scale-where-count-tables-do-not]]
- [[weight-regularization-is-equivalent-to-count-smoothing]]
- [[treat-broadcasting-with-respect]]
- [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers]]
- [[spelled-out-build-from-scratch]]
- [[check-shapes-and-broadcasting]]
- [[how-he-explains]]
- [[be-careful-with-shapes-and-be-explicit]]
- [[show-the-instructive-bug-failing-then-explain-it]]
