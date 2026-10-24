---
type: claim
stated_on: 2023-05-25
confidence: stated
sources: ["[[talk-2023-05-25-state-of-gpt]]"]
topic: "[[prompting-llms]]"
---
# Transformers need tokens to think
> "These transformers need tokens to think" — [[talk-2023-05-25-state-of-gpt]] @24:59

## Context
He contrasts a person writing one sentence that compares California's and Alaska's populations, using self-knowledge, tools such as Wikipedia and a calculator, sanity checks and revision, with what the GPT sees ([[talk-2023-05-25-state-of-gpt]] @20:34, @21:06, @21:38). The internal dialogue is stripped from the data, so the model sees only the resulting tokens and spends the same amount of compute on every one of them, through about 80 layers ([[talk-2023-05-25-state-of-gpt]] @22:13, @22:45). So you cannot expect it to do too much work per token, and on reasoning tasks you have to spread the reasoning over more tokens ([[talk-2023-05-25-state-of-gpt]] @22:45, @24:27). Few-shot examples that show their work, or asking it to think step by step, condition the model to show its work, so it does less computation per token ([[talk-2023-05-25-state-of-gpt]] @24:59, @25:32).

## Related claims
- **Note:** [[llms-want-to-imitate-not-succeed]] is the other prompting quirk he names in the same talk; neither depends on the other ([[talk-2023-05-25-state-of-gpt]] @30:02).
