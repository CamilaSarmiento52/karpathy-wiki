# Verification: batch 2, group C1 (CS25, State of GPT, profile README, Intro to LLMs)
Verified 2026-10-24 by a fresh reader. Sources: [[talk-2023-05-19-stanford-cs25-transformers]], [[talk-2023-05-25-state-of-gpt]], [[github-2023-07-25-karpathy-profile-readme]], [[youtube-2023-11-23-intro-to-llms]]

## Coverage
- pages checked: 37 (4 source pages; 20 claim pages; 12 topics: transformer-architecture, self-attention, tokenization, embeddings, character-level-language-modeling, prompting-llms, sampling-from-language-models, pretraining-and-finetuning, system-1-and-system-2-thinking, llm-tool-use, scaling-laws, llm-security, llm-self-improvement, llms-as-operating-systems, jagged-intelligence, partial-autonomy-apps; artifacts nanogpt, nn-zero-to-hero)
- claim pages fully checked: 20 (the 16 C1 claims: ai-has-converged-on-one-architecture, the-transformer-is-a-general-purpose-efficient-optimizable-computer, gpt-is-a-general-purpose-computer-running-natural-language-programs, with-enough-data-encode-less-inductive-bias, he-does-not-love-autoregressive-sampling, transformers-need-tokens-to-think, llms-want-to-imitate-not-succeed, rlhf-works-better-because-comparing-is-easier-than-generating, use-llms-as-copilots-with-human-oversight, an-llm-is-just-two-files, pretraining-is-lossy-compression-of-the-internet, llms-are-mostly-inscrutable-empirical-artifacts, scaling-offers-a-guaranteed-path-to-better-models, llms-currently-only-have-a-system-1, self-improvement-may-be-possible-in-narrow-domains, llms-are-the-kernel-of-an-emerging-operating-system; plus the existing attention-is-a-communication-mechanism, english-is-the-new-programming-language, pretraining-gives-a-document-completer, this-is-the-decade-of-agents)
- timeline entries checked: 0 (no timeline page cites these sources yet; llm-agents-over-time and llm-os-over-time are C2/C4)
- other sentences checked: ~75 of ~120. All 16 claim quotes grep-verified verbatim at the cited block and spoken by him (CS25 quotes all after @10:05; the two general-purpose-computer quotes are his own tweets read aloud, and the pages say so). The @16:08 "higher" garble is not repeated (pretraining-and-finetuning says the loss is "weighted by the reward"). Nothing from GPT-4's @40:31 address is quoted or attributed. The Scale AI valuation and the 38-hour nanoGPT figure are not stated as his.

## Findings
### F1 — wrong — [[attention-is-a-communication-mechanism]]
- sentence: "Four months later, in his Stanford CS25 lecture, he restates it: attention is the communication phase of the Transformer, ..."
- cited: [[talk-2023-05-19-stanford-cs25-transformers]] @22:45
- raw says: the course was taught in the winter 2023 quarter (@00:05, instructor) and he says he wrote nanoGPT "over the last few days" (@31:02), so the lecture was given around January 2023, about when the GPT-from-scratch video came out. Only the publication is four months later; the CS25 source page itself notes this.
- fix: "In his Stanford CS25 lecture, given in the winter 2023 quarter and published in May, he restates it: ..."

### F2 — wrong — [[prompting-llms]]
- sentence: "A week later he says prompting is to a large extent making up for the cognitive difference between brains and LLMs ([[talk-2023-05-25-state-of-gpt]] @23:55, @24:27)."
- cited: [[talk-2023-05-25-state-of-gpt]] @23:55, @24:27 (following a CS25 sentence)
- raw says: same dating problem as F1. The two were published six days apart, but CS25 was delivered in winter 2023, months before State of GPT (Microsoft Build, May 2023).
- fix: "In State of GPT (May 2023) he says prompting is to a large extent making up for ..."

### F3 — overstated — [[llms-as-operating-systems]]
- sentence: "His analogy that the LLM is a new kind of computer, first drawn in his November 2023 talk, where he calls the LLM the kernel process of an emerging operating system ..."
- cited: [[youtube-2023-11-23-intro-to-llms]] @42:06, @42:38
- raw says: the Intro talk is the wiki's first operating-system framing, but "LLM as a new kind of computer" is older in the wiki's own sources: in CS25 he reads his tweet that GPT is "a general purpose computer reconfigurable at runtime" (@59:51), and a "general purpose text computer" (@1:00:30).
- fix: "His analogy that the LLM is the kernel of a new kind of operating system, first drawn among the wiki's sources in his November 2023 talk, where ..." Optionally add a **Note:** linking [[gpt-is-a-general-purpose-computer-running-natural-language-programs]] as an earlier computer analogy (context only, no relation set).

### F4 — minor (relation strength) — [[use-llms-as-copilots-with-human-oversight]] ↔ [[this-is-the-decade-of-agents]]
- sentence: "Supports [[this-is-the-decade-of-agents]]: in 2023 he advises copilots with human oversight over autonomous agents ... Consistent caution, not an extension: the 2023 talk gives no timescale." (the mirror line on this-is-the-decade-of-agents says much the same)
- cited: [[talk-2023-05-25-state-of-gpt]] @39:57; [[youtube-2025-06-19-software-is-changing]] @27:09, @27:44
- raw says: in 2023 he says only that it is "not clear that the models are there right now" (@39:57). That supports the 2025 humans-in-the-loop point (@27:44) but is no evidence for the claim's title, a decade-long timescale. Both lines already admit there is no timescale, so the link is weak but kept honest. The merge map asks for the link, so keep it and narrow the wording.
- fix: on both pages, start the line "Supports the human-in-the-loop half of ...: ..." and keep "the 2023 talk gives no timescale". No link change.

### F5 — minor — [[pretraining-and-finetuning]]
- sentence: "On the Berkeley Elo ranking he puts GPT-4 best by far, then Claude and GPT-3.5, which he says are RLHF models, and the rest, to his knowledge, SFT models"
- cited: [[talk-2023-05-25-state-of-gpt]] @19:29, @20:02
- raw says: "The first three rows here are all RLHF models" — the first three rows are GPT-4, Claude and GPT-3.5, so GPT-4 is included.
- fix: "On the Berkeley Elo ranking he puts GPT-4 best by far, then Claude and GPT-3.5; he says these first three are RLHF models and the rest, to his knowledge, SFT models"

### F6 — minor — [[transformer-architecture]] (garble correction, note only)
- sentence: "the change he knows of that stuck is moving the layer norms to the pre-norm position"
- cited: [[talk-2023-05-19-stanford-cs25-transformers]] @21:39
- raw says: the caption says "the only thing ... that didn't stick was this uh we shuffling up the layer Norms". The sense, given "nothing like sticks" just before, is that pre-norm is the one change that did stick. The wiki's reading is right and it does not quote the garble, so no text change is needed. Logged so a later fixer does not "correct" it back to the caption.
- fix: none required.

## Checked and correct
- [[ai-has-converged-on-one-architecture]]: title, quote (@13:56), 7 Context sentences, Note; all supported. The brain hedge ("maybe") is kept.
- [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]: quote (@59:18), 7 sentences; the tweets-are-hyped preface is kept; all supported.
- [[gpt-is-a-general-purpose-computer-running-natural-language-programs]]: quote (@59:51, his tweet read aloud), 4 sentences, supports line; both sides verified (CS25 @59:51, Software Is Changing @03:19, @04:23). The "does not extend" judgement is correct.
- [[with-enough-data-encode-less-inductive-bias]]: quote (@1:06:28), 3 sentences, Note (@1:05:57); all supported.
- [[he-does-not-love-autoregressive-sampling]]: quote (@50:15), 3 sentences; all supported. ("when he writes" renders captioned "when I sample text", which is fair given the draft-one/draft-two analogy.)
- [[transformers-need-tokens-to-think]], [[llms-want-to-imitate-not-succeed]], [[rlhf-works-better-because-comparing-is-easier-than-generating]], [[use-llms-as-copilots-with-human-oversight]] (apart from F4): quotes verbatim at @24:59, @30:02, @18:21, @39:57; every Context sentence supported; paper findings (InstructGPT, "work this out step by step") credited to the papers; the RLHF title keeps his "one reason potentially" hedge.
- [[an-llm-is-just-two-files]], [[pretraining-is-lossy-compression-of-the-internet]], [[llms-are-mostly-inscrutable-empirical-artifacts]], [[scaling-offers-a-guaranteed-path-to-better-models]], [[llms-currently-only-have-a-system-1]], [[self-improvement-may-be-possible-in-narrow-domains]], [[llms-are-the-kernel-of-an-emerging-operating-system]]: quotes verbatim at @00:00, @05:30, @13:15, @26:02, @36:31, @40:27, @42:06; all numbers (140 GB, 2 bytes, ~500 lines, 10 TB, ~100x, 40 days) match; hedges and "field broadly interested" framing kept; titles dated where they describe the state of models.
- [[pretraining-gives-a-document-completer]]: the State of GPT paragraph (3 sentences, @08:56–@10:36) and the Intro sentence (@20:30) are supported; adding both as sources is correct.
- [[english-is-the-new-programming-language]]: the supported-by line is verified on both sides.
- [[this-is-the-decade-of-agents]]: the State of GPT line is accurate (see F4 for wording); State of GPT is correctly `context`, not evidence for the title.
- [[jagged-intelligence]]: 2023 sources are `context` only, `first_seen` stays 2025-06-19, and both 2023 sentences are labelled **Note:** and say he did not use "jagged". Checked against @22:45–@23:55 (SoG) and @12:43, @51:27, @51:59 (Intro). Not misused as evidence for the 2025 framing.
- [[partial-autonomy-apps]]: State of GPT is `context` only; the 2023 sentence is a labelled **Note:** ("background ..., not the same term"); @28:21, @28:54, @39:57 supported. Not misused.
- [[llms-as-operating-systems]] (apart from F3): 9 "2023 version" sentences checked (@24:22–@45:25), all supported; the kernel-vs-CPU Note is correctly editorial. The 2023 source is the original statement, not a stand-in for the 2025 framing.
- [[transformer-architecture]]: 14 of ~20 CS25 sentences checked (history @15:00–@19:57, BERT/T5 @44:20–@44:52, ResNet @48:28, flexible inputs @52:43–@55:30, RNN comparison @1:02:29–@1:03:35); all supported. The first author's attention story is attributed to him as relayed.
- [[self-attention]]: 8 of 11 checked; all supported (connectivity fixed @46:44; sqrt scaling @52:09).
- [[prompting-llms]] (apart from F2): 10 of ~16 checked; the hedged ResNet analogy and the papers' positions are attributed correctly.
- [[pretraining-and-finetuning]] (apart from F5): 14 of ~30 checked, including 99 percent compute, LLaMA 1.4T vs 300B, 2,000 GPUs / 21 days, 6,000 GPUs / 12 days / $2M, 100,000 Q&A, the RLHF naming at @22:09, and the labeling slider (correctly kept on labels, not agents); all supported.
- [[system-1-and-system-2-thinking]], [[llm-tool-use]], [[scaling-laws]], [[llm-security]], [[llm-self-improvement]]: 18 sentences checked; all supported. The Apps Script admission, the sleeper-agent fine-tuning-only caveat and the ChatGPT valuation-in-jest are all handled correctly.
- [[tokenization]], [[embeddings]], [[character-level-language-modeling]], [[sampling-from-language-models]], [[nanogpt]]: 12 sentences checked; all supported; the 38-hour figure is correctly omitted.
- [[nn-zero-to-hero]]: the one profile-README **Note:** sentence matches the five-word raw ("I like deep neural nets.").
- Source pages: Summaries and Key points of all four spot-checked (~15 sentences); speaker boundaries stated correctly; all supported.

## Resolution
Fixed 2026-10-24 (log: `## 2026-10-24 correction`).
- F1 fixed
- F2 fixed
- F3 fixed (also dropped "first", per the §2 rule on ordering from published dates, and made the definition a full sentence; optional Note not added)
- F4 fixed (mirror line on this-is-the-decade-of-agents also loses "two years earlier")
- F5 fixed
- F6 left as is: the report asks for no change; the wiki's pre-norm reading is correct
