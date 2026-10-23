# Log

Append-only journal of every ingest, query and lint. Never edit past entries.

## 2026-10-20 ingest [[x-2025-02-02-vibe-coding]]
- created: [[x-2025-02-02-vibe-coding]], [[vibe-coding]], [[vibe-coding-is-for-throwaway-weekend-projects]], [[vibe-coding-over-time]]
- notes: phase 1 hand-picked source; a single long post, not a thread.

## 2026-10-20 ingest [[youtube-2025-06-19-software-is-changing]]
- created: [[youtube-2025-06-19-software-is-changing]], [[software-3-0]], [[llms-as-operating-systems]], [[jagged-intelligence]], [[partial-autonomy-apps]], [[llm-gui]], [[building-for-agents]], [[english-is-the-new-programming-language]], [[this-is-the-decade-of-agents]], [[ai-assisted-coding-loop]], [[nanogpt]]
- updated: [[vibe-coding]], [[vibe-coding-over-time]]
- notes: published date is the YouTube upload (2025-06-19); the talk was given two days earlier. Auto-captions misspell names (e.g. "Andre Carpathy", "menu.app" for MenuGen); pages use the correct spelling.

## 2026-10-20 ingest [[blog-2025-12-19-year-in-review-2025]]
- created: [[blog-2025-12-19-year-in-review-2025]], [[rlvr]], [[vibe-coding-will-terraform-software]], [[claude-code-is-the-first-convincing-llm-agent]], [[nanochat]]
- updated: [[vibe-coding]], [[vibe-coding-over-time]], [[jagged-intelligence]], [[partial-autonomy-apps]], [[llms-as-operating-systems]], [[llm-gui]], [[software-3-0]], [[english-is-the-new-programming-language]]
- notes: first contradiction: [[vibe-coding-will-terraform-software]] contradicts [[vibe-coding-is-for-throwaway-weekend-projects]]; timeline explains it as a widening of scope.

## 2026-10-20 ingest [[x-2026-04-02-llm-knowledge-bases]]
- created: [[x-2026-04-02-llm-knowledge-bases]], [[llm-knowledge-bases]], [[llm-wiki-workflow]], [[no-rag-needed-for-a-small-wiki]]
- updated: [[vibe-coding]], [[vibe-coding-over-time]], [[llm-gui]], [[building-for-agents]]

## 2026-10-20 ingest [[github-2026-07-03-nanochat-readme]]
- created: [[github-2026-07-03-nanochat-readme]], [[quick-experiment-loop]]
- updated: [[nanochat]], [[nanogpt]], [[building-for-agents]]
- notes: README snapshot dated by its last commit (2026-07-03); the repo dates from 2025-10-13.

## 2026-10-21 correction
Review of the first ingest (external review, 2026-10-20). Compilation errors, fixed in place:
- [[vibe-coding-is-for-throwaway-weekend-projects]], [[vibe-coding-will-terraform-software]]: `contradicts` was wrong; the Feb post names where vibe coding is acceptable, not the only use. Now `extends`, and each comparison cites both sources.
- [[vibe-coding-over-time]]: no longer says the Feb post "limits" vibe coding; the closing note is labelled as editorial.
- [[this-is-the-decade-of-agents]]: the local-computer argument was cited to the talk @27:09; it is in the blog §4. Now cited there.
- [[claude-code-is-the-first-convincing-llm-agent]], [[english-is-the-new-programming-language]]: relationship lines now cite the passage they describe.
- [[llm-knowledge-bases]]: said knowledge now takes more of his tokens than code; the post says a large share is shifting toward knowledge. Talk moved from `sources` to `context`, so `first_seen` counts only direct sources.
- [[no-rag-needed-for-a-small-wiki]]: title narrowed to his one ~100-article wiki.
- [[nanogpt]]: said it covered only pretraining (nanochat's contrast); its own README also covers finetuning. Rewritten from that README; `superseded` now rests on its stated deprecation, not inference.
- [[nanochat]], [[quick-experiment-loop]]: kept the 2-hour 8×H100 and multi-GPU assumptions next to the $48 and five-minute figures.

## 2026-10-21 ingest [[github-2025-11-12-nanogpt-readme]]
- created: [[github-2025-11-12-nanogpt-readme]]
- updated: [[nanogpt]]
- notes: raw/ was refetched with the fixed fetcher (manifest v2: `ref`, pinned GitHub `commit`, body-only hash). Bodies unchanged except the blog, which now keeps its link targets.

## 2026-10-23 ingest [[youtube-2022-08-16-micrograd]]
- created: [[youtube-2022-08-16-micrograd]], [[backpropagation]], [[multilayer-perceptron]], [[activation-functions]], [[loss-functions]], [[gradient-descent]], [[pytorch]], [[neural-networks-are-just-mathematical-expressions]], [[backpropagation-is-more-general-than-neural-networks]], [[micrograd-is-all-you-need-everything-else-is-efficiency]], [[forgetting-to-zero-grad-is-a-common-neural-net-bug]], [[a-buggy-neural-net-can-still-train-on-a-simple-problem]], [[spelled-out-build-from-scratch]], [[verify-gradients-against-pytorch]], [[micrograd]]
- updated: none
- notes: first of batch 1 (merge group A1), following staging/batch-1-merge-map.md. Digest candidates chain-rule, derivatives and expression-graphs are sections of [[backpropagation]]; operation-granularity and production-libraries-are-meant-to-be-used are context paragraphs on [[micrograd-is-all-you-need-everything-else-is-efficiency]]; learning-rate-tuning-is-a-subtle-art is a sentence on [[gradient-descent]]; inline-gradient-check and verify-against-pytorch merged into [[verify-gradients-against-pytorch]]. Quotes keep caption spelling; pages use correct spelling. `status: active` on [[micrograd]] rests on stated intent only. The micrograd `supports` links are all within this source, so no timeline.

## 2026-10-23 ingest [[youtube-2022-09-07-makemore-1-bigram]]
- created: [[youtube-2022-09-07-makemore-1-bigram]], [[character-level-language-modeling]], [[bigram-language-model]], [[broadcasting]], [[softmax]], [[regularization]], [[counting-and-gradient-bigram-models-are-the-same-model]], [[gradient-based-models-scale-where-count-tables-do-not]], [[weight-regularization-is-equivalent-to-count-smoothing]], [[treat-broadcasting-with-respect]], [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers]], [[check-shapes-and-broadcasting]], [[makemore]]
- updated: [[loss-functions]], [[gradient-descent]], [[backpropagation]], [[pytorch]], [[micrograd]], [[spelled-out-build-from-scratch]]
- notes: per the merge map, sampling-from-a-language-model is a section of [[character-level-language-modeling]]; negative-log-likelihood and evaluate-with-a-single-loss-number are paragraphs on [[loss-functions]] (group A2's `training-diagnostics` method may pick the latter up); one-hot-encoding is on [[softmax]]; pytorch-tensor-basics on [[pytorch]]; gradient-based-optimization and guess-and-check on [[gradient-descent]]; the two scaling claims merged into [[gradient-based-models-scale-where-count-tables-do-not]]. `repo_url` for [[makemore]] comes from the map, not the raw. The [[nanogpt]] link on [[makemore]] is a labelled Note, not evidence.

## 2026-10-23 ingest [[youtube-2022-09-12-makemore-2-mlp]]
- created: [[youtube-2022-09-12-makemore-2-mlp]], [[embeddings]], [[overfitting-and-generalization]], [[use-cross-entropy-not-a-hand-rolled-loss]], [[approximate-gradient-with-more-steps-beats-exact-gradient]], [[learning-rate-sweep]], [[diagnose-under-or-overfitting]]
- updated: [[multilayer-perceptron]], [[character-level-language-modeling]], [[bigram-language-model]], [[activation-functions]], [[loss-functions]], [[gradient-descent]], [[pytorch]], [[broadcasting]], [[softmax]], [[regularization]], [[check-shapes-and-broadcasting]], [[makemore]], [[gradient-based-models-scale-where-count-tables-do-not]]
- notes: per the merge map, mlp-language-model is a section of [[multilayer-perceptron]]; embedding-index-equals-one-hot-linear-layer is on [[embeddings]] (and [[softmax]]); view-is-free-cat-copies on [[pytorch]]; minibatch-training and learning-rate on [[gradient-descent]]; the four dropped overfitting/test-set claims are sentences on [[overfitting-and-generalization]]; overfit-a-single-batch is folded into [[diagnose-under-or-overfitting]] (control-for-parameter-count left for group B). The "PyTorch Internals" blog post is not attributed to an author because the captions name only "Eric". The MLP lecture is cited on [[gradient-based-models-scale-where-count-tables-do-not]] as a later supporting passage, not a new claim, so no timeline. End of merge group A1; lint clean.

## 2026-10-23 ingest [[youtube-2022-10-04-makemore-3-activations-batchnorm]]
- created: [[youtube-2022-10-04-makemore-3-activations-batchnorm]], [[weight-initialization]], [[batch-normalization]], [[the-hockey-stick-loss-means-training-is-wasting-steps]], [[modern-innovations-make-precise-initialization-less-important]], [[avoid-batch-normalization-where-possible]], [[training-diagnostics]]
- updated: [[activation-functions]], [[gradient-descent]], [[pytorch]], [[loss-functions]], [[overfitting-and-generalization]], [[multilayer-perceptron]], [[makemore]]
- notes: first of merge group A2, following staging/batch-1-merge-map.md. kaiming-initialization is a section of [[weight-initialization]]; saturated-tanh-and-dead-neurons is a section of [[activation-functions]]; kaiming-init-is-probably-the-most-common-initialization and initialization-and-backpropagation-are-not-solved are context sentences on [[modern-innovations-make-precise-initialization-less-important]]; batchnorm-regularizes-as-a-side-effect and a-bias-before-batchnorm-is-useless are paragraphs on [[avoid-batch-normalization-where-possible]] (and [[batch-normalization]], [[overfitting-and-generalization]]); update-to-data-ratio-should-be-around-1e-3 is a step of [[training-diagnostics]], keeping his "rough guide" hedge; check-the-loss-at-initialization is its first step and evaluate-with-a-single-loss-number stays on [[loss-functions]], linked. makemore-mlp-is-bottlenecked-by-context-length is a sentence on [[makemore]] and [[multilayer-perceptron]] until group B creates wavenet-hierarchical-model. Caption garble ("bash normalization", "10h", "soled") kept out of quotes; pages use correct spelling. No supports/extends set within this source: the related-claim lines are labelled Notes.

## 2026-10-23 ingest [[youtube-2022-10-11-makemore-4-backprop-ninja]]
- created: [[youtube-2022-10-11-makemore-4-backprop-ninja]], [[understand-backprop-even-with-autograd]], [[batchnorm-train-test-variance-mismatch-is-a-bug]]
- updated: [[backpropagation]], [[broadcasting]], [[batch-normalization]], [[loss-functions]], [[activation-functions]], [[pytorch]], [[verify-gradients-against-pytorch]], [[check-shapes-and-broadcasting]], [[makemore]], [[micrograd]], [[avoid-batch-normalization-where-possible]]
- notes: per the merge map, cross-entropy-gradient, batchnorm-backward-pass and broadcasting-and-its-backward-pass are subsections of [[backpropagation]] (with a paragraph each on [[loss-functions]] and [[broadcasting]]); backprop-is-a-leaky-abstraction is folded into [[understand-backprop-even-with-autograd]], whose quote is the leaky-abstraction line because the digest's alternative carries caption garble; derive-gradients-by-shape-matching and check-manual-gradients-against-pytorch are steps 7–15 of [[verify-gradients-against-pytorch]]. [[micrograd]] cites this lecture as `context` only. The one `supports` pair in group A2 is [[batchnorm-train-test-variance-mismatch-is-a-bug]] ↔ [[avoid-batch-normalization-where-possible]], cited on both sides from both lectures; no `extends`/`contradicts`, so no timeline. The leaky-abstraction blog post is referred to but not named, per the digest. His hedges kept: `unbiased` default "not sure", "maybe someone can explain", unknown source of ~1e-9 differences. End of merge group A2.

## 2026-10-23 ingest [[github-2022-11-20-makemore-readme]]
- created: [[github-2022-11-20-makemore-readme]], [[small-hackable-educational-code]]
- updated: [[makemore]], [[character-level-language-modeling]]
- notes: first of merge group B, following staging/batch-1-merge-map.md. The README is dated by its commit (988aa59), two months after the first lectures. [[makemore]]'s `repo_url`, taken from the map by group A1, is now backed by this source; `status: active` stands because the snapshot has no deprecation notice. The CNN/WaveNet model is written as in progress, as the README marks it. `names.txt` typo ("takes") paraphrased, not quoted. [[small-hackable-educational-code]] is created from this README and will be extended by the minGPT and ng-video-lecture READMEs later in this group.

## 2026-10-23 ingest [[youtube-2022-11-21-makemore-5-wavenet]]
- created: [[youtube-2022-11-21-makemore-5-wavenet]], [[wavenet-hierarchical-model]], [[pytorch-documentation-is-unreliable]], [[deep-learning-is-largely-shape-gymnastics]], [[prototype-in-jupyter-then-repo]]
- updated: [[makemore]], [[pytorch]], [[batch-normalization]], [[avoid-batch-normalization-where-possible]], [[overfitting-and-generalization]], [[diagnose-under-or-overfitting]], [[check-shapes-and-broadcasting]], [[multilayer-perceptron]], [[gradient-descent]]
- notes: per the merge map, hierarchical-progressive-fusion, context-length-scaling and convolutions-as-efficiency are sections of [[wavenet-hierarchical-model]], which also takes the context-bottleneck motivation parked on [[makemore]] and [[multilayer-perceptron]] and cites makemore 3 for it; pytorch-style-layer-modules is a paragraph on [[pytorch]]; batchnorm-pitfalls and he-prefers-channels-last-batchnorm are a paragraph on [[batch-normalization]]; batchnorm-state-is-a-source-of-bugs is a context paragraph on [[avoid-batch-normalization-where-possible]] (no new relation set); train-and-validation-loss is on [[overfitting-and-generalization]]; experimental-harness and guess-and-check-is-not-a-typical-workflow are step 5 of [[prototype-in-jupyter-then-repo]] plus a sentence on [[gradient-descent]]; inspect-shapes-layer-by-layer is steps 7–12 of [[check-shapes-and-broadcasting]]; control-for-parameter-count is steps 10–14 of [[diagnose-under-or-overfitting]]; convolutions-do-not-change-the-model and hierarchical-model-did-not-beat-flat-at-equal-parameters are sentences on the wavenet topic. Loss numbers carried as the digest lists them (2.10 → 2.02 → 2.029 vs 2.027 → 2.022 → 1.993). Caption garble (Jupiter, bash Norm, patreon) kept out of quotes; the two claim quotes are clean. The [[quick-experiment-loop]] link is a labelled Note. The WaveNet authors are not named because he does not name them.

## 2026-10-23 ingest [[github-2023-01-08-mingpt-readme]]
- created: [[github-2023-01-08-mingpt-readme]], [[mingpt]], [[transformer-architecture]], [[gpt-is-not-a-complicated-model]]
- updated: [[nanogpt]], [[small-hackable-educational-code]]
- notes: per the merge map, gpt-architecture is absorbed by [[transformer-architecture]], which the GPT lecture will extend next. The §References numbers are written as his reading notes on OpenAI's papers, not quoted and not attributed to him as claims; §References subsections cited by abbreviated H4 title. [[mingpt]] `status: superseded` rests on the January 2023 semi-archive note; the relation to [[nanogpt]] is stated on both pages. No timeline: the map defers gpt-training-repos-over-time. The nanoGPT ~300-line parallel on the claim page is a labelled Note, not a `supports` link.

## 2026-10-23 ingest [[youtube-2023-01-17-gpt-from-scratch]]
- created: [[youtube-2023-01-17-gpt-from-scratch]], [[tokenization]], [[self-attention]], [[pretraining-and-finetuning]], [[attention-is-a-communication-mechanism]], [[pretraining-gives-a-document-completer]], [[ng-video-lecture]]
- updated: [[bigram-language-model]], [[embeddings]], [[transformer-architecture]], [[regularization]], [[nanogpt]], [[spelled-out-build-from-scratch]], [[training-diagnostics]], [[github-2023-01-08-mingpt-readme]] (Fed pages: tokenization)
- notes: per the merge map, lower-triangular-weighted-aggregation, query-key-value, scaled-attention, causal-masking and multi-head-attention are sections of [[self-attention]]; transformer-block, residual-connections, layer-norm and decoder-only-transformer are sections of [[transformer-architecture]]; positional-embeddings is a paragraph on [[embeddings]]; dropout on [[regularization]]; attention-has-no-notion-of-space and the-triangular-mask-is-what-makes-it-a-decoder are sentences on [[self-attention]] and in the Context of [[attention-is-a-communication-mechanism]]; gpt3-is-the-same-architecture-far-larger and the-finetuning-stage-is-harder-to-replicate are sentences on [[pretraining-and-finetuning]] and [[pretraining-gives-a-document-completer]]; check-the-loss-at-initialization went to [[training-diagnostics]] and build-up-from-a-bigram-baseline to [[spelled-out-build-from-scratch]] (steps 14–20). [[tokenization]] also cites the minGPT README for `bpe.py`, so that source's Fed pages gained it. [[pretraining-and-finetuning]] links [[rlvr]] as Related only, with a Note that the lecture describes RLHF. The lecture misstates GPT-2's year at @06:12; the wiki does not repeat a year. [[ng-video-lecture]]'s `repo_url` comes from the map and GitHub because the repo name is never spoken; the README is the next source. Validation-loss figures written as "about". Hardware figure kept with his hedge. Caption garble ("nanog GPT", "Byram") kept out of the two claim quotes.

## 2026-10-23 ingest [[github-2023-01-31-ng-video-lecture-readme]]
- created: [[github-2023-01-31-ng-video-lecture-readme]]
- updated: [[ng-video-lecture]], [[weight-initialization]], [[nanogpt]], [[small-hackable-educational-code]]
- notes: per the merge map, model-initialization-matters-for-good-performance is a paragraph on [[weight-initialization]], not a claim page. [[ng-video-lecture]]'s `repo_url` is now backed by this source; its `status: active` rests on his stated plan to keep the repo as taught. The supplementary lecture and code push are written as plans at snapshot time, not as done. The digest's unsourced alias "Let's build GPT code" was not added. neural-networks-zero-to-hero stays a mention. End of merge group B; lint clean.

## 2026-10-23 correction
Batch 1 verification (three fresh readers, reports in staging/verify/). Compilation errors fixed in place:
- [[youtube-2022-08-16-micrograd]]: said it took him 15 minutes to find the tanh backward kernel; he spent about 15 minutes without finding it and reached it through a pointer in a thread. Overstated.
- [[youtube-2022-09-12-makemore-2-mlp]], [[diagnose-under-or-overfitting]]: said he overfits a small batch "to check the training loop"; he develops on five words for efficiency and names the low loss overfitting a single batch. Purpose was invented; alias "sanity-check the training loop" dropped.
- [[weight-regularization-is-equivalent-to-count-smoothing]]: the smoothing/regularisation identification was cited to blocks that do not make it; now cites @1:50:05, where he does, and is worded as his tie-back.
- [[treat-broadcasting-with-respect]]: reversed the order of the encouragement (@44:10) and the `keepdim` demonstration; now in his order.
- [[avoid-batch-normalization-where-possible]], [[batchnorm-train-test-variance-mismatch-is-a-bug]]: the `supports` lines implied the variance mismatch was one of the coupling bugs he had in mind at @1:17:07 and called it PyTorch's; he attributes it to the paper (PyTorch follows it) and never connects the two. Both lines now say so; `supports` kept on both pages, with the line stating that the support runs variance-bug → avoid only, as the report allows.
- [[batchnorm-train-test-variance-mismatch-is-a-bug]], [[index]]: title stated the bug as fact; now "He considers … a bug", matching his hedged wording (@1:08:05, @1:08:38).
- [[youtube-2022-10-11-makemore-4-backprop-ninja]]: Summary called the variance mismatch PyTorch's; it is the paper's, which PyTorch follows (@1:05:49, @1:07:31).
- [[activation-functions]]: credited the ±1.5, no-saturation result to a 0.2 weight scale; it belongs to 0.1, after which he relaxed to 0.2 (@24:48, @25:22).
- [[the-hockey-stick-loss-means-training-is-wasting-steps]]: presented garbled caption numbers (2.2 → 2.16) as fact; now uses his clean summary, 2.17 → 2.13 (@25:57).
- [[understand-backprop-even-with-autograd]]: listed RNN gradient problems as "already covered"; he says he is about to cover them (@01:37).
- [[training-diagnostics]]: step 6's cause (weights shrunk by 0.1) was stated at @1:42:39, not in the cited blocks; added.
- [[batch-normalization]]: "forcing a unit Gaussian always gives poor results" misplaced his "always"; now "forcing the activations to stay unit Gaussian throughout training gives poor results".
- [[deep-learning-is-largely-shape-gymnastics]]: said the WaveNet lecture had "one bug"; it has two on camera. Now "its shape bug"; first stamp moved to @32:15 where the view is written.
- [[pytorch-documentation-is-unreliable]]: the Note cited the WaveNet lecture for `torch.tensor`/`torch.var` complaints made in other lectures; shortened to point at [[pytorch]], citing only the general complaint here.
- [[youtube-2023-01-17-gpt-from-scratch]]: 1 MB figure is at @03:57; added to the citation.
- [[pretraining-and-finetuning]]: labelled the reward-model/PPO stage "RLHF" as if his term; he never uses it. Now described in his words, with the modern label marked as the wiki's.
- [[gpt-is-not-a-complicated-model]], [[github-2025-11-12-nanogpt-readme]]: the Note compared the minGPT README to the nanoGPT README's line count citing only the former; now cites both, with the nanoGPT README under `context` and in its Fed pages. The January-2023 dating remark is now a labelled Note.
- [[small-hackable-educational-code]], [[mingpt]]: said the direction change "is why he started" / "became" nanoGPT; the README only points to his rewrite nanoGPT. Now worded as the pointer.
- [[nanogpt]], [[ng-video-lecture]]: run-together Related bullets split; duplicate [[transformer-architecture]] dropped.
