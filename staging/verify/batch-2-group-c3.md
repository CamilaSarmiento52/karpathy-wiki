# Verification: batch 2, group C3 (llm.c Discussions 84/224/344/454/481, llama2.c README, calorie README)
Verified 2026-10-24 by a fresh reader. Sources: [[github-2024-04-12-llmc-discussions-welcome]], [[github-2024-04-22-llmc-state-of-the-union]], [[github-2024-05-03-llmc-state-of-the-union]], [[github-2024-05-24-llmc-pytorch-cross-checks]], [[github-2024-05-28-llmc-gpt-2-124m]], [[github-2024-05-29-llama2c-readme]], [[github-2024-05-30-calorie-readme]]

## Coverage
- pages checked: 29. These are the 7 source pages plus the 22 fed pages: llm-c, llama2c, calorie, nanogpt, the four claims below, verify-against-a-reference-implementation, reproduce-a-published-model, small-hackable-educational-code, training-diagnostics, compute-efficiency, sampling-from-language-models, llm-evaluation, gradient-descent, pytorch, loss-functions, pretraining-and-finetuning, regularization, tokenization and transformer-architecture.
- claim pages fully checked: 4. These are llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements, gpt-2-is-the-first-recognizably-modern-llm-stack, his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag and small-llms-can-be-strong-in-narrow-domains. All four quotes are verbatim, his, at the cited location, and under 15 words. None of the four has supports/extends links to check.
- timeline entries checked: 0. No timeline cites these sources.
- other sentences checked: about 110 of about 120 that cite these sources. Every sentence carrying a number was checked against the raw.
- Numbers audit:
  - Every figure is attributed to the right Discussion: 2097 LOC, 6.4%, 32% and 8753/12879 MiB come from 224; ~3,000 LOC, 7%/11%/46%/3X, 16.6/37.2 GiB and 302.5 ms come from 344; 1e-3, ZeRO `-z 1` and 131072 come from 454; 90 min, $20, 60% MFU, 29.9, 18,865 steps and 350M/$200 come from 481.
  - Measured, target and comparison labels are correct throughout:
    - 29.4 and 33.7 are flagged as comparison numbers.
    - The 4–24 h single-GPU time, the ~1 week / $2.5K for 1558M and the "~2 weeks out" are flagged as estimates or forecasts.
    - The 224 qualifier (fp32, no flash attention, stale PyTorch) is kept.
    - Each 344 percentage stays with its baseline.
    - The 454 FP32/bf16 command inconsistency is handled with a Note.
- Not created: [[neural-net-training-should-not-be-complicated]] (merge map, "llm.c Discussions"). None of these seven raw files states it, so there is nothing missing from C3. Its source is presumably 580 or 677 (C4).

## Findings
### F1 — overstated — [[verify-against-a-reference-implementation]] (also [[github-2024-05-24-llmc-pytorch-cross-checks]] Key points)
- sentence: "Both sides train GPT-2 (124M) from scratch on FineWeb with micro-batch 16, sequence length 1024 and a total batch of 131072, learning rate 1e-4, warmup, learning-rate decay and weight decay switched off, for 50 iterations; …" (Steps, step 8)
- cited: [[github-2024-05-24-llmc-pytorch-cross-checks]] §1 GPU training in FP32
- raw says: The LR 1e-4 and the warmup/decay/weight-decay-off flags (`-l -u -q -c`) appear only in the llm.c command. The PyTorch command, which he calls the "Equivalent run in PyTorch", passes none of them. It also reads a single train shard (`fineweb_train_000001.bin`) where llm.c reads `fineweb_train_*.bin`. So the raw does not show "both sides" with those settings.
- fix: "The llm.c command trains GPT-2 (124M) from scratch on FineWeb with micro-batch 16, sequence length 1024, a total batch of 131072, learning rate 1e-4 and warmup, learning-rate decay and weight decay switched off, for 50 iterations; he gives a PyTorch command he calls equivalent (same model, micro-batch, sequence length, total batch and 50 iterations), pins the repo commit and the GPU (an A100 40GB), …". Make the same fix on the source page Key point: change "same model, data, batch, LR, with schedule and decay off" to "same model, batch and step count, with schedule and decay off on the llm.c side".

### F2 — overstated (conditional on C4) — [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- sentence: title "His llm.c GPT-2 reproductions beat OpenAI's GPT-2 checkpoints of the same size on HellaSwag"
- cited: [[github-2024-05-28-llmc-gpt-2-124m]] §intro (the only source on the page)
- raw says: 481 gives one HellaSwag comparison, 124M (29.9 vs 29.4). It gives no HellaSwag figure for the 350M, as the page itself notes. The plural title therefore rests on evidence that is not yet on the page.
- fix: no change needed if C4 adds 580/677 with their own size and HellaSwag comparisons, as the merge map plans. If C4 does not add them, make the title singular: "His llm.c GPT-2 (124M) reproduction beat OpenAI's 124M checkpoint on HellaSwag".

### F3 — overstated (invented connection) — [[small-llms-can-be-strong-in-narrow-domains]], [[llama2c]]
- sentence: "His own illustration is the repo's TinyStories series of 260K to 110M parameters; …" (claim Context). The llama2c Related line, "the claim the tiny models illustrate", makes the same link.
- cited: [[github-2024-05-29-llama2c-readme]] §feel the magic, §models
- raw says: §intro makes the small-LLM claim and cites only the TinyStories paper. §models presents the tinyllamas as "examples of smaller, from-scratch models". The README never offers them as evidence for the claim.
- fix: in the claim, change it to "The repo's own models are a TinyStories series of 260K to 110M parameters; …", or prefix the sentence with **Note:**. In llama2c Related, change it to "— his claim about small models in narrow domains".

### F4 — wrong (source silent) — [[calorie]] (and [[github-2024-05-30-calorie-readme]] header line)
- sentence: "His calorie deficit tracking web app, a personal project outside his AI work". The source page says the same: "A personal project, not part of his AI work."
- cited: [[github-2024-05-30-calorie-readme]] §intro
- raw says: only "Calorie deficit tracking web app." plus how he uses it. Nothing in it says the project is personal or separate from his AI work.
- fix: in the artifact, change it to "His calorie deficit tracking web app ([[github-2024-05-30-calorie-readme]] §intro)." If the characterisation is wanted, put it in a separate **Note:**. On the source page, delete "A personal project, not part of his AI work." or prefix it with **Note:**.

### F5 — minor — [[reproduce-a-published-model]]
- sentence: "…; next on his list is the 1558M "GPT-2"" (step 8)
- cited: [[github-2024-05-28-llmc-gpt-2-124m]] §intro (Coming up)
- raw says: he is moving on to "the 740M and then" the 1558M. Per the digest, 740M is a slip for 774M.
- fix: "…; next he names the next size up and then the 1558M "GPT-2"". This matches the wording already on [[llm-c]].

### F6 — minor — [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- sentence: "All of these are his measurements, scoped by him to that setting (…§intro)." In the third paragraph: "Each percentage holds only against its own baseline (…§intro)."
- cited: [[github-2024-04-22-llmc-state-of-the-union]] §intro; [[github-2024-05-03-llmc-state-of-the-union]] §intro
- raw says: "in this constrained setting" qualifies only the ~6.4% speed figure, not the memory figure. The "own baseline" sentence is the wiki's caution, not his.
- fix: change the first to "All of these are his measurements; he scopes the speed figure to "this constrained setting"". Change the second to "**Note:** each percentage holds only against its own baseline (…)".

### F7 — minor — [[compute-efficiency]]
- sentence: "76% of the time is in NVIDIA cutlass kernels, the matmuls, …". Also "with bf16 matmul kernels about 55% of the time".
- cited: [[github-2024-04-22-llmc-state-of-the-union]] §intro; [[github-2024-05-03-llmc-state-of-the-union]] §intro (Runtime, DRAM traffic, instructions)
- raw says: the profile names the kernels "cutlass::Kernel" and "ampere_bf16". The text never calls them matmuls.
- fix: drop ", the matmuls", and change "bf16 matmul kernels" to "`ampere_bf16` kernels".

### F8 — minor — [[gradient-descent]]
- sentence: "it warms up linearly from 0 over the first 700 iterations, 350M tokens"
- cited: [[github-2024-05-28-llmc-gpt-2-124m]] §intro (Args guide)
- raw says: "ramp up the learning rate from 0 to max learning rate over the first 700 iterations". He does not say "linearly".
- fix: "it ramps up from 0 to the maximum over the first 700 iterations, 350M tokens".

### F9 — minor — [[llama2c]]
- sentence: "`make runfast` (-Ofast) was fastest on his M1; `-march=native`, clang and OpenMP help, …"
- cited: [[github-2024-05-29-llama2c-readme]] §performance
- raw says: `-march=native` "may enable additional optimizations"; for clang, "you can also experiment with replacing gcc with clang"; only OpenMP gets "big improvements".
- fix: "`make runfast` (-Ofast) was fastest on his M1; he suggests trying `-march=native` and clang, says OpenMP can give big improvements, and that more threads is not always better, usually a bit U-shaped".

### F10 — minor — [[reproduce-a-published-model]]
- sentence: "How he tests a training stack: retrain a model someone has published, from scratch, and show that his run matches or beats the released checkpoint."
- cited: [[github-2024-05-28-llmc-gpt-2-124m]] §intro
- raw says: one reproduction, GPT-2 124M, described as a reproduction. He does not present it as his general way to test a training stack.
- fix: "How he validated the llm.c training stack: retrain a published model from scratch and compare the run with the released checkpoint."

## Checked and correct
- [[github-2024-04-12-llmc-discussions-welcome]]: summary, key point and header, all supported.
- [[github-2024-04-22-llmc-state-of-the-union]]: 5 summary and key-point sentences checked, all supported, including the A10/A100 split and the fp32 qualifier.
- [[github-2024-05-03-llmc-state-of-the-union]]: 6 checked, all supported, with each percentage kept with its baseline.
- [[github-2024-05-24-llmc-pytorch-cross-checks]]: 5 checked. All are supported except the Key point in F1.
- [[github-2024-05-28-llmc-gpt-2-124m]]: 7 checked, all supported. The measured, comparison and estimate labels are right.
- [[github-2024-05-29-llama2c-readme]]: 5 checked, all supported. These include 700 lines, 4X/3X, the micro-LLM range 100M–10B, and the snapshot-date caveat.
- [[github-2024-05-30-calorie-readme]]: summary all supported. The only problem is the header line in F4.
- [[gpt-2-is-the-first-recognizably-modern-llm-stack]]: title, quote, confidence and all 3 Context sentences are supported.
- [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]:
  - The title and quote are right, including the 73 vs 78.2 ms, 8753 vs 12879 MiB, ~7% (nightly), ~46% (2.3.0), ~3X, 167K/160K/150K/156K tok/s and 16.6 vs 37.2 GiB figures.
  - The rest is supported apart from F6.
- [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]:
  - The quote, confidence, the 29.9 / 29.4 / 33.7 labels, the 10B vs 300B tokens and the "no 350M HellaSwag figure" note are all correct.
  - The title is covered by F2.
- [[small-llms-can-be-strong-in-narrow-domains]]: the quote, the TinyStories attribution, the "I think" prediction, the 100M–1B / ~10B range and the edge-adjacent examples are correct. The only problem is F3.
- [[llm-c]]: 20 sentences, all supported. These include the "next model size up" handling of the 740M slip, the two-weeks forecast Note, and the ramp-post Note (the link target is X post 1760388761349927356).
- [[llama2c]]: 14 sentences, all supported except F9 and the Related line in F3. These include the 110 tok/s, 260K–110M models, ~24 h, 26GB, 4 tok/s on 96 threads, 13B+ overflow and 200-step tests.
- [[calorie]]: 7 sentences, all supported except F4. These include 2000 kcal, 500 kcal/day, 3500 kcal ≈ 1 lb, Big Mac ×5, 400 kcal ×4, 1000 kcal and the /24 constants.
- [[nanogpt]]: 1 llama2.c sentence, supported.
- [[verify-against-a-reference-implementation]]:
  - Steps 7, 9 and 10 and the FP32/bf16 Note are supported. Step 8 is supported except F1.
  - 454: the ~1e-3 loss/grad-norm match is his measurement, after 50 iterations, on an A100 40GB.
  - The 4-GPU llm.c "same results", the PyTorch 4-GPU mismatch and the 481 "parallel implementation" line are correct.
  - llama2.c: the C/Python known-good tests and the sample.py match are correct.
- [[reproduce-a-published-model]]: steps 1–7 are supported, with the HellaSwag labels right. The problems are in F5 and F10.
- [[compute-efficiency]]: 4 paragraphs, about 22 sentences, checked; supported except F7. Checked items:
  - 224: 212.4 ms and 47.8/25.8/23.0/3.3% breakdown, 8753 MiB, @ngc92 credit.
  - 344: 302.5 ms at batch 24, cuDNN SDPA ~9%, 1m24s compile.
  - 481: 312 TFLOPS, ~half on 40GB PCIe, ~60% on 80GB SXM, ~178K tok/s, `-r 1`, ZeRO-1, 6ND 7e18 / 7e19, $20 to $200.
  - llama2.c quantization: Q8_0, RMSNorm kept in fp32, 26GB vs 6.7GB, 4.6 vs 14 tok/s, "silently very slightly lower quality".
- [[sampling-from-language-models]]: 3 llama2.c sentences, all supported (t 1.0 / p 0.9 defaults, "unlucky", "off the rails", vary one but not both).
- [[llm-evaluation]]: 9 sentences, all supported (WikiText 103?, HellaSwag on the 454 checklist, WebText and five-years caveat, math/code caveat, labelled reference points).
- [[gradient-descent]]: 3 paragraphs checked; supported except F8. The 131072 / 8 accumulation, the 0.5M batch, 6e-4, 0.1 on 2-D weights, decay to 0, clipping 1.0 and the llama2.c guide (100K, 1e-3, 3e-4, 4e-4, 200K, ~day on 4 GPUs) are correct.
- [[pytorch]]: 4 sentences, all supported (50257 / 50304, tied weights, -inf masking, model surgery, @Chillee, torchrun approximation, PRs welcome).
- [[loss-functions]], [[training-diagnostics]]: the 7.577 / ~2,000, 3.29 / ~27 and 50,257 figures, gradient-norm spikes, clipping 1.0 and vislog.ipynb are all supported.
- [[pretraining-and-finetuning]], [[regularization]], [[tokenization]], [[transformer-architecture]]: 1, 1, 3 and 2 sentences, all supported. The 110M context comparison is paraphrased "as he puts it", as the digest asked.
- [[small-hackable-educational-code]]: steps 10–11 are supported (2097 LOC / 2.4 s / 2.2 s, ~3,000 LOC / 4.3 s "as bad as import torch", 1,000 → 3,500 LOC, contributing policy).
- Ordering and interval words are all consistent with published dates: "next report", "by the GPT-2 post", "came first", "day 24", "10 days ago" → "April 22 report".
