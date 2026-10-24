# Digest: Let's build the GPT Tokenizer
- raw: raw/youtube/zduSFxRajkE.md · published: 2024-02-20 · medium: youtube · words: 24,900 (approx., `wc -w` on the file)
- source slug: youtube-2024-02-20-gpt-tokenizer

## Source page

```
---
type: source
raw_path: raw/youtube/zduSFxRajkE.md
published: 2024-02-20
medium: youtube
summary: Two-hour lecture that builds a byte-level BPE tokenizer from scratch, walks through the GPT-2 and GPT-4 tokenizers, special tokens, SentencePiece and vocabulary size, and traces a list of LLM failures back to tokenization.
url: https://www.youtube.com/watch?v=zduSFxRajkE
title: "Let's build the GPT Tokenizer"
---
# Let's build the GPT Tokenizer
Raw: [[raw/youtube/zduSFxRajkE]] · Original: https://www.youtube.com/watch?v=zduSFxRajkE

## Summary
A 2h13m lecture on tokenization, which he calls his least favourite part of working with LLMs and the root of a lot of their oddness (@00:00, @04:27). He opens with a list of LLM failures he traces to tokenization and demonstrates several in a live tokenizer web app, then explains why Python strings are Unicode code points, why UTF-8 bytes are the starting vocabulary, and why raw bytes alone make sequences too long (@05:00, @15:41, @21:20). He builds byte-pair encoding from scratch in a notebook: count pairs, merge the most frequent, repeat to a chosen vocabulary size, then write decode and encode and test the round trip (@23:32, @28:32, @35:45, @42:59, @48:38, @55:56). He then walks through what real tokenizers add: the GPT-2 and GPT-4 regex pre-split, OpenAI's `encoder.py` and tiktoken, special tokens and the model surgery they need, and SentencePiece as used by Llama 2 (@57:37, @1:12:17, @1:18:23, @1:28:35). After a section on vocabulary size and multimodal tokens he returns to each failure on his list and explains it, ending with his recommendations and his wish that tokenization could be removed (@1:43:09, @1:51:24, @2:10:39). He publishes the code as minbpe with an exercise progression (@1:25:09, @1:25:45).

## Key points
- Tokenization converts text to and from integer tokens, the atom of an LLM; a lot of LLM oddness traces back to it → [[tokenization]], [[a-lot-of-llm-oddness-traces-back-to-tokenization]]
- Spelling, string reversal, non-English text, arithmetic, GPT-2's Python, `<|endoftext|>`, trailing spaces, SolidGoldMagikarp and JSON vs YAML are each explained through tokenization → [[a-lot-of-llm-oddness-traces-back-to-tokenization]]
- Byte-level BPE: start from 256 UTF-8 byte tokens, iteratively merge the most frequent pair into a new token → [[tokenization]]
- The tokenizer is a separate pre-processing stage with its own training set → [[the-tokenizer-is-a-separate-stage-from-the-llm]]
- GPT-2 and GPT-4 split text with a regex before BPE so some merges never happen → [[tokenization]]
- Special tokens such as `<|endoftext|>` and chat delimiters sit outside BPE and need embedding and output-layer surgery → [[tokenization]], [[embeddings]], [[pretraining-and-finetuning]]
- He prefers tiktoken's byte-level BPE to SentencePiece's code-point BPE with byte fallback → [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]]
- Vocabulary size is an empirical hyperparameter with a sweet spot → [[vocabulary-size-is-an-empirical-hyperparameter]]
- As a deep learning person he prefers not to normalise the raw text → [[leave-raw-text-unnormalized-for-llms]]
- Tokenization-free byte-level modelling would be amazing but is not yet proven at scale → [[tokenization-free-modeling-would-be-amazing-but-is-unproven]]
- An untrained embedding row behaves like unallocated memory → [[embeddings]]
- minBPE: his clean Python BPE tokenizer with training code, plus an exercise progression → [[minbpe]], [[small-hackable-educational-code]]
- He builds the tokenizer up from scratch with toy examples, pause-and-implement exercises and round-trip tests → [[spelled-out-build-from-scratch]]

## Fed pages
- [[tokenization]]
- [[embeddings]]
- [[pretraining-and-finetuning]]
- [[a-lot-of-llm-oddness-traces-back-to-tokenization]]
- [[tokenization-free-modeling-would-be-amazing-but-is-unproven]]
- [[the-tokenizer-is-a-separate-stage-from-the-llm]]
- [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]]
- [[vocabulary-size-is-an-empirical-hyperparameter]]
- [[leave-raw-text-unnormalized-for-llms]]
- [[minbpe]]
- [[spelled-out-build-from-scratch]]
- [[small-hackable-educational-code]]
```

## Candidates

### topic: tokenization
- existing: yes (`wiki/topics/tokenization.md`; aliases already include BPE, byte pair encoding, tokenizer, sub-word tokenizer)
- aliases to add: byte-level BPE, byte-pair encoding, tiktoken, SentencePiece, special tokens, `<|endoftext|>`, regex pre-tokenization, UTF-8, vocabulary size, merges
- suggested sections (merge map prefers sections over new pages): definition; Unicode and UTF-8; BPE training; decode and encode; regex pre-split; special tokens; SentencePiece vs tiktoken; vocabulary size; multimodal tokens; token efficiency of formats
- statements:
  - **Definition / framing**
  - Tokenization translates strings into sequences of tokens and back; tokens are the fundamental unit, the atom, of LLMs, and everything is in units of tokens (@03:20).
  - In his previous GPT video he used a naive character-level tokenizer with a vocabulary of 65 characters; state-of-the-art models instead work on character chunks built with algorithms such as byte-pair encoding (@00:33, @01:05, @02:12).
  - Each token's integer indexes a row of an embedding table of trainable parameters; that vector is how the Transformer perceives the token (@01:40, @02:12).
  - He credits the GPT-2 paper as probably the paper that introduced byte-level encoding for LLM tokenization; GPT-2 has a vocabulary of 50,257 tokens and a context of 1,024 tokens (@02:45, @03:20). (Caption numbers: "50,2 57", "1,24".)
  - **What the tokenizer web app shows**
  - In a live tokenizer web app, the same string becomes different tokens depending on leading space, position and case ("egg", " egg", "Egg"), so the model must learn from data that these are the same concept (@07:47, @08:21, @08:54).
  - Numbers split arbitrarily: 127 is one token while 677 is two (@07:12, @07:47).
  - GPT-2 tokenizes each indentation space in Python as a separate token 220 (@11:05, @11:42).
  - Switching from GPT-2 to the GPT-4 tokenizer (cl100k_base) dropped the same string from 300 to 185 tokens, because the vocabulary roughly doubled from about 50k to about 100k (@12:17, @12:51).
  - The GPT-4 tokenizer groups runs of spaces into single tokens, which he calls a deliberate choice by OpenAI that densifies Python (@13:58, @14:32).
  - **Unicode and UTF-8: why bytes**
  - Python strings are immutable sequences of Unicode code points; Unicode defines roughly 150,000 characters across 161 scripts, and `ord` gives a character's code point (@15:41, @16:14, @16:48).
  - He rejects using code points directly as tokens because the vocabulary would be about 150,000 and, more worryingly, the standard keeps changing so it is not a stable representation (@17:20, @17:54).
  - UTF-8 encodes each code point as one to four bytes; UTF-16 and UTF-32 are wasteful for simple ASCII text, and UTF-8 is the only one backwards compatible with ASCII, so he sticks with UTF-8 (@18:30, @19:39, @20:45).
  - Raw UTF-8 bytes alone mean a vocabulary of only 256, so text stretches over very long sequences that the finite attention context cannot afford; BPE compresses the byte sequences while keeping UTF-8 (@21:20, @21:52, @22:26).
  - **BPE training, step by step**
  - BPE, on a toy vocabulary a, b, c, d: find the most frequent pair, mint a new token for it, replace every occurrence, append it to the vocabulary, repeat; 11 tokens with vocabulary 4 became 5 tokens with vocabulary 7 (@23:32, @24:06, @24:41, @25:47, @26:21).
  - Applied to bytes, you start with 256 tokens, iteratively mint new ones, and end with a compressed training set plus a way to encode and decode any sequence (@26:21).
  - In his notebook a paragraph of 533 code points became 616 UTF-8 bytes, since non-ASCII characters take several bytes (@27:27, @28:01).
  - `get_stats` counts consecutive pairs; the top pair was (101, 32), "e" followed by a space, occurring 20 times (@28:32, @29:41, @30:14).
  - Merging it into new token 256 shortened the list from 616 to 596, the 20 occurrences (@30:47, @33:33).
  - The number of merges is a hyperparameter: more merges give a larger vocabulary and shorter sequences; GPT-4 uses roughly 100,000 tokens (@34:06, @34:39).
  - With a target vocabulary of 276 he does exactly 20 merges, records each in a `merges` dictionary, and newly minted tokens are themselves eligible for merging, so the result is a binary forest over the bytes rather than a single tree (@35:45, @36:20, @36:53, @38:01, @38:33).
  - 20 merges took about 24,000 bytes to 19,000 tokens, a compression ratio of roughly 1.27 (@38:33).
  - The tokenizer's parameters are just the merges dictionary, which builds the binary forest on top of raw bytes (@57:03).
  - **Decode and encode**
  - Decode: build `vocab` from token id to bytes (raw bytes for 0–255, then concatenated children for each merge, relying on insertion-ordered dicts from Python 3.7), join the bytes and UTF-8 decode (@42:59, @43:33, @44:08, @44:41).
  - Not every byte sequence is valid UTF-8, so decoding token 128 alone fails; the fix is `errors="replace"`, which is also what OpenAI's released code does, and a replacement character in output means the model emitted an invalid sequence (@45:16, @45:51, @46:24, @47:32, @48:05).
  - Encode: UTF-8 encode to bytes, then repeatedly merge the eligible pair with the lowest merge index (earliest learned) until none remains; guard against fewer than two tokens (@48:38, @49:12, @50:22, @50:57, @52:03, @53:41, @55:20).
  - Encode-then-decode returns the original string, including on validation text the tokenizer never saw, but decode-then-encode is not an identity because not all token sequences are valid UTF-8 (@55:56, @56:30).
  - **Regex pre-split in GPT-2 and GPT-4**
  - The GPT-2 paper says naive BPE would merge words with punctuation ("dog.", "dog!", "dog?"), clustering semantics with punctuation, so they enforce rules on top of BPE about what never merges (@58:09, @58:43).
  - GPT-2's `encoder.py` compiles a regex (with the `regex` package, not `re`) and `findall` splits text into chunks; each chunk is tokenized independently and the results concatenated, so merges never cross chunk boundaries (@59:51, @1:00:23, @1:03:13, @1:03:47, @1:04:21).
  - The pattern separates common apostrophe contractions, letters (`\p{L}`), numbers (`\p{N}`), punctuation, and whitespace, using a negative lookahead so a space stays attached to the following word as in " you" (@1:01:34, @1:02:08, @1:04:54, @1:05:28, @1:07:44, @1:08:20, @1:08:54, @1:09:27).
  - He does not love the apostrophe handling: it is hard-coded to the ASCII apostrophe, breaks on uppercase because `re.IGNORECASE` was left out (which the GPT-2 code comments acknowledge), and is probably language-specific; he calls it extremely gnarly and slightly gross (@1:05:28, @1:06:00, @1:06:34, @1:07:10).
  - OpenAI's training was not simply chunk-then-BPE: GPT-2's runs of spaces are never merged, so some additional unstated rule was enforced, and the GPT-2 tokenizer training code was never released, only inference code (@1:10:00, @1:10:35, @1:11:08).
  - The GPT-4 pattern (cl100k_base, in tiktoken's `openai_public.py`) is case-insensitive, handles whitespace differently, and only merges numbers of up to three digits; he says nobody really knows why because none of it is documented (@1:12:51, @1:13:26, @1:13:58, @1:14:31).
  - **OpenAI's code and tiktoken**
  - tiktoken is OpenAI's official tokenization library, inference only; in it GPT-2 leaves whitespace unmerged and GPT-4 merges it (@1:11:42, @1:12:17).
  - GPT-2's `encoder.json` is exactly his `vocab` and `vocab.bpe` is his `merges`; those two variables are all you need to represent a tokenizer (@1:15:05, @1:15:36, @1:16:11).
  - Their extra byte encoder/decoder layer is, to him, a spurious implementation detail; otherwise the code is messy but algorithmically identical to what he built (@1:16:44, @1:17:17, @1:17:50).
  - **Special tokens**
  - GPT-2's 50,257 = 256 byte tokens + 50,000 merges + one special token, `<|endoftext|>`, inserted between documents in the training stream; the model has to learn from data what it means (@1:18:58, @1:19:34, @1:20:07).
  - Special tokens do not go through BPE; tiktoken's Rust code swaps them in via special-case handling (@1:20:39, @1:21:15, @1:21:49).
  - Special tokens are used pervasively in finetuning to delimit conversations, such as the GPT-3.5-turbo `im_start` / `im_end` tokens, and GPT-4 adds fill-in-the-middle prefix/middle/suffix tokens and another one (@1:21:49, @1:22:24, @1:24:03).
  - tiktoken lets you fork cl100k_base and add your own special tokens (@1:22:58).
  - **SentencePiece vs tiktoken**
  - SentencePiece, used by Llama and Mistral, does both training and inference efficiently (@1:28:35, @1:29:09).
  - The big difference: tiktoken UTF-8 encodes and then runs BPE on bytes, while SentencePiece runs BPE on code points and, for rare code points (set by `character_coverage`), maps them to an unknown token or, with byte fallback on, to byte tokens (@1:29:09, @1:29:42, @1:30:16).
  - He configured SentencePiece to match, as far as he could tell, how Llama 2 trained its tokenizer, by reading the options out of Meta's released model file (@1:32:27).
  - SentencePiece has a huge number of options and historical baggage, including a concept of sentences he finds spurious for LLMs (@1:31:22, @1:33:33, @1:34:04).
  - SentencePiece vocabularies are ordered special tokens, byte tokens, merge tokens, then individual code-point tokens; a Korean string unseen in training fell back to byte tokens (@1:36:16, @1:36:50, @1:38:01, @1:38:36).
  - With byte fallback off, the unseen string became a single unknown token, which is why he thinks Llama correctly turned byte fallback on (@1:39:10, @1:39:44).
  - `add_dummy_prefix` adds a space at the start so a word at the start of text and mid-sentence become the same token; Llama 2 uses it (@1:40:21, @1:40:53, @1:41:27, @1:42:02).
  - He finds SentencePiece commonly used and efficient but full of quirks and not well documented (@1:42:36, @1:43:09).
  - **Vocabulary size**
  - In the GPT model, vocabulary size appears only in the token embedding table (rows) and the final `lm_head` linear layer (one dot product per token) (@1:43:40, @1:44:13, @1:44:46).
  - A larger vocabulary costs computation, risks undertrained rare-token vectors, and may squash too much into one token for the forward pass to process, while shorter sequences let the model attend to more text (@1:45:18, @1:45:51, @1:46:26).
  - Extending a pretrained model's vocabulary means adding embedding rows initialised with small random numbers and extending the output layer; he calls it mild model surgery, often done by freezing the base model and training only the new parameters (@1:24:37, @1:46:58, @1:47:32).
  - Gist tokens (a paper he cites): train only new token embeddings by distillation so a few tokens stand in for a long prompt; he presents it as one point in a larger design space (@1:48:04, @1:48:38, @1:49:11, @1:49:45).
  - **Multimodal**
  - He thinks many people are converging on keeping the Transformer and tokenizing other modalities, with hard (integer) or soft tokens; he cites an early image paper and OpenAI's Sora visual patches (@1:50:18, @1:50:52, @1:51:24).
  - **Token efficiency of formats**
  - The same data took 116 tokens as JSON and 99 as YAML; since you pay per token in context and dollars, he advises preferring YAML and measuring token efficiency of formats in a tokenizer app (@2:09:31, @2:10:06).
  - **Recommendations**
  - If you can, reuse the GPT-4 vocabulary with tiktoken; if you must train your own, use BPE with SentencePiece but copy Meta's settings carefully, or wait for minbpe to become efficient; the ideal, which does not exist yet, is tiktoken with training code (@2:10:39, @2:11:13, @2:11:45, @2:12:18).
- relation: extends the 2023 page content (character vs sub-word trade-off, @11:43 / @12:16 of youtube-2023-01-17-gpt-from-scratch) without contradicting it; both say vocabulary size trades against sequence length. It is a topic, so no claim link needed.

### topic: embeddings
- existing: yes
- statements:
  - The embedding table has one row per vocabulary token, a trainable vector looked up by the token's integer and fed into the Transformer (@01:40, @02:12).
  - A larger vocabulary means more rows; rare tokens get few examples and their vectors may be undertrained (@1:44:13, @1:45:18, @1:45:51).
  - Adding a token means adding a row initialised with small random numbers (@1:24:37, @1:47:32).
  - A token that never appears in the LLM's training data keeps a random, never-updated row; he likens it to unallocated memory in a C program, and invoking it produces undefined behaviour (@2:08:24, @2:08:57).

### topic: pretraining-and-finetuning
- existing: yes
- statements:
  - `<|endoftext|>` delimits documents in the pretraining stream (@1:19:34, @1:20:07).
  - Finetuning for ChatGPT introduces many new special tokens to hold conversation structure between user and assistant, and possibly tools such as a browser (@1:21:49, @1:46:58).
  - Adding special tokens for finetuning a base model into a chat model requires small model surgery on the embedding and output layers, a very common operation (@1:24:37, @1:25:09).
  - The trailing-space demo uses `gpt-3.5-turbo-instruct`, which he describes as a completion model closer to a base model that continues the token sequence (@1:58:52).
- relation: consistent with [[pretraining-gives-a-document-completer]] (youtube-2023-01-17-gpt-from-scratch) but does not argue it; use as a `## What he says` sentence, not a claim link.

### claim: a-lot-of-llm-oddness-traces-back-to-tokenization
- existing: no
- title: "A lot of LLM oddness traces back to tokenization"
- confidence: stated
- quote: "a lot of oddness with large language models typically traces back to tokenization" (@00:00)
- aliases: tokenization causes LLM problems, tokenization foot guns, LLM weaknesses from tokenization
- statements (his list at the start @04:27–@05:33, each revisited from @1:51:24):
  - He advises not brushing tokenization off: many issues that look like problems with the architecture or the LLM itself are actually tokenization issues (@04:27).
  - **Spelling and string processing.** He says difficulty with spelling tasks is usually due to tokenization (@04:27). He tested GPT-4 on ".DefaultCellStyle", a single long token: it miscounted the letter "l" (it said three; he believes four, hedging "if I'm not getting this wrong myself") and could not reverse the string directly, but succeeded when asked first to list the characters separated by spaces and then reverse the list (@1:51:58, @1:52:34, @1:53:11, @1:53:44).
  - **Non-English languages.** They can work much worse partly because of tokenization (@05:00). The tokenizer's training set has more English, so English gets longer tokens and other languages are split into more pieces, bloating sequences and using up context (@09:59, @10:33, @11:05). "Hello how are you" is 5 tokens and its Korean translation 15; even the common Korean greeting is three tokens (@1:54:20, @1:54:53).
  - **Arithmetic.** Bad simple arithmetic can be traced to tokenization (@05:00). Addition is a character-level algorithm, but numbers are split arbitrarily by whatever merged, as a blog post he cites ("integer tokenization is insane") shows for four-digit numbers in GPT-2; he calls it a headwind, and says Llama 2 splits all digits partly to improve simple arithmetic (@1:55:27, @1:56:02, @1:56:36).
  - **Python in GPT-2.** GPT-2 had more trouble with Python due to tokenization (@05:00): every indentation space is its own token, wasting context, which he calls almost a tokenization bug for GPT-2, fixed in GPT-4 (@11:42, @12:17, @1:56:36, @1:57:09). He says much of the Python improvement from GPT-2 to GPT-4 comes from the tokenizer design, not only from the model, architecture and optimisation (@14:32).
  - **`<|endoftext|>` halts the model.** Asking GPT-4 to print the string `<|endoftext|>` broke; he does not know what OpenAI does under the hood but suspects special tokens are being parsed from user input, which is attacker-controlled, making special tokens a potential attack surface (@1:57:09, @1:57:44, @1:58:18).
  - **Trailing whitespace.** The playground warns when a prompt ends in a space; because GPT tokens carry their leading space (" o" is one token), a lone trailing space becomes token 220, which splits the next token and puts the model out of distribution (@05:00, @1:58:52, @1:59:26, @2:00:00, @2:00:34, @2:01:10).
  - **Partial tokens / unstable tokens.** Prompting with ".DefaultCellSta" (part of a single token) made the model immediately emit a stop sequence, and on retry produced a usage-policy flag; he groups these as partial-token issues and points to the undocumented "unstable token" handling in tiktoken's Rust code (@2:01:41, @2:02:14, @2:02:47, @2:03:20, @2:03:53, @2:04:28).
  - **SolidGoldMagikarp.** Earlier GPT went "totally crazy" when asked about SolidGoldMagikarp (@05:33). A blog post found a cluster of strange tokens whose mention caused evasion, hallucination, insults and safety-violating behaviour (@2:05:01, @2:05:36, @2:06:09, @2:06:42). The thought-to-be explanation, which he says he does not know has been definitively explored: the tokenizer's training data had much Reddit text with that username, so it got its own token, but that data was absent from the LLM's training set, so the token's embedding was never trained (@2:07:16, @2:07:50, @2:08:24, @2:08:57).
  - **JSON vs YAML.** Being told to use YAML over JSON for structured data is a tokenization matter: YAML is more token-efficient (@05:33, @2:09:31).
  - **Overall.** He calls the stage full of foot guns and sharp edges, security issues and AI safety issues, and says it is worth understanding (@2:10:06, @2:10:39).
  - He puts the root cause as LLMs working on text chunks, not characters as people think of them (@2:01:10).
- relation: none to an existing claim page. **Note (do not link as a claim relation):** [[jagged-intelligence]] cites youtube-2025-06-19-software-is-changing @16:04 for the 9.11 > 9.9 error; that later talk does not attribute it to tokenization, so do not connect them as supports/extends.

### claim: tokenization-free-modeling-would-be-amazing-but-is-unproven
- existing: no
- title: "Feeding raw bytes without tokenization would be amazing, but it is not yet proven at scale"
- confidence: stated
- quote: "tokenization free would indeed be amazing" (@22:59)
- aliases: tokenization-free models, raw byte models, get rid of tokenization, eliminate tokenization
- statements:
  - He says he would love to feed raw byte sequences into language models, and cites a paper from the previous summer proposing a hierarchical Transformer to do it (@22:26, @22:59).
  - Doing so requires modifying the architecture, since attention becomes extremely expensive on such long sequences (@22:59).
  - He does not know that it has been proven out by enough groups at sufficient scale; he hopes someone comes up with it, but for now we must compress with BPE (@23:32).
  - At the end he says "eternal glory" goes to anyone who can get rid of tokenization, and hopes more work follows (@2:10:39).
  - He personally really dislikes the stage (@2:10:06), and calls it his least favourite part of working with LLMs (@00:00).
- relation: none.

### claim: the-tokenizer-is-a-separate-stage-from-the-llm
- existing: no
- title: "The tokenizer is a separate pre-processing stage with its own training set"
- confidence: stated
- quote: "tokenizer is a completely separate object from the large language model itself" (@39:06)
- statements:
  - The tokenizer has its own training set of documents, may differ from the LLM's, and is trained once with BPE as a pre-processing stage (@39:38).
  - It is a translation layer between raw text and tokens; typically all LLM training data is tokenized once, the raw text thrown away, and the model reads the stored tokens (@40:11, @40:45, @41:19).
  - The mix of languages and code in the tokenizer's training set determines how many merges each gets, and so how dense that data is in token space; more Japanese data means shorter Japanese sequences, which helps the LLM's finite context (@41:19, @41:53, @42:25).
  - The SolidGoldMagikarp case is his example of the two training sets differing (@2:07:16, @2:07:50).
- relation: none.

### claim: he-prefers-tiktoken-byte-level-bpe-to-sentencepiece
- existing: no
- title: "He prefers tiktoken's byte-level BPE to SentencePiece"
- confidence: stated
- quote: "I still think that the algorithm is kind of inferior to what's happening here" (@2:11:45)
- statements:
  - He finds tiktoken's approach (UTF-8 bytes, then BPE) significantly cleaner than SentencePiece's (BPE on code points, byte fallback for rare ones) (@1:30:16).
  - He says SentencePiece has a lot of historical baggage and potential foot guns, is not well documented, and that its quirks (a required unknown token, the way byte fallback works) are not elegant to him (@1:42:36, @1:43:09).
  - He likes the byte-level BPE that tiktoken and OpenAI use; he is not a huge fan of SentencePiece's byte fallback or code-point BPE, and its many settings are easy to mis-calibrate (@2:11:13).
  - Even with SentencePiece's settings right, he thinks the algorithm is inferior; the ideal is tiktoken with training code, which does not exist yet (@2:11:45, @2:12:18).
  - He still describes SentencePiece as efficient, widely used and a nice repo if you want to train your own tokenizer now (@1:42:36, @1:43:09).
- relation: none. (**Note:** the existing tokenization page cites youtube-2023-01-17-gpt-from-scratch @10:35/@11:10 naming both libraries as what is used in practice, with no preference; this is an addition, not a change of mind.)

### claim: vocabulary-size-is-an-empirical-hyperparameter
- existing: no (merge may prefer to fold this into the tokenization page's vocabulary-size section)
- title: "Vocabulary size is an empirical hyperparameter with a sweet spot"
- confidence: stated
- quote: "this is mostly an empirical hyperparameter" (@1:46:26)
- statements:
  - More tokens is not infinitely better: the embedding table and the output softmax grow, so there is a sweet spot where everything is appropriately dense and still efficient (@13:26).
  - The number of merges is a hyperparameter tuned for good vocabulary sizes, with GPT-4 at roughly 100,000 tokens (@34:06, @34:39).
  - State-of-the-art vocabularies are usually in the high tens of thousands or around 100,000 (@1:46:26).
  - Reasons not to make it infinite: compute in `lm_head`, undertrained rare tokens, and too much information squashed into single tokens (@1:45:18, @1:45:51, @1:46:26).
- relation: none to a claim. Extends the tokenization topic's 2023 trade-off sentence (youtube-2023-01-17-gpt-from-scratch @11:43, @12:16).

### claim: leave-raw-text-unnormalized-for-llms
- existing: no (small; merge may fold into the tokenization page's SentencePiece section)
- title: "For language models he prefers not to normalise the raw text"
- confidence: stated
- quote: "you want to not touch your data" (@1:33:01)
- statements:
  - Normalisation (lowercasing, removing double whitespace) was prevalent in pre-LLM NLP such as machine translation and text classification; in language models he prefers not to do any of it, as a deep learning person, keeping the data as raw as possible (@1:33:01).
  - He would rather treat a file as one giant stream of bytes than introduce SentencePiece's concept of sentences, which he finds hard to define (@1:34:04, @1:34:36).
- relation: none.

### artifact: minbpe
- existing: no (a separate raw README exists: `raw/github/karpathy__minbpe.md`, plus `karpathy__minbpe__discussion-98.md`; not read for this digest)
- aliases: minBPE, min bpe
- repo_url: https://github.com/karpathy/minbpe (from the raw README; the video caption only says "MBP")
- language: Python (@2:12:18)
- status: active (as of the video; merge to check README)
- statements:
  - He wrote it while developing the lecture and published it; he expected it to change a lot because he intends to keep working on it (@1:25:09, @1:25:45).
  - The repo includes an `exercise.md` breaking the task into four steps that build up to a GPT-4 tokenizer, with tests and the code as reference when stuck; he tried to keep the code fairly clean and understandable (@1:25:45, @1:26:20).
  - It reproduces tiktoken's GPT-4 encoding and decoding and adds a train function, which tiktoken lacks (@1:26:20, @1:26:52).
  - Trained on the Taylor Swift Wikipedia page (one of the longest), its merges look like GPT-4's, which he attributes to the same algorithm on a different training set; GPT-4's many whitespace merges suggest to him, unsure, a lot of Python in its tokenizer training data (@1:26:52, @1:27:27, @1:28:04, @1:28:35).
  - It is currently in Python; he hopes to make it efficient enough to be the tiktoken-with-training-code he wants (@2:11:45, @2:12:18).

### method: spelled-out-build-from-scratch
- existing: yes
- statements (new steps or new instances):
  - **Motivate with failures first.** He opens with the list of LLM weirdness tokenization causes and demos it in a tokenizer web app before writing code, promising to loop back (@03:54, @04:27, @05:33), and does loop back at the end (@1:51:24).
  - **Toy example before code.** He explains BPE on a four-letter vocabulary from Wikipedia before applying it to bytes (@23:32, @24:06).
  - **Pause-and-implement prompts.** He invites viewers to write `get_stats`, the merge, `decode` and `encode` themselves before pasting his own (@28:01, @30:47, @42:59, @48:38).
  - **Test on a tiny case, then check the numbers.** The merge function is checked on a short list, then on the real data: length falls by exactly the 20 occurrences and none of the merged pair remain (@32:59, @33:33).
  - **Leave a bug for the viewer.** He shows decode failing on token 128 and asks viewers to work out why before fixing it (@45:16, @45:51).
  - **Round-trip tests.** Encode-then-decode on training text and on unseen validation text (@55:56, @56:30).
  - **Map to the real code.** He shows that OpenAI's `encoder.py` is algorithmically identical to what he built (@1:15:36, @1:17:50).
  - **Ship an exercise progression.** minbpe's `exercise.md` breaks the build into four steps toward a GPT-4 tokenizer, with the repo and tests as reference, and the target is matching tiktoken's output (@1:25:45, @1:26:20).
- relation: supports the existing steps "Leave instructive errors in" / "Show a bug on purpose" and "Walk the real repo at the end".

### method: small-hackable-educational-code
- existing: yes
- statements:
  - He says he tried to keep minbpe's code fairly clean and understandable so learners can reference it (@1:26:20).
  - minbpe is Python and not yet efficient; he hopes to make it as efficient as possible (@2:11:45, @2:12:18).
- relation: supports the existing step "Give education-only code teeth when it needs them" (that step's sources are the minGPT/nanoGPT READMEs); here it is a stated intention, not done.

## Quotes
- "tokenization is my least favorite part of working with large language models" (@00:00)
- "a lot of oddness with large language models typically traces back to tokenization" (@00:00)
- "tokenization is at the heart of a lot of weirdness in large language models" (@04:27)
- "not able to do spelling tasks very easily that's usually due to tokenization" (@04:27)
- "non-english languages can work much worse" (@05:00)
- "so basically tokenization is at the heart of many issues" (@05:33)
- "tokenization free would indeed be amazing" (@22:59)
- "tokenizer is a completely separate object from the large language model itself" (@39:06)
- "you want to not touch your data" (@1:33:01)
- "I think that there's a lot of historical baggage in sentence piece" (@1:42:36)
- "this is mostly an empirical hyperparameter" (@1:46:26)
- "this is giving it brain damage" (@2:02:47)
- "it's kind of like unallocated memory in a typical binary program" (@2:08:24)
- "there's a lot of foot guns sharp edges here security issues" (@2:10:06)
- "eternal glory goes to anyone who can get rid of it" (@2:10:39)
- "I still think that the algorithm is kind of inferior to what's happening here" (@2:11:45)
- "really what we want is we want tick token but training code" (@2:12:18)

All grepped: each string occurs once in the raw file, in the block cited.

## Notes for merge
- **Caption spellings:** "bite"/"bite pair" = byte / byte pair; "MBP", "M bpe", "mean bpe" = minbpe; "Tik token", "tick token" = tiktoken; "Tik tokenizer bell.app" = the tiktokenizer web app (likely tiktokenizer.vercel.app; do not cite the URL from the caption); "sentence piece" = SentencePiece; "gp4", "gbt2", "gpd2" = GPT-4 / GPT-2; "SLP of L" = `\p{L}`; "rigix", "reex" = regex; "solid gold Magikarp", "sold gold Magikarp" = SolidGoldMagikarp; "at rot", "streamer bot" = other glitch tokens from the blog post; "default style", "default cell sta" = the ".DefaultCellStyle" token; "Thim prefix" = FIM; "Imaginary mcore start" = `im_start`; "ank", "an token", "un token" = `<unk>`; "Bap size", "voap", "vocap" = vocab size; "anang"/"anango" = annyeong; "Chachi"/"chbt" = ChatGPT; "Laura" = LoRA.
- **Garbled numbers:** "50,2 57" = 50,257; "1,24" = 1,024; "2556" at @38:01 should be 256; "10132"/"1032" = the pair (101, 32); the "25 and 259 becoming 275" merge at @38:01 is likely garbled; the emoji code point "128,000" is approximate in speech.
- **Hedges to keep:** the letter count for ".DefaultCellStyle" ("if I'm not getting this wrong myself", @1:52:34); the `<|endoftext|>` failure is his suspicion, he says he does not know what OpenAI does (@1:57:44); the SolidGoldMagikarp mechanism is "what is thought to have happened", not definitively explored (@2:07:16); GPT-4 having a lot of Python in its tokenizer data is "I suspect ... I'm not sure" (@1:28:04); Llama splitting digits is "partly" for arithmetic (@1:56:36).
- **Other people's work he reports (attribute to them, not him):** the GPT-2 paper's dog/punctuation argument (@58:09); the tokenization-free hierarchical Transformer paper (@22:59); the "integer tokenization is insane" blog post (@1:55:27); the SolidGoldMagikarp blog post (@2:05:01); the gist-tokens paper (@1:48:04); the multimodal image paper and Sora (@1:50:52); the "UTF-8 Everywhere" manifesto (@19:05).
- **Mentioned, not explained:** fill-in-the-middle ("beyond this video", @1:24:03); UTF-8 vs UTF-16/32 trade-offs beyond wastefulness ("beyond the scope", @19:05); the full GPT-4 regex ("I'm not going to go into the full detail", @1:13:26); unstable tokens (possible future video, @2:04:28); multimodal tokenization ("beyond the scope", @1:51:24). LoRA is only named.
- **Stray clips after the outro:** blocks @2:12:56 and @2:13:33 (GPT-1 context 512 to 1,024, a sneeze, "spurious layer") look like leftover outtakes after "bye". Do not cite them.
- **Possible later link, not checked:** the nanochat page says its BPE tokenizer in Rust was vibe-coded (blog-2025-12-19-year-in-review-2025 §5), and `raw/github/karpathy__rustbpe.md` exists. That could relate to his 2024 wish for "tiktoken but training code" (@2:12:18), but only after the rustbpe source is read; this digest does not support the link.
- **minbpe README:** `raw/github/karpathy__minbpe.md` is a separate source; the artifact page should cite both, and repo_url/status should come from it.
- **Granularity:** BPE, the regex pre-split, special tokens and SentencePiece are proposed as sections of `tokenization`, per the batch-1 merge map, not as new topics. The page will get long; merge may decide otherwise.
- **Phase-gate question:** the failure list and his position on removing tokenization are in the claims `a-lot-of-llm-oddness-traces-back-to-tokenization` and `tokenization-free-modeling-would-be-amazing-but-is-unproven`, with timestamps for both the opening list (@04:27–@05:33) and the explanations (@1:51:24–@2:10:06).
