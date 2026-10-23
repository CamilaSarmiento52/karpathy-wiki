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
