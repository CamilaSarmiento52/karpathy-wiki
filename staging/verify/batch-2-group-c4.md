# Verification: batch 2, group C4 (GPT-2 lecture, llm.c 580, build-nanogpt README, Berkeley keynote, llm.c 677)
Verified 2026-10-24 by a fresh reader. Sources: [[youtube-2024-06-09-reproduce-gpt-2]], [[github-2024-06-12-llmc-gpt-2-774m]], [[github-2024-06-17-build-nanogpt-readme]], [[talk-2024-07-03-berkeley-hackathon-keynote]], [[github-2024-07-11-llmc-gpt-2-1-6b]]

## Coverage
- Fed pages: every `## Fed pages` list matches the pages that cite that source (fixed files left out). Checked by grep for all five.
- Pages checked: 46. These are the 5 source pages, 14 claim pages, 1 timeline, 9 topics (compute-efficiency, gradient-descent, llm-evaluation, transformer-architecture, weight-initialization, embeddings, pytorch, pretraining-and-finetuning, llms-as-operating-systems), 6 more topics by sample (tokenization, activation-functions, regularization, overfitting-and-generalization, loss-functions, sampling-from-language-models), 3 artifacts (build-nanogpt, nanogpt, llm-c) and 8 methods (reproduce-a-published-model, training-diagnostics, verify-against-a-reference-implementation, small-hackable-educational-code, spelled-out-build-from-scratch, prototype-in-jupyter-then-repo, diagnose-under-or-overfitting, build-and-publish-projects).
- Claim pages fully checked: 14. Eight are new in C4: memory-access-not-flops-limits-training-speed, his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag, do-not-decay-the-learning-rate-to-zero, llm-c-was-not-yet-careful-enough-about-training-stability, neural-net-training-should-not-be-complicated, small-projects-can-snowball, success-comes-from-repeated-practice and physical-automation-will-lag-digital-automation. Six existing claims gained these sources: inherited-gpt-3-hyperparameters-look-conservative, llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements, pytorch-documentation-is-unreliable, pretraining-gives-a-document-completer, gpt-is-not-a-complicated-model and attention-is-a-communication-mechanism. Every quote was grepped and is verbatim and his. Whitespace was normalised for the Berkeley caption wraps.
- Timeline entries checked: 5 of 5 on llm-os-over-time, plus its closing Note. The earlier sources were checked against their raw files: zjkBMFhNj_g @42:06/@42:38, c3b-JASoPi0 @04:05/@04:39, LCEmiRjPEtQ @08:54–@11:05 and year-in-review-2025 §6.
- Other sentences checked: about 135 of about 330 citing these sources. For the GPT-2 lecture, about 70 of about 190 citing sentences were checked against the raw blocks, more than one in five. Every number in the compute-efficiency speed-up sequence was included.
- Berkeley boundary: every Berkeley citation in the wiki falls between @04:14 and @21:39. Nothing from the host, judges or pitches is attributed to him, and the garbled "just below 1 billion" figure is not repeated.

## Findings
### F1 — overstated — [[build-nanogpt]] (also [[compute-efficiency]])
- sentence: "**Note:** his own on-camera run of 19,073 steps over 10B tokens on eight A100s took about 1.7 hours" (build-nanogpt). On compute-efficiency: "a step took about 330 ms and the 19,073-step run about 1.7 hours".
- cited: [[youtube-2024-06-09-reproduce-gpt-2]] @3:22:06
- raw says: the 1.7 hours is his projection at launch, 19,073 × 0.33 s, "so this will run for 1.7 hours". Later he says one epoch "took roughly two hours" (@3:48:43). The video never reports a measured 1.7 h.
- fix: on build-nanogpt, "**Note:** at launch he projected his on-camera run of 19,073 steps over 10B tokens on eight A100s at about 1.7 hours; he later says the epoch took roughly two hours ([[youtube-2024-06-09-reproduce-gpt-2]] @3:22:06, @3:48:43)." On compute-efficiency, "...a step took about 330 ms, and he projected the 19,073-step run at about 1.7 hours" (same citation).

### F2 — mis-cited — [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- sentence 1: "His lecture run, trained for one epoch of FineWeb-Edu's 10B-token sample, rose from 25% on HellaSwag past OpenAI's GPT-2 124M, which his script scores at 29.55%; he does not read out his own final score at 10B (@3:37:16, @3:44:15, @3:44:50)."
- sentence 2: "An overnight four-epoch run of about 40B tokens reached 33.24, almost GPT-3 124M, which he says trained on 300B tokens (@3:48:43, @3:49:15, @3:52:37)."
- raw says: @3:37:16 says "29.5%". The 29.55 figure ("2955") is at @3:37:48. The one epoch of the 10B sample is at @3:43:41. GPT-3 124M on 300B tokens is at @3:44:15/@3:44:50 and @3:50:56, not in the blocks cited. The content is right.
- fix: sentence 1 cites (@3:37:16, @3:37:48, @3:43:41, @3:44:15, @3:44:50). Sentence 2 cites (@3:44:50, @3:48:43, @3:49:15, @3:50:56, @3:52:37).

### F3 — minor — [[do-not-decay-the-learning-rate-to-zero]]
- sentence (a): "**Note:** the PyTorch run in the GPT-2 lecture, published 2024-06-09, already decayed to 10% at its last step, following the GPT-3 paper; that lecture does not discuss decaying to zero (@2:24:59; 580 §intro (Reflections))."
- raw says: the 10% decay at @2:24:59 is correct. But at @2:21:02 he says of the plotted schedule that "here the minimum learning rate is zero" before giving the paper's 10%. Zero is mentioned, though not argued against.
- fix (a): "...following the GPT-3 paper; the lecture mentions a zero minimum only on the schedule plot it starts from, and does not argue for or against decaying to zero ([[youtube-2024-06-09-reproduce-gpt-2]] @2:21:02, @2:24:59; [[github-2024-06-12-llmc-gpt-2-774m]] §intro (Reflections))."
- sentence (b): "...no earlier claim page said to decay to zero, so no `contradicts` or `extends` is set (580 §intro (Reflections); 481 §intro (Args guide))."
- issue: this is wiki-editorial reasoning sitting unlabelled inside a cited evidence paragraph. Neither cited source says anything about claim pages.
- fix (b): split it out as "**Note:** no earlier claim page said to decay to zero, so no `contradicts` or `extends` is set." The rest of the paragraph stays as it is.
- The dated-practice sentences are correct on both this page and [[gradient-descent]]: 481 `-q 0.0`, 580 "We shouldn't decay the LR to 0%", 677 `-q 0.1`, and the lecture's 10% at @2:24:59/@2:25:33.

### F4 — mis-cited — [[llm-os-over-time]]
- sentence: "**2025-06-19** — The operating system is the analogy he finds strongest, at roughly the 1960s of computing: expensive, centralised, time-shared ([[youtube-2025-06-19-software-is-changing]] @08:54, @10:34)"
- raw says: @08:54 has the operating-system analogy ("makes the most sense perhaps") and @10:34 has "1960sish". The expensive, centralised in the cloud and time-sharing part is in @11:05.
- fix: cite (@08:54, @10:34, @11:05). In the closing Note, "kernel (2023) against CPU (2024, 2025)" rests on the 2025 "CPU equivalent" at @10:01, which the Note does not cite. Add `[[youtube-2025-06-19-software-is-changing]] @10:01` to its citation.
- The other four entries are correct: 2023-11-23 at @42:06/@42:38, 2024-03-26 at @04:05/@04:39, 2024-07-03 at @06:10/@06:49 and 2025-12-19 at §6 ("1970s, 80s, etc.").

### F5 — mis-cited — [[tokenization]]
- sentence: "The GPT-2 tokenizer compresses English roughly 3:1, so 1,000 characters is about 300 tokens, and tiny Shakespeare's roughly 1M characters became 338,000 tokens (@46:06, @1:05:47)."
- raw says: "338,000 tokens" is in block @1:05:12; @1:05:47 has the "1 million characters".
- fix: cite (@46:06, @1:05:12, @1:05:47).

### F6 — minor — [[small-projects-can-snowball]]
- sentence: "**Note:** he joins this to [[success-comes-from-repeated-practice]] and [[build-and-publish-projects]] in his closing summary: publishing keeps you rewarded, which builds the hours that let a small snowball become a big one (@21:39)."
- raw says: the reward-to-hours-to-snowball link begins in @21:02 ("the way that this comes together is you are getting your dopamine") and ends in @21:39. Also, this is his statement, not a connection the wiki made, so the **Note:** label is not needed. Leaving it is harmless.
- fix: cite (@21:02, @21:39).

### F7 — minor — [[training-diagnostics]]
- sentence: "In the same log he expects the gradient norm to stabilise around 0.1–1 while the learning rate warms up, and uses validation loss as a sanity check rather than the comparison (677 §intro (Training), §intro (Evals))."
- raw says: these are two separate observations: "The norm will stabilize around 0.1-1, the learning rate is being warmed up over the first few steps." Joining them with "while" ties the norm's level to the warmup.
- fix: "In the same log he expects the gradient norm to stabilise around 0.1–1, with the learning rate warming up over the first few steps, and uses validation loss as a sanity check rather than the comparison (same citations)."

## Checked and correct
- [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]: every size, token count and score was checked against each source. 124M/10B: 29.9 vs 29.4, GPT-3 Small 33.7, 300B (481). Lecture 124M/10B: 29.55, 25% start, GPT-2 at 100B per him, 40B run 33.24, about 10× (correct apart from F2). 774M/150B: no score and no eval named in the text, which the page says. 1558M/33.6B: crossover at about 25K steps, GPT-2 at about 100B, GPT-3 at 300B and about 10X, 57.7 / 62.7, 420B run at about 61%. The title holds and confidence `stated` is right.
- [[memory-access-not-flops-limits-training-speed]]: 5 sentences and the quote are correct (@1:27:04/@1:27:38 idle tensor cores and 60%; TF32 3× vs the datasheet's 8×; flash attention does more FLOPs and never materialises T×T; vocabulary padding). The title's "much of" keeps it no stronger than his words.
- [[compute-efficiency]]: 30 lecture sentences checked. His measurements are correct: about 1,000 → 300 ms (TF32), 333 → 300 ms (bf16), 300 → 129 ms (compile, 2.3×), 130 → 96 ms (flash), 96.5 → 93 ms (padding, 4%; about 30% on 2.3.1), about 11× overall, 93 → 90 ms (fused AdamW), 1.5M tok/s on 8 GPUs, and 223K vs 185K tok/s for llm.c vs PyTorch. Figures from the paper or datasheet are labelled as such: 19.5 / 8× / 16× / 312 TFLOPS from the A100 datasheet, 7.6× from the flash attention paper and the 2018 NVIDIA online softmax. The garbled 163,000 tok/s is not repeated. The 580, 677 and memory-guide sentences are also correct. Only F1 needs a fix.
- [[gradient-descent]]: 12 sentences correct, including the GPT-3 schedule (375M warmup, 10% at 260B, 6e-4), his 10%-at-last-step schedule, gradient accumulation (2^19, 32 micro-steps), the AdamW "bug fix" opinion, the dated decay sentences and the 1.6B recipe.
- [[inherited-gpt-3-hyperparameters-look-conservative]], [[llm-c-was-not-yet-careful-enough-about-training-stability]], [[neural-net-training-should-not-be-complicated]] and [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]] (lecture and 677 paragraphs): all sentences are correct and the quotes verbatim. The `supports` link between neural-net-training-should-not-be-complicated and gpt-is-not-a-complicated-model is set on both pages, with both sides cited. The stability claim's Note to modern-innovations-make-precise-initialization-less-important is a Note only, as the merge map requires.
- [[small-projects-can-snowball]] (correct apart from F6), [[success-comes-from-repeated-practice]] and [[physical-automation-will-lag-digital-automation]]: all sentences are correct. Relative dates are left unconverted, and the "Her" and "I, Robot" details match @07:27–@09:19.
- [[pytorch-documentation-is-unreliable]], [[pretraining-gives-a-document-completer]], [[gpt-is-not-a-complicated-model]] and [[attention-is-a-communication-mechanism]]: the C4 sentences are correct (@3:00:24, @1:47:23, @1:42:51, @3:55:21/@3:55:54, README §intro, @27:27, @19:38/@20:12).
- [[llms-as-operating-systems]]: 4 Berkeley sentences and the decade Note are correct.
- [[build-and-publish-projects]]: 9 sentences are correct, and the LLM101n sentence matches @13:01.
- [[llm-evaluation]]: 9 sentences are correct (HellaSwag 95% / 48% are the paper's figures, 96% today, 29.55 and 49%, the 580 overlap kink, the 677 2.83 / 2.61 and its caveats).
- [[transformer-architecture]], [[weight-initialization]] and [[embeddings]]: 14 sentences are correct (wrong GPT-2 table, 12×768, pre-norm, std 0.02 / 0.01 from the code, 1/√N from the paper, 2 × n_layer, weight tying saves about 30%).
- [[pytorch]] and [[pretraining-and-finetuning]]: 12 sentences are correct (the README errata, the 677 testing-reference sentence, WebText 45M / 40 GB / 3 karma from the paper, FineWeb 15T and FineWeb-Edu 1.3T / 5.4T from Hugging Face, SFT as a dataset swap).
- [[llm-c]], [[build-nanogpt]] (apart from F1), [[nanogpt]], [[reproduce-a-published-model]], [[verify-against-a-reference-implementation]], [[small-hackable-educational-code]], [[spelled-out-build-from-scratch]], [[prototype-in-jupyter-then-repo]] and [[diagnose-under-or-overfitting]]: 20 sentences checked, all correct apart from F1.
- [[training-diagnostics]]: 6 sentences checked, all correct apart from F7 (initial loss 10.82 vs about 11; gradient norm about 30 settling below 1; watcher.sh about two minutes; skipped updates).
- [[tokenization]] (apart from F5), [[activation-functions]], [[regularization]], [[overfitting-and-generalization]], [[loss-functions]] and [[sampling-from-language-models]]: 10 sentences checked, all correct.
- Source pages: every Summary sentence of all five was checked and is correct (580: 6 days / 150B / 1.5 epochs, the config arithmetic described as planning, about two minutes for the watcher; 677: 24 h / $672 / 33.6B / about 50% MFU / 57GB vs about 80GB / about 19%).

## Resolution
Fixed 2026-10-24 (log: `## 2026-10-24 correction`).
- F1 fixed (build-nanogpt and compute-efficiency)
- F2 fixed
- F3 fixed (a and b)
- F4 fixed (entry and closing Note)
- F5 fixed
- F6 fixed (citation; the Note label is kept, as the report allows)
- F7 fixed
