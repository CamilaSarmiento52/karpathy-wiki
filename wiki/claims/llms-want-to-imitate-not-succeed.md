---
type: claim
stated_on: 2023-05-25
confidence: stated
sources: ["[[talk-2023-05-25-state-of-gpt]]"]
topic: "[[prompting-llms]]"
---
# LLMs don't want to succeed, they want to imitate, so ask for good performance
> "LLMs don't want to succeed, they want to imitate." — [[talk-2023-05-25-state-of-gpt]] @30:02

## Context
He calls this an almost psychological quirk of LLMs: training data spans everything from wrong student answers to expert ones, and by default the model imitates all of it ([[talk-2023-05-25-state-of-gpt]] @30:02, @30:35). In a paper he cites, "let's work this out in a step by step way to be sure we have the right answer" beat "let's think step by step"; the finding is the paper's, and his reading is that the prompt conditions on a right answer, so the model need not hedge its probability mass on low-quality solutions ([[talk-2023-05-25-state-of-gpt]] @31:08). So he says to ask for a strong solution, for example by saying it is a leading expert, but not too much: asking for an IQ of 400 may go out of distribution or into sci-fi role-play, and he guesses there is a U-shaped curve ([[talk-2023-05-25-state-of-gpt]] @31:08, @31:41).

## Related claims
- **Note:** [[transformers-need-tokens-to-think]] is the companion prompting point from the same talk ([[talk-2023-05-25-state-of-gpt]] @24:59).
