# Verification: batch 3, group D2 (Deep Dive, How I use LLMs, digital hygiene, append-and-review, sleep tracker)
Verified 2026-10-24 by a fresh reader. Sources: [[youtube-2025-02-05-deep-dive-into-llms]], [[youtube-2025-02-27-how-i-use-llms]], [[blog-2025-03-17-digital-hygiene]], [[blog-2025-03-19-append-and-review-note]], [[blog-2025-03-24-best-sleep-tracker]]

## Coverage
- pages checked: 45. 5 source pages; 11 new claims (chatgpt-answers-simulate-a-human-data-labeler, hallucinations-come-from-imitating-confident-answers, parameters-are-vague-recollection-context-is-working-memory, rl-lets-models-discover-their-own-thinking-strategies, rlhf-is-not-real-rl, use-llms-as-tools-and-check-their-work, longer-context-windows-alone-will-not-scale-to-long-multimodal-tasks, he-prefers-to-pay-and-be-the-customer, use-hardware-security-keys-not-sms-as-a-second-factor, one-text-note-beats-many-organized-notes, oura-and-whoop-were-the-best-sleep-trackers-he-tested); 12 older claims that gained D2 sentences (transformers-need-tokens-to-think, pretraining-gives-a-document-completer, pretraining-is-lossy-compression-of-the-internet, an-llm-is-just-two-files, a-lot-of-llm-oddness-traces-back-to-tokenization, tokenization-free-modeling-would-be-amazing-but-is-unproven, rlhf-works-better-because-comparing-is-easier-than-generating, gpt-2-is-the-first-recognizably-modern-llm-stack, llms-want-to-imitate-not-succeed, use-llms-as-copilots-with-human-oversight, self-improvement-may-be-possible-in-narrow-domains, llms-currently-only-have-a-system-1); 7 methods (choose-a-model-tier, start-a-new-chat-per-topic, verify-citations, read-with-an-llm, voice-input, digital-hygiene-checklist, append-and-review-note); timeline llm-self-improvement-over-time; topics llm-hallucinations (fully), jagged-intelligence (all D2 sentences), pretraining-and-finetuning, tokenization, sampling-from-language-models, transformer-architecture, compute-efficiency, scaling-laws, prompting-llms, llm-tool-use, rlvr, llm-self-improvement, system-1-and-system-2-thinking, llm-evaluation, ai-ecosystem, partial-autonomy-apps, llm-gui, vibe-coding, user-hostile-technology; artifact llm-c.
- claim pages fully checked: 11 new. In the 12 older claims, every D2 sentence was checked, plus their `supports`/`extends` back-links.
- timeline entries checked: 3 of 3, plus the closing Note.
- other sentences checked: about 75 of about 160. That covers all of llm-hallucinations, the jagged-intelligence Swiss cheese paragraph, every method step, and the numeric or opinion sentences on the other topics.
- A script checked every `@` timestamp citing Deep Dive, How I use LLMs, Sequoia or Intro to LLMs anywhere in `wiki/` against the raw markers. All exist.

## Findings

### F1 — overstated (wrong link type) — [[rl-lets-models-discover-their-own-thinking-strategies]] ↔ [[llms-currently-only-have-a-system-1]] (also [[system-1-and-system-2-thinking]])
- sentence: "Extends [[llms-currently-only-have-a-system-1]]: on 2023-11-23 LLMs "currently" could not convert time into accuracy …; on 2025-02-05 he describes thinking models whose longer responses raise accuracy …" (and the mirror "Extended by …" bullet on the System 1 page; and on system-1-and-system-2-thinking: "His claim is [[rl-lets-models-discover-their-own-thinking-strategies]], which extends [[llms-currently-only-have-a-system-1]]")
- cited: [[youtube-2023-11-23-intro-to-llms]] @36:31, @37:06, @37:40; [[youtube-2025-02-05-deep-dive-into-llms]] @2:30:24, @2:32:04
- raw says: in 2023 he describes a current limitation: no model can yet trade time for accuracy, and people are "working towards" it. In 2025 he describes RL-trained models whose longer outputs raise accuracy. The 2025 claim does not broaden or add to "LLMs only have System 1". It describes the thing the 2023 claim said did not yet exist. The 2023 statement was dated, so this is not `contradicts`. It is not `supports` either. No link type fits.
- fix: remove `extends` from both frontmatters and drop both "Extends"/"Extended by" bullets. Put a **Note:** on each page instead, for example: "**Note:** the 2023 limitation was dated; on 2025-02-05 he describes RL-trained thinking models whose longer responses raise accuracy, without the System 1/System 2 words ([[youtube-2023-11-23-intro-to-llms]] @37:06; [[youtube-2025-02-05-deep-dive-into-llms]] @2:30:24). A connection, not a claim link." On system-1-and-system-2-thinking, replace ", which extends [[llms-currently-only-have-a-system-1]]" with "; **Note:** it describes the kind of model his 2023 claim [[llms-currently-only-have-a-system-1]] said did not yet exist". Both entries can stay on the timeline as dated entries.

### F2 — overstated — [[llm-self-improvement-over-time]] (closing Note)
- sentence: "what changed between 2023-11-23 and 2025-02-05 is that the narrow-domain RL he speculated about and the time-into-accuracy wish both appear in his account as working thinking models, so the 2025 claim extends both 2023 claims"
- cited: [[youtube-2023-11-23-intro-to-llms]] @40:27; [[youtube-2025-02-05-deep-dive-into-llms]] @2:44:20
- raw says: the 2023 speculation was about AlphaGo step two, self-improvement that goes past human level (@39:20, @40:27). In 2025 he says LLMs show only "hints of this diagram" (@2:44:52), that RL is "way too new primordial and nascent" (@3:29:18), and that transfer to unverifiable domains is unknown (@3:28:45). What works in his 2025 account is accuracy gains and emergent chains of thought on math and code. Self-improvement past human level is not described as working. He also never says "narrow domains" in 2025; he says "verifiable domains".
- fix: "**Note:** what changed between 2023-11-23 and 2025-02-05: RL against checkable answers, which he had speculated could work in narrow domains, is in his 2025 account training thinking models whose longer outputs raise accuracy on math and code. What did not change: he still sees only hints of AlphaGo-style progress beyond human level, calls the RL early, and treats RLHF as a weak form of RL ([[youtube-2023-11-23-intro-to-llms]] @40:27; [[talk-2024-03-26-sequoia-making-ai-accessible]] @26:39; [[youtube-2025-02-05-deep-dive-into-llms]] @2:30:24, @2:44:52, @3:05:54)." Drop "so the 2025 claim extends both 2023 claims", which F1 also requires.

### F3 — minor (link type judgement) — [[rl-lets-models-discover-their-own-thinking-strategies]] ↔ [[self-improvement-may-be-possible-in-narrow-domains]]
- sentence: "Extends [[self-improvement-may-be-possible-in-narrow-domains]]: on 2023-11-23 he thought self-improvement may be possible in narrow domains with a reward function …; on 2025-02-05 he describes RL on math and code problems with known answers producing reasoning strategies, while saying it is still early …"
- cited: [[youtube-2023-11-23-intro-to-llms]] @40:27; [[youtube-2025-02-05-deep-dive-into-llms]] @2:32:04, @2:44:20
- raw says: both sides' text supports a real link. 2023: RL against a reward in narrow domains may let models self-improve. 2025: RL against verifiable answers lets the model find strategies no human could hardcode (@2:31:30, @2:19:55), framed with AlphaGo, but "only starting to see hints" (@2:44:20–@2:44:52). The 2025 claim adds a concrete mechanism and evidence. It does not broaden the scope, since it covers math and code only and leaves the general case open, as 2023 did. `extends` is defensible, and the bullet's own hedges (early, no "self-improvement" word) are accurate. But §7 says to pick the weakest true link, and `supports` is true here.
- fix (optional, reviewer's call): change to `supports` on both pages and in both bullets ("Supports …: the 2025 lecture gives evidence for the 2023 hedge in verifiable domains while saying it is still early"). If `extends` stays, add to the bullet that the 2025 lecture says "verifiable" rather than "narrow" domains. The timeline does not require `extends`, since a timeline entry is allowed for any dated statement.

### F4 — mis-cited / attribution — [[llm-self-improvement-over-time]] (2025-02-05 entry) and [[youtube-2025-02-05-deep-dive-into-llms]] (Summary, Key points)
- sentence: "he describes RL on practice problems with known answers, with DeepSeek-R1 and OpenAI's thinking models as examples, in which models discover their own chains of thought … (@2:28:46, @2:32:04)". Summary: "models like DeepSeek-R1 and OpenAI's o-series discover chains of thought themselves". Key point: "DeepSeek-R1, o1/o3 are thinking models"
- cited: @2:28:46, @2:32:04 (timeline); @2:13:19 … @2:32:04 (summary)
- raw says: @2:28:46 is about the DeepSeek paper only. That o1/o3-mini were trained with RL "very similar to" R1's he reports "per public statements of OpenAI employees" (@2:37:07). The rlvr topic attributes this correctly.
- fix: timeline: "… with DeepSeek-R1 as his worked example and OpenAI's o1/o3-mini, which he says were trained similarly per OpenAI employees' public statements, …" and add @2:37:07. Summary: "… where models like DeepSeek-R1 discover chains of thought themselves (OpenAI's o-series, he reports from OpenAI employees' statements, are trained similarly) …" and add @2:37:07. Key point: "DeepSeek-R1, and o1/o3 per OpenAI employees, are thinking models".

### F5 — mis-cited — [[jagged-intelligence]]
- sentence: "His example is that models answer Olympiad-grade and PhD-grade questions yet sometimes say 9.11 is bigger than 9.9, not reproducibly ([[youtube-2025-02-05-deep-dive-into-llms]] @2:05:30, @2:06:03)."
- cited: @2:05:30, @2:06:03
- raw says: the PhD-grade physics, chemistry and biology remark is in the @2:04:57 block. @2:05:30 has the 9.11 output and "I don't believe that this is very reproducible". @2:06:03 has "Olympiad grade".
- fix: cite "@2:04:57, @2:05:30, @2:06:03". The rest of the Swiss cheese paragraph is correct: the wording "Swiss cheese" (@3:08:39, @3:09:14, @3:25:55, @3:26:26), "Jagged edges" (@2:04:57) and "Jagged issues" (@2:07:12) are all verbatim. The Bible-verse finding is attributed to "this team", and he says he has not read the paper (@2:06:03).

### F6 — minor ("you", not "he") — [[choose-a-model-tier]]
- sentence: "**Compare tiers.** Bigger models cost more to run, so companies charge more for them; decide whether the cheaper tiers are enough"
- cited: [[youtube-2025-02-27-how-i-use-llms]] @20:07
- raw says: he tells viewers to "make those tradeoffs for yourself" and to see whether "you can get away with the cheaper offerings".
- fix: "… so companies charge more for them; he says to decide for yourself whether the cheaper tiers are enough ([[youtube-2025-02-27-how-i-use-llms]] @20:07)."

### F7 — minor (option presented as his practice) — [[voice-input]]
- sentence: step "Use read-aloud or text-to-speech for output" / "**Output.** For reading the reply back, apps may have a read-aloud option, or you can use a system-wide text-to-speech app"
- cited: [[youtube-2025-02-27-how-i-use-llms]] @1:25:53, @1:26:26, @1:26:59
- raw says: he demonstrates ChatGPT's read-aloud button once and lists the options ("those are the options available to you"). Unlike dictation ("I use this pervasively"), he never says he uses text-to-speech himself. The method's definition says these are his own practices.
- fix: body: "**Output.** He notes that apps may have a read-aloud option and that a system-wide text-to-speech app is an alternative; he does not say he uses either himself (…@1:26:26, @1:26:59)." Frontmatter step: "Know the read-aloud options for output", or drop the step.

### F8 — minor (wording slightly stronger) — [[read-with-an-llm]]
- sentence: "he says it is no longer the case that he reads books by himself, and always involves an LLM"
- cited: [[youtube-2025-02-27-how-i-use-llms]] @55:03
- raw says: "it is rarely ever the case anymore that I read books just by myself I always involve an LM" (@54:30–@55:03).
- fix: "he says it is rarely the case any more that he reads books by himself; he always involves an LLM". Also add @54:30, where the phrase starts.

### F9 — minor (he corrects his own figure) — [[gpt-2-is-the-first-recognizably-modern-llm-stack]]
- sentence: "everything in it is recognizable today, only bigger: 1.6 billion parameters, a context of 1,024 tokens and about 100 billion training tokens"
- cited: [[youtube-2025-02-05-deep-dive-into-llms]] @31:52
- raw says: he says 1.6 billion at @31:52 and @44:47, but corrects himself at @43:38 ("1.6 billion sorry 1.5 billion model") and says 1.5 billion again at @45:20. [[an-llm-is-just-two-files]] uses 1.5 billion from @45:20, so the two pages disagree.
- fix: "… about 1.5 billion parameters (he says 1.6 billion at one point and corrects it to 1.5), …" and add @43:38.

## Checked and correct
- [[rlhf-is-not-real-rl]]: `stated_on: 2024-03-26` is right. The Sequoia quote "super weak form of reinforcement learning doesn't even count as reinforcement learning" is verbatim at @26:39 (followed by "I think"), and it is his, inside his answer that begins at @24:59. The Sequoia vibe-check and reward-hacking sentences are at @27:13. All seven Deep Dive sentences are supported (@2:51:02–@3:06:27, @3:27:03), including "what I usually say is that RLHF is not RL" (@3:04:50), which supports the two-source framing. The Note to rlhf-works-better… is accurate (@2:58:09, @2:58:41).
- [[chatgpt-answers-simulate-a-human-data-labeler]]: 7 sentences, all supported. The quote is verbatim at @1:18:17. The `supports` link is reciprocal and correctly limited to imitation.
- [[hallucinations-come-from-imitating-confident-answers]]: 6 sentences, all supported. The quote is verbatim at @1:22:42, and the Llama 3 procedure is attributed to Meta.
- [[parameters-are-vague-recollection-context-is-working-memory]]: 8 sentences, all supported. The quote is verbatim at @1:39:25, and "about ten times" for Wikipedia is at @53:50.
- [[rl-lets-models-discover-their-own-thinking-strategies]]: title, quote (@2:32:04) and all Context sentences are supported. Only the Related claims bullets have problems (F1, F3).
- [[longer-context-windows-alone-will-not-scale-to-long-multimodal-tasks]]: 5 sentences, all supported. The quote is verbatim at @3:14:13, and "I think" is kept.
- [[use-llms-as-tools-and-check-their-work]]: 9 sentences, all supported. The quote is verbatim at @3:30:23. "Always reads the code" is @1:06:19 ("I always read it"), and the `supports` link is reciprocal.
- [[he-prefers-to-pay-and-be-the-customer]]: 7 sentences, all supported. The quote is verbatim (§Search engine), and "You paid for it and now it is yours" is verbatim in the calculator post. The Note on the calculator post is accurate.
- [[use-hardware-security-keys-not-sms-as-a-second-factor]]: 6 sentences, all supported. The quote is verbatim, and "about 1000X" keeps "about".
- [[one-text-note-beats-many-organized-notes]]: 5 sentences, all supported. The title is scoped "for him".
- [[oura-and-whoop-were-the-best-sleep-trackers-he-tested]]: every number matches the raw: 0.65 and 0.14; the matrix values 0.947 and 0.879; RHR ~51 to ~48; HRV ~49 to 54; Oura best score 92; Whoop 9.5/10 and Oura 10/10. The 8Sleep discrepancy is reported without being reconciled, as the digest asks. Bryan Johnson's habits are attributed to him.
- [[llm-self-improvement-over-time]]: the 2023-11-23 and 2024-03-26 entries are supported (@36:31, @37:06, @39:20, @40:27; Sequoia @24:59–@26:39). The dates are published dates, and no interval wording is used.
- [[self-improvement-may-be-possible-in-narrow-domains]], [[llms-currently-only-have-a-system-1]]: the D2 sentences are accurate in content (link type aside, F1/F3).
- [[llm-hallucinations]]: all 13 sentences are supported, including "cooked up and bolted on" (@1:46:42), the 240 OLMo conversations (@1:44:59) and the Falcon/OpenAI identity explanation (@1:43:55).
- [[jagged-intelligence]]: 7 D2 sentences; all supported apart from F5.
- [[start-a-new-chat-per-topic]], [[verify-citations]], [[digital-hygiene-checklist]], [[append-and-review-note]]: every step is checked and supported. The definitions say "he"/"his" and no steps are invented. Product names are written as his choices as of the post date.
- [[choose-a-model-tier]], [[read-with-an-llm]], [[voice-input]]: every other step is supported. The "llm Council" quote, the $100/$200 slip reported as he says it, the NotebookLM hosts flagged as AI voices, and the Mermaid diagrams are all correct.
- [[transformers-need-tokens-to-think]], [[pretraining-gives-a-document-completer]], [[pretraining-is-lossy-compression-of-the-internet]], [[an-llm-is-just-two-files]], [[a-lot-of-llm-oddness-traces-back-to-tokenization]], [[tokenization-free-modeling-would-be-amazing-but-is-unproven]], [[rlhf-works-better-because-comparing-is-easier-than-generating]], [[use-llms-as-copilots-with-human-oversight]], [[llms-want-to-imitate-not-succeed]]: all D2 sentences are supported.
- Topics, sampled. All of these are supported:
  - pretraining-and-finetuning: 2.7B pages as of 2024; 65% English; 8,000-token windows; Llama 3 405B on 15T tokens; three months vs three hours; separate teams; RL "not standard"; zip file and six-month cutoff.
  - tokenization: 100,277; the strawberry "may have hardcoded" hedge; ~200,000 for GPT-4o.
  - compute-efficiency: $40,000, $600 and $100; $3 per GPU-hour.
  - scaling-laws: $3.4T, as of the lecture.
  - llm-c: 1M tokens per step, ~7 s, 32,000 steps, ~33B tokens.
  - prompting-llms: 80–90% GPT-4o use; few-shot "always increases the accuracy".
  - llm-tool-use: deep research comparison; memory "coming around".
  - llm-self-improvement: Move 37 at 1 in 10,000.
  - system-1-and-system-2-thinking: DeepSeek paper "first to talk about it publicly" (the F1 clause aside).
  - llm-evaluation: LM Arena "a little bit gamed"; Sonnet 14th.
  - ai-ecosystem: "unprecedented"; MIT licence.
  - llm-gui: not a daily artifacts user.
  - partial-autonomy-apps: Claude 3.7 Sonnet under Cursor.
  - vibe-coding: about five sentences; the "probably minted" hedge.
  - user-hostile-technology: the fraud-apparatus and CO2-monitor sentences; the internetofshit link is in both posts.
- Source pages: the Summary and Key points of all five checked about 1 in 3. All are supported apart from F4.
