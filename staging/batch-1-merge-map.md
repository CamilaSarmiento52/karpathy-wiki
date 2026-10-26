# Batch 1 merge map

Decided 2026-10-23 after reading every digest's candidate list. The digests proposed ~60
topics, ~50 claims and 17 methods for ten sources; many are the same idea under different
names, or a sub-step of a bigger idea. This map fixes the canonical slugs. Merge creates
ONLY these pages (plus source pages). A digest candidate not listed here becomes
sentences on the page named in its "→" line, never a page of its own.

## Source pages (slugs fixed by the digests)

| raw | source slug | merge group |
|---|---|---|
| VMj-3S1tku0 | youtube-2022-08-16-micrograd | A1 |
| PaCmpygFfXo | youtube-2022-09-07-makemore-1-bigram | A1 |
| TCH_1BHY58I | youtube-2022-09-12-makemore-2-mlp | A1 |
| P6sfmUTpUmc | youtube-2022-10-04-makemore-3-activations-batchnorm | A2 |
| q8SA3rM6ckI | youtube-2022-10-11-makemore-4-backprop-ninja | A2 |
| karpathy__makemore | github-2022-11-20-makemore-readme | B |
| t3YJ5hKiMQ0 | youtube-2022-11-21-makemore-5-wavenet | B |
| karpathy__minGPT | github-2023-01-08-mingpt-readme | B |
| kCc8FmEb1nY | youtube-2023-01-17-gpt-from-scratch | B |
| karpathy__ng-video-lecture | github-2023-01-31-ng-video-lecture-readme | B |

## Topics (20)

| canonical slug | absorbs these digest candidates | aliases to set |
|---|---|---|
| backpropagation | chain-rule, derivatives, expression-graphs, cross-entropy-gradient, batchnorm-backward-pass, broadcasting-and-its-backward-pass | Backpropagation, backprop, chain rule, autograd, expression graph |
| multilayer-perceptron | multi-layer-perceptron (micrograd), mlp-language-model (makemore 2) | Multilayer perceptron, MLP, MLP language model, Bengio et al. 2003 |
| activation-functions | activation-functions, saturated-tanh-and-dead-neurons | Activation functions, tanh, ReLU, dead neurons, saturation |
| loss-functions | loss-functions, negative-log-likelihood, cross-entropy-loss | Loss functions, cross-entropy, negative log likelihood, NLL, mean squared error |
| gradient-descent | gradient-descent, gradient-based-optimization, learning-rate, minibatch-training | Gradient descent, learning rate, minibatch, SGD, optimization |
| pytorch | pytorch, pytorch-tensor-basics, pytorch-tensor-views, pytorch-style-layer-modules | PyTorch, tensors, view, nn.Module, torch.cat |
| broadcasting | broadcasting-semantics | Broadcasting, broadcasting semantics |
| character-level-language-modeling | character-level-language-modeling (both), sampling-from-a-language-model | Character-level language model, language modeling, sampling, makemore task |
| bigram-language-model | bigram-language-model (both) | Bigram model, bigram, count table |
| softmax | softmax, one-hot-encoding | Softmax, logits, one-hot encoding |
| regularization | model-smoothing-and-regularization, dropout | Regularization, smoothing, label smoothing, weight decay, dropout |
| embeddings | embeddings, positional-embeddings | Embeddings, embedding table, lookup table, positional embeddings |
| overfitting-and-generalization | train-dev-test-splits, overfitting-and-underfitting, train-and-validation-loss | Overfitting, underfitting, train/dev/test split, validation loss, generalization |
| weight-initialization | weight-initialization, kaiming-initialization | Weight initialization, Kaiming init, He init, initial loss |
| batch-normalization | batch-normalization (all), batchnorm-pitfalls | Batch normalization, BatchNorm, running statistics |
| wavenet-hierarchical-model | hierarchical-progressive-fusion, context-length-scaling, convolutions-as-efficiency | WaveNet, hierarchical model, progressive fusion, dilated causal convolution, context length |
| tokenization | tokenization | Tokenization, tokenizer, tokens, character vs sub-word |
| self-attention | self-attention, lower-triangular-weighted-aggregation, query-key-value, scaled-attention, causal-masking, multi-head-attention | Self-attention, attention, query key value, multi-head attention, causal mask |
| transformer-architecture | transformer-block, residual-connections, layer-norm, decoder-only-transformer, gpt-architecture (minGPT) | Transformer, Transformer block, GPT architecture, decoder-only, residual connections, layer norm |
| pretraining-and-finetuning | pretraining-and-finetuning | Pretraining, finetuning, RLHF, ChatGPT training stages |

Dropped as topics: experimental-harness → method prototype-in-jupyter-then-repo;
neural-networks-zero-to-hero (mention only; its README is batch 2).
Existing topic `rlvr`: link from pretraining-and-finetuning as `## Related` only (the
lecture describes RLHF, not RLVR); do not cite the lecture on the rlvr page.

## Claims (18)

| canonical slug | from digest(s) | folds in |
|---|---|---|
| neural-networks-are-just-mathematical-expressions | micrograd | |
| backpropagation-is-more-general-than-neural-networks | micrograd | |
| micrograd-is-all-you-need-everything-else-is-efficiency | micrograd | operation-granularity-in-autograd-is-up-to-you, production-libraries-are-meant-to-be-used-not-inspected (as context sentences) |
| forgetting-to-zero-grad-is-a-common-neural-net-bug | micrograd | |
| a-buggy-neural-net-can-still-train-on-a-simple-problem | micrograd | |
| counting-and-gradient-bigram-models-are-the-same-model | makemore 1 | |
| gradient-based-models-scale-where-count-tables-do-not | makemore 1 (gradient-based-approach-is-more-flexible-than-counting + bigram-count-tables-do-not-scale-to-longer-contexts) | |
| weight-regularization-is-equivalent-to-count-smoothing | makemore 1 | |
| treat-broadcasting-with-respect | makemore 1 | |
| the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers | makemore 1 | |
| use-cross-entropy-not-a-hand-rolled-loss | makemore 2 | |
| approximate-gradient-with-more-steps-beats-exact-gradient | makemore 2 | |
| the-hockey-stick-loss-means-training-is-wasting-steps | makemore 3 | |
| modern-innovations-make-precise-initialization-less-important | makemore 3 | kaiming-init-is-probably-the-most-common-initialization, initialization-and-backpropagation-are-not-solved (context) |
| avoid-batch-normalization-where-possible | makemore 3 | batchnorm-regularizes-as-a-side-effect, a-bias-before-batchnorm-is-useless, batchnorm-state-is-a-source-of-bugs (makemore 5, as support) |
| understand-backprop-even-with-autograd | makemore 4 (backprop-is-a-leaky-abstraction + understand-backprop-despite-autograd) | |
| batchnorm-train-test-variance-mismatch-is-a-bug | makemore 4 | he-prefers-channels-last-batchnorm (makemore 5) stays a sentence on batch-normalization |
| attention-is-a-communication-mechanism | gpt lecture | attention-has-no-notion-of-space, the-triangular-mask-is-what-makes-it-a-decoder (sentences on self-attention) |
| pretraining-gives-a-document-completer | gpt lecture | gpt3-is-the-same-architecture-far-larger, the-finetuning-stage-is-harder-to-replicate (sentences on pretraining-and-finetuning) |
| gpt-is-not-a-complicated-model | minGPT README | |
| pytorch-documentation-is-unreliable | makemore 5 | |
| deep-learning-is-largely-shape-gymnastics | makemore 5 | |

(That is 22 rows; the four "folds in" rows carry no page of their own, so 22 claim pages.)

Dropped as claims (become sentences on the named page): learning-rate-tuning-is-a-subtle-art
→ gradient-descent; guess-and-check-is-not-how-you-optimize / -not-a-typical-workflow →
gradient-descent; embedding-index-equals-one-hot-linear-layer → embeddings; view-is-free-cat-copies
→ pytorch; lower-training-loss-alone-does-not-mean-a-better-model, test-set-evaluated-very-few-times,
equal-train-and-dev-loss-means-underfitting → overfitting-and-generalization; update-to-data-ratio
→ method training-diagnostics; makemore-mlp-is-bottlenecked-by-context-length →
wavenet-hierarchical-model (motivation; cite makemore 3); convolutions-do-not-change-the-model,
hierarchical-model-did-not-beat-flat-at-equal-parameters → wavenet-hierarchical-model;
model-initialization-matters-for-good-performance (ng-video-lecture) → weight-initialization.

Relations between claims: set `supports` / `extends` only where the digest gives both
sides a citation; no `contradicts` is expected in this batch. Existing claims from phase 1
(2025–2026) are unrelated to this material; do not force links.

## Methods (7)

| canonical slug | absorbs |
|---|---|
| spelled-out-build-from-scratch | spelled-out-build-from-scratch, spell-it-out-step-by-step, explicit-baseline-then-neural-net, build-up-from-a-bigram-baseline |
| small-hackable-educational-code | small-hackable-educational-code (three READMEs) |
| verify-gradients-against-pytorch | inline-gradient-check, verify-against-pytorch, check-manual-gradients-against-pytorch, derive-gradients-by-shape-matching |
| check-shapes-and-broadcasting | check-broadcasting-carefully, inspect-shapes-layer-by-layer |
| learning-rate-sweep | learning-rate-sweep |
| training-diagnostics | training-diagnostics-plots, check-the-loss-at-initialization, evaluate-with-a-single-loss-number |
| diagnose-under-or-overfitting | diagnose-under-or-overfitting, overfit-a-single-batch, control-for-parameter-count |
| prototype-in-jupyter-then-repo | prototype-in-jupyter-then-repo, experimental-harness |

(8 rows: 8 method pages.)

## Artifacts (5)

| slug | notes |
|---|---|
| micrograd | new. repo_url https://github.com/karpathy/micrograd (the manifest's url for the 2026 README snapshot, batch 4); language Python; status active |
| makemore | new. repo_url https://github.com/karpathy/makemore; language Python; status active. Group A1 creates it from the lectures; group B adds the README source |
| mingpt | new, group B. status superseded (its README says so); relation to existing `nanogpt` |
| ng-video-lecture | new, group B. aliases [nanogpt-lecture] |
| nanogpt | existing; group B adds the GPT lecture and minGPT README as sources |

## Timelines

None planned. Create one only if a `supports`/`extends`/`contradicts` pair appears
(CLAUDE.md §7 step 7). `gpt-training-repos-over-time` (minGPT → nanoGPT → nanochat) is
deferred: the relation is stated on the artifact pages.

## Merge groups (sequential; lint clean before the next starts)

- **A1**: micrograd, makemore 1, makemore 2 → creates most topic, claim, method pages and
  artifacts micrograd, makemore.
- **A2**: makemore 3, makemore 4 → weight-initialization, batch-normalization, their
  claims and methods; extends backpropagation, gradient-descent, pytorch.
- **B**: makemore README, makemore 5, minGPT README, GPT lecture, ng-video-lecture README →
  wavenet, tokenization, self-attention, transformer-architecture, pretraining-and-finetuning,
  artifacts mingpt, ng-video-lecture, nanogpt update, small-hackable-educational-code.
