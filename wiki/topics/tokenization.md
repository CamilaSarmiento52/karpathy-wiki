---
type: topic
aliases: [Tokenization, tokenizer, tokens, character vs sub-word, character-level tokenizer, sub-word tokenizer, BPE, byte pair encoding]
first_seen: 2023-01-08
last_updated: 2023-05-25
sources: ["[[github-2023-01-08-mingpt-readme]]", "[[youtube-2023-01-17-gpt-from-scratch]]", "[[talk-2023-05-19-stanford-cs25-transformers]]", "[[talk-2023-05-25-state-of-gpt]]"]
related: ["[[character-level-language-modeling]]", "[[embeddings]]", "[[mingpt]]", "[[nanogpt]]"]
---
# Tokenization
To tokenize, in his words, is to convert raw text into a sequence of integers according to a vocabulary of possible elements ([[youtube-2023-01-17-gpt-from-scratch]] @09:31).

## What he says
The GPT lecture uses a character-level tokenizer: a lookup table from each of the 65 characters in tiny Shakespeare to an integer and back ([[youtube-2023-01-17-gpt-from-scratch]] @08:59, @10:35). Sub-word tokenizers such as Google's SentencePiece and OpenAI's tiktoken (byte-pair encoding, used by GPT) encode neither whole words nor single characters, and are what is usually adopted in practice ([[youtube-2023-01-17-gpt-from-scratch]] @10:35, @11:10). The GPT-2 encoding has roughly 50,000 tokens, so "hi there" becomes three integers instead of eight ([[youtube-2023-01-17-gpt-from-scratch]] @11:43). You can trade off codebook size against sequence length: small vocabularies give long sequences, large vocabularies give short ones ([[youtube-2023-01-17-gpt-from-scratch]] @11:43, @12:16). He keeps the character-level tokenizer because it is the simplest thing, accepting very long sequences ([[youtube-2023-01-17-gpt-from-scratch]] @12:16). Because OpenAI uses sub-word tokens, the Shakespeare set would be around 300,000 tokens in their vocabulary rather than 1 million characters ([[youtube-2023-01-17-gpt-from-scratch]] @1:49:47).

minGPT ships the sub-word side: its `bpe.py` is a mildly refactored Byte Pair Encoder that translates between text and sequences of integers exactly as OpenAI did in GPT ([[github-2023-01-08-mingpt-readme]] §intro).

In the CS25 lecture he repeats that Transformers need text encoded as integers, in the simplest case one integer per character so the whole text becomes one long one-dimensional sequence ([[talk-2023-05-19-stanford-cs25-transformers]] @31:35, @32:07). With multiple documents people splice in special end-of-text tokens, which have no modelling effect beyond the Transformer learning that the token means wipe the memory ([[talk-2023-05-19-stanford-cs25-transformers]] @32:07, @32:40). Real models' tokens, he notes in passing, are usually BPE, SentencePiece or WordPiece tokens ([[talk-2023-05-19-stanford-cs25-transformers]] @42:39).

In State of GPT he describes tokenization as the step before training that turns raw text into integer sequences, the native representation GPTs work over ([[talk-2023-05-25-state-of-gpt]] @02:16, @02:48). He calls it a lossless translation between text, tokens and integers, with several algorithms available, for example byte pair encoding, which iteratively merges text chunks into tokens ([[talk-2023-05-25-state-of-gpt]] @02:48). Vocabularies are usually a couple of tens of thousands of tokens; his example distribution has 50,257 entries ([[talk-2023-05-25-state-of-gpt]] @03:21, @06:13).

## Claims
- [[pretraining-gives-a-document-completer]] — the 300,000-token versus 300-billion-token comparison runs through tokenization

## Related
- [[character-level-language-modeling]] — the character-level choice the makemore series and this lecture share
- [[embeddings]] — what the integers index into
- [[mingpt]] — `bpe.py`
- [[nanogpt]] — the Shakespeare quick start
