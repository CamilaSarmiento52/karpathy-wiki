---
type: claim
stated_on: 2024-05-28
confidence: stated
sources: ["[[github-2024-05-28-llmc-gpt-2-124m]]"]
topic: "[[llm-evaluation]]"
---
# His llm.c GPT-2 reproductions beat OpenAI's GPT-2 checkpoints of the same size on HellaSwag
> "We get to 29.9 here, which surpasses GPT-2 (124M) at 29.4." — [[github-2024-05-28-llmc-gpt-2-124m]] §intro

## Context
**2024-05-28, 124M on 10B tokens.** His llm.c reproduction of GPT-2 (124M), trained from scratch on 10B tokens of FineWeb, reaches 29.9 on HellaSwag, his measured result, against 29.4 for OpenAI's GPT-2 (124M) checkpoint, a comparison number ([[github-2024-05-28-llmc-gpt-2-124m]] §intro). It does not reach the 33.7 that the GPT-3 paper's Appendix H cites for GPT-3 Small (124M), and he points out that the GPT-3 models trained on 300B tokens against his 10B ([[github-2024-05-28-llmc-gpt-2-124m]] §intro).

He qualifies the comparison: the run also beats OpenAI's checkpoint on FineWeb validation loss, which he says is not a fair comparison because GPT-2 trained on the unreleased WebText, and HellaSwag has no math or code, so it slightly favours his common-crawl-like data ([[github-2024-05-28-llmc-gpt-2-124m]] §intro). The same post reports a 350M reproduction on about 30B tokens but gives no HellaSwag figure for it in the text ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (350M model)).
