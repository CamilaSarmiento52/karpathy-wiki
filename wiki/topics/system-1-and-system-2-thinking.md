---
type: topic
aliases: [System 1, System 2, System 1 and System 2, Thinking Fast and Slow, thinking longer, reasoning, Tree of Thought, converting time into accuracy]
first_seen: 2023-05-25
last_updated: 2025-02-27
sources: ["[[talk-2023-05-25-state-of-gpt]]", "[[youtube-2023-11-23-intro-to-llms]]", "[[youtube-2025-02-05-deep-dive-into-llms]]", "[[youtube-2025-02-27-how-i-use-llms]]"]
related: ["[[prompting-llms]]", "[[rlvr]]"]
---
# System 1 and System 2 thinking
In his framing, System 1 is a fast, automatic process that corresponds to an LLM just sampling tokens, and System 2 is the slower, deliberate planning part of the brain that much prompting tries to recreate ([[talk-2023-05-25-state-of-gpt]] @27:12, @27:46).

## What he says
**Recreating System 2 (State of GPT, 2023).** He says a lot of prompting techniques, such as asking the model to check its work, fall into the bucket of recreating System 2 on top of token sampling, and points to Tree of Thought as a recent paper in that direction ([[talk-2023-05-25-state-of-gpt]] @27:12, @27:46). Tree of Thought, he notes, is not just a prompt but prompts used with Python glue code and a tree search over which prompts to expand ([[talk-2023-05-25-state-of-gpt]] @28:21). He draws a parallel to AlphaGo, whose policy imitates humans while Monte Carlo tree search plays out possibilities and keeps what works, calling Tree of Thought an equivalent for text ([[talk-2023-05-25-state-of-gpt]] @28:21, @28:54). Right after AutoGPT, which he doubts works very well yet, he says this kind of work is like giving the model System 2 thinking ([[talk-2023-05-25-state-of-gpt]] @29:28, @30:02).

**A research direction (Intro to LLMs, November 2023).** He takes the distinction from the book Thinking, Fast and Slow: System 1 is quick and instinctive, as for 2+2, and System 2 slower, rational and conscious, as for 17×24 or tournament rather than speed chess ([[youtube-2023-11-23-intro-to-llms]] @35:23, @35:57). LLMs currently have only System 1: words enter in a sequence and each chunk of next-word prediction takes roughly the same time, so they cannot reason through a tree of possibilities ([[youtube-2023-11-23-intro-to-llms]] @36:31). Many people, he says, want to give LLMs a System 2: to convert time into accuracy, for example allowing 30 minutes on a question with accuracy rising monotonically with thinking time, which no model could do then ([[youtube-2023-11-23-intro-to-llms]] @37:06, @37:40). He presents this as a direction the field is broadly interested in, not an OpenAI product announcement ([[youtube-2023-11-23-intro-to-llms]] @34:52).

**Thinking models (Deep Dive, 2025-02-05).** He does not use the System 1 / System 2 words in this lecture; he describes thinking models trained with RL whose responses grow longer, and says the extra tokens are what raise accuracy ([[youtube-2025-02-05-deep-dive-into-llms]] @2:30:24, @2:32:04, @2:34:51). He calls what emerges chains of thought and cognitive strategies, like what goes on in your head rather than what you write down in a solution ([[youtube-2025-02-05-deep-dive-into-llms]] @2:31:30, @2:32:04). DeepSeek-R1's output shows the thinking and then a nicely written solution for the human, and he separates the correctness of the one from the presentation of the other ([[youtube-2025-02-05-deep-dive-into-llms]] @2:34:19, @2:34:51). His claim is [[rl-lets-models-discover-their-own-thinking-strategies]], which extends [[llms-currently-only-have-a-system-1]] ([[youtube-2025-02-05-deep-dive-into-llms]] @2:32:04).

**Thinking models in use (How I use LLMs, 2025-02-27).** Thinking models are additionally tuned with RL; they think longer, sometimes for minutes, and give higher accuracy on hard math and code, while simple questions may not benefit ([[youtube-2025-02-27-how-i-use-llms]] @24:36, @25:12). He calls this stage relatively recent and points to DeepSeek's paper as the first to talk about it publicly ([[youtube-2025-02-27-how-i-use-llms]] @24:02). He likes Perplexity's hosting of DeepSeek R1 because its raw thoughts are visible ([[youtube-2025-02-27-how-i-use-llms]] @28:35, @29:08). He usually starts with a non-thinking model for speed; that habit is a step of [[choose-a-model-tier]] ([[youtube-2025-02-27-how-i-use-llms]] @29:41, @30:13).

## Claims
- [[llms-currently-only-have-a-system-1]]
- [[rl-lets-models-discover-their-own-thinking-strategies]] — extends it; dated on [[llm-self-improvement-over-time]]

## Related
- [[prompting-llms]] — the techniques he groups this way
- [[rlvr]] — **Note:** his 2025 account of test-time compute, letting models think longer, is compatible with the 2023 wish; a later, separate page, not a change of view
- [[llm-self-improvement]] — the other open direction in the same talk
