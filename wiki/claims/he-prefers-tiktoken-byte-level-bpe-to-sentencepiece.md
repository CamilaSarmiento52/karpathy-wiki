---
type: claim
stated_on: 2024-02-20
confidence: stated
sources: ["[[youtube-2024-02-20-gpt-tokenizer]]"]
context: ["[[youtube-2023-01-17-gpt-from-scratch]]"]
topic: "[[tokenization]]"
---
# He prefers tiktoken's byte-level BPE to SentencePiece
> "I still think that the algorithm is kind of inferior to what's happening here" — [[youtube-2024-02-20-gpt-tokenizer]] @2:11:45

## Context
tiktoken UTF-8 encodes text and runs BPE on the bytes, while SentencePiece runs BPE on Unicode code points and falls back to byte tokens for rare ones; he finds the tiktoken way significantly cleaner ([[youtube-2024-02-20-gpt-tokenizer]] @1:29:09, @1:30:16). He sees a lot of historical baggage and potential foot guns in SentencePiece, finds quirks such as the required unknown token and its byte fallback inelegant, and says it is not well documented ([[youtube-2024-02-20-gpt-tokenizer]] @1:42:36, @1:43:09). He still calls it commonly used, efficient and a nice repo if you want to train your own tokenizer now ([[youtube-2024-02-20-gpt-tokenizer]] @1:42:36, @1:43:09). In his closing recommendations he says he really likes the byte-level BPE that tiktoken and OpenAI use, is not a huge fan of SentencePiece's byte fallback or code-point BPE, and finds its many settings easy to mis-calibrate ([[youtube-2024-02-20-gpt-tokenizer]] @2:10:39, @2:11:13). Even with the settings right he thinks its algorithm inferior; the ideal, which does not exist yet, is tiktoken with training code ([[youtube-2024-02-20-gpt-tokenizer]] @2:11:45, @2:12:18).

## Related claims
- **Note:** in the January 2023 GPT lecture he named SentencePiece and tiktoken as the sub-word tokenizers used in practice without stating a preference; this is an addition, not a change of mind ([[youtube-2023-01-17-gpt-from-scratch]] @10:35; [[youtube-2024-02-20-gpt-tokenizer]] @1:30:16).
