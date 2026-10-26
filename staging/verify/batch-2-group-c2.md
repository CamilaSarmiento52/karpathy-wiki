# Verification: batch 2, group C2 (Zero to Hero README, GPT tokenizer lecture, technical-accessibility post, Sequoia interview, minbpe README)
Verified 2026-10-24 by a fresh reader. Sources: [[github-2024-02-20-nn-zero-to-hero-readme]], [[youtube-2024-02-20-gpt-tokenizer]], [[x-2024-02-21-technical-accessibility]], [[talk-2024-03-26-sequoia-making-ai-accessible]], [[github-2024-04-22-minbpe-readme]]

## Coverage
- pages checked: 37 (5 source pages; 15 claim pages; 12 topics: tokenization, embeddings, pretraining-and-finetuning, ai-ecosystem, compute-efficiency, elon-musk-management-style, scaling-laws, llm-self-improvement, llms-as-operating-systems, partial-autonomy-apps, sampling-from-language-models, transformer-architecture; 4 artifacts: nn-zero-to-hero, minbpe, micrograd, makemore; 4 methods: spelled-out-build-from-scratch, small-hackable-educational-code, verify-against-a-reference-implementation, make-it-work-then-make-it-cheap; 1 timeline: llm-agents-over-time)
- claim pages fully checked: 15. The 8 new C2 claims, checked whole: a-lot-of-llm-oddness-traces-back-to-tokenization, tokenization-free-modeling-would-be-amazing-but-is-unproven, he-prefers-tiktoken-byte-level-bpe-to-sentencepiece, open-weights-models-are-not-open-source, build-the-ramp-not-just-the-thing, ai-is-far-less-energy-efficient-than-the-brain, the-transformer-is-probably-not-the-final-architecture, llm-products-will-take-years-to-figure-out. Every sentence that cites a C2 source was also checked on: he-does-not-love-autoregressive-sampling, self-improvement-may-be-possible-in-narrow-domains, scaling-offers-a-guaranteed-path-to-better-models, the-transformer-is-a-general-purpose-efficient-optimizable-computer, this-is-the-decade-of-agents, understand-backprop-even-with-autograd, deep-learning-is-largely-shape-gymnastics.
- timeline entries checked: 4 of 4 plus the closing Note, on llm-agents-over-time. The State of GPT, Software Is Changing and Year in Review entries were checked against their own raw files.
- other sentences checked: about 115 of about 210. This includes every bullet of the tokenization failure list (about 25 sentences), each checked against its cited blocks.
- All 8 new claim quotes were found verbatim with grep at the cited block, and each is his own words: @00:00, @22:59 and @2:11:45 in the lecture; @07:27, @13:27, @33:51 and @06:54 in the interview; "Step 2 build the ramp." in the post.
- Sequoia attribution: the wiki was searched for every host and audience framing that the digest lists ("scale is all that matters", the rowing joke, "democratizing", "graduate school", "within sight", "dominating", "many agents", "investor"). None is attributed to him. scaling-laws says "Asked by the host"; elon-musk-management-style marks the rowing joke as the host's; the @04:39 "many agents" clause is not quoted anywhere.

## Findings
### F1 — wrong — [[a-lot-of-llm-oddness-traces-back-to-tokenization]] (and minor on [[tokenization]])
- sentence: "His list: spelling and simple string processing, non-English languages, simple arithmetic, GPT-2's trouble with Python, the model halting at `<|endoftext|>`, warnings about trailing whitespace, SolidGoldMagikarp, and being told to prefer YAML over JSON ([[youtube-2024-02-20-gpt-tokenizer]] @04:27, @05:00, @05:33). At the end of the lecture he returns to each item and explains it, adding partial and unstable tokens; ... (@1:51:24, @2:01:41)."
- cited: [[youtube-2024-02-20-gpt-tokenizer]] @04:27–@05:33
- raw says: the opening list (@04:27–@05:33) has spelling, string processing, non-English, arithmetic, GPT-2 Python, trailing whitespace, SolidGoldMagikarp and YAML over JSON. `<|endoftext|>` is not on it. He first raises it in the closing walkthrough (@1:57:09, "my llm abruptly halts when it sees the string end of text"). The partial and unstable tokens come at @2:01:41–@2:04:28; "unstable" is first named at @2:03:20.
- fix: "His list: spelling and simple string processing, non-English languages, simple arithmetic, GPT-2's trouble with Python, warnings about trailing whitespace, SolidGoldMagikarp, and being told to prefer YAML over JSON (... @04:27, @05:00, @05:33). At the end of the lecture he returns to each item and explains it, adding the model halting at `<|endoftext|>` and partial and unstable tokens; ... (@1:51:24, @1:57:09, @2:01:41, @2:03:20)."
- also, on [[tokenization]] under "The failures he traces to tokenization": the intro says he "returns at the end to explain each", and the bullets that follow include two items that were not on the opening list. Add "(added in the closing walkthrough)" to the **Halting at `<|endoftext|>`** bullet and to the **Partial and unstable tokens** bullet.

### F2 — overstated — [[tokenization]]
- sentence: "Prompting with part of a single token, ".DefaultCellSta", made the model emit end of text at once and on retry trip a usage-policy flag; he points to tiktoken's undocumented handling of unstable tokens as the gnarly mechanism"
- cited: [[youtube-2024-02-20-gpt-tokenizer]] @2:02:14, @2:03:20, @2:04:28
- raw says: the model "predicted the stop sequence immediately". He hedges what it emitted: "sort of like end of text token I think or something like that". tiktoken's unstable-token code is where this case gets special handling, which he says is undocumented; it is not the cause. The cause he gives is partial tokens.
- fix: "Prompting with part of a single token, ".DefaultCellSta", made the model predict a stop sequence at once (an end-of-text token, he thinks) and on retry trip a usage-policy flag; he points to tiktoken's undocumented special-case code for 'unstable tokens', which deals with exactly this partial-token problem"

### F3 — minor (date) — [[he-does-not-love-autoregressive-sampling]], [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]], [[this-is-the-decade-of-agents]]
- sentences: "On 2024-03-26, asked about open research problems, he names ..." / "**Note:** on 2024-03-26 he again calls it remarkably resilient ..." / "on 2024-03-26 he says LLM systems are quite autonomous but not fully ..."
- cited: [[talk-2024-03-26-sequoia-making-ai-accessible]] @12:22, @33:51, @06:54
- raw says: 2024-03-26 is the date the interview was published, not the date he spoke. The talk refers to "Jensen at GTC that happened just yesterday or two days ago" (@01:46, also @12:55). From outside the sources: the GTC 2024 keynote was 18 March 2024, so he likely spoke about a week earlier. Ordering is unaffected.
- fix: replace each "On/on 2024-03-26" with "In the Sequoia interview (published 2024-03-26)". The "(Sequoia, 2024-03-26)" headings on topic pages can stay as source labels.

### F4 — mis-cited — [[llm-agents-over-time]]
- sentence: "**2023-05-25** — Recommends low-stakes uses with human oversight, as copilots rather than autonomous agents; AutoGPT does not work well yet → ... ([[talk-2023-05-25-state-of-gpt]] @29:28, @39:57)"
- cited: [[talk-2023-05-25-state-of-gpt]] @29:28, @39:57
- raw says: @29:28 only introduces AutoGPT as hyped but inspirationally interesting. "I don't think this currently works very well" is at @30:02. "use LLMs in low-stakes applications" ends the @39:24 block. The content is right.
- fix: cite "@29:28, @30:02, @39:24, @39:57".

### F5 — minor — [[tokenization]] (Non-English bullet)
- sentence: "\"Hello how are you\" is 5 tokens and its Korean translation 15"
- cited: [[youtube-2024-02-20-gpt-tokenizer]] @1:54:20
- raw says: "its translation is 15 tokens". The language is not named. Korean comes up only in the next clause, with the greeting annyeong.
- fix: "... is 5 tokens and its translation 15, and even the common Korean hello is three tokens"

### F6 — minor (hedge) — [[embeddings]]
- sentence: "... so invoking it gives undefined behaviour, his reading of SolidGoldMagikarp"
- cited: [[youtube-2024-02-20-gpt-tokenizer]] @2:08:24, @2:08:57 (the hedge is at @2:07:16)
- raw says: he presents it as "what is thought to have happened" and says he does not know that it "has been like really definitively explored". It is the explanation he passes on, not his own reading. [[tokenization]] keeps this hedge.
- fix: "..., which he gives as what is thought to have happened with SolidGoldMagikarp (@2:07:16, @2:08:24, @2:08:57)"

### F7 — minor — [[ai-ecosystem]]
- sentence: "He proposes three categories, open-weights, open-source and proprietary models, and expects the ecosystem to look much like today's"
- cited: [[talk-2024-03-26-sequoia-making-ai-accessible]] @09:05
- raw says: "probably it's going to look very similar to the ones that we have today". In context "the ones" are the operating-system ecosystems he has just compared (proprietary Windows and macOS beside Linux), not today's AI market.
- fix: "... and expects it to look much like today's operating-system ecosystems"

### F8 — minor (dropped condition) — [[talk-2024-03-26-sequoia-making-ai-accessible]] (Summary)
- sentence: "... and says founders can copy it if they set it up from the start (@16:13, @18:25, @20:02, @22:46)"
- cited: @22:14, @22:46
- raw says: his first condition is "it's up to the DNA of the founder", then making it clear up front and staying consistent. [[elon-musk-management-style]] keeps both.
- fix: "... and says founders with the same DNA can run a company that way if they set it up from the start and stay consistent (... @22:14, @22:46)"

## Checked and correct
- [[a-lot-of-llm-oddness-traces-back-to-tokenization]] (apart from F1): quote verbatim @00:00. The @04:27 "do not brush it off" advice, the @2:01:10 root cause, both hedges (@1:57:44, @2:07:16) and the README Lecture 8 sentence are all supported.
- [[tokenization]] failure list (apart from F1, F2, F5), every bullet checked: spelling (the hedge "if I'm not getting this wrong myself" is kept, and the list-then-reverse result is right); arithmetic (the blog post is credited to its author; Llama 2 splits digits "partly"); Python (partly modelling, @14:32 tokenizer-design claim); `<|endoftext|>` (his suspicion, "attack surface potentially"); trailing whitespace; SolidGoldMagikarp (hedged, the blog post is credited); JSON 116 vs YAML 99. Nothing he hedges is stated as fact except the stop-token detail in F2. Also spot-checked: 150,000 characters across 161 scripts, 20 occurrences of (101, 32), 616→596, compression of about 1.27, GPT-4 regex merging up to three digits ("we don't really know why"), vocabulary size as "mostly an empirical hyperparameter", SentencePiece summary @1:42:36–@1:43:09, recommendations @2:10:39–@2:12:18; and the minbpe README paragraph (hedges, footgun, the special token id 32,768).
- [[tokenization-free-modeling-would-be-amazing-but-is-unproven]]: quote @22:59. The paper's conclusion is credited to its authors, his doubt that it is proven ("by sufficiently many groups and a sufficient scale") is kept at @23:32, and "eternal glory" is at @2:10:39. The title is properly hedged.
- [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]]: quote @2:11:45. "Significantly cleaner" @1:30:16, baggage and quirks @1:31:22/@1:42:36, "nice repo ... train your own" @1:43:09, ideal "tiktoken but training code" @2:12:18. The Note against GPT lecture @10:35 is verified.
- [[open-weights-models-are-not-open-source]]: quote @07:27, binary analogy @07:27–@07:59, regression on finetuning @08:32, three categories @09:05, Meta "only just done the open weights" @31:06. All supported.
- [[build-the-ramp-not-just-the-thing]]: quote verbatim, emoji dropped. "Many months", "almost 100X", "somewhere 10-100X" and the "voice in your head" are all hedged as in the post. Sequoia @32:13 and @32:45 are his, answering an audience member.
- [[ai-is-far-less-energy-efficient-than-the-brain]]: quote @13:27. The 20 W vs megawatts comparison and the "I don't know how much you need exactly" hedge are at @12:55; the levers are at @13:59 and @14:33. Supported.
- [[the-transformer-is-probably-not-the-final-architecture]]: quote @33:51, "absolutely it's not" verbatim @34:24, designed for the GPU @34:57, resilient @35:30. The CS25 Note (@21:39, @58:44) is verified. Correctly no relation.
- [[llm-products-will-take-years-to-figure-out]]: quote @06:54 (his words), iPhone-apps analogy @06:20, "next few years" @06:54, agents @04:39 (his clause, not the uncertain one). The weak supports line is honest about the horizon. The mirror line on [[this-is-the-decade-of-agents]] is verified against Software Is Changing @26:01–@27:44.
- [[llm-agents-over-time]] (apart from F4): entries 2–4 match Sequoia @06:54, Software Is Changing @27:09/@27:44 and Year in Review §4. The order is right by publication date and also by delivery date. No entry spaces sources apart. The closing Note is labelled, and it says the dates are publication dates and that the view accumulated.
- [[he-does-not-love-autoregressive-sampling]], [[self-improvement-may-be-possible-in-narrow-domains]], [[scaling-offers-a-guaranteed-path-to-better-models]], [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]: the Sequoia sentences are supported (@12:22, @12:55, @34:24; @24:59–@26:39; @09:38, @11:15; @33:51, @35:30). The self-improvement page rightly says Sequoia does not speak of narrow domains.
- [[understand-backprop-even-with-autograd]], [[deep-learning-is-largely-shape-gymnastics]]: the README Lecture 5 and Lecture 6 sentences match the raw closely.
- [[ai-ecosystem]] (apart from F7): 10 of 12 sentences checked, including the coral reef @21:10, megacorps @21:41 (the "think that through more" hedge is kept), the Meta incentive @30:33–@31:40 and LLM360 (garble flagged). Supported.
- [[elon-musk-management-style]]: 7 sentences checked (@16:13–@22:46), including the 50-person meetings, doubling the GPU cluster and the DNA condition. The rowing joke is the host's. Supported.
- [[compute-efficiency]], [[scaling-laws]], [[llm-self-improvement]], [[llms-as-operating-systems]], [[pretraining-and-finetuning]], [[sampling-from-language-models]], [[transformer-architecture]], [[partial-autonomy-apps]]: every Sequoia paragraph was checked. "A few bits or even 1.58" avoids the garble. The physicist and composability questions are attributed to the audience. The "graduate school" framing is not used. Supported.
- [[make-it-work-then-make-it-cheap]]: the Sequoia definition sentence and steps 1, 3, 5 and 6 (@28:56–@30:01) are supported. It correctly separates "the paradigm a few people ... say works" from his own suggestion.
- [[minbpe]]: 7 of 14 bullets checked (@1:25:09–@1:28:04 with the "I'm not sure" Python hedge kept; README §intro, §todos, §tests). Supported.
- [[nn-zero-to-hero]], [[micrograd]], [[makemore]]: README Lectures 1–8, "Ongoing...", and the post's ~200 lines vs the lecture's 150 kept apart. Supported.
- [[spelled-out-build-from-scratch]], [[small-hackable-educational-code]], [[verify-against-a-reference-implementation]]: 10 sentences checked (@28:01, @45:16, @55:56, @56:30, @1:11:42, @1:17:50, @1:26:20; README §inference, §exercise, §lecture, §training; the post). Supported.
- Source pages: the Summaries and Key points of all five were checked about 1 in 3. Fed pages match the pages that actually cite each source. The minbpe "in principle and to my knowledge" hedge is kept. Apart from F8, supported.

## Resolution
Fixed 2026-10-24 (log: `## 2026-10-24 correction`).
- F1 fixed (claim page and both tokenization bullets)
- F2 fixed (citation also adds @2:02:14, @2:03:53)
- F3 fixed (all three pages)
- F4 fixed
- F5 fixed
- F6 fixed
- F7 fixed
- F8 fixed (Summary and the matching Key point)
