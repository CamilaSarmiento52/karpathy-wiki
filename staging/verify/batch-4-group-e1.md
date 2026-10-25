# Verification: batch 4, group E1 (strawberry guide, Verifiability, reader3, reading-with-LLMs post, d34, llm-council, Space of minds)
Verified 2026-10-25 by a fresh reader. Sources: [[github-2025-10-24-nanochat-strawberry-guide]], [[blog-2025-11-17-verifiability]], [[github-2025-11-18-reader3-readme]], [[x-2025-11-18-reading-with-llms]], [[github-2025-11-20-nanochat-d34-model]], [[github-2025-11-22-llm-council-readme]], [[blog-2025-11-29-space-of-minds]]

## Coverage
- pages checked: 37 (7 source pages; claims: software-2-0-automates-what-you-can-verify, verifiability-drives-the-jagged-frontier, code-is-ephemeral-now-and-libraries-are-over, writers-may-increasingly-write-for-llms, llms-are-shaped-by-commercial-not-biological-evolution, a-lot-of-llm-oddness-traces-back-to-tokenization, transformers-need-tokens-to-think, synthetic-data-is-the-future-if-you-keep-its-entropy, rl-lets-models-discover-their-own-thinking-strategies, vibe-coding-will-terraform-software, llm-research-summons-ghosts-not-animals; timeline vibe-coding-over-time; methods teach-a-capability-with-synthetic-tasks, read-with-an-llm, choose-a-model-tier, training-diagnostics; artifacts reader3, llm-council, nanochat; topics tokenization, llm-tool-use, rlvr, pretraining-and-finetuning, software-3-0, jagged-intelligence, ai-and-the-economy, llm-self-improvement, scaling-laws, llm-evaluation, compute-efficiency, building-for-agents, vibe-coding, bitter-lesson)
- claim pages fully checked: 11 (the 5 new E1 claims, the 4 existing claims gaining the strawberry guide, and the 2 `supports` partners)
- timeline entries checked: 1 (vibe-coding-over-time, 2025-11-18), plus its two Notes for consistency
- other sentences checked: ~145 of ~155 citing these sources (nearly all; every number on nanochat, scaling-laws, llm-evaluation and compute-efficiency checked against the d34 stats block and tables)

## Findings

### F1 — overstated — [[nanochat]]
- sentence: "The GPT-2 CORE is 0.25 here and 0.26 for GPT-2 xl in the launch post, likely rounding of nearby figures, not reconciled"
- cited: [[github-2025-11-20-nanochat-d34-model]] §intro; [[github-2025-10-13-nanochat-discussion-introducing]] §Pretraining
- raw says: d34 post gives "GPT-2 is 0.25" with no model size; the launch post gives GPT-2 xl at 0.26 (§Pretraining) and, separately, "a GPT-2 capability model of CORE about 0.25" (§Your turn). "Likely rounding" is the wiki's guess, unlabelled, and it reconciles what the merge map says to leave unreconciled.
- fix: "**Note:** the GPT-2 CORE is 0.25 here; the launch post gives 0.26 for GPT-2 xl (§Pretraining) and about 0.25 for a GPT-2 capability model (§Your turn); not reconciled ([[github-2025-11-20-nanochat-d34-model]] §intro; [[github-2025-10-13-nanochat-discussion-introducing]] §Pretraining, §Your turn)." (llm-evaluation's matching Note is correct as written and could also add the §Your turn figure.)

### F2 — minor — [[scaling-laws]]
- sentence: "the parameter-to-token ratio is overridden from 20 (comparison, Chinchilla) to 40 (setting)"
- cited: [[github-2025-11-20-nanochat-d34-model]] §intro
- raw says: he writes "param:token ratio is overridden from 20 up to 40", but the stats print "Tokens : Params ratio: 40.0000" (88.7B tokens / 2.2B params). His label is inverted; the source page already says "tokens-to-parameters". Slips go corrected outside quotes.
- fix: "the tokens-to-parameters ratio (he writes "param:token") is overridden from 20 (comparison, Chinchilla) to 40 (setting)"

### F3 — minor — [[scaling-laws]]
- sentence: "The script derives 88,683,315,200 training tokens and 169,150 iterations at 524,288 tokens per batch and sequence length 2048 (settings)"
- cited: [[github-2025-11-20-nanochat-d34-model]] §intro
- raw says: the iterations are labelled "Calculated number of iterations"; tokens and iterations are derived, only batch size and max_seq_len are settings. The single "(settings)" tag reads as covering all four numbers.
- fix: "The script derives 88,683,315,200 training tokens and 169,150 iterations (estimates, calculated by the script) from 524,288 tokens per batch and sequence length 2048 (settings)"

### F4 — minor — [[compute-efficiency]]
- sentences: "2,217,082,880 parameters (counted)"; "on a DDP world size of 8 (measured)"; "He sets `--device_batch_size=4` (setting) for the larger model"
- cited: [[github-2025-11-20-nanochat-d34-model]] §intro
- raw says: world size 8 is a configuration (8 GPUs, `--nproc_per_node=8`), not a measurement; "counted" is not one of the legend's five tags; the post gives no reason for batch size 4 (the "larger model" reason is from the launch post's §Your turn, not this post).
- fix: "(estimate, computed by the script)" for the parameter count; "on a DDP world size of 8 (setting)"; "He sets `--device_batch_size=4` (setting)" (delete "for the larger model", or cite the launch post's §Your turn for the reason).

### F5 — minor — [[nanochat]]
- sentence: "ChatCORE rose from d32's 0.27 to 0.41 (measured)"; also "(settings)" after the command flags
- cited: [[github-2025-11-20-nanochat-d34-model]] §intro
- raw says: 0.41 is d34's measured result; d32's 0.27 is the comparison baseline (llm-evaluation tags it so). Legend tag is "setting".
- fix: "ChatCORE rose from d32's 0.27 (comparison) to 0.41 (measured)"; "(setting)".

### F6 — minor — [[verifiability-drives-the-jagged-frontier]], [[llm-council]]
- sentences: quote "This is what's driving the “jagged” frontier of progress in LLMs." (claim heading quote); llm-council definition quote "you can group them into your “LLM Council”"
- cited: [[blog-2025-11-17-verifiability]] §intro; [[github-2025-11-22-llm-council-readme]] §intro
- raw says: both raws use straight double quotes ("jagged", "LLM Council"); the wiki quotes have curly ones, so they do not string-match.
- fix: replace “ ” with " inside both quotes.

### F7 — minor — [[a-lot-of-llm-oddness-traces-back-to-tokenization]]
- sentence: "he gives three reasons, the first two from tokenization: whitespace makes the model translate between tokens with and without a space ("Tokenization makes whitespace annoying"), and it has to break tokens into individual characters; the third is comparing and counting"
- cited: [[github-2025-10-24-nanochat-strawberry-guide]] §Summary
- raw says: the guide does tie the difficulty to tokenization: reason 1 names it ("Tokenization makes whitespace annoying"), reason 2 is breaking tokens ("chunks of characters") into individual characters, and §Spelling says restating the query is computational work "because of tokenization". So the `sources` entry is earned. But only reason 1 names tokenization, and the guide also puts the hardness down to doing it all in one forward pass (§Summary), and says tokenization matters less for bigger models (§Counting). "the first two from tokenization" is a bit firmer than the text.
- fix: "he gives three reasons: tokenization makes whitespace annoying, so the model must translate between tokens with and without a space; it has to break tokens, chunks of characters, into individual characters; and it has to compare and count ([[github-2025-10-24-nanochat-strawberry-guide]] §Summary). Answering in a single token means solving all of that in one forward pass, and he says smaller models care about tokenization more than bigger ones ([[github-2025-10-24-nanochat-strawberry-guide]] §Summary, §Counting)."

### F8 — minor (overstated) — [[jagged-intelligence]]
- sentence: "His reason for the difference is an objective shaped by commercial rather than biological evolution; see [[llms-are-shaped-by-commercial-not-biological-evolution]]"
- cited: [[blog-2025-11-29-space-of-minds]] §intro
- raw says: the reason he gives for spikiness is the training data/task distribution and that failing a task does not mean death. Commercial vs. biological evolution is what he calls the most important difference between animal and LLM minds overall ("because it dictates asymptotics"), not a reason given for spikiness.
- fix: "He calls the different objective, commercial rather than biological evolution, the most important difference between the two kinds of mind; see [[llms-are-shaped-by-commercial-not-biological-evolution]] ([[blog-2025-11-29-space-of-minds]] §intro)."

### F9 — minor — [[tokenization]]
- sentence: "One of his spelling examples had a stray space after ":" by mistake, which he says was fine "because of the magic of neural networks""
- cited: [[github-2025-10-24-nanochat-strawberry-guide]] §Spelling
- raw says: "I actually had a bug here where I included a space right after ':'", i.e. a bug in the `SimpleSpelling` task's format, not one example.
- fix: "He had a bug that put a space right after ":" in the `SimpleSpelling` format, which he says was okay "because of the magic of neural networks" ([[github-2025-10-24-nanochat-strawberry-guide]] §Spelling)."

## Checked and correct
- [[software-2-0-automates-what-you-can-verify]]: quote verbatim; title fair; confidence stated; Context 7 sentences and 3 Related lines supported (Intro to LLMs @40:27 block checked; review §1/§2 Note is dates only).
- [[verifiability-drives-the-jagged-frontier]]: apart from F6 typography, quote and 3 Context sentences supported; "neural net magic of generalization fingers crossed" verbatim; RL-is-terrible Note checked at Dwarkesh @41:33; review Note dates only, and the benchmark argument is correctly placed in the review §2.
- [[code-is-ephemeral-now-and-libraries-are-over]]: quote verbatim (reader3 §intro; repeated verbatim in llm-council §Vibe Code Alert); "free, ephemeral, malleable, discardable after single use" verbatim in review §5; `supports` set on both sides; listed on vibe-coding-over-time.
- [[writers-may-increasingly-write-for-llms]]: quote verbatim; hedge kept; Note on building-for-agents checked at Software Is Changing @33:19.
- [[llms-are-shaped-by-commercial-not-biological-evolution]]: quote and "the only kind we've ever known", "the optimization pressure / objective is different" verbatim; DAU A/B tests kept apart from LM Arena; ghosts quote checked in animals-vs-ghosts §intro; `supports` set on both sides; "earlier" is his own word.
- [[vibe-coding-will-terraform-software]], [[llm-research-summons-ghosts-not-animals]]: the reverse `supports` lines are correct, dates only.
- [[transformers-need-tokens-to-think]], [[synthetic-data-is-the-future-if-you-keep-its-entropy]], [[rl-lets-models-discover-their-own-thinking-strategies]]: strawberry paragraphs all supported ("it only has so many layers per token!", "smoke and mirrors", "prior", the imitation-learning recovery, GSM8K RL, no mention of collapse).
- [[vibe-coding-over-time]]: 2025-11-18 entry correct (90%, 99%, Saturday hack, same sentences); dated by README commits; no interval words.
- [[teach-a-capability-with-synthetic-tasks]]: definition and all 7 steps supported; generated templates and example conversations are not quoted as his.
- [[reader3]], [[llm-council]] (apart from F6): all sentences supported; council config strings, stack, three stages, "nice and useful" without a better-answer claim; "llm Council" checked at How I Use LLMs @22:22; review §5 Notes dates only. Alias "LLM council" removed from choose-a-model-tier as the map asked.
- [[nanochat]] (apart from F1, F5): strawberry paragraph and d34 command, ~100 h / ~4 days, ~$2,500, CORE 0.3382 vs 0.3168 / 0.22 / 0.25, "$1000 run", Hugging Face upload and live deployment all match.
- [[llm-evaluation]]: all 13 table values, both quotes and the Note match the raw.
- [[training-diagnostics]], [[pretraining-and-finetuning]], [[llm-tool-use]], [[rlvr]], [[software-3-0]], [[ai-and-the-economy]], [[llm-self-improvement]], [[building-for-agents]], [[vibe-coding]], [[bitter-lesson]] (space of minds correctly in `context`), [[read-with-an-llm]], [[choose-a-model-tier]]: all sentences citing E1 sources supported.
- Source pages: all 7 Summaries and Key points supported; Fed pages match the pages citing each source; every year-in-review link is dates only.

## Resolution
Applied 2026-10-25 (correction entry in wiki/log.md).
- F1: fixed
- F2: fixed
- F3: fixed
- F4: fixed
- F5: fixed
- F6: fixed
- F7: fixed
- F8: fixed
- F9: fixed
