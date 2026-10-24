---
type: topic
aliases: [System 1, System 2, System 1 and System 2, Thinking Fast and Slow, thinking longer, reasoning, Tree of Thought, converting time into accuracy]
first_seen: 2023-05-25
last_updated: 2023-11-23
sources: ["[[talk-2023-05-25-state-of-gpt]]", "[[youtube-2023-11-23-intro-to-llms]]"]
related: ["[[prompting-llms]]", "[[rlvr]]"]
---
# System 1 and System 2 thinking
In his framing, System 1 is a fast, automatic process that corresponds to an LLM just sampling tokens, and System 2 is the slower, deliberate planning part of the brain that much prompting tries to recreate ([[talk-2023-05-25-state-of-gpt]] @27:12, @27:46).

## What he says
**Recreating System 2 (State of GPT, 2023).** He says a lot of prompting techniques, such as asking the model to check its work, fall into the bucket of recreating System 2 on top of token sampling, and points to Tree of Thought as a recent paper in that direction ([[talk-2023-05-25-state-of-gpt]] @27:12, @27:46). Tree of Thought, he notes, is not just a prompt but prompts used with Python glue code and a tree search over which prompts to expand ([[talk-2023-05-25-state-of-gpt]] @28:21). He draws a parallel to AlphaGo, whose policy imitates humans while Monte Carlo tree search plays out possibilities and keeps what works, calling Tree of Thought an equivalent for text ([[talk-2023-05-25-state-of-gpt]] @28:21, @28:54). Right after AutoGPT, which he doubts works very well yet, he says this kind of work is like giving the model System 2 thinking ([[talk-2023-05-25-state-of-gpt]] @29:28, @30:02).

**A research direction (Intro to LLMs, November 2023).** He takes the distinction from the book Thinking, Fast and Slow: System 1 is quick and instinctive, as for 2+2, and System 2 slower, rational and conscious, as for 17×24 or tournament rather than speed chess ([[youtube-2023-11-23-intro-to-llms]] @35:23, @35:57). LLMs currently have only System 1: words enter in a sequence and each chunk of next-word prediction takes roughly the same time, so they cannot reason through a tree of possibilities ([[youtube-2023-11-23-intro-to-llms]] @36:31). Many people, he says, want to give LLMs a System 2: to convert time into accuracy, for example allowing 30 minutes on a question with accuracy rising monotonically with thinking time, which no model could do then ([[youtube-2023-11-23-intro-to-llms]] @37:06, @37:40). He presents this as a direction the field is broadly interested in, not an OpenAI product announcement ([[youtube-2023-11-23-intro-to-llms]] @34:52).

## Claims
- [[llms-currently-only-have-a-system-1]]

## Related
- [[prompting-llms]] — the techniques he groups this way
- [[rlvr]] — **Note:** his 2025 account of test-time compute, letting models think longer, is compatible with the 2023 wish; a later, separate page, not a change of view
- [[llm-self-improvement]] — the other open direction in the same talk
