---
type: claim
stated_on: 2023-05-25
confidence: stated
sources: ["[[talk-2023-05-25-state-of-gpt]]", "[[youtube-2025-02-05-deep-dive-into-llms]]", "[[youtube-2025-02-27-how-i-use-llms]]", "[[github-2025-10-24-nanochat-strawberry-guide]]"]
topic: "[[prompting-llms]]"
---
# Transformers need tokens to think
> "These transformers need tokens to think" — [[talk-2023-05-25-state-of-gpt]] @24:59

## Context
He contrasts a person writing one sentence that compares California's and Alaska's populations, using self-knowledge, tools such as Wikipedia and a calculator, sanity checks and revision, with what the GPT sees ([[talk-2023-05-25-state-of-gpt]] @20:34, @21:06, @21:38). The internal dialogue is stripped from the data, so the model sees only the resulting tokens and spends the same amount of compute on every one of them, through about 80 layers ([[talk-2023-05-25-state-of-gpt]] @22:13, @22:45). So you cannot expect it to do too much work per token, and on reasoning tasks you have to spread the reasoning over more tokens ([[talk-2023-05-25-state-of-gpt]] @22:45, @24:27). Few-shot examples that show their work, or asking it to think step by step, condition the model to show its work, so it does less computation per token ([[talk-2023-05-25-state-of-gpt]] @24:59, @25:32).

**Deep Dive, 2025-02-05.** He restates it for a general audience under a section he calls "models need tokens to think": a modern network has on the order of 100 layers, so the compute per token is finite and roughly fixed, and reasoning has to be distributed over tokens ([[youtube-2025-02-05-deep-dive-into-llms]] @1:49:28, @1:50:01, @1:50:34, @1:57:46). For a training label, an answer that states the result first makes the rest post-hoc justification and trains the model to guess in one token; a worked answer with intermediate steps is the better label ([[youtube-2025-02-05-deep-dive-into-llms]] @1:51:07, @1:51:39, @1:52:11, @1:52:44). With bigger numbers a single-token answer fails where a step-by-step one is right ([[youtube-2025-02-05-deep-dive-into-llms]] @1:54:23, @1:54:58, @1:55:32). He adds that wherever possible you should lean on tools rather than let the model do the work in its memory, and that counting fails for the same reason ([[youtube-2025-02-05-deep-dive-into-llms]] @1:57:46, @1:58:18).

**How I use LLMs, 2025-02-27.** In practice he describes thinking models emitting many tokens over minutes and reaching higher accuracy on hard math and code, so he tries a fast non-thinking model first and switches when the answer could be better ([[youtube-2025-02-27-how-i-use-llms]] @24:36, @25:12, @29:41). A model without a code tool doing a big multiplication "in its head" gets close but wrong ([[youtube-2025-02-27-how-i-use-llms]] @1:02:58, @1:04:06).

**Strawberry guide, 2025-10-24.** Writing nanochat's letter-counting answers, he breaks the problem into all its implicit calculations spread across tokens, so no single token carries too much computation, since "it only has so many layers per token!" ([[github-2025-10-24-nanochat-strawberry-guide]] §Counting). An explicit running counter lets the model attend back to the latest count and just add one ([[github-2025-10-24-nanochat-strawberry-guide]] §Counting). Forced to answer in a single token, he says, even a state-of-the-art LLM must solve all of this in one forward pass, which is really hard; reasoning models break the task over many tokens and attend back to that work like memory registers of a partial solution ([[github-2025-10-24-nanochat-strawberry-guide]] §Summary). **Note:** here he applies the idea to how training answers are written, as the Deep Dive did for labels ([[youtube-2025-02-05-deep-dive-into-llms]] @1:51:07; [[github-2025-10-24-nanochat-strawberry-guide]] §Counting).

## Related claims
- **Note:** [[llms-want-to-imitate-not-succeed]] is the other prompting quirk he names in the same talk; neither depends on the other ([[talk-2023-05-25-state-of-gpt]] @30:02).
