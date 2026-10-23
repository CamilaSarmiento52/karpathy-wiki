# Verification: batch 1, group A1 (micrograd, makemore 1, makemore 2)
Verified 2026-10-23 by a fresh reader. Sources: [[youtube-2022-08-16-micrograd]], [[youtube-2022-09-07-makemore-1-bigram]], [[youtube-2022-09-12-makemore-2-mlp]]

## Coverage
- pages checked: 35 (3 source pages; claims: [[a-buggy-neural-net-can-still-train-on-a-simple-problem]], [[approximate-gradient-with-more-steps-beats-exact-gradient]], [[backpropagation-is-more-general-than-neural-networks]], [[counting-and-gradient-bigram-models-are-the-same-model]], [[forgetting-to-zero-grad-is-a-common-neural-net-bug]], [[gradient-based-models-scale-where-count-tables-do-not]], [[micrograd-is-all-you-need-everything-else-is-efficiency]], [[neural-networks-are-just-mathematical-expressions]], [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers]], [[treat-broadcasting-with-respect]], [[use-cross-entropy-not-a-hand-rolled-loss]], [[weight-regularization-is-equivalent-to-count-smoothing]]; topics: [[backpropagation]], [[multilayer-perceptron]], [[activation-functions]], [[loss-functions]], [[gradient-descent]], [[pytorch]], [[bigram-language-model]], [[character-level-language-modeling]], [[broadcasting]], [[regularization]], [[softmax]], [[embeddings]], [[overfitting-and-generalization]]; methods: [[spelled-out-build-from-scratch]], [[verify-gradients-against-pytorch]], [[check-shapes-and-broadcasting]], [[learning-rate-sweep]], [[diagnose-under-or-overfitting]]; artifacts: [[micrograd]], [[makemore]]), claim pages fully checked: 12, other sentences checked: ~100 of ~350 (every quote grepped verbatim; every claim Context/Related sentence read against its block; in topics/methods/artifacts/source pages I checked the sentences carrying numbers, quotes, comparisons or attributions of opinion, reading the cited block and its neighbours in the raw)

Method note: all 12 claim quotes are verbatim in the raw file at the cited block and are his own words (no paper or other speaker is quoted in these three lectures). All 12 `confidence: stated` values are justified. No claim title is stronger than the cited passage. Caption garble ("10h", "storage.org that function", "pi torch") was corrected only outside quotes. No sentence citing these sources attributes a paper's claim to him: the Bengio 2003 description in [[embeddings]] and [[multilayer-perceptron]] is framed as the paper's model. The **Note:** sentences on [[micrograd]] and [[makemore]] (nanogpt/nanochat connections) are real editorial connections and say so.

## Findings
### F1 — overstated — [[youtube-2022-08-16-micrograd]]
- sentence: "Production libraries like PyTorch are meant to be used, not inspected: it took him 15 minutes to find the tanh backward kernel (@2:21:33, @2:22:07)"
- cited: [[youtube-2022-08-16-micrograd]] @2:21:33
- raw says: he spent about 15 minutes and "couldn't find" tanh; he eventually stumbled on a thread where someone pointed to the CPU and CUDA kernels. The 15 minutes is the time he failed, not the time to success.
- fix: "Production libraries like PyTorch are meant to be used, not inspected: he spent about 15 minutes searching PyTorch for tanh's backward without finding it, and only reached the kernel through a pointer in a thread (@2:21:33, @2:22:07)". (The same fact is stated correctly on [[micrograd-is-all-you-need-everything-else-is-efficiency]] and [[pytorch]].)

### F2 — overstated — [[youtube-2022-09-12-makemore-2-mlp]]
- sentence: "Overfit a single small batch first to check the training loop; loss cannot reach zero where one context has several labels (@39:23, @40:28)"
- cited: [[youtube-2022-09-12-makemore-2-mlp]] @39:23
- raw says: he develops on the first five words "just for efficiency while we are developing all the code" (@10:02) and then observes that the very low loss is "because we're only overfitting 32 examples ... we're doing what's called overfitting a single batch of the data". He never says he did it to check the training loop; the purpose he states is efficiency, the overfitting is an observation.
- fix: "Developing on 32 examples, he gets a very low loss and names it overfitting a single batch; loss cannot reach zero where one context has several labels (@39:23, @40:28)"

### F3 — overstated — [[diagnose-under-or-overfitting]]
- sentence: "How he reads whether a model is too small or memorising: first check the training loop by overfitting a handful of examples, then compare the loss on the train and dev splits ([[youtube-2022-09-12-makemore-2-mlp]] @39:23, @1:00:20)."
- cited: [[youtube-2022-09-12-makemore-2-mlp]] @39:23
- raw says: same as F2; the "check the training loop" purpose is not in the source. Step 1 of the same page ("for efficiency", @10:02) has it right, and the `steps` entry "Overfit a handful of examples first" is acceptable; only the definition sentence and the alias "sanity-check the training loop" go beyond him.
- fix: "How he reads whether a model is too small or memorising: note that a few dozen examples are overfit to a very low loss, then compare the loss on the train and dev splits ([[youtube-2022-09-12-makemore-2-mlp]] @39:23, @1:00:20)." Drop the alias "sanity-check the training loop" or keep it only if a later source states the purpose.

### F4 — mis-cited — [[weight-regularization-is-equivalent-to-count-smoothing]]
- sentence: "What he calls label smoothing here is the technique he called model smoothing earlier in the lecture ([[youtube-2022-09-07-makemore-1-bigram]] @1:01:43, @1:51:45)."
- cited: [[youtube-2022-09-07-makemore-1-bigram]] @1:01:43, @1:51:45
- raw says: the identification is his, but it is made at @1:50:05–@1:50:40 ("remember the smoothing where we added fake counts ... the gradient-based framework has an equivalent to smoothing"), not in either cited block. As cited, the sentence reads as the wiki's own inference and would need **Note:**; with the right block it is stated.
- fix: "He ties the regularisation back to the fake-count smoothing from earlier in the lecture, though he now calls it label smoothing ([[youtube-2022-09-07-makemore-1-bigram]] @1:01:43, @1:50:05, @1:51:45)."

### F5 — minor — [[treat-broadcasting-with-respect]]
- sentence: "Having shown that dropping `keepdim=True` silently normalises columns instead of rows, he strongly encourages reading the broadcasting semantics, practising, and checking the direction of broadcasting, because mistakes produce very subtle, hard-to-find bugs ([[youtube-2022-09-07-makemore-1-bigram]] @44:10, @46:21, @49:08, @49:40)."
- cited: [[youtube-2022-09-07-makemore-1-bigram]] @44:10
- raw says: the quoted encouragement at @44:10 comes before the demonstration ("let me show you what I mean"); he repeats the warning after it at @49:08–@49:40. Content is right, order is reversed.
- fix: "He strongly encourages reading the broadcasting semantics and treating them with respect, then demonstrates dropping `keepdim=True`, which silently normalises columns instead of rows, and repeats that such mistakes produce very subtle, hard-to-find bugs ([[youtube-2022-09-07-makemore-1-bigram]] @44:10, @46:21, @49:08, @49:40)."

## Checked and correct
- [[youtube-2022-08-16-micrograd]]: Summary (6 sentences) and 14 of 15 key points supported at the cited blocks; see F1.
- [[youtube-2022-09-07-makemore-1-bigram]]: Summary (6 sentences) and all 18 key points supported; "amateur hour", 228,000 bigrams, 2.45/2.47, "even 50" learning rate, `W.exp()` all at the cited blocks.
- [[youtube-2022-09-12-makemore-2-mlp]]: Summary (6 sentences) and 16 of 17 key points supported; see F2.
- [[a-buggy-neural-net-can-still-train-on-a-simple-problem]]: quote verbatim @2:13:16; 3 sentences, all supported.
- [[approximate-gradient-with-more-steps-beats-exact-gradient]]: quote verbatim @43:50; 3 sentences, all supported.
- [[backpropagation-is-more-general-than-neural-networks]]: quote verbatim @04:51; 3 sentences, all supported.
- [[counting-and-gradient-bigram-models-are-the-same-model]]: quote verbatim @1:48:58; 5 sentences, all supported (2.45 before smoothing, 2.47 after, net at 2.46/2.45).
- [[forgetting-to-zero-grad-is-a-common-neural-net-bug]]: quote verbatim @2:11:01; 3 sentences, all supported ("number three" on his tweeted list, `+=` accumulation, PyTorch `zero_grad`).
- [[gradient-based-models-scale-where-count-tables-do-not]]: quote verbatim @1:45:39; 5 sentences incl. the makemore-2 Related claim (27/729/20,000, @09:28 block size 3), all supported.
- [[micrograd-is-all-you-need-everything-else-is-efficiency]]: quote verbatim @06:30; 10 sentences, all supported (150 lines, 2,800 results/406 files, `torch.autograd.Function` garbled in captions, corrected outside the quote).
- [[neural-networks-are-just-mathematical-expressions]]: quote verbatim @04:19; 4 sentences, all supported.
- [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers]]: quote verbatim @1:46:46; 2 sentences, all supported.
- [[treat-broadcasting-with-respect]]: quote verbatim @44:10; 1 sentence, content supported, order fixed in F5.
- [[use-cross-entropy-not-a-hand-rolled-loss]]: quote verbatim @33:16; 2 sentences, all supported (three reasons at @33:16/@34:56/@37:41, max-subtraction at @37:08).
- [[weight-regularization-is-equivalent-to-count-smoothing]]: quote verbatim @1:51:45; 3 sentences, content supported, citation fixed in F4.
- [[backpropagation]]: 12 sentences citing micrograd/makemore-1 checked (chain-rule phrasing and car/bicycle analogy, "a plus is just a distributor of gradient" verbatim @1:04:28, -8 to -7 step, h=0.001 and float precision, topological sort, `+=` from the multivariate chain rule, graph built in the forward pass @1:39:36), all supported.
- [[multilayer-perceptron]]: 12 sentences checked (trigger happiness, w2 grad zero because x2 = 0, 41 parameters, 17,000-word vocabulary, "expensive layer", 3,400 / 10,000 / 11,000 parameters, 2.17, Bengio paper "not the first" but influential and readable), all supported.
- [[activation-functions]]: 6 sentences checked (tanh needs exp, 1 - tanh², relu/tanh/sigmoid "roughly equivalent" and why he chose tanh @2:17:40, tanh as the makemore-2 backward example @33:49), all supported.
- [[loss-functions]]: 9 sentences checked (single-number "trick" @1:52:10, MSE zero only at equality, max-margin / BCE / cross-entropy mentions @2:16:00 @2:19:51, 4% uniform baseline, equivalence of the three optimisation problems, 3.76 vectorised, three reasons for `F.cross_entropy`), all supported.
- [[gradient-descent]]: 12 sentences checked ("a subtle art" verbatim @2:07:43, 0.01 too small / 0.1 dangerously high / 20 steps, "That's not how you optimize a neural net." verbatim @1:32:20, `.grad = None`, even 50, 1 unstable / 10 does not work, "janky", decay "at random" and optimisation "suspect", 0.1 then 0.01 for 100,000 each, log10 squashes the hockey stick), all supported.
- [[pytorch]]: 10 sentences checked (double for float64, `requires_grad` default false for efficiency, 2,800/406, autograd.Function as Lego block, float32 default and int32 counts, `torch.Tensor` vs `torch.tensor` and unclear docs, randn few above 3, `torch.unbind`, Eric's PyTorch Internals post and a possible video, `C[X]`), all supported.
- [[bigram-language-model]]: 7 sentences checked (one `.` token at 0 replacing two tokens that wasted a row and column, P as parameters @50:13, 2.45 @1:00:02, stared a few minutes / H with no history, 27 neurons no bias no nonlinearity, 2.46 vicinity, 27/729/20,000), all supported.
- [[character-level-language-modeling]]: 6 sentences checked (shortest 2 / longest 15, Isabella examples incl. word end, `replacement=True` default false, seeded generator, uniform baseline "more name-like", 228,000 examples), all supported.
- [[broadcasting]]: 6 sentences checked (rules as stated @42:01/@42:32, row and column sums identical @40:55, `P[0].sum()` is 7, silent dimension on the left, in-place ops faster, 32×100 bias check), all supported.
- [[regularization]]: 5 sentences checked (model smoothing with counts 1 or 5, a million → uniform, spring/gravity force, strength = added counts, regularisation strength listed as a dev hyperparameter "not yet" used @55:22), all supported.
- [[softmax]]: 6 sentences checked (outputs positive and negative so not probabilities or counts, logits = log counts, `num_classes=27` to avoid guessing 13, int64 and no dtype argument, one-hot times C equals indexing and "much much faster", `F.softmax` careful about overflow), all supported.
- [[embeddings]]: 6 sentences checked (30-dim shared table C, "a"/"the" and cats/dogs transfer, two equivalent readings, vowels cluster / q and dot outliers, 2-D bottleneck suspicion and "holding us back very likely"), all supported.
- [[overfitting-and-generalization]]: 8 sentences checked (memorise verbatim / held-out loss very high, 80/10/10, 25,000 / 3,000 / 3,000, test "very, very sparingly", test evaluated a single time @1:10:30, equal train and dev = under-fitting, slow departure = starting to overfit, bigger tanh layer did not help much), all supported.
- [[spelled-out-build-from-scratch]]: 7 sentences citing micrograd/makemore-1 checked (blank notebook, bias 6.88 for a 0.5 local derivative, copy-pasted "slightly scary" plumbing, pause-the-video prompts @1:30:38/@1:33:56, "20th time" bug, seeded generator, counting baseline then net), all supported.
- [[verify-gradients-against-pytorch]]: 6 micrograd sentences checked (inline gradient check @37:50, every node, double-precision single-element tensors, 0.707 and 0.5/0/-1.5/1, test file comparing against PyTorch @2:18:45), all supported.
- [[check-shapes-and-broadcasting]]: 5 sentences citing makemore-1/2 checked (27×27 vs 27×1 walk, `keepdim`, `P[0].sum()` check, deliberate break with pause prompt @46:57, 32×3×2 → 32×6 and bias broadcast), all supported.
- [[learning-rate-sweep]]: 6 steps checked (range search, -1 unstable / -10 not optimising, linspace on exponents -3 to 0 with 1,000 steps, plot against exponent, valley near -1, confidence in 0.1), all supported.
- [[diagnose-under-or-overfitting]]: 9 makemore-2 steps checked (first five words for efficiency, 3,400 params vs 32 examples, max logits vs labels, dots → E/O/A/S, dev about 2.3, equal = under-fitting, 300 neurons then 10-dim embeddings, slow departure, test once), all supported; see F3 for the definition sentence.
- [[micrograd]]: 7 sentences checked (two years earlier and source-only, ~100 + ~50 lines, relu present and tanh "intend to add", `Module` and `zero_grad` matching nn.Module, test against PyTorch, demo with batching / max-margin / L2 / lr decay, `_prev` set "I believe for efficiency"), all supported.
- [[makemore]]: 7 sentences citing makemore-1/2 checked (32,000 names from a government website, Dontal/Irot/Zendy, GPT-2-equivalent transformer, DALL-E / Stable Diffusion extensions, 228,000 examples and 2.17, Colab with no installation), all supported.
