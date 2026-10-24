# Digest: State of GPT | BRK216HFS
- raw: raw/talks/bZQun8Y4L2A.md · published: 2023-05-25 · medium: talk · words: ~8,000 (42:40)
- source slug: talk-2023-05-25-state-of-gpt

## Source page

```
---
type: source
raw_path: raw/talks/bZQun8Y4L2A.md
published: 2023-05-25
medium: talk
summary: "Microsoft Build 2023 talk in two halves: the four-stage recipe for training GPT assistants (pretraining, supervised finetuning, reward modeling, RL), then how to use them: prompting around their cognitive differences from people, tools and retrieval, finetuning, and low-stakes, human-overseen use."
url: https://www.youtube.com/watch?v=bZQun8Y4L2A
title: "State of GPT | BRK216HFS"
---
# State of GPT
Raw: [[raw/talks/bZQun8Y4L2A]] · Original: https://www.youtube.com/watch?v=bZQun8Y4L2A

## Summary
He splits the talk into how GPT assistants are trained and how to use them well (@00:35). The training recipe has four serial stages, pretraining, supervised finetuning, reward modeling and reinforcement learning, with pretraining taking about 99 percent of the compute and the other three needing few GPUs for hours or days (@00:35, @01:07, @01:41). Base models complete documents rather than answer questions; SFT swaps in tens of thousands of contractor-written prompt and response pairs, and RLHF adds a reward model trained on rankings and RL that weights the language-modeling loss by reward (@10:36, @11:43, @13:23, @15:35). In the second half he argues that LLMs differ cognitively from people, spending equal compute per token with no inner monologue or self-check, and that prompting largely makes up for that difference: spread reasoning over tokens, sample several times, ask the model to check itself, ask for good performance, give it tools and retrieved context (@22:13, @23:22, @24:27, @25:32, @30:02, @32:15, @32:48). He recommends getting top performance first with GPT-4 and detailed prompts, then optimising cost, treating finetuning (and especially RLHF) as slower and harder (@37:12, @38:17, @38:51). Given current limitations he recommends low-stakes uses, always with human oversight, as copilots rather than autonomous agents (@39:24, @39:57).

## Key points
- Four serial stages, each with its own dataset, objective and resulting model; pretraining is about 99 percent of compute → [[pretraining-and-finetuning]]
- Tokenization is a lossless translation of text to integers, typically by byte pair encoding; vocabularies are a couple of tens of thousands of tokens → [[tokenization]]
- LLaMA 65B beats GPT-3 175B because it trained on far more tokens; parameter count alone is not a guide to power → [[pretraining-and-finetuning]]
- Base models want to complete documents, not answer; few-shot documents can trick them into tasks or even into acting as assistants, unreliably → [[pretraining-gives-a-document-completer]]
- Base, SFT and RLHF models are distinct; ChatGPT is RLHF, Vicuna-13B is SFT → [[base-models-vs-assistant-models]]
- RLHF works better than SFT in human comparisons; his offered reason is that comparing is easier than generating → [[rlhf-works-better-because-comparing-is-easier-than-generating]]
- RLHF models lose entropy, so he still uses base models to generate more things like a list → [[rlhf-models-lose-entropy]]
- Transformers spend the same compute on every token and cannot think much per token, so reasoning must be spread across tokens → [[transformers-need-tokens-to-think]]
- Prompting largely makes up for the cognitive differences between human brains and LLMs: chain of thought, self-consistency, asking it to check, System 2 techniques with Python glue code → [[prompting-llms]]
- LLMs imitate the whole quality range of their data, so ask for a strong solution → [[llms-want-to-imitate-not-succeed]]
- Give LLMs tools and tell them what they are bad at; fill the context window with retrieved documents → [[tool-use-and-retrieval]]
- His default recommendations: GPT-4 with detailed prompts, few-shot examples, tools, chains; finetune only after prompting is squeezed; then cut cost → [[top-performance-then-optimize]]
- Use LLMs in low-stakes applications with human oversight, as copilots rather than autonomous agents; AutoGPT does not work well yet → [[use-llms-as-copilots-with-human-oversight]]
- The copilot stance connects to his later autonomy-slider framing → [[partial-autonomy-apps]]

## Fed pages
- [[pretraining-and-finetuning]]
- [[tokenization]]
- [[pretraining-gives-a-document-completer]]
- [[base-models-vs-assistant-models]]
- [[rlhf-works-better-because-comparing-is-easier-than-generating]]
- [[rlhf-models-lose-entropy]]
- [[transformers-need-tokens-to-think]]
- [[prompting-llms]]
- [[llms-want-to-imitate-not-succeed]]
- [[tool-use-and-retrieval]]
- [[top-performance-then-optimize]]
- [[use-llms-as-copilots-with-human-oversight]]
- [[partial-autonomy-apps]]
- [[jagged-intelligence]]
```

## Candidates

### topic: pretraining-and-finetuning
- existing: yes (aliases include RLHF, ChatGPT training stages)
- aliases to add: four-stage training recipe, supervised finetuning, SFT, reward modeling, RLHF pipeline, reinforcement learning from human feedback
- statements:
  - He calls the recipe emerging, very new and still rapidly evolving, with four major stages that follow each other serially: pretraining, supervised finetuning, reward modeling and reinforcement learning (@00:35, @01:07).
  - Each stage has a dataset, an algorithm (an objective for training the network) and a resulting model (@01:07).
  - Pretraining is about 99 percent of training compute and flops, with internet-scale data, thousands of GPUs and possibly months; the other three stages use few GPUs for hours or days (@01:07, @01:41).
  - The pretraining data is a mixture, his example being LLaMA's: CommonCrawl, C4 and higher-quality sets such as GitHub, Wikipedia, books and others, sampled in given proportions (@01:41, @02:16).
  - Typical orders of magnitude: a vocabulary of a couple of tens of thousands of tokens, context length of 2,000 to 4,000 or even 100,000, LLaMA at 65 billion parameters (@03:21, @03:56).
  - LLaMA 65B is significantly more powerful than GPT-3 175B because it trained on 1.4 trillion tokens instead of 300 billion; he says not to judge a model's power by its parameter count (@03:56).
  - Meta trained the 65B model on about 2,000 GPUs for about 21 days at roughly several million dollars (@04:31).
  - Documents are packed into B×T batch rows separated by end-of-text tokens, and at every position the transformer predicts the next token, the actual next token supervising the weights (@05:06, @05:41, @06:45).
  - The pretraining plot to watch is the loss over time; lower loss means higher probability on the correct next integer (@07:48).
  - The field noticed that language-model pretraining learns powerful general representations that can be finetuned efficiently for downstream tasks such as sentiment with only a few examples, because predicting the next token forces the model to multitask (@07:48, @08:23, @08:56). He labels that GPT-1 (@08:56).
  - Around GPT-2, people found prompting with fake documents could work even better than finetuning, which he says kicked off an era of prompting over finetuning (@08:56, @09:31).
  - SFT collects small, high-quality datasets of prompt and ideal response from human contractors, typically tens of thousands, and still does language modeling; nothing changes algorithmically except the training set (@11:43).
  - Contractors follow long labelling documentation asking them to be helpful, truthful and harmless (@12:15, @12:48).
  - Reward modeling collects comparisons: the SFT model writes several completions per prompt, people rank them (sometimes taking hours per prompt), and a transformer predicts a reward at a special readout token, trained to agree with the rankings (@13:23, @13:57, @14:31).
  - The reward model is not deployable as an assistant but scores any completion for the RL stage (@15:04).
  - In RL the model, initialised from SFT, samples completions, the frozen reward model scores them, and the language-modeling loss on the sampled tokens is weighted by the reward (@15:35, @16:08).
  - RLHF in his account is reward modeling plus reinforcement learning; ChatGPT is an RLHF model (@12:48, @16:43).
  - Finetuning is getting more accessible through parameter-efficient methods such as LoRA (captioned "Laura"), which train small pieces and keep most of the model clamped, allowing low-precision inference for the frozen parts (@35:00, @35:33, @36:07).
  - Finetuning needs more technical expertise, contractors or synthetic-data pipelines, and slows iteration; SFT is achievable, but RLHF is research territory, unstable, not beginner friendly, and he would not advise rolling your own (@36:07, @36:40).
- relation: **Note:** the 2023-01-17 lecture gave a three-step finetuning stage (SFT, reward model, PPO) after pretraining; this talk repackages it as four stages and names the last two RLHF. Same recipe, more detail; not a change of view.

### topic: tokenization
- existing: yes
- statements:
  - Before training, raw text is tokenized into integer sequences, the native representation GPTs work over (@02:16, @02:48).
  - He calls it a lossless translation between text, tokens and integers, with several algorithms available, for example byte pair encoding, which iteratively merges text chunks into tokens (@02:48).
  - Vocabularies are usually a couple of tens of thousands of tokens; his example distribution has 50,257 entries (@03:21, @06:13).

### topic: base-models-vs-assistant-models
- existing: no (merge may prefer to make this a section of pretraining-and-finetuning; it is the "resulting model" column of the same recipe)
- aliases: [Base model, assistant model, SFT model, RLHF model, GPT assistant]
- statements:
  - There is an evolutionary tree of base models; the GPT-4 base model was never released, and the GPT-4 served over the API is an assistant model (@09:31, @10:05).
  - He says the GPT-3 base model is on the API (captioned "Devanshi", presumably davinci), GPT-2's weights are on GitHub, and LLaMA is probably the best available base model though not commercially licensed (@10:05).
  - Asked for a poem, a base model answers with more questions; prompting it as "here's a poem about bread and cheese" works (@10:36).
  - A few-shot prompt laid out as a human–assistant exchange can make a base model act as an assistant, but this is not very reliable (@10:36, @11:09).
  - There are three kinds of model: base, SFT and RLHF; ChatGPT is RLHF, Vicuna-13B is SFT (@16:43).
  - On the Berkeley Elo ranking he puts GPT-4 best by far, then Claude and GPT-3.5, which he says are RLHF; the rest, to his knowledge, are SFT models (@19:29, @20:02).

### claim: pretraining-gives-a-document-completer
- existing: yes
- statements:
  - Base models are not assistants; they want to complete documents, so a request may be answered with more questions (@10:05, @10:36).
  - Few-shot prompts trick them into tasks by making them believe they are imitating a document (@08:56, @09:31).
- quote: "They don't want to make answers to your questions, they want to complete documents." (@10:36)
- relation: supports (restates the 2023-01-17 lecture's claim four months later: "you get a document completer" @1:51:29 vs. @10:36 here). Same claim, add source.

### claim: rlhf-works-better-because-comparing-is-easier-than-generating
- existing: no
- title: "RLHF models are preferred over SFT models, and he offers the ease of comparing over generating as one possible reason"
- confidence: stated
- statements:
  - In InstructGPT experiments humans prefer RLHF (PPO) outputs over SFT outputs, and both over a prompted base model; he calls this the unexciting answer that it works better (@17:16).
  - He says the community has not agreed on a single answer for why, and offers one possible reason: comparing is computationally easier than generating (@17:16, @17:49).
  - His example: a contractor may not be able to write a good haiku about paper clips but can judge which of several is better (@17:49, @18:21).
  - RLHF currently works a bit better than SFT if you can get it to work (@38:51).
- quote: "Judging which one of these is good is a much easier task." (@18:21)
- relation: none. **Note:** [[rlvr]] (2025-12-19) says the pre-2025 recipe was pretraining, SFT and RLHF; consistent, but it is background, not support. Title must keep "one reason potentially" hedge.

### claim: rlhf-models-lose-entropy
- existing: no
- title: "RLHF models lose entropy, so he still prefers base models for generating more of a kind"
- confidence: stated
- statements:
  - He says RLHF models are not strictly an improvement on base models in some cases: they lose entropy and give peakier, less varied samples (@18:21).
  - He still prefers a base model when you have n things and want more like them; his example is seven Pokemon names completed into many more, which he checked were fictitious (@18:55, @19:29).
- quote: none under 15 words without a fragment; candidate fragment "they lose some entropy" (@18:21, grep-verified as part of "they lose some entropy. That means...").
- relation: none. Could fold into base-models-vs-assistant-models.

### claim: transformers-need-tokens-to-think
- existing: no
- title: "Transformers need tokens to think"
- confidence: stated
- statements:
  - A human writing one sentence comparing California's and Alaska's populations uses self-knowledge, tool use (Wikipedia, a calculator), sanity checks and revision (@20:34, @21:06, @21:38).
  - The GPT sees only the resulting tokens, with that internal dialogue stripped from the data, and spends roughly the same compute on every token through about 80 layers (@22:13, @22:45).
  - So you cannot expect it to do too much work per token, and on reasoning tasks you have to spread the reasoning over more tokens (@22:45, @24:27).
  - Few-shot examples that show work, or "let's think step by step", condition it to show its work and so do less computation per token (@24:59, @25:32).
- quote: "These transformers need tokens to think" (@24:59)
- relation: none in the wiki. **Note:** loosely related to [[rlvr]] (2025: "test-time compute" by letting models think longer, blog §1), but the 2023 talk is about prompting, not training; do not link as supports without a reviewer's judgement.

### topic: prompting-llms
- existing: no (check software-3-0 for overlap: that page is prompts as programs; this is how to write them)
- aliases: [Prompt engineering, prompting, chain of thought, let's think step by step, self-consistency, few-shot prompting, System 2, Tree of Thought, constrained prompting]
- statements:
  - He describes LLMs as token simulators: they do not know what they don't know or what they are good at, do not reflect, sanity check or correct mistakes, and have no separate inner monologue (@22:45, @23:22).
  - Their advantages are vast fact-based knowledge in tens of billions of parameters and a relatively large, perfect working memory in the context window, losslessly accessible through self-attention (@23:22, @23:55).
  - He says prompting is to a large extent making up for this cognitive difference between brains and LLMs (@23:55, @24:27).
  - Self-consistency: sample several times and keep the good ones or majority-vote, because a model that samples a bad token cannot recover and continues down the blind alley (@25:32, @26:05).
  - Bigger models like GPT-4 often know when they failed (a poem that rhymes when asked not to), but only check if prompted to (@26:40, @27:12).
  - He groups these as recreating System 2 (slow, deliberate planning) on top of System 1 token sampling, citing Tree of Thought (@27:12, @27:46).
  - Tree of Thought is not just a prompt but prompts plus Python glue code with tree search; he compares it to AlphaGo's policy plus Monte Carlo tree search, for text (@28:21, @28:54).
  - ReAct structures answers as thought–action–observation rollouts with tool use (@28:54, @29:28).
  - Constrained prompting, his example Microsoft's Guidance, clamps token probabilities to force a template such as JSON (@34:27, @35:00).
- relation: **Note:** the token-simulator deficits (no self-knowledge) overlap [[jagged-intelligence]]'s 2025 list ("lack self-knowledge", software-is-changing @16:04) and the perfect-working-memory point overlaps [[llms-as-operating-systems]] (context window as memory, @10:01). Connection, not evidence.

### claim: llms-want-to-imitate-not-succeed
- existing: no
- title: "LLMs don't want to succeed, they want to imitate, so ask for good performance"
- confidence: stated
- statements:
  - He calls it an almost psychological quirk: training data spans everything from wrong student answers to expert ones, and by default the model imitates all of it (@30:02, @30:35).
  - In the paper he cites, "let's work this out in a step by step way to be sure we have the right answer" beat "let's think step by step", which he reads as conditioning on a right answer so the model need not hedge on low-quality solutions (@31:08).
  - So ask for a strong solution, such as "you are a leading expert"; but not too much (IQ 400 may go out of distribution or into sci-fi role-play); he guesses a U-shaped curve (@31:08, @31:41).
- quote: "LLMs don't want to succeed, they want to imitate." (@30:02)
- relation: none.

### topic: tool-use-and-retrieval
- existing: no
- aliases: [Tool use, tools and plugins, retrieval-augmented generation, RAG, vector store, LlamaIndex]
- statements:
  - As people lean on tools for what they are bad at, give LLMs calculators, code interpreters and search (@31:41, @32:15).
  - Since models may not know what they don't know, he suggests telling them in the prompt they are bad at mental arithmetic and spelling out how to call the calculator (@32:15, @32:48).
  - He says the pendulum swung from retrieval-only to memory-only LLMs, and the retrieval-augmented space between works extremely well in practice (@32:48).
  - Loading the context window, the model's working memory, with relevant information makes it work extremely well (@32:48, @33:21).
  - The emerging RAG recipe: chunk documents, embed them, store vectors, query at test time and stuff relevant chunks into the prompt; LlamaIndex is his data-connector example (@33:21, @33:53).
  - He likens it to people looking things up in a textbook or library documentation rather than relying on memory (@33:53, @34:27).
  - AutoGPT keeps a task list and recursively breaks tasks down (@29:28).
- relation: **Note:** [[no-rag-needed-for-a-small-wiki]] (2026-04-02) is about a ~100-article wiki working without RAG; it does not contradict this (different scale and claim). Link as related only, if at all.

### method: top-performance-then-optimize
- existing: no
- aliases: [His default LLM recommendations (2023), achieve top performance then optimize]
- steps:
  - Split the task into achieving top performance, then optimising cost, in that order (@37:12)
  - Start with GPT-4, the most capable model by far (@37:12)
  - Write very detailed prompts, as for a contractor who cannot email back, but cater to LLM psychology (@37:12, @37:44)
  - Retrieve and add relevant context (@37:44)
  - Show with few-shot examples rather than only tell (@37:44, @38:17)
  - Offload hard tasks to tools and plugins (@38:17)
  - Think in chains, reflection and multiple samples, not one prompt (@38:17)
  - Only after prompting is squeezed, consider finetuning; RLHF is a fragile research zone (@38:17, @38:51)
  - Then cut cost with lower-capacity models or shorter prompts (@38:51)

### claim: use-llms-as-copilots-with-human-oversight
- existing: no
- title: "In 2023 he recommended using LLMs in low-stakes applications, with human oversight, as copilots rather than autonomous agents"
- confidence: stated
- statements:
  - He lists limitations: bias, fabrication and hallucination, reasoning errors, whole classes of applications they struggle with, a knowledge cutoff around September 2021, and attacks such as prompt injection, jailbreaks and data poisoning (@38:51, @39:24).
  - So his recommendation is low-stakes use, always combined with human oversight, as a source of inspiration and suggestions, thinking copilots rather than autonomous agents performing a task somewhere, because it is not clear the models are there yet (@39:24, @39:57).
  - On AutoGPT, he finds it inspirationally interesting but does not think it works well and would not advise using it in practical applications; it is something to take inspiration from about where this is going over time (@29:28, @30:02).
- quote: "think co-pilots, instead of completely autonomous agents" (@39:57); also "It's just not clear that the models are there right now." (@39:57)
- relation to existing claims:
  - **supports [[this-is-the-decade-of-agents]]** (2025-06-19). Two years earlier he already advised against autonomous agents and for human oversight ("Combine them always with human oversight." @39:57; AutoGPT "I don't think this currently works very well" @30:02); in 2025 he says agents need humans in the loop and will take a decade (software-is-changing @27:09, @27:44). Consistent caution, not a change of view. It does not *extend* it: the 2023 talk gives no timescale, and its AutoGPT remark ("where this is going, I think over time") only gestures at future autonomy.
  - Also consistent with [[partial-autonomy-apps]]: copilots/human oversight anticipates the 2025 Iron Man suits and autonomy slider (software-is-changing @27:44, @28:17). Use as topic statement there; a `supports` link from this claim to the topic is not a claim-to-claim relation.
  - Background, not a relation: [[claude-code-is-the-first-convincing-llm-agent]] (2025-12-19) is later evidence agents became convincing; it does not contradict the 2023 claim, which is explicitly about "right now" (@39:57). Could go on a timeline `llm-agents-over-time` if merge wants one (2023 copilots and AutoGPT not working → 2025 decade of agents → 2025-12 Claude Code first convincing agent). Since the links are `supports`, CLAUDE.md §7.7 does not require a timeline.

### topic: partial-autonomy-apps
- existing: yes
- statements:
  - In 2023 he recommends copilots under human oversight over autonomous agents (@39:57).
  - He describes advanced prompting as Python glue code stringing together many prompts, called in a loop or bigger algorithm (@28:21, @28:54).
- relation: background for the 2025 page. **Note:** he does not use "autonomy slider" or "partial autonomy" in 2023; merge may prefer `context` over `sources` here.

### topic: jagged-intelligence
- existing: yes (aliases: people spirits, ghosts vs animals)
- statements:
  - LLMs have large fact-based knowledge and perfect working memory but lack self-knowledge, reflection and error correction (@23:22, @23:55).
- relation: **Note:** he does not use "jagged" or "people spirits" here; this is an earlier description of the same strengths and deficits. Merge decides `sources` vs `context`.

## Quotes
- "This is 99 percent of the training compute time and also flops." (@01:07)
- "base models are not assistants" (@10:05)
- "They don't want to make answers to your questions, they want to complete documents." (@10:36)
- "One answer that's not that exciting is that it works better." (@17:16)
- "Judging which one of these is good is a much easier task." (@18:21)
- "they don't know what they don't know" (@23:22)
- "They don't reflect in the loop." (@23:22)
- "These transformers need tokens to think" (@24:59)
- "recreating our System 2" (@27:12)
- "I don't think this currently works very well" (@30:02) — about AutoGPT
- "LLMs don't want to succeed, they want to imitate." (@30:02)
- "You want to succeed, and you should ask for it." (@30:02)
- "RLHF, I would say is very much research territory" (@36:40)
- "So my recommendation right now is use LLMs in low-stakes applications." (@39:24)
- "Combine them always with human oversight." (@39:57)
- "think co-pilots, instead of completely autonomous agents" (@39:57)
- "It's just not clear that the models are there right now." (@39:57)
- "GPT-4 is an amazing artifact." (@39:57)

All grep-verified once each in the raw file.

## Notes for merge
- Speakers: only the ANNOUNCER's intro line at @00:00 is not his. The passage from @40:31 to the end ("ladies and gentlemen ... Your journey begins today!") is GPT-4's output, which he reads aloud; never quote or attribute it as his words.
- Caption errors: "GPT Assistance" = GPT assistants (@00:35); "hybrid parameters" = hyperparameters (@03:21); "GPP-3s" = GPT-3's (@03:56); "Devanshi" is presumably davinci, but do not correct silently in a quote (@10:05); "Q8" in "Q8 prompt response data" (@11:43) is garbled; "Archives, Stock Exchange" are probably arXiv and StackExchange (@02:16); "Laura" = LoRA (@35:33); "retrieval-augment degeneration" = retrieval-augmented generation (@33:21); "let things step-by-step" = let's think step by step (@24:59); "Elo" rankings are from "a team at Berkeley" (@19:29).
- Probable caption/speech slip at @16:08: for the -1.2 row he is captioned saying every token gets "a slightly higher probability"; the sense is lower. Do not reproduce the number-direction as he stated it without flagging.
- "GPT-4, we did not release too much information" (@03:21): he speaks as OpenAI staff ("we"). Statements about LLaMA's training cost and GPT-3's age are his figures, not verified.
- Papers he cites (InstructGPT, Tree of Thought, ReAct, the "work this out step by step" paper) are their authors' results he reports; attribute the findings to the papers and only the readings to him.
- Mentioned without explanation: Vicuna, Koala, Claude, LlamaIndex, Guidance, AutoGPT, the New York Times Shakespeare demo; do not create pages for them.
- Source slug uses medium `talk` per CLAUDE.md §2/§3 (`talk-2023-05-25-state-of-gpt`, as instructed).
