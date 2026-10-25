# Verification: batch 4, group E2 (auto-grade-hn, hn-time-capsule README, chemical hygiene, rustbpe README, nanochat #420, nanochat #481, microgpt)
Verified 2026-10-25 by a fresh reader. Sources: [[blog-2025-12-10-auto-grade-hn]], [[github-2025-12-10-hn-time-capsule-readme]], [[blog-2025-12-18-chemical-hygiene]], [[github-2026-01-03-rustbpe-readme]], [[github-2026-01-07-nanochat-miniseries-v1]], [[github-2026-01-31-nanochat-beating-gpt-2]], [[blog-2026-02-12-microgpt]]

## Coverage
- pages checked: 55 (7 source pages; topic chemical-hygiene, every sentence; claims future-llms-are-watching, us-chemical-regulation-lags-the-industry, nanochat-reproduces-chinchillas-equal-scaling-of-parameters-and-tokens, only-actual-metrics-are-real-and-comparable, gpt-2-training-cost-falls-to-about-40-percent-a-year, small-scale-tuning-does-not-always-transfer, microgpt-is-the-full-algorithm-everything-else-is-efficiency, plus the reverse Related line on micrograd-is-all-you-need-everything-else-is-efficiency; artifacts hn-time-capsule, rustbpe, microgpt, nanochat, minbpe, micrograd, makemore, nanogpt; topics scaling-laws, compute-efficiency, llm-evaluation, vibe-coding, llm-knowledge-bases, tokenization, gradient-descent, transformer-architecture, pretraining-and-finetuning, self-attention, backpropagation, sampling-from-language-models, loss-functions, llm-hallucinations, character-level-language-modeling; methods fit-your-own-scaling-law, quick-experiment-loop, reproduce-a-published-model, verify-against-a-reference-implementation, small-hackable-educational-code, spelled-out-build-from-scratch, training-diagnostics; other claims he-prefers-tiktoken-byte-level-bpe-to-sentencepiece, coding-models-are-weak-at-code-never-written-before, progress-comes-from-everything-improving-together, do-not-decay-the-learning-rate-to-zero, his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag, gpt-is-not-a-complicated-model, neural-net-training-should-not-be-complicated, attention-is-a-communication-mechanism, pretraining-gives-a-document-completer; timeline vibe-coding-over-time)
- claim pages fully checked: 7 (all E2 claims; every quote grepped verbatim, all are his and under 15 words)
- timeline entries checked: 1 of 1 (vibe-coding-over-time 2025-12-10)
- other sentences checked: ~175 of ~330. Every number from #420 and #481 on nanochat, scaling-laws, compute-efficiency, llm-evaluation, fit-your-own-scaling-law and quick-experiment-loop was checked against the raw tables, with its tag.

## Findings
### F1 — minor — [[chemical-hygiene]]
- sentence: "He uses HVAC filters and/or a standalone purifier: he got a Dyson Big+Quiet and names an IQAir model as the top tier"
- cited: [[blog-2025-12-18-chemical-hygiene]] §intro (Air)
- raw says: an instruction, "Install HVAC filters, and/or get a standalone air purifier", then "e.g. I got the Dyson". He does not say he uses HVAC filters.
- fix: "He recommends HVAC filters and/or a standalone purifier: he got a Dyson Big+Quiet, and for top performance he says he would get an IQAir model ([[blog-2025-12-18-chemical-hygiene]] §intro (Air))."

### F2 — minor (overstated) — [[us-chemical-regulation-lags-the-industry]]
- sentence (title): "He says US chemical and food regulation lags far behind the industry and behind Europe"
- cited: [[blog-2025-12-18-chemical-hygiene]] §intro (Food), (TLDR)
- raw says: "far behind" is about other countries ("lags far behind other countries (e.g. Europe especially)"); against the industry he says "significantly lagging behind".
- fix: "He says US chemical and food regulation lags significantly behind the industry and far behind Europe"

### F3 — minor — [[gpt-2-training-cost-falls-to-about-40-percent-a-year]] and [[github-2026-01-31-nanochat-beating-gpt-2]]
- sentence: "When OpenAI released GPT-2 in February 2019, he writes, the largest model, 1.5B parameters, took 32 TPU v3 chips..."
- cited: [[github-2026-01-31-nanochat-beating-gpt-2]] §intro
- raw says: #481 gives 1.5B. But #420, one of this group's own sources, lists the same model as "XL 1.6B" (§Details (GPT-2 / GPT-3 CORE scores)) and heads its extrapolation row "GPT-2 XL (1.6B)". The 481 source page notes the 1.5B/1.6B mismatch only against the README, and the claim page does not mention it. Nothing is reconciled, but the inconsistency is not fully stated.
- fix: on the 481 source page's *GPT-2's size* bullet, add "; the 2026-01-07 post's CORE table also lists GPT-2 XL as 1.6B ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (GPT-2 / GPT-3 CORE scores))". On the claim, add after the first Context sentence: "The 2026-01-07 post lists the same model as 1.6B; neither post reconciles them ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (GPT-2 / GPT-3 CORE scores); [[github-2026-01-31-nanochat-beating-gpt-2]] §intro)." Then add #420 to the claim's `context` and add the claim to #420's Fed pages.

### F4 — minor — [[scaling-laws]]
- sentence: "A fit over d12 and up gives `CORE = 1.0000 - 3.7555 * FLOPs^(-0.0344)` (estimate, fit)..."
- cited: [[github-2026-01-07-nanochat-miniseries-v1]] §Details (Miniseries v1 CORE scores)
- raw says: the prose introduces the fit as "predicting (total) parameters -> CORE", but the formula it prints is in FLOPs. This is a garble in the source, and the wiki passes it on silently.
- fix: append "; the post's text calls it a parameters-to-CORE fit while the formula uses FLOPs, and the wiki gives the formula as printed ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Miniseries v1 CORE scores))."

### F5 — minor — [[small-hackable-educational-code]]
- sentence: "It goes past step 2, PyTorch as the only dependency, to none at all ([[blog-2026-02-12-microgpt]] §Run it)."
- cited: [[blog-2026-02-12-microgpt]] §Run it
- raw says: "no pip install, no dependencies". The link to the method's step 2 is the wiki's own connection, written as if it were evidence.
- fix: "**Note:** this goes past step 2, PyTorch as the only dependency, to none at all ([[github-2022-11-20-makemore-readme]] §intro; [[blog-2026-02-12-microgpt]] §Run it)."

### F6 — minor — [[pretraining-and-finetuning]]
- sentence: "**Midtraining deleted from base training (2026-01-31).** ... this post removes it from the base-training pipeline as of its date and does not discuss SFT"
- cited: [[github-2026-01-31-nanochat-beating-gpt-2]] §What Worked
- raw says: the BOS-aligned dataloader "Made midtraining unnecessary (deleted it)". This deletes the midtraining stage. It does not remove it "from base training", since midtraining was never part of base training.
- fix: heading "**Midtraining deleted (2026-01-31).**", and Note end: "this post says the BOS-aligned loader made that stage unnecessary and that he deleted it, as of its date; it does not discuss SFT ([[github-2026-01-31-nanochat-beating-gpt-2]] §What Worked)."

### F7 — minor — [[rustbpe]]
- sentence (## Related): "[[minbpe]] — his Python tokenizer, which it names as too slow"
- cited: [[github-2026-01-03-rustbpe-readme]] §intro (implicit)
- raw says: minbpe works "only in Python and not optimized for speed". The README does not say "too slow".
- fix: "[[minbpe]] — his Python tokenizer, which it calls not optimized for speed"

## Checked and correct
- [[blog-2025-12-18-chemical-hygiene]] / [[chemical-hygiene]]: all ~45 sentences checked. Every health line is framed as his choice ("he recommends", "he prefers", "he says", "he advises"). His hedges are kept: "evolving, opinionated", "possibly mildly harmful", "controversially", "hotly contested", "personally ... highly suspicious", "not personally convinced just yet", "a little suspicious", "probably deficient", "simply decreasing risk", "not a professional toxicologist or food scientist", "work in progress". The linked studies (golf-course Parkinson's study, Blueprint sauna post, plasticlist.org) are attributed to their sources and not restated as fact. The two fluoride passages are both given and not reconciled. The plastic toothbrush, plastic floss and occasional beeswax candles are kept. MAHA is reported neutrally. Nothing is stated as medical fact. The grocery-post link (§Food sourcing) is correct: the tweet id matches x-2025-07-08-ideal-grocery-store. F1 is the only issue.
- [[us-chemical-regulation-lags-the-industry]]: the quote is verbatim and his. Context sentences (10%/10X labelled as illustration, GRAS, EU, "part-time investigative journalist") are supported. confidence stated is right. The calculator Note is correctly labelled as editorial. Only F2.
- [[future-llms-are-watching]]: the quote is verbatim (§intro). Context is supported, including both hedges and "security by obscurity". confidence stated. The README Note is fine.
- [[nanochat-reproduces-chinchillas-equal-scaling-of-parameters-and-tokens]]: the quote is verbatim. The ~0.5 exponents, 1.41×, 20 (comparison) vs 8 (measured, fit), the Muon or small-size hedge, and Kaplan's LR-decay bug all check out (the bug being pointed out by Chinchilla is in his code docstring). The 12:1 header is stated and not reconciled. The title is no stronger than the source.
- [[only-actual-metrics-are-real-and-comparable]]: the quote is verbatim. The modded-nanogpt B=1 explanation and the unknown-data-mix reason check out.
- [[gpt-2-training-cost-falls-to-about-40-percent-a-year]]: the quote is verbatim. $43,000 = 32×168×$8 (comparison). $73 ≈ 3.04 h × $24 (estimate). ~600× and the "understimate" hedge (quoted with his typo, inside the quote) check out. The four gain sources match. Only F3.
- [[small-scale-tuning-does-not-always-transfer]]: the quote is verbatim. 320 experiments, x0_beta1=0.96 at d20, "many (but not all!)" and d12 ~5 min check out. The title is scoped to his sweep.
- [[microgpt-is-the-full-algorithm-everything-else-is-efficiency]]: all four quotes are verbatim. The §Real stuff, §Autograd and §FAQ sentences are supported. `supports` [[micrograd-is-all-you-need-everything-else-is-efficiency]] is set on both pages, and the reverse Related line and the micrograd video @05:56/@06:30 ("none of the math changes ... purely for efficiency"; "micrograd is what you need") match. It is the weakest true link, with no timeline, as the map says.
- microgpt and nanochat: no sentence links microgpt to nanochat as fact. The source page says the post never mentions nanochat. The only connection is the labelled **Note:** on [[microgpt]] ("the comparison is the wiki's"), and [[nanochat]] has no microgpt sentence.
- nanochat inconsistencies, each stated and none reconciled: 8 vs "12:1 D:N" (source page, [[nanochat]], [[scaling-laws]], [[fit-your-own-scaling-law]], the claim); ~150M vs printed 603,979,776 of 1,384,124,976 ([[nanochat]] and source page); "~1000 lines" vs 8,304 lines in 44 files ([[nanochat]] Note); "Feb 1 2026" vs published 2026-01-31 ([[nanochat]] Note, source page); d12 ~6 min vs table 7.8 min vs ~5 min ([[quick-experiment-loop]]); ratio ~8 / ~10 / 10.5 / 12 each given with its own date and tag ([[scaling-laws]], [[fit-your-own-scaling-law]]); CORE 0.257 vs 0.256525 ([[llm-evaluation]]). The 1.5B vs 1.6B mismatch is stated, but see F3.
- [[nanochat]] (#420, #481 paragraphs): 7 paragraphs. Every number checks out: d10–d20, 2^19, ~4 h, ~$100, $24/h, d38/2.2B/17.8B/22.7 h/$546, 3.04 h, d24, 0.256525, 0.25851, 10,949 s, 348fbb3, 24 layers/1536/12×128, and the parameter counts. Tags are right.
- [[scaling-laws]], [[compute-efficiency]], [[llm-evaluation]], [[fit-your-own-scaling-law]]: every #420/#481 number checks out. That covers the quadratic-fit table (137M/1.12B, 240M/1.88B, 330M/2.71B; 8.2/8.1/8.5), the 5.7e23 vs ~3e23 FLOPs, all GPT-2 calculated and GPT-3 estimated CORE values, d10/d12/d16/d20 rows, ~9% FA3, SSSL, +13GB/+2GB/1%, 524,288 = 32×2048×8, ~35% waste and ~8.8B tokens. The tags are right. Only F4.
- [[quick-experiment-loop]], [[gradient-descent]], [[transformer-architecture]], [[reproduce-a-published-model]], [[training-diagnostics]], [[do-not-decay-the-learning-rate-to-zero]], [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]], [[progress-comes-from-everything-improving-together]]: ~30 sentences, all supported.
- [[hn-time-capsule]], [[blog-2025-12-10-auto-grade-hn]], [[github-2025-12-10-hn-time-capsule-readme]], [[vibe-coding]], [[vibe-coding-over-time]], [[llm-knowledge-bases]]: ~30 sentences, all supported. The pipeline, 930 queries, ~$58, ~1 h vs ~3 h coding, "a few hours" vs "about 3 hours", the five steps vs five stages plus clean, and gpt-5-mini all check out.
- [[rustbpe]], [[tokenization]], [[minbpe]], [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]], [[verify-against-a-reference-implementation]], [[coding-models-are-weak-at-code-never-written-before]]: ~20 sentences, all supported. The nanochat link is always a hedged **Note:**. Only F7.
- [[microgpt]] and the microgpt sentences on [[micrograd]], [[makemore]], [[nanogpt]], [[backpropagation]], [[self-attention]], [[tokenization]], [[sampling-from-language-models]], [[loss-functions]], [[llm-hallucinations]], [[character-level-language-modeling]], [[pretraining-and-finetuning]], [[spelled-out-build-from-scratch]], [[gpt-is-not-a-complicated-model]], [[neural-net-training-should-not-be-complicated]], [[attention-is-a-communication-mechanism]], [[pretraining-gives-a-document-completer]]: ~35 sentences, all supported. The quotes are verbatim; 4,192, 27, 32,033, 3.3→2.37, temperature 0.5, 20 samples and GPT-2 1.6B "in his figures" all check out. The 1-minute and seconds-per-step timings are kept apart. Only F5.

## Resolution
Applied 2026-10-25 (correction entry in wiki/log.md).
- F1: fixed
- F2: fixed
- F3: fixed
- F4: fixed
- F5: fixed
- F6: fixed
- F7: fixed
