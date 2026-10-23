---
type: topic
aliases: [Tokenization, tokenizer, tokens, character vs sub-word, character-level tokenizer, sub-word tokenizer, BPE, byte pair encoding]
first_seen: 2023-01-08
last_updated: 2023-01-17
sources: ["[[github-2023-01-08-mingpt-readme]]", "[[youtube-2023-01-17-gpt-from-scratch]]"]
related: ["[[character-level-language-modeling]]", "[[embeddings]]", "[[mingpt]]", "[[nanogpt]]"]
---
# Tokenization
To tokenize, in his words, is to convert raw text into a sequence of integers according to a vocabulary of possible elements ([[youtube-2023-01-17-gpt-from-scratch]] @09:31).

## What he says
The GPT lecture uses a character-level tokenizer: a lookup table from each of the 65 characters in tiny Shakespeare to an integer and back ([[youtube-2023-01-17-gpt-from-scratch]] @08:59, @10:35). Sub-word tokenizers such as Google's SentencePiece and OpenAI's tiktoken (byte-pair encoding, used by GPT) encode neither whole words nor single characters, and are what is usually adopted in practice ([[youtube-2023-01-17-gpt-from-scratch]] @10:35, @11:10). The GPT-2 encoding has roughly 50,000 tokens, so "hi there" becomes three integers instead of eight ([[youtube-2023-01-17-gpt-from-scratch]] @11:43). You can trade off codebook size against sequence length: small vocabularies give long sequences, large vocabularies give short ones ([[youtube-2023-01-17-gpt-from-scratch]] @11:43, @12:16). He keeps the character-level tokenizer because it is the simplest thing, accepting very long sequences ([[youtube-2023-01-17-gpt-from-scratch]] @12:16). Because OpenAI uses sub-word tokens, the Shakespeare set would be around 300,000 tokens in their vocabulary rather than 1 million characters ([[youtube-2023-01-17-gpt-from-scratch]] @1:49:47).

minGPT ships the sub-word side: its `bpe.py` is a mildly refactored Byte Pair Encoder that translates between text and sequences of integers exactly as OpenAI did in GPT ([[github-2023-01-08-mingpt-readme]] §intro).

## Claims
- [[pretraining-gives-a-document-completer]] — the 300,000-token versus 300-billion-token comparison runs through tokenization

## Related
- [[character-level-language-modeling]] — the character-level choice the makemore series and this lecture share
- [[embeddings]] — what the integers index into
- [[mingpt]] — `bpe.py`
- [[nanogpt]] — the Shakespeare quick start
