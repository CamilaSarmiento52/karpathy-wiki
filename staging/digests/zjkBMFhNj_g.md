# Digest: [1hr Talk] Intro to Large Language Models
- raw: raw/youtube/zjkBMFhNj_g.md · published: 2023-11-23 · medium: youtube · words: 12285
- source slug: youtube-2023-11-23-intro-to-llms

## Source page

```
---
type: source
raw_path: raw/youtube/zjkBMFhNj_g.md
published: 2023-11-23
medium: youtube
summary: "A one-hour general-audience talk: an LLM as two files, pretraining as lossy compression of the internet, finetuning into an assistant, scaling laws, tool use, System 2 and self-improvement as open directions, the LLM as an operating-system kernel, and LLM security."
url: https://www.youtube.com/watch?v=zjkBMFhNj_g
title: "[1hr Talk] Intro to Large Language Models"
---
# [1hr Talk] Intro to Large Language Models
Raw: [[raw/youtube/zjkBMFhNj_g]] · Original: https://www.youtube.com/watch?v=zjkBMFhNj_g

## Summary
A re-recording, on his own channel, of a 30-minute intro talk he had given at an event run by Scale AI (@00:00, @03:18). He describes an LLM such as Llama 2 70B as two files, a 140 GB parameters file and about 500 lines of C that run it, and training as a lossy compression of roughly 10 TB of internet text into those parameters (@01:40, @02:13, @04:25, @05:30). He explains next-word prediction, why it forces the network to learn about the world, and why sampling from it "dreams" internet documents, then describes pretraining, finetuning on human-written Q&A, and an optional comparison-based RLHF stage (@07:43, @08:50, @14:21, @21:03, @22:09). The middle of the talk covers scaling laws, tool use (browser, calculator, Python, DALL-E) and multimodality, and research directions: System 2 thinking, AlphaGo-style self-improvement and customization (@25:28, @32:07, @33:12, @35:23, @38:14, @40:27). He ties these into the LLM as the kernel process of an emerging operating system, then closes with LLM security: jailbreaks, prompt injection and data poisoning (@42:06, @43:45, @45:59, @51:27, @56:28).

## Key points
- An LLM is two files, the parameters and a small program that runs them; inference is cheap, training is the expensive part → [[lossy-compression-of-the-internet]], [[an-llm-is-just-two-files]]
- Pretraining compresses about 10 TB of text into 140 GB of parameters, roughly 100x and lossy → [[lossy-compression-of-the-internet]], [[pretraining-is-lossy-compression-of-the-internet]]
- Next-word prediction forces the network to learn a lot about the world → [[next-word-prediction-forces-learning-about-the-world]]
- Sampling dreams internet documents; you never know which parts are memorized or hallucinated → [[lossy-compression-of-the-internet]]
- We know the architecture but not what the parameters do; treat LLMs as mostly inscrutable empirical artifacts → [[llms-are-mostly-inscrutable-empirical-artifacts]], [[jagged-intelligence]]
- Pretraining is about knowledge, finetuning about alignment; base models answer questions with more questions → [[pretraining-and-finetuning]], [[pretraining-gives-a-document-completer]]
- Stage three uses comparisons because comparing is easier than writing; OpenAI calls it RLHF → [[pretraining-and-finetuning]]
- Closed models currently work better; open models chase them → [[llms-as-operating-systems]]
- Performance is a smooth, predictable function of parameters and data, which drives the GPU gold rush → [[scaling-laws]], [[scaling-offers-a-guaranteed-path-to-better-models]]
- Tool use and multimodality are major axes of improvement → [[llm-tool-use]], [[tool-use-is-a-major-source-of-llm-capability]]
- LLMs currently have only System 1; the aim is to convert time into accuracy → [[system-1-and-system-2-thinking]], [[llms-currently-only-have-a-system-1]]
- Self-improvement lacks a general reward criterion but may work in narrow domains → [[llm-self-improvement]], [[self-improvement-may-be-possible-in-narrow-domains]]
- The LLM is the kernel process of an emerging OS; the context window is its RAM → [[llms-as-operating-systems]], [[llms-are-the-kernel-of-an-emerging-operating-system]]
- Jailbreaks, prompt injection and data poisoning are a new cat-and-mouse security field → [[llm-security]], [[llm-security-is-a-cat-and-mouse-game]]

## Fed pages
- [[lossy-compression-of-the-internet]]
- [[an-llm-is-just-two-files]]
- [[pretraining-is-lossy-compression-of-the-internet]]
- [[next-word-prediction-forces-learning-about-the-world]]
- [[llms-are-mostly-inscrutable-empirical-artifacts]]
- [[jagged-intelligence]]
- [[pretraining-and-finetuning]]
- [[pretraining-gives-a-document-completer]]
- [[scaling-laws]]
- [[scaling-offers-a-guaranteed-path-to-better-models]]
- [[llm-tool-use]]
- [[tool-use-is-a-major-source-of-llm-capability]]
- [[system-1-and-system-2-thinking]]
- [[llms-currently-only-have-a-system-1]]
- [[llm-self-improvement]]
- [[self-improvement-may-be-possible-in-narrow-domains]]
- [[llms-as-operating-systems]]
- [[llms-are-the-kernel-of-an-emerging-operating-system]]
- [[llm-security]]
- [[llm-security-is-a-cat-and-mouse-game]]
```

## Candidates

### topic: lossy-compression-of-the-internet
- existing: no
- aliases: LLM as two files, parameters file, run file, zip file of the internet, lossy compression, next-word prediction, model inference vs training, hallucination, dreaming internet documents
- statements:
  - Llama 2 70B is the example: Meta released weights, architecture and paper, so anyone can work with it, unlike ChatGPT, whose architecture was never released and which you use through a web interface (@00:33, @01:06).
  - The model is two files: a parameters file of 140 GB (70 billion parameters at 2 bytes each, float16) and a run file, which in C would be about 500 lines with no dependencies (@01:40, @02:13).
  - The two files are a self-contained package: compile the C code, point the binary at the parameters, and talk to the model on a MacBook without internet (@02:45). He admits the demo video ran the 7B model; 70B would be about 10 times slower (@03:18).
  - The architecture and forward pass are algorithmically understood and open; the magic, and the computational cost, is in obtaining the parameters (@03:52).
  - Training Llama 2 70B took roughly 10 TB of crawled internet text, about 6,000 GPUs for about 12 days, and about $2 million (@04:25, @04:57).
  - Training compresses that text into parameters best thought of as a zip file of the internet, about 100x compression, but lossy: a Gestalt of the text, not an identical copy (@05:30).
  - He calls these "rookie numbers" by state-of-the-art standards; frontier models are off by a factor of 10 or more, and their runs cost tens or hundreds of millions of dollars (@06:02). Once trained, running the network is fairly cheap (@06:37).
  - The network predicts the next word in a sequence (example: "cat sat on a" → "mat" at 97%) (@06:37, @07:10). There is a close mathematical relationship between prediction and compression, which is why he calls training a compression of the internet (@07:10, @07:43).
  - Sampling word by word and feeding the output back in makes the network "dream" internet documents: Java code, an Amazon product page with a made-up ISBN, a Wikipedia-like article (@08:50, @09:25, @09:58).
  - The fish article is not verbatim in the training set but roughly correct; the model fills the right form with its knowledge, and you never know which parts are memorized and which are hallucinated (@10:30, @11:02).
- relation to an existing page: none; **Note** for merge: the lecture-era pages describe next-token prediction at toy scale ([[character-level-language-modeling]], [[pretraining-and-finetuning]]); this is his first general-audience framing.

### claim: an-llm-is-just-two-files
- existing: no
- title: "A large language model is just two files: parameters and the code that runs them"
- confidence: stated
- quote: "a large language model is just two files" (@00:00)
- statements: as in the topic above (@00:00, @01:40, @02:13, @02:45).
- relation to an existing claim: supports [[gpt-is-not-a-complicated-model]] (2023-01-08: GPT is about 300 lines, the complexity is batching) — here the run code is about 500 lines of C and the architecture is fully understood (@02:13, @03:52). Weak link; merge may prefer a `## Related claims` note over a `supports` field.

### claim: pretraining-is-lossy-compression-of-the-internet
- existing: no
- title: "Pretraining is like a lossy compression of a chunk of the internet into the parameters"
- confidence: stated
- quote: "like a zip file of the internet" (@05:30); also "What's Happening Here is a lossy compression" (@05:30)
- statements: 10 TB to 140 GB, about 100x, lossy, a Gestalt (@04:25, @05:30); prediction and compression are closely related (@07:10).
- relation to an existing claim: supports [[pretraining-gives-a-document-completer]] in part: the compressed model "dreams" internet documents (@08:50) as the 2023-01 lecture's model "babbles internet". Merge may fold this claim into the topic instead of a page; it overlaps the topic heavily.

### claim: next-word-prediction-forces-learning-about-the-world
- existing: no
- title: "Next-word prediction is a simple but powerful objective that forces the network to learn about the world"
- confidence: stated
- quote: "you're learning a ton about the world" (@08:50) (grep-verified; the fuller sentence at @07:43 is garbled, "next word predition", and over 15 words)
- statements: predicting the next word on a Wikipedia page about Ruth Handler requires knowing who she was, when she was born and died, and what she did; that knowledge is compressed into the weights (@07:43, @08:16, @08:50).
- relation: none.

### claim: llms-are-mostly-inscrutable-empirical-artifacts
- existing: no
- title: "LLMs are mostly inscrutable artifacts, treated as empirical objects and needing sophisticated evaluations"
- confidence: stated
- quote: "they're not like a car where we sort of understand all the parts" (@13:15)
- statements:
  - We know every mathematical operation in the Transformer, but not what the ~100 billion parameters do; we only know how to adjust them to improve next-word prediction (@11:36, @12:10).
  - They seem to build a knowledge database that is strange and imperfect; the "reversal curse" (GPT-4 knows Tom Cruise's mother but not her son) shows knowledge that is one-dimensional, accessible from one direction (@12:43).
  - Mechanistic interpretability can explain parts but not fully; for now we treat them as empirical artifacts, measuring behaviour, which needs correspondingly sophisticated evaluations (@13:15, @13:49).
- relation to an existing page: no existing claim; the reversal curse is an early example of the uneven capability on [[jagged-intelligence]] (2025-06-19 @16:04 lists hallucination and errors no human would make). **Note:** he does not use the word "jagged" in 2023; merge should cite this source on jagged-intelligence as a `context` or with a **Note:**, not as the 2023 origin of the term.

### topic: pretraining-and-finetuning
- existing: yes (aliases include Pretraining, finetuning, RLHF, ChatGPT training stages, alignment stage, fine-tuning)
- statements:
  - Stage one, pretraining, yields internet document generators; stage two, finetuning, yields an assistant model (@14:21).
  - Finetuning keeps the optimisation identical (next-word prediction) but swaps the dataset for manually collected conversations written by people hired with labeling instructions (@14:21, @14:55).
  - Pretraining data is large but low quality; finetuning prefers quality over quantity, e.g. 100,000 high-quality conversations (@16:04).
  - It is remarkable, empirical and not fully understood that the finetuned model changes its format to a helpful assistant while still using the knowledge built in pretraining (@17:11).
  - Roughly, pretraining is about knowledge and finetuning is about alignment, changing the format from internet documents to Q&A (@17:11).
  - Pretraining costs millions of dollars and happens inside companies maybe once a year; finetuning is much cheaper, perhaps a day, so companies iterate on it weekly or daily (@17:45, @18:18, @18:50, @19:58).
  - The finetuning loop: evaluate, deploy, monitor misbehaviours, have a person write the correct response, add it to the training data, repeat (@19:24).
  - Meta's Llama 2 release includes both base and assistant models; the base model is not directly usable because it answers questions with more questions, but it lets you do your own finetuning (@19:58, @20:30).
  - An optional stage three uses comparison labels because comparing candidate answers is easier than writing one, e.g. picking the best haiku (@21:03, @21:36). At OpenAI this is called reinforcement learning from human feedback, RLHF (@22:09).
  - Labeling instructions (from the InstructGPT paper) ask for helpful, truthful and harmless responses and can run to tens or hundreds of pages (@22:09).
  - Labeling is increasingly human-machine collaboration — models sample answers, check work or create comparisons, with people in oversight — "a slider" that is moving to the right as models improve (@22:42, @23:15).
  - Chatbot Arena ranks models by Elo from blind pairwise votes (@23:15, @23:47).
- relation: extends the 2023-01-17 lecture's account (supervised finetuning, reward model, PPO) with costs, the iteration loop, base vs assistant models, and the name RLHF. **Note** for merge: the existing page's `## Related` says he "does not use the term" RLHF in the lecture; this source does name it (@22:09), so that note should be updated to say the term first appears here, not edited as a correction (the lecture statement stays true).

### claim: pretraining-gives-a-document-completer
- existing: yes
- statements: the Llama 2 base model "is not directly usable" and, given questions, gives more questions, because it is just an internet document sampler (@20:30).
- relation: supports (same view ten months later, citing both: 2023-01-17 @1:51:29 and this source @20:30). Add as a second source.

### topic: scaling-laws
- existing: no
- aliases: Scaling laws, N and D, bigger models more data, GPU gold rush
- statements:
  - Next-word prediction accuracy is a remarkably smooth, predictable function of two variables: N, the number of parameters, and D, the amount of training text (@25:28, @26:02).
  - The trends do not seem to show signs of topping out, so a bigger model on more text gives better prediction with high confidence (@26:02).
  - Next-word accuracy is not the goal, but empirically it correlates with evaluations we care about; going from GPT-3.5 to GPT-4 improved all of the tests he shows (@26:35, @27:10).
  - This drives the "gold rush" for bigger GPU clusters and more data; algorithmic progress is a bonus that organizations still invest in (@27:10).
- relation: none to existing pages. **Note:** the 2025 [[rlvr]] page says RLVR took compute labs had meant for pretraining and added test-time compute as a new knob; that is a different axis, not a link to set.

### claim: scaling-offers-a-guaranteed-path-to-better-models
- existing: no
- title: "In 2023 he said scaling offers one guaranteed path to better models; algorithmic progress is a bonus"
- confidence: stated
- quote: "algorithmic progress is not necessary it's a very nice bonus" (@26:02)
- statements: "the scaling kind of offers one guaranteed path to success" (@27:10, sentence crosses into the @27:43 block; over the paraphrase limit as a single quote).
- relation: none existing. Possible future link to his 2025 RLVR account (test-time compute as a new scaling knob) — not a contradiction.

### topic: llm-tool-use
- existing: no
- aliases: Tool use, browsing, calculator, code interpreter, DALL-E, multimodality, retrieval augmented generation, RAG, customization, GPTs App Store
- statements:
  - Finetuning teaches ChatGPT that some queries call for tools rather than answering directly; it emits special words that trigger a search, and the results are fed back as text (@27:43, @28:18, @28:49).
  - His Scale AI funding demo uses the browser for funding rounds, a calculator to impute missing valuations because, like people, the model is not good at math in its head, Python with matplotlib to plot, and DALL-E to generate an image (@28:49, @29:53, @30:25, @31:00, @32:40).
  - Tool use ties existing computing infrastructure together with words; it is not just working in its head and sampling words (@32:07). People solve problems with tools too, and he sees the same for LLMs (@33:12).
  - Multimodality is a major axis: seeing images (Greg Brockman's sketched joke website turned into working HTML and JavaScript), generating them, and hearing and speaking in speech-to-speech mode (@33:12, @33:45, @34:19).
  - Customization is another axis: OpenAI's GPTs App Store allows custom instructions and uploaded files, which ChatGPT references via retrieval augmented generation, like browsing your files; future customization might include finetuning (@40:27, @41:00, @41:32). The aim is many expert models for specific tasks rather than one model for everything (@42:06).
- relation: none existing. **Note:** merge may fold multimodality and customization into [[llms-as-operating-systems]] (they reappear in his LLM OS list @42:38, @43:11); kept here as one coarse topic per the batch-1 merge map.

### claim: tool-use-is-a-major-source-of-llm-capability
- existing: no
- title: "Tool use is a major aspect of how LLMs are becoming more capable"
- confidence: stated
- quote: "it's not just about sort of working in your head and sampling words" (@32:07)
- relation: none.

### topic: system-1-and-system-2-thinking
- existing: no
- aliases: System 1, System 2, Thinking Fast and Slow, tree of thoughts, converting time into accuracy, thinking longer
- statements:
  - He takes the distinction from the book Thinking, Fast and Slow: System 1 is quick and instinctive (2+2), System 2 is slower, rational and conscious (17×24; tournament vs speed chess) (@35:23, @35:57).
  - LLMs currently only have System 1: words go in, and each "chunk" of next-word prediction takes about the same time; they cannot reason through a tree of possibilities (@36:31).
  - Many people want to give LLMs a System 2: to convert time into accuracy, e.g. allow 30 minutes on a question, with accuracy rising monotonically with thinking time; no model could do this then (@37:06, @37:40).
  - He presents this as a direction the field is interested in, not an OpenAI product announcement (@34:52).
- relation: none to an existing claim. **Note:** two years later, the [[rlvr]] page (2025-12-19 §1) describes test-time compute, letting models think longer, as a new knob, with o1 as the first RLVR model. The 2023 wish and the 2025 report are compatible; link as `## Related` (and possibly a timeline "thinking longer over time"), not as a changed view.

### claim: llms-currently-only-have-a-system-1
- existing: no
- title: "In November 2023, LLMs had only System 1 thinking"
- confidence: stated
- quote: "large language models currently only have a system one" (@36:31)
- secondary quote: "intuitively what we want to do is we want to convert time into accuracy" (@37:06)
- relation: none existing; see Note above re [[rlvr]]. Not `contradicts`: dated statement about the state of models.

### topic: llm-self-improvement
- existing: no
- aliases: Self-improvement, AlphaGo step two, beyond imitation, reward function
- statements:
  - AlphaGo had two stages: imitating expert human games, which can only reach the best human, then self-improvement by playing millions of games against a cheap, automatic reward (winning); it surpassed top humans in 40 days (@38:14, @38:46, @39:20).
  - LLMs today only do stage one, imitating human labelers, so it would be hard to exceed human response accuracy (@39:20, @39:52).
  - The open question is the step-two equivalent for open language modeling; the main challenge is the lack of a fast, simple reward criterion in the general case (@39:52).
  - In narrow domains such a reward function could be achievable, so self-improvement there may be possible; the general case is open (@40:27).
- relation: **Note:** the [[rlvr]] page (2025-12-19 §1) describes training against automatically checkable rewards in verifiable domains, and [[jagged-intelligence]] (§2) says capability spikes near verifiable domains. That is close to the narrow-domain case he speculated about in 2023. Merge should link these as Related with a **Note:**; there is no existing claim page to set `supports` on.

### claim: self-improvement-may-be-possible-in-narrow-domains
- existing: no
- title: "He thinks LLM self-improvement may be possible in narrow domains with a reward function"
- confidence: stated (hedged: "I think it is possible")
- quote: "in narrow domains it will be possible to self-improve language models" (@40:27)
- secondary quote: "there's a lack of a reward Criterion in the general case" (@39:52)
- relation: none to an existing claim (rlvr is a topic). See Note above.

### topic: llms-as-operating-systems
- existing: yes (aliases: LLM OS, LLMs are operating systems)
- statements:
  - He says it is more correct to think of an LLM not as a chatbot or word generator but as the kernel process of an emerging operating system, coordinating memory and computational tools for problem solving (@42:06, @42:38).
  - His picture of an LLM in a few years: reads and generates text, knows more than any single human, browses and uses RAG, uses calculator and Python, sees and generates images and video, hears, speaks, generates music, thinks for a long time with a System 2, maybe self-improves in narrow domains, and is customized into many experts in an App Store (@42:38, @43:11).
  - The memory hierarchy maps over: disk or internet via browsing, RAM as the context window, a finite precious working memory that the kernel pages information in and out of (@43:45).
  - He sees further equivalents: multithreading, multiprocessing, speculative execution, user space and kernel space (@44:18).
  - The ecosystem also matches: proprietary OSes like Windows and macOS versus a Linux-based open ecosystem, and proprietary GPT, Claude and Bard versus an open ecosystem mostly based on Llama (@44:52).
  - The new computing stack is built around LLMs orchestrating tools for problem solving through a natural-language interface (@45:25).
  - Supporting observation: on Chatbot Arena closed models work a lot better, open models work worse but may be good enough, and open source is chasing the proprietary ecosystems (@24:22, @24:55).
- relation: **supports and extends** the 2025 page. Supports: the core analogy and the Windows/macOS vs Linux mapping are the same as 2025-06-19 (@08:54, @09:28, @10:01: model as CPU, context window as memory). Extends: the 2023 version adds the memory hierarchy (internet as disk), paging, multithreading, speculative execution, user/kernel space, and the tool and modality list; 2025 adds the utility and fab analogies and the 1960s time-sharing framing. Nothing contradicts. Consequence for merge: the topic's `first_seen` moves from 2025-06-19 to 2023-11-23, and its definition sentence should say he introduced the analogy in this 2023 talk. **Note:** in 2023 the LLM is the "kernel process"; in 2025 it is "like the CPU" — the component named differs; record both, not as a change of view.

### claim: llms-are-the-kernel-of-an-emerging-operating-system
- existing: no
- title: "An LLM is better thought of as the kernel process of an emerging operating system than as a chatbot"
- confidence: stated
- quote: "I don't think it's accurate to think of large language models as a chatbot" (@42:06)
- secondary quote: "this context window is your finite precious resource of your working memory" (@43:45)
- relation: no existing claim page on the LLM OS; topic-level supports/extends as above. If merge also creates a claim from the 2025 talk, set `extends` between them and add a timeline `llms-as-operating-systems-over-time`.

### topic: llm-security
- existing: no
- aliases: LLM security, jailbreak, jailbreaks, prompt injection, data poisoning, backdoor attack, sleeper agent attack, adversarial suffix
- statements:
  - Just as the original OS stack had security challenges, the LLM computing paradigm has its own (@45:25, @45:59).
  - Jailbreaks: role-play (the "deceased grandmother" napalm prompt) gets ChatGPT past its refusal (@45:59, @46:33, @47:06).
  - Base64-encoded queries jailbreak Claude because refusal training data is mostly English, so it learns to refuse harmful queries mostly in English; multilingual data helps, but there are many encodings to cover (@47:38, @48:10, @48:44, @49:17).
  - A universal transferable suffix found by optimisation jailbreaks models; adding it to training does not help because the optimisation can be rerun to find another (@49:17, @49:50, @50:22).
  - An image of a panda with optimised noise jailbreaks a vision model; the new capability of seeing images also adds an attack surface (@50:22, @50:55).
  - Prompt injection hijacks the model with what looks like new instructions: faint text in an image, a web page Bing retrieves that inserts a fraud link, a shared Google Doc that makes Bard exfiltrate personal data via image URLs or, after Google's content security policy blocked that, via Apps Script into an attacker-owned Google Doc (@51:27, @51:59, @52:32, @53:05, @53:37, @54:10, @54:45, @55:20, @55:54).
  - Data poisoning or backdoor ("sleeper agent") attacks: a trigger phrase in training data, e.g. "James Bond", corrupts the model's outputs; the paper showed it for finetuning, and he is not aware of a convincing pretraining demonstration, but it is possible in principle (@56:28, @57:00, @57:32, @58:06).
  - Many of these attacks have published defenses and may no longer work; it is a cat-and-mouse game like traditional security, and a new, rapidly evolving field (@58:40, @59:11).
- relation: supports [[jagged-intelligence]]'s 2025 statement that LLMs are gullible and open to prompt injection (2025-06-19 @17:44); this source explains the mechanism two years earlier.

### claim: llm-security-is-a-cat-and-mouse-game
- existing: no
- title: "LLM security is a new cat-and-mouse game of attacks and defenses, as in traditional security"
- confidence: stated
- quote: "we're going to have new security challenges that are specific to large language models" (@45:59)
- secondary quotes: "it learns to refuse harmful queries in English mostly" (@48:44); "prompt injection is about hijacking the large language model" (@51:59)
- relation: none to an existing claim.

### Not candidates (checked)
- tokenization: not discussed. He says "words" throughout, including for the context window (@43:45); no tokens, no tokenizer. Do not cite this source on [[tokenization]].
- agents / autonomy: see Notes.

## Quotes
- "a large language model is just two files" (@00:00)
- "like a zip file of the internet" (@05:30)
- "What's Happening Here is a lossy compression" (@05:30)
- "this network then dreams internet documents" (@08:50)
- "they're not like a car where we sort of understand all the parts" (@13:15)
- "in this second stage uh we prefer quality over quantity" (@16:04)
- "it is much easier to compare candidate answers than to write an answer yourself" (@21:03)
- "the closed models work a lot better" (@24:55)
- "algorithmic progress is not necessary it's a very nice bonus" (@26:02)
- "it's not just about sort of working in your head and sampling words" (@32:07)
- "large language models currently only have a system one" (@36:31)
- "intuitively what we want to do is we want to convert time into accuracy" (@37:06)
- "there's a lack of a reward Criterion in the general case" (@39:52)
- "in narrow domains it will be possible to self-improve language models" (@40:27)
- "I don't think it's accurate to think of large language models as a chatbot" (@42:06)
- "this context window is your finite precious resource of your working memory" (@43:45)
- "we're going to have new security challenges that are specific to large language models" (@45:59)
- "it learns to refuse harmful queries in English mostly" (@48:44)
- "prompt injection is about hijacking the large language model" (@51:59)

All grep-verified as single matches in the raw file.

## Notes for merge
- **Agents and [[this-is-the-decade-of-agents]]:** relation is none. The talk never uses "agent" for LLM agents (the one hit is the garbled "Lux leaper agent attack" = sleeper agent, @56:28) and says nothing about autonomy timelines. What bears on it indirectly: (1) the LLM OS kernel "coordinating" tools and experts for problem solving (@42:38, @43:11), a capability picture rather than a timeline; (2) in labeling, human-machine collaboration is "a slider" moving right as models improve, with people in an oversight role (@23:15) — an early form of the slider idea on [[partial-autonomy-apps]], but about creating training labels, not about agent products. Mention at most as a **Note:** on partial-autonomy-apps; do not set supports/extends on the decade-of-agents claim.
- **LLM OS (supports/extends 2025):** this is the earliest source for [[llms-as-operating-systems]]; update `first_seen` to 2023-11-23. "Kernel process" (2023) vs "like the CPU" (2025): different component named, not a change of view.
- **RLHF term:** first named here (@22:09); the [[pretraining-and-finetuning]] page's Related note says the lecture does not use the term — still true of the lecture, but should be expanded, not corrected.
- **Caption garbles:** "Llama 270b" = Llama 2 70B; "C set on a" = "cat sat on a"; "Matt" = mat; "Ruth Handler" correct; "black nose days" = blacknose dace (fish); "reversal course" = reversal curse; "merily feifer"/"merely Fifer" = Mary Lee Pfeiffer; "gptc" = GPT series; "mistol" = Mistral; "di" = DALL-E; "Chachi/chpt/chbt/CHT" = ChatGPT; "Claud/Cloud/claw" = Claude; "B series"/"Bart" = Bard; "Lux leaper agent" = sleeper agent; "penda" = panda; "abling instructions" = labeling instructions; "fine truning/fine chaining/fing" = finetuning; "rhf" = RLHF; "Valu ation" = evaluation; "Gestalt" correct. Avoid quoting garbled spans.
- **Numbers to keep as stated:** 140 GB, 2 bytes/float16, ~500 lines of C, ~10 TB, ~6,000 GPUs, ~12 days, ~$2M, ~100x compression, 100,000 Q&A examples, AlphaGo 40 days. The Scale AI valuation numbers ($150B today, $2T by end of 2025) are ChatGPT's tongue-in-cheek extrapolation in his demo, not his estimate — do not record as his view.
- **Other people's work he reports:** reversal curse (a viral example), InstructGPT labeling instructions, Chatbot Arena (Berkeley team), universal transferable suffix paper, panda adversarial-noise paper, James Bond poisoning paper, Bard/Apps Script exfiltration — report as findings he describes, not his own results. He says he does not know what Google Apps Script is exactly (@55:20).
- **Hedges:** System 2, self-improvement and customization are framed as what "the field broadly is interested in", explicitly not OpenAI product announcements (@34:52) — he was at OpenAI then (he says "we" for OpenAI labeling at @22:09). Keep claim titles dated ("In November 2023 ...") where they describe the state of models.
- **next-word-prediction-forces-learning-about-the-world:** no clean verbatim quote under 15 words (the @07:43 sentence is garbled, "next word predition"). Merge may fold this into [[lossy-compression-of-the-internet]] or use the clean fragment "you're learning a ton about the world" (@08:50), grep-verified.
- **Coarseness:** merge may reasonably fold an-llm-is-just-two-files and pretraining-is-lossy-compression-of-the-internet into the one topic; and multimodality/customization into llm-tool-use or llms-as-operating-systems.
- He was re-recording a talk originally given at a Scale AI event, hence the Scale AI examples (@03:18).
