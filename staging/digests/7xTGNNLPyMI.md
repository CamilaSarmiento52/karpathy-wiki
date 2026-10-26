# Digest: Deep Dive into LLMs like ChatGPT
- raw: raw/youtube/7xTGNNLPyMI.md · published: 2025-02-05 · medium: youtube · words: 41520
- source slug: youtube-2025-02-05-deep-dive-into-llms

## Source page

```
---
type: source
raw_path: raw/youtube/7xTGNNLPyMI.md
published: 2025-02-05
medium: youtube
summary: "A 3.5-hour general-audience walk through the whole ChatGPT pipeline: FineWeb data, tokenization, pretraining a base model, SFT on labeler conversations, LLM psychology (hallucination, self-knowledge, tokens to think, Swiss-cheese capabilities), RL and thinking models such as DeepSeek-R1, and why RLHF is not real RL."
url: https://www.youtube.com/watch?v=7xTGNNLPyMI
title: "Deep Dive into LLMs like ChatGPT"
---
# Deep Dive into LLMs like ChatGPT
Raw: [[raw/youtube/7xTGNNLPyMI]] · Original: https://www.youtube.com/watch?v=7xTGNNLPyMI

## Summary
A comprehensive general-audience lecture on what sits behind the ChatGPT text box, aimed at giving mental models for a tool that is good at some things, bad at others and has sharp edges (@00:00, @00:34). Pretraining starts from filtered web text such as FineWeb (about 44 TB, 15 trillion tokens), tokenized with byte-pair encoding, and trains a Transformer to predict the next token; the result is a base model, an internet-document simulator and lossy compression of the internet (@02:14, @10:38, @14:40, @43:04, @49:59). Post-training swaps the data for conversations written by human labelers under labeling instructions, so the assistant is a statistical simulation of a labeler; he then covers the "LLM psychology" this produces: hallucination and its two mitigations, missing self-knowledge, needing tokens to think, and tokenization-driven failures at counting and spelling (@1:02:42, @1:18:17, @1:20:31, @1:26:02, @1:32:43, @1:41:37, @1:57:46, @2:01:07). The third stage is reinforcement learning on practice problems with known answers, where models like DeepSeek-R1 and OpenAI's o-series discover chains of thought themselves; he compares this to AlphaGo and Move 37, and says RLHF, whose learned reward model gets gamed, is not RL in that sense (@2:13:19, @2:28:46, @2:32:04, @2:42:07, @2:45:26, @3:04:50). He closes with the Swiss cheese model of capabilities, advice to use LLMs as tools and check their work, and expected developments: multimodality, supervised agents, computer use and test-time learning (@3:08:39, @3:09:14, @3:09:48, @3:11:26, @3:13:05).

## Key points
- FineWeb-style filtering of Common Crawl into ~44 TB / 15T tokens; pretraining predicts the next token in windows of tokens → [[pretraining-and-finetuning]]
- Bits to bytes to BPE; GPT-4 uses 100,277 tokens; models see tokens, not characters → [[tokenization]], [[a-lot-of-llm-oddness-traces-back-to-tokenization]], [[tokenization-free-modeling-would-be-amazing-but-is-unproven]]
- Inference flips a biased coin per token; outputs are stochastic remixes of the training data → [[sampling-from-language-models]]
- The Transformer is a fixed, stateless mathematical expression; its neurons are far simpler than biological ones → [[transformer-architecture]]
- GPT-2 was the first recognizably modern stack; his llm.c reproduction cost about $600 against an estimated $40,000 in 2019 → [[gpt-2-is-the-first-recognizably-modern-llm-stack]], [[llm-c]], [[compute-efficiency]]
- GPU demand and the Nvidia gold rush come from bigger networks on more tokens → [[scaling-laws]]
- A base model is an internet text token simulator; a release is code plus parameters → [[pretraining-gives-a-document-completer]], [[an-llm-is-just-two-files]]
- The parameters are a lossy compression of the internet; knowledge is a vague recollection, context is working memory → [[pretraining-is-lossy-compression-of-the-internet]], [[parameters-are-vague-recollection-context-is-working-memory]]
- Few-shot prompts and a fake conversation page can make a base model useful → [[prompting-llms]]
- An assistant's answer is a simulation of a human data labeler following labeling instructions → [[chatgpt-answers-simulate-a-human-data-labeler]], [[pretraining-and-finetuning]]
- Hallucination comes from imitating confident answers; mitigations are "I don't know" training data and web search → [[llm-hallucinations]], [[hallucinations-come-from-imitating-confident-answers]], [[llm-tool-use]]
- Models need tokens to think; use code for arithmetic, counting and spelling → [[transformers-need-tokens-to-think]], [[llm-tool-use]]
- Swiss cheese capabilities: Olympiad problems solved, 9.11 vs 9.9 failed → [[jagged-intelligence]], [[llm-capabilities-are-swiss-cheese]]
- RL on practice problems lets models discover their own chains of thought; DeepSeek-R1, o1/o3 are thinking models → [[rlvr]], [[rl-lets-models-discover-their-own-thinking-strategies]], [[system-1-and-system-2-thinking]]
- AlphaGo and Move 37 show RL is not capped by human performance; LLMs show only hints so far → [[llm-self-improvement]]
- RLHF trains against a gameable reward model, so it is "not real RL"; it still helps, perhaps via the discriminator-generator gap → [[rlhf-is-not-real-rl]], [[rlhf-works-better-because-comparing-is-easier-than-generating]]
- Use LLMs as tools, check their work, own the result; agents will need supervision → [[use-llms-as-tools-and-check-their-work]], [[use-llms-as-copilots-with-human-oversight]]
- Longer context windows alone will not scale to long multimodal tasks; test-time learning needs new ideas → [[longer-context-windows-alone-will-not-scale-to-long-multimodal-tasks]]
- LM Arena has become a bit gamed; DeepSeek's MIT-licensed open weights near the top → [[llm-evaluation]], [[ai-ecosystem]]

## Fed pages
- [[pretraining-and-finetuning]]
- [[tokenization]]
- [[sampling-from-language-models]]
- [[transformer-architecture]]
- [[compute-efficiency]]
- [[scaling-laws]]
- [[prompting-llms]]
- [[llm-tool-use]]
- [[llm-hallucinations]]
- [[jagged-intelligence]]
- [[rlvr]]
- [[llm-self-improvement]]
- [[system-1-and-system-2-thinking]]
- [[llm-evaluation]]
- [[ai-ecosystem]]
- [[llm-c]]
- [[pretraining-gives-a-document-completer]]
- [[pretraining-is-lossy-compression-of-the-internet]]
- [[an-llm-is-just-two-files]]
- [[gpt-2-is-the-first-recognizably-modern-llm-stack]]
- [[transformers-need-tokens-to-think]]
- [[a-lot-of-llm-oddness-traces-back-to-tokenization]]
- [[tokenization-free-modeling-would-be-amazing-but-is-unproven]]
- [[rlhf-works-better-because-comparing-is-easier-than-generating]]
- [[llms-want-to-imitate-not-succeed]]
- [[use-llms-as-copilots-with-human-oversight]]
- [[self-improvement-may-be-possible-in-narrow-domains]]
- [[llms-currently-only-have-a-system-1]]
- [[chatgpt-answers-simulate-a-human-data-labeler]]
- [[hallucinations-come-from-imitating-confident-answers]]
- [[parameters-are-vague-recollection-context-is-working-memory]]
- [[rl-lets-models-discover-their-own-thinking-strategies]]
- [[rlhf-is-not-real-rl]]
- [[llm-capabilities-are-swiss-cheese]]
- [[use-llms-as-tools-and-check-their-work]]
- [[longer-context-windows-alone-will-not-scale-to-long-multimodal-tasks]]
- [[llm-self-improvement-over-time]]
```

## Candidates

### topic: pretraining-and-finetuning
- existing: yes (aliases include FineWeb, Common Crawl, SFT, RLHF, base model, labeling instructions)
- aliases to add: post-training, conversation protocol, special tokens im_start, SFT mixtures, UltraChat, InstructGPT, OpenAssistant, three stages of training
- statements:
  - Hugging Face's FineWeb is his example of the processed internet data that every major provider has some internal equivalent of; it ends up about 44 TB (@01:09, @02:14).
  - Most of the data comes from Common Crawl, which he says had indexed 2.7 billion web pages as of 2024 (@02:48).
  - The pipeline he walks through is URL block-listing, text extraction from HTML, language filtering (FineWeb keeps pages over 65% English), deduplication and PII removal (@03:21, @03:54, @04:28, @05:35).
  - Language filtering is a design decision: filter out Spanish and the model will be weak at Spanish (@05:02).
  - FineWeb is about 15 trillion tokens (@14:40).
  - Training samples windows of tokens (up to some maximum such as 8,000) and nudges the network so the actual next token gets higher probability, for all tokens in parallel in large batches (@15:44, @18:32, @19:38).
  - A base model is a token simulator of internet text and is not by itself an assistant; few companies release base models (@43:04, @43:38).
  - Llama 3 is a 405B-parameter model trained on 15 trillion tokens, and Meta released both base and instruct versions (@45:54, @46:30).
  - Post-training is computationally much cheaper than pretraining: pretraining can take about three months on thousands of computers, post-training something like three hours (@1:00:31, @1:03:51).
  - Post-training keeps the same algorithm and swaps the internet documents for a dataset of conversations, which programs the assistant implicitly, by example (@1:02:08, @1:03:16, @1:04:26).
  - Conversations are encoded into one-dimensional token sequences with new special tokens such as GPT-4o's im_start, trained only in post-training; formats differ by provider, "a little bit of a wild west" (@1:06:03, @1:06:39, @1:07:10).
  - At inference, the server appends the assistant's start tokens and samples the reply (@1:08:51, @1:09:24).
  - InstructGPT (OpenAI, 2022) used contractors from Upwork or Scale AI who wrote prompts and ideal responses following labeling instructions (helpful, truthful, harmless), usually hundreds of pages long (@1:10:29, @1:11:35, @1:12:08).
  - Modern SFT datasets such as UltraChat are largely synthetic, with LLMs drafting and humans editing, and run to millions of conversations (@1:14:58, @1:15:29, @1:16:02).
  - He maps the three stages onto a textbook: exposition is pretraining, worked solutions are SFT, practice problems with answers in the key are RL (@2:11:38, @2:12:13, @2:13:19, @2:26:32).
  - At companies like OpenAI each stage is a separate team handing the model on (@2:10:31).
  - Pretraining and SFT are standard everywhere; RL is early and not standard (@2:27:37).
  - Closing recap: pretraining is knowledge acquisition, and personality comes in SFT (@3:23:06, @3:23:39).
- relation: none needed (topic)

### topic: tokenization
- existing: yes
- statements:
  - Neural networks want a one-dimensional sequence over a finite set of symbols, and sequence length is a precious resource to trade against vocabulary size (@07:48, @08:56, @09:32).
  - He goes from UTF-8 bits to bytes (256 symbols, best thought of as unique IDs or emojis) to byte-pair encoding, which mints a new symbol for a common pair and repeats (@10:06, @10:38, @11:13).
  - About 100,000 symbols is a good vocabulary size in practice; GPT-4 uses 100,277 (@11:48).
  - He uses the tiktokenizer website to show cl100k_base tokenizations, and that they are case- and whitespace-sensitive (@12:19, @12:54, @13:28).
  - Models don't see characters, so character-level tasks such as printing every third letter of "ubiquitous" often fail (@2:01:07, @2:01:39, @2:02:12).
  - Tokens exist mostly for efficiency; many people want character- or byte-level models, but those sequences would be very long and people do not know how to handle that yet (@2:02:44).
  - Strawberry's r count combines not seeing characters with not being good at counting; he guesses OpenAI may have hardcoded the answer (@2:03:51, @2:04:25).
  - Audio (spectrogram slices) and images (patches) can be tokenized and interleaved with text in one model, so multimodality is not a fundamental change (@3:10:20, @3:10:53).

### topic: sampling-from-language-models
- existing: yes
- statements:
  - Generation feeds a prefix in, samples one token from the predicted distribution like flipping a biased coin, appends it and repeats (@26:18, @26:54, @27:27).
  - Because of sampling, outputs are stochastic remixes inspired by the training data, statistically similar but not identical (@28:00, @28:32, @29:06).
  - The same prompt to a base model gives a different continuation each time (@48:49).
  - ChatGPT itself is only inference on fixed parameters trained months earlier (@30:11, @30:44).

### topic: transformer-architecture
- existing: yes
- statements:
  - Inputs and parameters are mixed in a mathematical expression of simple operations; architecture research designs expressions that are expressive, optimizable and parallelizable, and they are not complex (@21:52, @22:27).
  - Using a web visualization of a ~85,000-parameter Transformer, he walks through embeddings, attention, MLP, layer norms and the output softmax (@22:59, @23:33, @24:06).
  - He warns against thinking of these values as biological neurons: the expression is stateless with no memory, and biological neurons are complex dynamical processes (@24:40, @25:12).
  - A modern network has on the order of 100 layers, so compute per token is finite and roughly fixed (@1:49:28).

### topic: compute-efficiency
- existing: yes
- statements:
  - Training GPT-2 was estimated at about $40,000 in 2019; his llm.c reproduction took about a day and $600, and he thinks about $100 is possible now (@33:01, @33:36).
  - He attributes the fall to better datasets and filtering, and above all to faster hardware and better software for squeezing speed out of it (@33:36, @34:10).
  - He rents an 8×H100 node from Lambda, about $3 per GPU per hour; GPUs suit training because the matrix multiplications are highly parallel (@39:06, @39:42, @40:16).
  - Smaller distilled models at lower precision can run locally, e.g. in LM Studio on a MacBook (@3:19:45, @3:20:20, @3:20:53).

### topic: scaling-laws
- existing: yes (alias: GPU gold rush)
- statements:
  - Big tech's demand for GPUs to train language models is, he says, what drove Nvidia to $3.4 trillion; he calls getting enough GPUs the gold rush (@41:23).
  - More GPUs let you process the data faster, iterate faster and train a bigger network (@41:56).
- note: he does not state a scaling law here; only background. Merge may prefer `context`.

### topic: prompting-llms
- existing: yes (aliases: in-context learning, few-shot prompting)
- statements:
  - A base model can be prompted to elicit knowledge, e.g. by starting a top-10 list of Paris landmarks (@50:34).
  - Few-shot prompts such as English–Korean word pairs use in-context learning, so apps can be built on a base model alone (@56:04, @56:37, @57:11).
  - An assistant can be instantiated from a base model by a prompt shaped like a web page of human–assistant turns; it then also hallucinates the next human turn (@57:11, @57:43, @58:17, @58:52).
  - Recall works better if you paste the material into the prompt, e.g. the text of Pride and Prejudice chapter one, rather than relying on memory (@1:40:32, @1:41:04).
  - Saying "don't use any tools" is enough to make ChatGPT answer from memory (@1:38:15).
  - For hard math or code he reaches for thinking models; about 80–90% of his own use is GPT-4o, since thinking 30 seconds about a factual question is overkill (@2:40:27).

### topic: llm-tool-use
- existing: yes
- statements:
  - Web search works by the model emitting special tokens around a query; the sampling program pauses, runs the search and pastes the results into the context window (@1:33:53, @1:34:26, @1:34:58).
  - The model learns when and how to search from a few thousand example conversations, and it already understands what a good query is from pretraining (@1:36:04, @1:36:36).
  - He calls search an additional mitigation for hallucination and factuality (@1:39:25).
  - He would not trust a model's mental arithmetic and asks it to "use code", trusting a Python interpreter's result much more (@1:55:32, @1:56:08, @1:56:42, @1:57:14).
  - Counting dots works with code because copying tokens into a Python string is easy for the model; the interpreter does the counting (@1:59:57, @2:00:33).
  - He expects models to become natively multimodal, agents that run for minutes or hours under supervision, and computer use such as OpenAI's Operator (@3:09:48, @3:11:26, @3:12:00, @3:12:33).

### topic: llm-hallucinations
- existing: no (near-duplicates checked: jagged-intelligence lists hallucination as one deficit; no page explains it)
- aliases: hallucination, hallucinations, factuality, making stuff up, knowledge of self, self-knowledge, model identity, "who built you", LLM psychology
- statements:
  - He opens a section on "LLM psychology", the emergent cognitive effects of the training pipeline, with hallucination, when LLMs fabricate information (@1:20:31).
  - Training conversations answer "who is X" confidently, so at test time the model imitates that style and gives its most likely guess rather than saying it doesn't know (@1:21:36, @1:22:09, @1:22:42).
  - An old model, Falcon 7B, gives a different fabricated biography each resample for a made-up name; a current ChatGPT says it does not know (@1:23:15, @1:23:48, @1:25:29).
  - Mitigation one, which he describes from Meta's Llama 3 paper: generate questions from training documents with an LLM, interrogate the model several times, use an LLM judge to compare, and where it gets them wrong add training conversations whose correct answer is "I don't know" (@1:26:02, @1:27:39, @1:28:14, @1:29:20, @1:30:30, @1:31:03).
  - He presumes some neuron represents uncertainty, and those examples let the model wire it to saying it doesn't know; he calls this a large mitigation (@1:27:06, @1:31:37).
  - Mitigation two is tools: web search refreshes the model's working memory (@1:32:43, @1:33:17).
  - Hallucinations have gotten better over time and will keep improving, but models still hallucinate (@3:08:39).
  - **Self-knowledge section:** asking a model what it is and who built it is "a little bit nonsensical", since it has no persistent existence and restarts every conversation (@1:41:37, @1:42:11).
  - Falcon claiming to be built by OpenAI is not evidence it trained on OpenAI data; more likely it is a hallucinated label from internet text about ChatGPT (@1:42:44, @1:43:55).
  - Developers override identity with hardcoded conversations (OLMo's SFT mixture has 240 of them) or with a hidden system message; he calls both "cooked up and bolted on" (@1:44:27, @1:44:59, @1:45:33, @1:46:07, @1:46:42).

### topic: jagged-intelligence
- existing: yes (aliases: jagged intelligence, people spirits) — add aliases: Swiss cheese model, sharp edges, 9.11 vs 9.9
- statements:
  - Besides counting and spelling, there are "Jagged edges" that make little sense even if you understand the models in depth (@2:04:57).
  - Models answer PhD-grade science questions better than he can but sometimes say 9.11 is bigger than 9.9; he reports, from a team he talked to (he has not read the paper), that Bible-verse-related neurons light up (@2:05:30, @2:06:03, @2:06:37).
  - He calls this the Swiss cheese model: very good across many disciplines but failing almost at random in unique cases (@3:08:39, @3:09:14).
  - LM Arena has become "a little bit gamed" in the last few months and he trusts it less; use it as a first pass (@3:16:57). (Merge may put this on llm-evaluation instead.)
  - The model doesn't learn at test time; humans update their parameters, e.g. during sleep (@3:13:05, @3:13:39).

### topic: rlvr
- existing: yes (aliases: RLVR) — add aliases: reinforcement learning stage, RL for LLMs, thinking models, reasoning models, DeepSeek-R1, o1, o3, chains of thought, verifiable domains, LLM judge, practice problems
- statements:
  - RL is the last of three major stages, still under post-training; he calls it practice problems with a final answer but no worked solution (@2:09:57, @2:13:19, @2:13:53).
  - The procedure: sample many solutions per prompt (up to thousands or a million), find those that reach the correct answer and train on them, across tens of thousands of prompts (@2:20:28, @2:21:34, @2:23:13, @2:24:20).
  - He calls it "a guess and check", with SFT still useful as an initialization near correct solutions (@2:25:25, @2:25:58).
  - In verifiable domains a candidate is scored against a concrete answer, by checking a boxed answer or with an LLM judge, with no humans in the loop (@2:48:14, @2:48:47).
  - The high-level idea is simple but the details are hard; companies experimented internally without talking publicly, which is why the DeepSeek-R1 paper was such a big deal (@2:28:11, @2:28:46, @2:29:18).
  - In the R1 paper accuracy climbs with steps and the average response length grows (@2:29:50, @2:30:24).
  - o1, o3-mini and similar ChatGPT models were trained with RL similar to R1, per public statements of OpenAI employees; GPT-4o and the free tier are mostly SFT models (@2:37:07, @2:37:40).
  - OpenAI shows summaries rather than raw chains of thought, he thinks partly over distillation risk (@2:38:14, @2:38:46).
  - He judges OpenAI's top paid models and DeepSeek-R1 roughly on par, with evaluation hard to read (@2:38:46, @2:39:19).
  - Google offered an experimental thinking model, Anthropic did not yet; thinking models are experimental "as of 2025 very early 2025" (@2:41:02, @2:41:35).
  - Frontier research, he says, is building large, diverse prompt distributions, game environments for every domain of knowledge (@2:47:40).
  - Whether thinking learned in verifiable domains transfers to unverifiable ones is unknown in the field (@3:28:45, @3:29:18).
  - These models will mostly shine in verifiable domains like math and code (@3:29:50).
- relation: **Note:** this source predates the 2025-12-19 blog on the page; the merge must not write "first" — date both.

### topic: llm-self-improvement
- existing: yes
- statements:
  - In AlphaGo, supervised learning on expert games tops out below the best humans, while RL plays moves that lead to wins and beats Lee Sedol (@2:42:41, @2:43:14, @2:43:46, @2:44:20).
  - He says we are only starting to see hints of that diagram in LLMs for reasoning, and need to go beyond imitating experts (@2:44:20, @2:44:52).
  - Move 37, a move a human would play about 1 in 10,000 times, is his example of RL discovering a strategy unknown to humans (@2:45:26, @2:46:00, @2:46:33).
  - What the LLM equivalent looks like is unknown: perhaps new analogies, new thinking strategies or its own language rather than English (@2:46:33, @2:47:05).
  - He calls RL in LLMs "primordial" and nascent, in principle capable of a Move 37 in open-domain thinking (@3:29:18, @3:29:50).
  - Note: he never uses the words "self-improvement" in this lecture.

### topic: system-1-and-system-2-thinking
- existing: yes (aliases: thinking longer, reasoning, converting time into accuracy)
- statements:
  - Thinking models produce longer responses: the extra tokens are what raise accuracy (@2:30:24, @2:32:04, @2:34:51).
  - He calls what emerges "chains of thought" and cognitive strategies, like what goes on in your head rather than what you write down (@2:31:30, @2:32:04).
  - The R1 output shows the thinking and then a nicely written solution for the human; he separates correctness from presentation (@2:34:19, @2:34:51).
- note: he does not use the System 1 / System 2 words here (grep finds none).

### topic: llm-evaluation
- existing: yes
- statements:
  - LM Arena ranks models by blind human comparisons; it was good for a long time but he thinks it has become a little gamed, citing Claude Sonnet's low rank against how widely it is used (@3:15:18, @3:16:57).
  - Follow the AI News newsletter (swyx and friends) and people you trust on X (@3:17:32, @3:18:04).

### topic: ai-ecosystem
- existing: yes
- statements:
  - DeepSeek-R1 is open weights under an MIT license, ranking third on LM Arena; he calls a model that strong with open weights unprecedented (@3:15:51, @3:16:24).
  - Use the provider's site for proprietary models, inference providers such as together.ai for open weights, and hyperbolic for a base model; he wishes more people hosted base models (@3:18:37, @3:19:10, @3:19:45).
  - Some people are wary of putting sensitive data into DeepSeek's own site because it is a Chinese company; the open weights can be used through US hosts (@2:35:24, @2:36:33).

### artifact: llm-c
- existing: yes
- statements:
  - He reproduced GPT-2 "for fun" in llm.c; the writeup is on the repo's GitHub, about one day and $600 (@33:01, @33:36).
  - He shows a GPT-2 run live: one line per update of 1 million tokens, about 7 seconds each, 32,000 steps (~33B tokens), sampling every 20 steps (@35:15, @36:20, @36:54).
  - The loss is the number a researcher watches (@35:49, @36:20).

### claim: chatgpt-answers-simulate-a-human-data-labeler
- existing: no
- title: "An assistant's answer is, roughly, a statistical simulation of a human data labeler following the company's labeling instructions"
- confidence: stated
- quote: "you're not talking to a magical AI you're talking to an average labeler" (@1:18:17)
- statements:
  - The answer is statistically aligned with a training set seeded by humans following labeling instructions (@1:16:35, @1:17:10).
  - The labelers are often educated experts, so it is like asking an instantaneous simulation of a fairly skilled person (@1:17:43, @1:18:17).
  - If the query is in the post-training data the answer will resemble what the labeler wrote; otherwise it is more emergent, combining pretraining knowledge with the post-training style (@1:18:52, @1:19:25, @1:19:59).
  - Closing recap: it is "the neural network simulation of a data labeler at openai", a lossy simulation limited to fixed compute per token (@3:24:12, @3:24:47, @3:25:20).
  - Thinking models change this: their output is not just imitation of a labeler but comes from RL (@3:27:03, @3:28:11).
- relation: **supports** [[llms-want-to-imitate-not-succeed]] weakly — both say the model imitates its training data (2023-05-25 State of GPT, @30:02 per that page) — but the 2025 lecture does not repeat the advice to ask for strong performance. If the merge judges this too loose, make it a Note.

### claim: hallucinations-come-from-imitating-confident-answers
- existing: no
- title: "Models hallucinate because they imitate the confident style of training answers, even when some part of the network may know it doesn't know"
- confidence: stated
- quote: "these are statistical token tumblers as I call them" (@1:22:42)
- statements: as in llm-hallucinations, @1:21:36 to @1:22:42 (cause), @1:26:33 to @1:27:06 (the presumed uncertainty neuron not wired to words), @1:31:37 (training "I don't know" examples is a large mitigation).
- hedges: "might know", "we presume exists", "probably the case".
- relation: none to an existing claim page. **Note:** [[jagged-intelligence]] lists hallucination as a deficit (2025-06-19 YC talk @16:04); this explains its cause, a connection rather than a link.

### claim: parameters-are-vague-recollection-context-is-working-memory
- existing: no
- title: "Knowledge in the parameters is a vague recollection; the context window is working memory"
- confidence: stated
- quote: "knowledge in the parameters of the neural network is a vague recollection" (@1:39:25)
- second quote: "the tokens that make up the context window is the working memory" (@1:39:25)
- statements:
  - Frequent things are more likely to be remembered correctly; the base model's knowledge is "vague and probabilistic and statistical" (@51:07, @51:40).
  - Highly weighted sources like Wikipedia may be seen ~10 times and recited verbatim (regurgitation), usually undesirable (@52:13, @53:18, @53:50).
  - Knowledge in the weights is like something read a month ago; looking things up refreshes working memory (@1:32:43, @1:33:17).
  - Context-window data is directly accessible, not a recollection (@1:34:58, @1:35:31).
  - Practical consequence: paste material into the prompt (@1:40:32, @1:41:04).
- relation: **supports** [[pretraining-is-lossy-compression-of-the-internet]] — he restates that the parameters are a lossy compression, "kind of like a zip file" (2025-02-05 @49:59; 2023-11-23 per that page). **supports** [[llms-are-the-kernel-of-an-emerging-operating-system]] — the 2023-11-23 talk calls the context window RAM; here it is working memory (@1:34:58). The merge should check the 2023 wording on that page before linking.

### claim: rl-lets-models-discover-their-own-thinking-strategies
- existing: no
- title: "Through RL on problems with known answers, models discover their own ways of thinking that humans could not write down for them"
- confidence: stated
- quote: "the model is discovering ways to think" (@2:32:04)
- statements:
  - Humans are not in a good position to write the best token sequences, because what is easy or hard for a labeler differs from what is easy or hard for the LLM; some steps are leaps for it, others wasted tokens (@2:17:44, @2:18:16, @2:18:49, @2:19:21).
  - So imitation is useful to initialize, but the LLM needs to discover what reliably works for it through trial and error (@2:19:55).
  - In DeepSeek-R1 the model learns to re-evaluate, backtrack and try other perspectives ("aha moment"); no human could hardcode this into an ideal response (@2:30:56, @2:31:30).
  - He calls it emergent from the optimization, given only correct answers (@2:32:04, @2:32:37).
  - It is still early, and transfer to unverifiable domains is unknown (@3:28:45, @3:29:18).
- relations:
  - **extends** [[self-improvement-may-be-possible-in-narrow-domains]] (2023-11-23): there he said self-improvement may be possible in narrow domains with a reward function (@40:27 per that page); in the 2025-02-05 lecture he describes RL on verifiable math and code problems producing reasoning, while saying LLMs show only "hints" of AlphaGo's curve (@2:44:20). Not a contradiction: he still frames it as early, and the 2025 source never uses "self-improvement".
  - **extends** [[llms-currently-only-have-a-system-1]] (2023-11-23, explicitly "currently"): in 2025 he describes thinking models that use more tokens for higher accuracy (@2:30:24, @2:40:27). The 2023 claim was dated, so both can hold.
  - **supports** the Sequoia 2024-03-26 statements on [[llm-self-improvement]] (human and model psychology differ; the model must practise for itself; textbooks have exercises). These are on a topic page, not a claim page, so it is a Note there. Compare 2025 @2:18:16, @2:19:55 and @2:11:38 with Sequoia @25:32, @26:04 and @28:19 as cited on that page.
  - Needs a timeline per CLAUDE.md §7.7: see `llm-self-improvement-over-time` below.

### claim: rlhf-is-not-real-rl
- existing: no
- title: "RLHF is not RL in the magical sense, because its learned reward model can be gamed"
- confidence: stated
- quote: "I kind of see rhf as not real RL because the reward function is gameable" (@3:05:54)
- statements:
  - RLHF handles unverifiable domains (jokes, poems, summaries) by training a reward model to match human orderings of rollouts, then running RL against that simulator of human preferences (@2:51:02, @2:52:08, @2:52:41, @2:54:19, @2:57:04).
  - Downside one: the simulation is lossy and may mislead (@3:00:55).
  - Downside two: RL finds adversarial inputs that game the reward model; after a few hundred updates pelican jokes collapse to "the the the", which scores top (@3:01:31, @3:02:05, @3:02:38, @3:03:10).
  - Patching adversarial examples never wins, so you run RLHF a few hundred steps, crop it and ship (@3:03:43, @3:04:15).
  - Verifiable rewards and Go's win/loss are hard to game, so RL can run indefinitely there; RLHF is "a little fine-tune" (@3:05:21, @3:05:54, @3:06:27).
  - GPT-4o has been through RLHF, but he says it basically doesn't do RL (@3:06:27, @3:27:03).
- relations:
  - **compatible with** [[rlhf-works-better-because-comparing-is-easier-than-generating]], not a contradiction: in the same lecture he says RLHF empirically gives slightly better models (@2:58:09, @2:58:41). Set no link, or a Note.
  - The Sequoia interview (2024-03-26), as cited on [[llm-self-improvement]], already says RLHF barely counts as RL because its reward model is a vibe check that is easy to hack (@26:39, @27:13 there). The merge may want this claim to carry both sources with `stated_on: 2024-03-26`; I could only check the Sequoia wording through the wiki page, not its raw file.

### claim: llm-capabilities-are-swiss-cheese
- existing: no
- title: "LLM capabilities are like Swiss cheese: very good across many disciplines, with random holes"
- confidence: stated
- quote: "the Swiss cheese uh sort of model of llm capabilities" (@3:08:39)
- statements: @3:08:39, @3:09:14 (9.11 vs 9.9 alongside Olympiad questions; there are many holes); recap @3:25:55, @3:26:26 (holes include too few tokens to think, mental-arithmetic slips, letter counting).
- relation: none to a claim page. **Note:** this is the same picture as [[jagged-intelligence]] (2025-06-19, 2025-12-19 on that page); here he says "Jagged edges" (@2:04:57) but not "jagged intelligence". The merge could fold this into the topic and drop the claim if it is too close.

### claim: use-llms-as-tools-and-check-their-work
- existing: no
- title: "Use LLMs as tools: for inspiration and first drafts, check their work and own the result"
- confidence: stated
- quote: "use it as a tool in a toolbox don't trust it fully" (@3:30:23)
- statements: @2:07:12 (a stochastic system that is magical but can't be fully trusted; don't let it rip and copy-paste); @3:08:07 (useful tools, don't trust fully); @3:09:14 (not infallible; first draft; you are responsible); @3:30:23, @3:30:56 (he uses them tens or hundreds of times a day; check and verify).
- agents: he expects human-to-agent ratios, with people supervising agent tasks (@3:12:00, @3:12:33).
- relation: **supports** [[use-llms-as-copilots-with-human-oversight]] (2023-05-25, State of GPT @39:57 per that page): both keep a human checking the output. Also Note to [[this-is-the-decade-of-agents]] (2025-06-19): he expects supervised long-running agents (@3:11:26, @3:12:00), but gives no timescale, so no link.

### claim: longer-context-windows-alone-will-not-scale-to-long-multimodal-tasks
- existing: no
- title: "He thinks longer context windows alone will not scale to long-running multimodal tasks, and new ideas such as test-time training are needed"
- confidence: stated (hedged: "I think")
- quote: "the context window is a finite and precious resource" (@3:14:13)
- statements: @3:13:05, @3:13:39 (fixed parameters; in-context learning is the only test-time learning); @3:14:13, @3:14:46 (videos will push windows far past hundreds of thousands of tokens; lengthening them by itself will not scale).
- relation: none. **Note:** the missing consolidation is the "anterograde amnesia" on [[jagged-intelligence]] (2025-06-19 @16:38) — a connection, not a link.

### claim (existing, add source): transformers-need-tokens-to-think
- existing: yes (2023-05-25)
- statements: fixed compute per token, ~100 layers, so distribute reasoning over tokens (@1:49:28, @1:50:01, @1:50:34); an answer stating "$3" first makes the rest post-hoc justification and trains guessing in one token (@1:51:07, @1:51:39); worked intermediate steps are the better label (@1:52:11, @1:52:44); with bigger numbers, a single-token answer fails and a step-by-step one is right (@1:54:23, @1:54:58, @1:55:32); he named the section "models need tokens to think" and adds: use tools rather than letting the model do it in memory (@1:57:46); counting fails for the same reason (@1:58:18).
- quote: "these are not for you these are for the model" (@1:53:50)
- relation: **supports** — the same claim restated on 2025-02-05, with labeling advice and "lean on tools" added. His section title is "models need tokens to think", not "transformers".

### claim (existing, add source): pretraining-gives-a-document-completer
- statements: base model is "a token simulator", an internet text token simulator that dreams internet pages (@43:04, @43:38); asked "what is 2 plus 2" it continues the sequence, "a glorified autocomplete" (@47:39, @48:10); recap "internet document simulator on the token level" (@59:58).
- relation: supports (same position, 2025-02-05).

### claim (existing, add source): pretraining-is-lossy-compression-of-the-internet
- statements: the 405B parameters are a lossy compression of the internet, "kind of like a zip file" (@49:59); recap "kind of a lossy compression of the internet" (@2:07:45).
- relation: supports.

### claim (existing, add source): an-llm-is-just-two-files
- statements: a model release needs two things, the code for the forward pass (a couple hundred lines, standard) and the parameters, where the value is (@44:13, @44:47, @45:20).
- relation: supports. He says "two things", not "two files"; GPT-2 here, Llama 2 70B in 2023.

### claim (existing, add source): gpt-2-is-the-first-recognizably-modern-llm-stack
- quote: "it is the first time that a recognizably modern stack came together" (@31:19)
- statements: everything in GPT-2 is recognizable today, just bigger: 1.6B parameters, 1,024 context, ~100B tokens (@31:52, @32:28, @33:01).
- relation: supports.

### claim (existing, add source): a-lot-of-llm-oddness-traces-back-to-tokenization
- statements: spelling, every-third-letter and strawberry failures come from seeing tokens not characters (@2:01:07, @2:02:12, @2:03:51); the dots in a counting prompt are chunked into a few tokens (@1:58:51, @1:59:25).
- relation: supports.

### claim (existing, add source): tokenization-free-modeling-would-be-amazing-but-is-unproven
- statements: many people want to delete tokens for character- or byte-level models, but the sequences would be very long and people do not know how to handle that yet (@2:02:44).
- relation: supports (he does not say "amazing" here; he reports others' interest and the obstacle).

### claim (existing, add source): rlhf-works-better-because-comparing-is-easier-than-generating
- statements: done correctly, RLHF gives slightly better models, but why is not well established; his best guess is the "discriminator generator Gap": ordering five poems is far easier for a labeler than writing the ideal one (@2:58:09, @2:58:41, @2:59:15, @2:59:49); humans order rather than score because ordering is easier (@2:54:19).
- quote: "the discriminator generator Gap" (@2:58:41)
- relation: supports — same reason, same hedge ("my best guess").

### claim (existing): self-improvement-may-be-possible-in-narrow-domains — see extends under rl-lets-models-discover-their-own-thinking-strategies.
### claim (existing): llms-currently-only-have-a-system-1 — see extends under rl-lets-models-discover-their-own-thinking-strategies.
### claim (existing): llms-want-to-imitate-not-succeed — see supports under chatgpt-answers-simulate-a-human-data-labeler.
### claim (existing): use-llms-as-copilots-with-human-oversight — see supports under use-llms-as-tools-and-check-their-work.

### timeline: llm-self-improvement-over-time
- existing: no (needed for the two `extends` links)
- entries (dates only, no intervals):
  - 2023-11-23 — [[self-improvement-may-be-possible-in-narrow-domains]]; [[llms-currently-only-have-a-system-1]] ([[youtube-2023-11-23-intro-to-llms]])
  - 2024-03-26 — AlphaGo's RL step not yet done for LLMs; RLHF a vibe check ([[talk-2024-03-26-sequoia-making-ai-accessible]], per [[llm-self-improvement]])
  - 2025-02-05 — RL on verifiable problems; DeepSeek-R1 and o1/o3 as thinking models; "hints" of AlphaGo's curve; RLHF not real RL → [[rl-lets-models-discover-their-own-thinking-strategies]], [[rlhf-is-not-real-rl]] ([[youtube-2025-02-05-deep-dive-into-llms]] @2:28:46, @2:44:20, @3:05:54)
  - 2025-12-19 — RLVR as the new 2025 training stage ([[blog-2025-12-19-year-in-review-2025]], per [[rlvr]])

## Quotes
- "it's just a glorified autocomplete" (@48:10)
- "it's an internet text token simulator" (@43:04)
- "you're not talking to a magical AI you're talking to an average labeler" (@1:18:17)
- "these are statistical token tumblers as I call them" (@1:22:42)
- "this model knows that it doesn't know" (@1:25:29)
- "knowledge in the parameters of the neural network is a vague recollection" (@1:39:25)
- "the tokens that make up the context window is the working memory" (@1:39:25)
- "it has no persistent self it has no sense of self" (@1:42:11)
- "these are not for you these are for the model" (@1:53:50)
- "the models they don't see the characters they see tokens" (@2:01:07)
- "it's basically a guess and check" (@2:25:25)
- "the model is discovering ways to think" (@2:32:04)
- "reinforcement learning is not going to be constrained by human performance" (@2:44:20)
- "I kind of see rhf as not real RL because the reward function is gameable" (@3:05:54)
- "it's not RL in the sense that it lacks magic" (@3:06:27)
- "the Swiss cheese uh sort of model of llm capabilities" (@3:08:39)
- "the extent to which that transfer happens is unknown in the field" (@3:28:45)
- "use it as a tool in a toolbox don't trust it fully" (@3:30:23)

All were grep-checked as exact substrings of the raw file.

## Notes for merge
- **Solo lecture on his own channel**, no other speakers. Some positions are other people's and must stay theirs: the Llama 3 factuality procedure (Meta's paper, @1:26:02); the 9.11-vs-9.9 Bible-verse finding, which he got from "this team" and says he has not read the paper on (@2:06:03); R1's results (DeepSeek's paper); o1/o3 being trained with RL "per public statements of opening ey employees" (@2:37:07); InstructGPT's labeler setup (OpenAI's paper).
- **Caption errors:** "Chachi PT / chash apt" = ChatGPT; "45 billion" (@45:54, @49:59) is the 405B Llama 3.1 (he says 405 elsewhere); "8 5,000" = ~85,000 parameters (@22:59); "1,24" = 1,024; "100, 277" / "100, 27777" = 100,277; "tick/Tech tokenizer" = tiktokenizer; "CL 100 a base" = cl100k_base; "imore start / IM imaginary monologue" = im_start (he says he doesn't know why it is named that, @1:06:39); "medications" = mitigations (@1:21:04); "Orson kovats" is his made-up name; "Dominic kek / Hasek" = Dominik Hašek; "rhf / arlef / our LF" = RLHF; "DC car1 / Deep seek R1" = DeepSeek-R1; "01 03 mini" = o1, o3-mini; "leas dull / LEL" = Lee Sedol; "Almo / MMO / Theo" = OLMo; "El Marina" = LM Arena; "swix" = swyx; "together. a" = together.ai; "Nota moment" = "aha moment"; "lm. C" = llm.c.
- **Garbled arithmetic:** "30 - 4 is 9" (@1:52:11) and "30 - 4 IDE 3" (@2:17:11) should be 13 − 4 = 9 and 9 / 3; don't quote them.
- **Open source vs open weights:** he calls DeepSeek-R1 "an open source model or open weights model" (@2:35:24) and later "open weights" under MIT (@3:15:51), and calls OLMo "fully open source" because its paper and data are open (@1:44:27). Loose wording, not a contradiction of [[open-weights-models-are-not-open-source]]; at most a Note.
- **Date-sensitive statements**, which should be written with "as of 2025-02-05": Anthropic offered no thinking model (@2:41:35); Google led LM Arena with DeepSeek third and Sonnet 14th (@3:15:51, @3:16:24); 80–90% of his use was GPT-4o (@2:40:27); Nvidia at $3.4 trillion (@41:23); the 100,000-GPU Musk data center was "about a month ago" (@42:30).
- **No "self-improvement", "System 1/2" or "RLVR" wording** in this lecture (grep-checked). The links to those pages are conceptual; keep paraphrases at his words ("reinforcement learning", "thinking models", "verifiable domains").
- **Ordering:** the [[rlvr]] page now cites only 2025-12-19. Do not write that this lecture "first" explained RL or came "before" the blog; give both dates.
- **No new method page proposed.** His practical habits (paste the source into the prompt, "use code" for arithmetic, counting and spelling, pick a thinking model only for hard math or code, check the work) are on prompting-llms, llm-tool-use and the tools claim. The merge could make them a method, e.g. `work-around-llm-cognitive-deficits`, if it wants one.
- The GPT-2 training shown live (@34:43 onward) is his llm.c run on an 8×H100 node; the figures are his on-screen ones.
- Mentioned but not explained: Elon Musk's 100,000-GPU cluster, Operator, LM Studio's model zoo, distillation and quantization precisions (fp8, bf16).
