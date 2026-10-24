---
type: topic
aliases: [Prompting, in-context learning, few-shot prompting, chain of thought, prompt engineering, meta-learning, scratchpad, self-consistency, let's think step by step, constrained prompting]
first_seen: 2023-05-19
last_updated: 2023-05-25
sources: ["[[talk-2023-05-19-stanford-cs25-transformers]]", "[[talk-2023-05-25-state-of-gpt]]"]
related: ["[[software-3-0]]", "[[transformer-architecture]]", "[[gpt-is-a-general-purpose-computer-running-natural-language-programs]]"]
---
# Prompting LLMs
In-context learning, in his framing, is a Transformer learning from examples placed in its prompt, in its activations and without gradient descent, which he says is kind of what makes Transformers really special ([[talk-2023-05-19-stanford-cs25-transformers]] @55:30, @56:34). In State of GPT (May 2023) he says prompting is to a large extent making up for the cognitive difference between brains and LLMs ([[talk-2023-05-25-state-of-gpt]] @23:55, @24:27).

## What he says
**In-context learning (CS25, 2023).** He points to the GPT-3 paper "Language Models are Few-Shot Learners", which he would have renamed something like "Transformers are capable of in-context learning or meta learning" ([[talk-2023-05-19-stanford-cs25-transformers]] @55:30). In the paper's setting the prompt holds a passage plus example question–answer pairs, and accuracy improves with more examples in context ([[talk-2023-05-19-stanford-cs25-transformers]] @56:02, @56:34). He reads this as the Transformer learning in its activations, unlike finetuning, which updates on example–answer pairs by gradient descent ([[talk-2023-05-19-stanford-cs25-transformers]] @56:34). The paper distinguishes an outer loop, training by gradient descent, from an inner loop, in-context learning as the model reads the sequence ([[talk-2023-05-19-stanford-cs25-transformers]] @56:34, @57:07). He reports that recent papers hint something like gradient-based learning may happen inside the activations; that is the papers' position, and his own reason it is not impossible, which he calls much more hand-wavy, is that forward, backward and update add to the weights like a ResNet, and a Transformer is a ResNet ([[talk-2023-05-19-stanford-cs25-transformers]] @57:07, @57:38).

On extending memory, he likes keeping the context fixed and teaching the model, via prompt examples, to write to a scratchpad between special tokens that external logic saves and lets it attend over; because it is so meta-learned it can be taught such gadgets, like a person learning to use a notepad ([[talk-2023-05-19-stanford-cs25-transformers]] @1:08:47, @1:09:20).

**Prompting around LLM psychology (State of GPT, 2023).** He describes LLMs as token simulators: they do not know what they don't know or what they are good at, do not reflect, sanity-check or correct mistakes along the way, and have no separate inner monologue ([[talk-2023-05-25-state-of-gpt]] @22:45, @23:22). Their advantages are a very large fact-based knowledge in tens of billions of parameters and a relatively large, perfect working memory: whatever fits in the context window is losslessly available through self-attention ([[talk-2023-05-25-state-of-gpt]] @23:22, @23:55). Prompting, he says, is largely making up for this difference ([[talk-2023-05-25-state-of-gpt]] @23:55, @24:27).

So he spreads reasoning over tokens with few-shot examples that show their work or by asking for step-by-step thinking ([[talk-2023-05-25-state-of-gpt]] @24:59, @25:32). Self-consistency samples several times and keeps the good ones or takes a majority vote, because a model that samples a bad token cannot recover and continues down the blind alley ([[talk-2023-05-25-state-of-gpt]] @25:32, @26:05). Bigger models such as GPT-4 often know when they failed, for instance a poem that rhymes when asked not to, but only check if prompted to ([[talk-2023-05-25-state-of-gpt]] @26:40, @27:12). He groups such techniques as recreating System 2, citing Tree of Thought, and describes ReAct's thought–action–observation rollouts with tool use ([[talk-2023-05-25-state-of-gpt]] @27:12, @27:46, @28:54, @29:28). Constrained prompting, his example being Microsoft's Guidance, clamps token probabilities to force a template such as JSON ([[talk-2023-05-25-state-of-gpt]] @34:27, @35:00).

**His default recommendations.** He splits the work into achieving top performance first and optimising cost second ([[talk-2023-05-25-state-of-gpt]] @37:12). For the first: start with GPT-4, the most capable model by far; write very detailed prompts, as for a contractor who cannot email back, while catering to LLM psychology; retrieve and add relevant context; show with few-shot examples rather than only tell; offload hard tasks to tools and plugins; and think in chains, reflection and multiple samples rather than one prompt ([[talk-2023-05-25-state-of-gpt]] @37:12, @37:44, @38:17). Only after prompting is squeezed should you consider finetuning, with RLHF a fragile research zone; then cut cost with lower-capacity models or shorter prompts ([[talk-2023-05-25-state-of-gpt]] @38:17, @38:51). **Note:** the full order, with the Sequoia interview's distillation step, is the method [[make-it-work-then-make-it-cheap]] ([[talk-2023-05-25-state-of-gpt]] @37:12).

## Claims
- [[gpt-is-a-general-purpose-computer-running-natural-language-programs]] — prompts as the programs GPT runs
- [[transformers-need-tokens-to-think]] — spread reasoning over tokens
- [[llms-want-to-imitate-not-succeed]] — ask for a strong solution

## Related
- [[software-3-0]] — prompts as programs, his 2025 framing
- [[transformer-architecture]]
- [[system-1-and-system-2-thinking]] — the System 2 techniques
- [[llm-tool-use]] — tools and retrieval
- [[jagged-intelligence]] — the strengths and deficits prompting works around
