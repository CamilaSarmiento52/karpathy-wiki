# Batch 2 merge map

Decided 2026-10-24 after reading every digest's candidate list. Same rules as batch 1
(`staging/batch-1-merge-map.md`): merge creates ONLY the pages named here (plus source
pages). Every other digest candidate becomes sentences on the page its "→" names. Existing
pages are extended, never duplicated. The index is split: add new pages to their type file
in `wiki/index/`.

## Source pages (slugs fixed by the digests) and merge groups

| group | raw stem | source slug |
|---|---|---|
| C1 | XfpMkf4rD6E | talk-2023-05-19-stanford-cs25-transformers |
| C1 | bZQun8Y4L2A | talk-2023-05-25-state-of-gpt |
| C1 | karpathy__karpathy | github-2023-07-25-karpathy-profile-readme |
| C1 | zjkBMFhNj_g | youtube-2023-11-23-intro-to-llms |
| C2 | karpathy__nn-zero-to-hero | github-2024-02-20-nn-zero-to-hero-readme |
| C2 | zduSFxRajkE | youtube-2024-02-20-gpt-tokenizer |
| C2 | 1760388761349927356 | x-2024-02-21-technical-accessibility |
| C2 | c3b-JASoPi0 | talk-2024-03-26-sequoia-making-ai-accessible |
| C2 | karpathy__minbpe | github-2024-04-22-minbpe-readme |
| C3 | karpathy__llm.c__discussion-84 | github-2024-04-12-llmc-discussions-welcome |
| C3 | karpathy__llm.c__discussion-224 | github-2024-04-22-llmc-state-of-the-union |
| C3 | karpathy__llm.c__discussion-344 | github-2024-05-03-llmc-state-of-the-union |
| C3 | karpathy__llm.c__discussion-454 | github-2024-05-24-llmc-pytorch-cross-checks |
| C3 | karpathy__llm.c__discussion-481 | github-2024-05-28-llmc-gpt-2-124m |
| C3 | karpathy__llama2.c | github-2024-05-29-llama2c-readme |
| C3 | karpathy__calorie | github-2024-05-30-calorie-readme |
| C4 | l8pRSuU81PU | youtube-2024-06-09-reproduce-gpt-2 |
| C4 | karpathy__llm.c__discussion-580 | github-2024-06-12-llmc-gpt-2-774m |
| C4 | karpathy__build-nanogpt | github-2024-06-17-build-nanogpt-readme |
| C4 | tsTeEkzO9xc | talk-2024-07-03-berkeley-hackathon-keynote |
| C4 | karpathy__llm.c__discussion-677 | github-2024-07-11-llmc-gpt-2-1-6b |

Groups run in this order, one at a time, lint clean before the next. Within a group,
sources go in published order.

## New topics (11)

| slug | absorbs | aliases | group that creates it |
|---|---|---|---|
| prompting-llms | prompting-llms, in-context-learning, transformers-are-capable-of-in-context-learning | Prompting, in-context learning, few-shot prompting, chain of thought, prompt engineering | C1 |
| llm-tool-use | tool-use-and-retrieval, llm-tool-use, tool-use-is-a-major-source-of-llm-capability | Tool use, retrieval, retrieval-augmented generation, RAG, browsing, code interpreter | C1 |
| scaling-laws | scaling-laws; Sequoia scale-matters-most-but-is-not-enough (sentences + **Note:** on the claim) | Scaling laws, scale, model size, compute | C1 |
| system-1-and-system-2-thinking | system-1-and-system-2-thinking | System 1, System 2, thinking longer, reasoning | C1 |
| llm-self-improvement | llm-self-improvement; Sequoia llms-have-done-only-step-one-of-alphago, rlhf-is-a-weak-form-of-rl | Self-improvement, AlphaGo step two, reinforcement learning beyond RLHF | C1 |
| llm-security | llm-security, llm-security-is-a-cat-and-mouse-game | LLM security, jailbreaks, prompt injection, data poisoning, sleeper agents | C1 |
| sampling-from-language-models | sampling (llama2.c), he-does-not-love-autoregressive-sampling context, diffusion-and-autoregressive-models-should-meet | Sampling, temperature, top-p, autoregressive sampling, diffusion | C1 |
| ai-ecosystem | ai-ecosystem, he-cares-about-the-ecosystem-more-than-any-company | AI ecosystem, open weights, open source AI, coral reef | C2 |
| compute-efficiency | compute-efficiency (Sequoia), training-efficiency (GPT-2 lecture), gpu-training-efficiency and training-compute-budget (llm.c Discussions), use-torch-compile-by-default, use-nice-numbers-in-neural-network-code, batch-size-ramp, quantization (llama2.c) | Compute efficiency, training efficiency, mixed precision, bfloat16, TF32, torch.compile, flash attention, distributed data parallel, DDP, quantization | C2 |
| elon-musk-management-style | elon-musk-management-style, founders-can-copy-elons-style-only-from-the-start | Elon Musk, running companies, small teams | C2 |
| llm-evaluation | llm-evaluation (GPT-2 lecture, llm.c Discussions) | Evaluation, HellaSwag, benchmarks, eval | C3 |

For `sampling-from-language-models`: move the alias "sampling" off
`character-level-language-modeling` (whose page keeps its bigram sampling sentences) and
link the two pages. Create it in C1 from the CS25 talk; C3 adds llama2.c's temperature
and top-p.

Folded into EXISTING topics (no new page):
- base-models-vs-assistant-models, lossy-compression-of-the-internet, pretraining-data,
  rlhf-models-lose-entropy → `pretraining-and-finetuning` (sections; it is the main page
  for how LLMs are trained). The lecture-era note that he does not use the term RLHF is
  expanded: he names RLHF in Intro to LLMs (@22:09) and in State of GPT.
- transformers-are-flexible-about-their-inputs, the-transformer-has-proven-remarkably-resilient,
  history of the architecture → `transformer-architecture`.
- the-tokenizer-is-a-separate-stage-from-the-llm, vocabulary-size-is-an-empirical-hyperparameter,
  leave-raw-text-unnormalized-for-llms → `tokenization`.
- adamw-is-a-bug-fix-of-adam, gradient-clipping-is-a-patch-on-deeper-issues,
  choose-training-hyperparameters (llama2.c) → `gradient-descent`.
- Kernel vs CPU wording, 1960s vs 1970s–80s vs 1980s comparisons → `llms-as-operating-systems`
  (a dated sentence each; differences are wording, not a change of view).
- Reversal curse, prompt injection (Intro to LLMs) → `jagged-intelligence` as `context`
  only: he does not use the word "jagged" in 2023. Do not move `first_seen`.

## New claims (27, plus the llm.c rows below)

| slug | from | folds in / relation |
|---|---|---|
| ai-has-converged-on-one-architecture | CS25 | |
| the-transformer-is-a-general-purpose-efficient-optimizable-computer | CS25 | the-transformer-has-proven-remarkably-resilient |
| gpt-is-a-general-purpose-computer-running-natural-language-programs | CS25 | supports [[english-is-the-new-programming-language]] (both sides cited) |
| with-enough-data-encode-less-inductive-bias | CS25 | |
| he-does-not-love-autoregressive-sampling | CS25; Sequoia as second source | diffusion-and-autoregressive-models-should-meet |
| transformers-need-tokens-to-think | State of GPT | |
| llms-want-to-imitate-not-succeed | State of GPT | |
| rlhf-works-better-because-comparing-is-easier-than-generating | State of GPT | |
| use-llms-as-copilots-with-human-oversight | State of GPT | supports [[this-is-the-decade-of-agents]] |
| an-llm-is-just-two-files | Intro to LLMs | |
| pretraining-is-lossy-compression-of-the-internet | Intro to LLMs | next-word-prediction-forces-learning-about-the-world |
| llms-are-mostly-inscrutable-empirical-artifacts | Intro to LLMs | |
| scaling-offers-a-guaranteed-path-to-better-models | Intro to LLMs | Sequoia's "scale is not enough" is a **Note:** + sentence on scaling-laws, not a relation |
| llms-currently-only-have-a-system-1 | Intro to LLMs | |
| self-improvement-may-be-possible-in-narrow-domains | Intro to LLMs; Sequoia as second source | llms-have-done-only-step-one-of-alphago |
| llms-are-the-kernel-of-an-emerging-operating-system | Intro to LLMs | topic llms-as-operating-systems |
| a-lot-of-llm-oddness-traces-back-to-tokenization | tokenizer lecture; nn-zero-to-hero README as second source | |
| tokenization-free-modeling-would-be-amazing-but-is-unproven | tokenizer lecture | |
| he-prefers-tiktoken-byte-level-bpe-to-sentencepiece | tokenizer lecture | |
| open-weights-models-are-not-open-source | Sequoia | |
| build-the-ramp-not-just-the-thing | Sequoia; X post as second source | |
| ai-is-far-less-energy-efficient-than-the-brain | Sequoia | topic compute-efficiency |
| the-transformer-is-probably-not-the-final-architecture | Sequoia | **Note:** against the CS25 resilience claim; both can hold, no relation |
| llm-products-will-take-years-to-figure-out | Sequoia | supports [[this-is-the-decade-of-agents]] (weak: say "a few years", not "a decade") |
| small-llms-can-be-strong-in-narrow-domains | llama2.c | he-expects-demand-for-custom-micro-llms-at-the-edge |
| memory-access-not-flops-limits-training-speed | GPT-2 lecture | topic compute-efficiency |
| inherited-gpt-3-hyperparameters-look-conservative | whichever of llm.c 481 or the GPT-2 lecture states it first creates it; later sources are added | folds gpt-3-paper-hyperparameters-look-suboptimal |
| his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag | llm.c 481 (C3) first; GPT-2 lecture, 580, 677 added in C4 | folds his-gpt-2-reproduction-beat-the-checkpoint-on-fewer-tokens; say which model size and token count each source reports; the $10 / one-hour cost goes on build-nanogpt |
| small-projects-can-snowball | Berkeley | |
| success-comes-from-repeated-practice | Berkeley | |
| physical-automation-will-lag-digital-automation | Berkeley | |

| llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements | llm.c Discussions (C3) | "in his measurements" stays in the title |
| gpt-2-is-the-first-recognizably-modern-llm-stack | llm.c Discussions (C3) | |
| neural-net-training-should-not-be-complicated | llm.c Discussions | supports [[gpt-is-not-a-complicated-model]]; Note to [[micrograd-is-all-you-need-everything-else-is-efficiency]] |
| do-not-decay-the-learning-rate-to-zero | llm.c 580 (C4) | his practice across 481 (decays to 0), 580 (says not to) and 677 (decays to 10%) is stated as dated sentences on this claim and on gradient-descent; no timeline |
| llm-c-was-not-yet-careful-enough-about-training-stability | llm.c 677 (C4) | **Note:** only to modern-innovations-make-precise-initialization-less-important; not a contradiction |

(36 rows.) Dropped as claims: rlhf-models-lose-entropy, tool-use-is-a-major-source…,
llm-security-is-a-cat-and-mouse-game, the vocabulary / normalisation / separate-stage
tokenizer claims, founders-can-copy-elons-style, he-cares-about-the-ecosystem,
rlhf-is-a-weak-form-of-rl, scale-matters-most-but-is-not-enough, use-torch-compile-by-default,
use-nice-numbers, gradient-clipping-is-a-patch, batch-size-ramp, adamw-is-a-bug-fix,
he-expects-demand-for-custom-micro-llms. Each becomes a cited sentence on the page named
above.

`supports` to EXISTING claims (set on both pages, both sides cited, in the group that
writes the new side): pretraining-gives-a-document-completer gains State of GPT, Intro to
LLMs, build-nanogpt and the GPT-2 lecture as supporting sources (add them to that claim's
`sources`; no new claim page). attention-is-a-communication-mechanism gains CS25.
understand-backprop-even-with-autograd and deep-learning-is-largely-shape-gymnastics gain
the nn-zero-to-hero README only if its text says so; otherwise skip. No `contradicts` is
expected. No `extends` is planned; if a merge agent finds a real one, it must add the
timeline entry too.

## New methods (4)

Groups (added after C1): make-it-work-then-make-it-cheap and
verify-against-a-reference-implementation in C2 (the first also cites State of GPT, which
C1 merged; add it to that source's Fed pages); reproduce-a-published-model in C3 (from
llm.c 481); build-and-publish-projects in C4.

| slug | absorbs |
|---|---|
| make-it-work-then-make-it-cheap | top-performance-then-optimize (State of GPT), make-it-work-then-make-it-cheap (Sequoia) |
| verify-against-a-reference-implementation | minbpe vs tiktoken, llama2.c vs the PyTorch reference, the llm.c cross-checks (454: two whole training runs match), benchmark-against-pytorch (llm.c speed comparisons); Related → [[verify-gradients-against-pytorch]] (that one is about gradients) |
| reproduce-a-published-model | GPT-2 lecture, llm.c GPT-2 Discussions |
| build-and-publish-projects | Berkeley keynote |

keep-long-training-runs-alive (llm.c 677) → steps on `training-diagnostics`.
llm.c Discussions never mention nanoGPT: do not cite them on `nanogpt`. Most cite as
`§intro`; add the bold paragraph label when the digest gives one, e.g. `§intro (Training)`.

Existing methods extended: spelled-out-build-from-scratch (tokenizer, minbpe, build-nanogpt,
GPT-2 lecture), small-hackable-educational-code (minbpe, llama2.c, X post, nn-zero-to-hero),
training-diagnostics, diagnose-under-or-overfitting, prototype-in-jupyter-then-repo (GPT-2
lecture).

## New artifacts (6)

| slug | repo_url | language | status | created by |
|---|---|---|---|---|
| nn-zero-to-hero | https://github.com/karpathy/nn-zero-to-hero | Python | active (only if the README supports it; otherwise as the README says) | C2 |
| minbpe | https://github.com/karpathy/minbpe | Python | from its README | C2 (tokenizer lecture first, README same group) |
| llm-c | https://github.com/karpathy/llm.c | C / CUDA | from the Discussions | C3 |
| llama2c | https://github.com/karpathy/llama2.c | C | from its README | C3 |
| calorie | https://github.com/karpathy/calorie | from its README | from its README | C3 |
| build-nanogpt | https://github.com/karpathy/build-nanogpt | Python | from its README | C4 |

`llm101n` is deferred to batch 3, where its README is; the Berkeley mention becomes a
sentence on build-and-publish-projects. Existing artifacts extended: nanogpt, micrograd,
makemore, mingpt where the sources mention them.

**Profile README** (`github-2023-07-25-karpathy-profile-readme`): five words, feeds no
page on its own. Cite it once as `context` on `nn-zero-to-hero` with a labelled **Note:**
sentence, so its source page has an inbound link. Do not create a page for it.

## New timelines (2)

| slug | topic | entries | group |
|---|---|---|---|
| llm-agents-over-time | [[partial-autonomy-apps]] | 2023-05-25 copilots with oversight (State of GPT); 2024-03-26 products will take years (Sequoia); 2025-06-19 decade of agents (existing); 2025-12-19 Claude Code first convincing agent (existing) | C2 |
| llm-os-over-time | [[llms-as-operating-systems]] | 2023-11-23 kernel process; 2024-03-26 Sequoia; 2024-07-03 1980s comparison (Berkeley); 2025-06-19 1960s (existing); 2025-12-19 (existing) | C4 |

Each entry is dated and cited. The closing line, if any, is a labelled **Note:**. A timeline
does not by itself mean he changed his mind; say so where views only accumulate.
