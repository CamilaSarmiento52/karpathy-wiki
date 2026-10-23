# Verification: batch 1, group B (makemore README, makemore 5, minGPT README, GPT lecture, ng-video-lecture README)
Verified 2026-10-23 by a fresh reader. Sources: [[github-2022-11-20-makemore-readme]], [[youtube-2022-11-21-makemore-5-wavenet]], [[github-2023-01-08-mingpt-readme]], [[youtube-2023-01-17-gpt-from-scratch]], [[github-2023-01-31-ng-video-lecture-readme]]

## Coverage
- pages checked: 36 (5 source pages; claims gpt-is-not-a-complicated-model, pytorch-documentation-is-unreliable, deep-learning-is-largely-shape-gymnastics, attention-is-a-communication-mechanism, pretraining-gives-a-document-completer, avoid-batch-normalization-where-possible [WaveNet sentences only]; topics wavenet-hierarchical-model, tokenization, self-attention, transformer-architecture, pretraining-and-finetuning, bigram-language-model, character-level-language-modeling, batch-normalization, pytorch, regularization, embeddings, weight-initialization, overfitting-and-generalization, multilayer-perceptron, gradient-descent; methods small-hackable-educational-code, prototype-in-jupyter-then-repo, spelled-out-build-from-scratch, check-shapes-and-broadcasting, diagnose-under-or-overfitting, training-diagnostics; artifacts nanogpt, makemore, mingpt, ng-video-lecture), claim pages fully checked: 6, other sentences checked: ~95 of ~170
- Method: every claim quote grepped in the raw and read in its block; every cited `@time` in the claim pages read with its neighbours; the three READMEs read in full against every sentence citing them; for the two videos, every numeric, comparative or opinion-bearing sentence on the other pages read against its cited block(s) (about 60 blocks of t3YJ5hKiMQ0 and 55 of kCc8FmEb1nY).
- Special checks: GPT-2 "2017" misstatement at @06:12 is not repeated anywhere in wiki/ (grep clean); no page calls ChatGPT's finetuning RLVR (rlvr is linked as related only, with an explicit Note); minGPT §References is presented on [[transformer-architecture]] as "his reading notes on those papers, not statements about his own models" and nothing elsewhere lifts a paper number as his position; `mingpt` status superseded rests on the Jan-2023 semi-archived note plus "see my rewrite nanoGPT" (supported); `ng-video-lecture` status active rests on "For now I'm keeping it as is" plus his plan to push the init changes (supported, if thin).

## Findings
### F1 — overstated (minor) — [[deep-learning-is-largely-shape-gymnastics]]
- sentence: "The lecture itself is the example: the hierarchy is a `view` into (B, T//n, C*n) plus the same Linear layer, and its one bug was a BatchNorm reducing over the wrong dimensions of a 3-D input"
- cited: [[youtube-2022-11-21-makemore-5-wavenet]] @31:42, @40:32
- raw says: the shape bug is at @38:53–@42:49 as described, but the lecture hits a second on-camera bug at @15:30–@16:35 (BatchNorm left in training mode on a single example gives NaN). [[avoid-batch-normalization-where-possible]] itself says "That lecture hits two such bugs on camera". "its one bug" is wrong as a count.
- fix: "...and its shape bug was a BatchNorm reducing over the wrong dimensions of a 3-D input ([[youtube-2022-11-21-makemore-5-wavenet]] @32:15, @40:32)." (also move the first stamp from @31:42 to @32:15, where the (B, T//n, C*n) view is actually written)

### F2 — mis-cited — [[pytorch-documentation-is-unreliable]]
- sentence: "**Note:** earlier lectures made smaller versions of the same complaint, that `torch.tensor` versus `torch.Tensor` and `torch.var`'s `unbiased` default are unclear in the docs; those sentences are on [[pytorch]] ([[youtube-2022-11-21-makemore-5-wavenet]] @52:51)."
- cited: [[youtube-2022-11-21-makemore-5-wavenet]] @52:51
- raw says: @52:51 is the general complaint only ("it will lie to you it will be wrong it will be incomplete"); nothing in this video mentions torch.tensor/torch.Tensor or torch.var's unbiased default. The citation supports none of the specifics; a sentence comparing sources must cite both (§5).
- fix: cite the earlier lecture pages that carry those two complaints as they are cited on [[pytorch]] (the makemore-1 and makemore-3 source pages), e.g. "**Note:** earlier lectures made smaller versions of the same complaint ... ([[youtube-2022-09-07-makemore-1-bigram]] @…; [[youtube-2022-10-04-makemore-3-activations-batchnorm]] @…; [[youtube-2022-11-21-makemore-5-wavenet]] @52:51)", and list them under `context` in frontmatter; or shorten to "**Note:** [[pytorch]] collects his earlier, smaller complaints about the same docs (@52:51 is the general one)."

### F3 — mis-cited (minor) — [[youtube-2023-01-17-gpt-from-scratch]]
- sentence: "A 1h56m coding lecture that writes a character-level Transformer language model from an empty file, training on the 1 MB tiny Shakespeare text (@03:23, @06:45)."
- cited: @03:23, @06:45
- raw says: "this file is about 1 megab" is in the @03:57 block (and again @07:50, "about a 1 Megabyte file ... 1 million characters"); @03:23 proposes tiny Shakespeare without the size, @06:45 says the lecture will train on it.
- fix: cite "(@03:23, @03:57, @06:45)".

### F4 — minor — [[pretraining-and-finetuning]]
- sentence: "Anything that is not a plain document completer, such as task performance, alignment or sentiment, requires further finetuning stages, simple supervised or RLHF-style ([[youtube-2023-01-17-gpt-from-scratch]] @1:55:22, @1:55:55)." and, in Related, "**Note:** the lecture describes the 2023 recipe of pretraining, supervised finetuning and RLHF; ..."
- cited: @1:55:22, @1:55:55 (and @1:52:36–@1:53:43 for the recipe)
- raw says: he never uses the term RLHF or "human feedback" anywhere in the transcript (grep: 0 hits); he says "simple supervised fine tuning or ... train a reward model and then do rounds of PPO". The label is the wiki's, placed as if it were his.
- fix: "...simple supervised finetuning or, as in ChatGPT, a reward model with rounds of PPO (...)". In the Note: "pretraining, supervised finetuning and reward-model/PPO finetuning (the recipe now called RLHF; he does not use the term)". Not wrong on substance; the term should not read as his.

### F5 — mis-cited (minor) — [[gpt-is-not-a-complicated-model]]
- sentence: "**Note:** the [[nanogpt]] README makes the same point in code size, a roughly 300-line model file, without stating the claim; a later claim page could carry it ([[github-2023-01-08-mingpt-readme]] §intro)."
- cited: [[github-2023-01-08-mingpt-readme]] §intro
- raw says: the minGPT README says nothing about the nanoGPT README's line count; the "roughly 300-line" figure for nanoGPT comes from [[github-2025-11-12-nanogpt-readme]] §intro (as [[nanogpt]] cites it). A comparison must cite both sides.
- fix: add "([[github-2023-01-08-mingpt-readme]] §intro; [[github-2025-11-12-nanogpt-readme]] §intro)" and list the nanoGPT README under `context`. Also in Context, the sentence "The README is dated by its January 2023 snapshot; the repo itself is older" is the wiki's dating remark, not something the README says; prefix with **Note:** or move it to the line under the H1 as the source page does.

### F6 — overstated (minor) — [[small-hackable-educational-code]], [[mingpt]]
- sentence: step 5 "Once minGPT was widely referenced, large changes became harder, and education-only code lacked the teeth to reproduce benchmarks, which is why he started nanoGPT"; and on [[mingpt]] "...accepting some tradeoffs for runtime efficiency, which became nanoGPT"
- cited: [[github-2023-01-08-mingpt-readme]] §intro
- raw says: he says minGPT is semi-archived, "for more recent developments see my rewrite nanoGPT", and that he "wanted to change the direction a bit ... to something that is still simple and hackable but has teeth". He does not say this is why nanoGPT was started, nor that the direction change "became" nanoGPT; the link is strongly implied but not stated.
- fix: "...and he points to his rewrite nanoGPT for the direction he wanted instead" (method step 5); "...accepting some tradeoffs for runtime efficiency; he points to his rewrite nanoGPT for more recent developments" ([[mingpt]]).

### F7 — minor — [[nanogpt]], [[ng-video-lecture]]
- sentence: Related lists have run-together bullets: "- [[weight-initialization]]- [[ng-video-lecture]] — ...", "- [[self-attention]], [[transformer-architecture]], [[pretraining-and-finetuning]]- [[mingpt]] — ...", "- [[small-hackable-educational-code]]- [[nanochat]]" (nanogpt) and "- [[small-hackable-educational-code]] — published to be hacked, with its history- [[nanogpt]] — ..." (ng-video-lecture); [[transformer-architecture]] is listed twice on nanogpt.
- cited: n/a (formatting)
- raw says: n/a
- fix: split each into separate "- " lines; drop the duplicate [[transformer-architecture]].

## Checked and correct
- [[github-2022-11-20-makemore-readme]]: Summary and 3 Key points, all supported by §intro/§Usage (200K params, 32K names, ssa.gov 2018, MacBook Air, CNN "in progress").
- [[youtube-2022-11-21-makemore-5-wavenet]]: Summary (14 stamps) and 11 Key points, all supported; 2.10→2.02, 22,000, 2.029 vs 2.027, 2.022, 76,000, 1.993, 12,000 all at the cited blocks.
- [[github-2023-01-08-mingpt-readme]]: Summary and 6 Key points, all supported; "sprawling", "teeth", three files, demos, §References described as his notes.
- [[youtube-2023-01-17-gpt-from-scratch]]: Summary (apart from F3) and 13 Key points, all supported; 1.48 / 15 min / A100 at @1:40:21.
- [[github-2023-01-31-ng-video-lecture-readme]]: Summary and 4 Key points, all supported.
- [[gpt-is-not-a-complicated-model]]: quote verbatim §intro; title no stronger than the README; Context 2 sentences supported; `stated` correct (F5 is the Note only).
- [[pytorch-documentation-is-unreliable]]: quote verbatim @52:51; title matches "no one is maintaining any documentation it will lie to you"; Context 2 sentences supported at @52:15/@52:51; `stated` correct (F2 is the Note only).
- [[deep-learning-is-largely-shape-gymnastics]]: quote verbatim @53:24; title matches "a ton of trying to make the shapes work"; Context sentences 1–2 supported ("promoting" caption garble corrected to "permuting" outside quotes, fine); `stated` correct (F1 is sentence 3).
- [[attention-is-a-communication-mechanism]]: quote verbatim @1:11:26; 5 Context sentences all supported at @1:11:26–@1:13:03, @1:15:19, @1:43:07; `stated` correct.
- [[pretraining-gives-a-document-completer]]: quote verbatim @1:51:29; title supported ("you don't get something that responds to your questions ... you get a document completer"); 4 Context sentences supported (@1:50:56 nearly identical; @1:55:22 10,000–1M×; @1:54:16 internal data, nanoGPT pretraining only); Note on rlvr correctly marked as related only; `stated` correct.
- [[avoid-batch-normalization-where-possible]]: 2 WaveNet sentences (@03:52/@04:25 state is harmful; @16:03/@40:32 two bugs), supported.
- [[wavenet-hierarchical-model]]: 14 sentences checked (2016 WaveNet, two consecutive elements, +10,000 params, 2.10→2.02, (4,5,80)→(4,5,200), (4,4,20), even/odd concat = view, FlattenConsecutive naming, shape chain, receptive field 8 vs 16, no gated/residual/skip, 22,000 / 2.029 vs 2.027, 1.993, "embarrassing" @55:40, convolution for efficiency, variable reuse), all supported.
- [[batch-normalization]]: 6 WaveNet sentences, all supported (NaN on single example, (1,4,68) running mean, tuple dims, (N,C,L) vs channels-last, 2.029→2.022 "not statistically significant").
- [[pytorch]]: 9 WaveNet sentences, all supported (global RNG @04:59, Embedding/Flatten kwargs @11:03, 200×1000 view @08:17, matmul over leading dims @24:52, re-implemented torch.nn @51:42, docs @52:51).
- [[overfitting-and-generalization]]: 3 sentences (2.05 vs 2.10 @17:09; watch both losses @47:13; @55:40), all supported.
- [[multilayer-perceptron]]: 2 sentences (@00:33/@19:56; @55:40), supported.
- [[gradient-descent]]: 1 sentence (@46:42, @54:32), supported.
- [[check-shapes-and-broadcasting]]: 6 steps (scratch batch of four @21:34/@22:06; print class+shape @35:06; break after one step @12:10/@19:56/@44:28; runs ≠ correct @38:20/@39:26; explicit view/squeeze @32:49/@33:56; re-run cells @15:30), all supported.
- [[diagnose-under-or-overfitting]]: 5 steps (@17:09; 68 units → 22,000; clean run; 2.029 vs 2.027 with bug caveat; both losses), all supported.
- [[prototype-in-jupyter-then-repo]]: definition and 5 steps, all supported at @52:15–@55:06; the quick-experiment-loop Note is correctly labelled as the wiki's connection.
- [[character-level-language-modeling]]: 3 README sentences, supported.
- [[small-hackable-educational-code]]: definition and steps 1–4, 6–7 supported (F6 is step 5); the Hugging Face "90% unused code" criticism is in §References as cited.
- [[tokenization]]: 7 sentences (definition @09:31; 65 chars; SentencePiece/tiktoken "usually adopted in practice"; ~50,000 tokens and "hi there" 3 vs 8 integers @11:43; trade-off; simplest thing; 300,000 tokens @1:49:47; minGPT bpe.py §intro), all supported.
- [[bigram-language-model]]: 6 GPT-lecture sentences (simplest possible neural network "in my opinion" @21:57; AdamW, ~2.5; translation invariant @1:01:20), all supported.
- [[training-diagnostics]]: 4 sentences (4.17 expected vs 4.87 @28:03/@28:37; estimate_loss; eval/train mode as practice; no_grad), all supported.
- [[spelled-out-build-from-scratch]]: steps 14–20 (loss ladder 2.5/2.4/2.28/2.24/2.08/2.06/1.48 at the cited stamps; "self attention can't tolerate very very high learning rates" @1:21:27; 120-line bigram.py @41:36), all supported.
- [[self-attention]]: 12 sentences spot-checked (vowel/consonant @1:03:36; bias=False @1:04:45–@1:05:18; private information/communicate @1:10:53; variance ~head size 16 @1:17:34; buffer @1:19:15; 2.5→2.4; 2.28; group convolution @1:23:08; cross-attention @1:15:55/@1:16:28; nanoGPT batched heads @1:47:36), all supported.
- [[transformer-architecture]]: 11 sentences (minGPT framing §intro; §References paragraph correctly framed as his paper notes with the figures matching the README; stacking blocks "doesn't actually give a very good result" @1:28:02; 2015 residual paper; ×4 inner layer 512→2048; 2.08 with "a little bit of overfitting"; pre-norm "slight deviation" @1:35:19; 2.06; "exactly as done in GPT" @1:45:55; GPT-3 nearly identical), all supported.
- [[regularization]]: 3 sentences (2014 paper, ensemble, placement, dropout 0.2 before scaling), supported.
- [[embeddings]]: 3 sentences, supported.
- [[pretraining-and-finetuning]]: 11 sentences supported apart from the RLHF label (F4): two stages @1:48:42; 10M params / 1M chars / 300,000 tokens; 175B / 300B tokens / millionfold; thousands of GPUs; thousands of examples; sample efficient; PPO "a form of policy gradient reinforcement learning optimizer"; internal to OpenAI.
- [[weight-initialization]]: 2 README sentences, supported.
- [[makemore]]: 11 sentences citing group-B sources (12,000 params and "name-like results that do not exist in a training set" @05:33–@06:40; 2.02 / 76,000 / 1.993; the beat-1.993 invitation list @55:06–@56:12; future-lecture list @53:57–@55:06; all README facts incl. test logprob ~1.92), all supported.
- [[mingpt]]: 9 sentences, all supported by the README (F6 is the "which became nanoGPT" tail only).
- [[nanogpt]]: 5 group-B sentences (two files of 300 lines, GPT-2 124M reproduction @05:36/@06:12 without the "2017" slip; train.py features @1:46:28; batched heads, GELU "because OpenAI used it and I want to be able to load their checkpoints", weight-decay split @1:47:36/@1:48:10; pretraining focus @1:54:16; `_init_weights` from the README), all supported.
- [[ng-video-lecture]]: 9 sentences (Colab in the description @07:50; 120 lines @41:36; hyperparameters at top/GPU/estimate_loss @37:41–@39:56; 6 layers/384/6 heads/256/64/0.2 and 1.48 in ~15 min on his A100 @1:39:13–@1:40:21; "I would not run this on a CPU or MacBook" @1:40:54; ~200 lines with git log @1:54:50; all README caveats), all supported.
