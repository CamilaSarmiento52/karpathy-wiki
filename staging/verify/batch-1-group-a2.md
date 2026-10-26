# Verification: batch 1, group A2 (makemore 3, makemore 4)
Verified 2026-10-23 by a fresh reader. Sources: [[youtube-2022-10-04-makemore-3-activations-batchnorm]], [[youtube-2022-10-11-makemore-4-backprop-ninja]]

## Coverage
- pages checked: 23 (claims: the-hockey-stick-loss-means-training-is-wasting-steps, modern-innovations-make-precise-initialization-less-important, avoid-batch-normalization-where-possible, batchnorm-train-test-variance-mismatch-is-a-bug, understand-backprop-even-with-autograd; topics: weight-initialization, batch-normalization, backpropagation, activation-functions, gradient-descent, pytorch, broadcasting, loss-functions, overfitting-and-generalization, multilayer-perceptron, wavenet-hierarchical-model; methods: training-diagnostics, verify-gradients-against-pytorch, check-shapes-and-broadcasting; artifacts: makemore, micrograd; the two source pages), claim pages fully checked: 5 (36 sentences, 5 block quotes all verbatim at the cited block), other sentences checked: ~105 of ~150
- Both raw files were read in full, so every timestamp below was checked against the actual 30-second block, not just grepped.
- The `supports` pair was checked in both directions (see F1, F2).

## Findings
### F1 — overstated — [[avoid-batch-normalization-where-possible]]
- sentence: "supports [[batchnorm-train-test-variance-mismatch-is-a-bug]]: the following lecture names one of the bugs, PyTorch's biased-in-training, unbiased-at-inference variance, which he says gives anyone using the layer a bit of a bug"
- cited: [[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:17:07; [[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:08:05
- raw says: at @1:17:07 the bugs are blamed on the layer "coupling examples" in the forward pass. At @1:05:49–@1:08:05 the variance mismatch is attributed to the paper ("they actually introduce a train test mismatch"), with PyTorch following the paper exactly (@1:07:31); it is a statistics-estimator issue, not a coupling issue, and he never connects it to the previous lecture's warning. "names one of the bugs" invents that connection, and "PyTorch's" misplaces the origin.
- fix: "supports [[batchnorm-train-test-variance-mismatch-is-a-bug]]: a week later he calls another property of the layer a bug, the paper's (and PyTorch's) biased-in-training, unbiased-at-inference variance, which in his view gives anyone using the layer a bit of a bug; he does not tie it to the coupling he blames here ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:17:07; [[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:05:49, @1:08:05)." The `supports` link itself is defensible in the direction variance-bug → avoid (one more bug in the layer); it is weak in the reverse direction, which the frontmatter convention forces anyway.

### F2 — minor — [[batchnorm-train-test-variance-mismatch-is-a-bug]]
- sentence: "supports [[avoid-batch-normalization-where-possible]]: a week earlier he said the layer causes a huge amount of bugs and told viewers to avoid it; this variance mismatch is one concrete bug he points to"
- cited: [[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:17:07; [[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:08:05
- raw says: both halves are individually true, but juxtaposed they read as if this is one of the bugs he had in mind at @1:17:07, where his reason was coupling of examples. He does not make that link.
- fix: append "; he does not connect it to the coupling he blamed in the earlier lecture" before the citation.

### F3 — minor — [[batchnorm-train-test-variance-mismatch-is-a-bug]]
- sentence: title "Using the biased variance in training and the unbiased one at test time is a bug in batchnorm"
- cited: [[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:08:05
- raw says: "I basically consider this to be a bug", "in my view has a bit of a bug", and at @1:08:38 "maybe someone can explain why this is okay". It is explicitly his hedged view; the title states it as fact (cf. §4: "his wiki worked without RAG", not "wikis don't need RAG").
- fix: title "He considers batchnorm's biased-in-training, unbiased-at-test variance a bug" (slug can stay). `confidence: stated` is correct.

### F4 — minor — [[youtube-2022-10-11-makemore-4-backprop-ninja]]
- sentence: Summary, "…and calls PyTorch's train/test variance mismatch a bug"
- cited: @1:05:16, @1:08:05
- raw says: the mismatch is introduced by the paper (@1:05:49 "they actually introduce a train test mismatch"); PyTorch "follow[s] the paper exactly" (@1:07:31). He says "they don't really go into the detail of the reasoning behind it in this paper" (@1:08:05).
- fix: "…and calls the paper's train/test variance mismatch, which PyTorch follows, a bug (@1:05:49, @1:07:31, @1:08:05)".

### F5 — minor — [[activation-functions]]
- sentence: "Scaling the first-layer weights to about 0.2 brought the pre-activations to roughly ±1.5 with no saturated neurons"
- cited: [[youtube-2022-10-04-makemore-3-activations-batchnorm]] @24:48, @25:22
- raw says: at @24:48 he multiplies W1 by 0.1 and gets pre-activations "between -1.5 and 1.5" with "no white"; at @25:22 he then says "maybe we can go up a little bit… 0.2" and settles on 0.2 as "a nice distribution". The ±1.5 / zero-saturation reading belongs to 0.1, not 0.2.
- fix: "Scaling the first-layer weights by 0.1 brought the pre-activations to roughly ±1.5 with no saturated neurons; he then relaxed the scale to 0.2 as a nicer distribution ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @24:48, @25:22)."

### F6 — minor — [[the-hockey-stick-loss-means-training-is-wasting-steps]]
- sentence: "The final loss improved slightly, about 2.2 to 2.16 in that run, because more cycles went to real training instead of shrinking weights"
- cited: [[youtube-2022-10-04-makemore-3-activations-batchnorm]] @12:19, @12:52
- raw says: @12:19 is garbled and hedged: "I believe this was 2. um2 and this was this was 2.16". His own clean summary at @25:57 gives validation loss 2.17 before and 2.13 after fixing the softmax. The wiki presents the garbled numbers as fact.
- fix: "The final loss improved slightly (his later summary puts validation loss at 2.17 before and 2.13 after this fix), because more cycles went to real training instead of shrinking weights ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @12:19, @12:52, @25:57)."

### F7 — minor — [[understand-backprop-even-with-autograd]]
- sentence: "He refers to a blog post of his on this from a while ago, and lists examples already covered: saturating nonlinearities killing gradients, dead neurons, exploding or vanishing gradients in RNNs"
- cited: [[youtube-2022-10-11-makemore-4-backprop-ninja]] @00:31, @01:37
- raw says: @01:37 — flat tails and dead neurons "I've already covered", but exploding/vanishing gradients in RNNs "which we are about to cover".
- fix: "…and lists examples: saturating nonlinearities killing gradients and dead neurons, which he has already covered, and exploding or vanishing gradients in RNNs, which he is about to cover".

### F8 — mis-cited — [[training-diagnostics]]
- sentence: step 6, "the output layer was an outlier because its weights were shrunk by 0.1, giving 10× larger gradients that stabilise after about 1,000 steps"
- cited: [[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:36:35, @1:37:07, @1:37:41, @1:38:15, @1:38:47, @1:39:20
- raw says: the 1:38 blocks give the symptom (last layer ~10× larger gradient std, "100 times greater sorry 10 times") and @1:39:20 the stabilisation; the cause ("artificially shrunk down… multiplied the weight by 0.1") is stated at @1:42:39 in the update-ratio discussion, not within the cited blocks.
- fix: add @1:42:39 to the citation list.

### F9 — minor — [[batch-normalization]]
- sentence: "Forcing a unit Gaussian always gives poor results, so the paper adds a learned scale…"
- cited: [[youtube-2022-10-04-makemore-3-activations-batchnorm]] @45:19, @45:52, @46:27
- raw says: "you actually won't achieve a very good result with this… we don't want these to be forced to be Gaussian always". "always" modifies the forcing, not the result; the wiki wording reads as "always gives poor results".
- fix: "Forcing the activations to stay unit Gaussian throughout training gives poor results, so…"

## Checked and correct
- [[the-hockey-stick-loss-means-training-is-wasting-steps]]: 6 sentences, quote verbatim @11:11, title and confidence supported (@11:44, @12:19, @1:14:18); only F6
- [[modern-innovations-make-precise-initialization-less-important]]: 6 sentences, all supported; quote verbatim @36:26; "probably the most common way of initializing neural networks" verbatim @33:45; RMSprop correctly de-garbled from "ARS prop" outside quotes
- [[avoid-batch-normalization-where-possible]]: 9 sentences citing my sources, 8 supported (@49:49–@53:44, @1:01:31–@1:08:13, @1:17:07, @1:17:40); quote verbatim @1:17:07; only F1
- [[batchnorm-train-test-variance-mismatch-is-a-bug]]: 7 sentences, Context all supported (@1:00:11–@1:08:38); quote verbatim @1:08:05; F2, F3 only
- [[understand-backprop-even-with-autograd]]: 8 sentences, 7 supported; quote verbatim @00:31; only F7
- [[weight-initialization]]: 13 sentences checked (3, √2, 5/3, fan-in 30, 0.3 vs 0.2, 2.17→2.13→2.10, nn.Linear uniform ±1/√fan_in, gain 1 vs 3, "no idea where 5/3 came from", pencil), all supported; paper findings correctly attributed to He et al.
- [[batch-normalization]]: 14 sentences checked (2015/Google, 0.999/0.001, eps 1e-5, momentum 0.1 vs 0.001, variance not std, placement options, 10× learning rate, Bessel paragraph, "notable exception"), 13 supported; only F9
- [[backpropagation]]: 15 sentences checked (`**-1` division bug, router, 1e-9, 5e-9, MATLAB 2010 / numpy 2014, 33 arrows, dσ²/dμ vanishing, i→j renaming, (σ²+ε)^(-3/2)), all supported
- [[activation-functions]]: 8 sentences checked, 7 supported (−5..15, 1−t², 0.99 / 0.97 thresholds, 5% / 0.65, leaky ReLU vs ELU, @01:37); only F5
- [[gradient-descent]]: 4 sentences checked (−3 guide, 0.001 → 10,000× too small, 10× to 1.0, "did not fully explain"), all supported
- [[pytorch]]: 6 sentences checked (no_grad decorator, nn. prefix, retain_grad/allclose, torch.var default), all supported
- [[broadcasting]]: 4 sentences checked (27→32×27 bias, 1×64 gain/bias, duality @1:09:12/@1:09:47), all supported
- [[loss-functions]]: 2 sentences, both supported
- [[overfitting-and-generalization]]: 1 sentence, supported
- [[multilayer-perceptron]]: 3 sentences checked (11,000 params / 200,000 steps / 2.16; 46,000 params; universal approximator), all supported
- [[wavenet-hierarchical-model]]: 1 sentence, supported (@1:53:45, @1:54:17)
- [[training-diagnostics]]: 8 sentences checked (3.29, 0.97, 5%/0.65, −3 heuristic, −2.5 "decent", 10,000×, fan-in demo, @1:53:12), 7 supported; only F8
- [[verify-gradients-against-pytorch]]: 6 steps checked (non-zero bias init, cmp exact/allclose/maxdiff, "only one way" shapes, 5e-9/1e-9, 100-iteration break, "always like simpler examples"), all supported
- [[check-shapes-and-broadcasting]]: step 6, supported (@1:08:38 "scrutinize the shapes first")
- [[makemore]]: 6 bullets checked (32,000 names, 27 tokens, GitHub/Colab, ~20 lines, RNN/LSTM next), all supported
- [[micrograd]]: 1 bullet, supported (@02:43, @25:02, @53:30, @1:39:25)
- [[youtube-2022-10-04-makemore-3-activations-batchnorm]]: Summary + 8 key points checked (27 vs 3.29, √2 / 5/3, "most common", 1e-3, pencil, linear collapse, redundant bias, context-length bottleneck), all supported at the cited blocks
- [[youtube-2022-10-11-makemore-4-backprop-ninja]]: Summary + 6 key points checked (leaky abstraction, 2010–2014 MATLAB/numpy, 1e-9, 5e-9, n−1 throughout, 20 lines; "highly non-trivial" is at @1:49:24, one block after the cited @1:48:50, within tolerance), all supported; only F4
- Paper attributions: Kaiming/He et al. findings (√2 gain, forward→backward, fan-in vs fan-out) and BatchNorm paper proposals (scale/shift, calibration stage, running stats, biased 1/m) are everywhere attributed to the papers, not to him. No disguised claims in **Note:** sentences. Caption garble ("ARS prop", "one5", "bathroom", "Bachelor") is corrected outside quotes throughout.

## Resolution
Resolved 2026-10-23 (log entry `## 2026-10-23 correction`).
- F1 — fixed; `supports` kept on both pages (CLAUDE.md sets it on both), with the line on [[avoid-batch-normalization-where-possible]] stating that the support runs variance-bug → avoid only
- F2 — fixed
- F3 — fixed (title and index line)
- F4 — fixed
- F5 — fixed
- F6 — fixed
- F7 — fixed
- F8 — fixed
- F9 — fixed
