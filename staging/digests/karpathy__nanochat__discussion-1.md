# Digest: Introducing nanochat: The best ChatGPT that $100 can buy.
- raw: raw/github/karpathy__nanochat__discussion-1.md · published: 2025-10-13 · medium: github · words: 4262 (frontmatter)
- source slug: github-2025-10-13-nanochat-discussion-introducing

Number tags used below: **[measured]** his reported result from a run; **[target]** a goal or
recommendation for a run not reported; **[comparison]** someone else's figure or a baseline
he compares against; plus **[setting]** (a configuration value he chose, not a result) and
**[estimate]** (arithmetic printed by the script or done by him before or instead of
measuring), because some numbers are none of the first three.

## Source page
```
---
type: source
raw_path: raw/github/karpathy__nanochat__discussion-1.md
published: 2025-10-13
medium: github
summary: "His launch walkthrough of nanochat's speedrun on one 8×H100 node: a Rust BPE tokenizer, a d20 pretraining run that slightly beats GPT-2 large on CORE, midtraining, SFT and an optional GSM8K RL stage, about 3h51m and $92 up to SFT, with every stage's evals in a report card."
url: https://github.com/karpathy/nanochat/discussions/1
title: "Introducing nanochat: The best ChatGPT that $100 can buy."
---
# Introducing nanochat: The best ChatGPT that $100 can buy.
Raw: [[raw/github/karpathy__nanochat__discussion-1]] · Original: https://github.com/karpathy/nanochat/discussions/1

The text before the first heading is cited `§intro`.

## Summary
He steps through `speedrun.sh`, which trains "the best ChatGPT that $100 can buy" on an 8×H100 node at about $24/hour (§intro, §Environment setup). He trains a 65,536-token byte-level BPE tokenizer with a new Rust implementation, because minbpe is too slow and Hugging Face tokenizers too bloated, and compares its compression with GPT-2's and GPT-4's (§Environment setup, §Train the tokenizer). Pretraining a 20-layer, ~560M-parameter model on ~11.2B FineWeb-EDU tokens, the Chinchilla ratio, takes about 3 hours and reaches a CORE score of 0.22, between GPT-2 large and GPT-2 xl (§Pretraining). Midtraining on conversations, multiple-choice and tool-use data, then SFT, give a chat model he evaluates on ARC, MMLU, GSM8K, HumanEval and his own ChatCORE; an optional, simplified GRPO stage hill-climbs GSM8K (§Midtraining, §Supervised Finetuning (SFT), §Reinforcement Learning (RL)). Up to SFT the run took 3h51m, about $92.4, summarised in an auto-generated report card, and `--depth` scales the whole recipe to bigger models (§Report card, §Your turn).

## Key points
- The launch post: speedrun.sh, d20, stages, report card, $100 budget → [[nanochat]]
- rustbpe for training, tiktoken for inference; 65,536 vocab; 4.8 chars/token; vs GPT-2 and GPT-4 → [[tokenization]], [[minbpe]]
- Pretraining, midtraining, SFT and RL as four stages, each with what it adapts → [[pretraining-and-finetuning]]
- Base model is a fancy autocomplete → [[pretraining-gives-a-document-completer]]
- CORE, bits per byte, ChatCORE, multiple choice taught in midtraining → [[llm-evaluation]]
- Small models must be taught multiple choice → [[small-models-must-be-taught-multiple-choice]]
- Simplified GRPO on GSM8K; RL sucks supervision bits through a straw → [[rlvr]], [[rl-sucks-supervision-bits-through-a-straw]]
- Chinchilla 20 tokens per parameter, 4e19 FLOPs, ~half MFU, Muon plus AdamW, 1/√dim LR scaling → [[compute-efficiency]], [[scaling-laws]], [[gradient-descent]]
- GPT-2 CORE scores as the comparison target; d26 for ~0.25 → [[reproduce-a-published-model]]
- Read bpb, CORE, reward and pass@k curves → [[training-diagnostics]]
- `--depth` as the single slider; tune anything and re-run → [[quick-experiment-loop]]
- Readable code, re-packaged dataset, own tokenizer to avoid bloat → [[small-hackable-educational-code]]
- Engine with KV cache, prefill/decode, Python-interpreter tool use → [[sampling-from-language-models]], [[llm-tool-use]]
- DeepWiki to ask questions of the repo → [[building-for-agents]]

## Fed pages
- [[nanochat]]
- [[tokenization]]
- [[minbpe]]
- [[pretraining-and-finetuning]]
- [[pretraining-gives-a-document-completer]]
- [[llm-evaluation]]
- [[small-models-must-be-taught-multiple-choice]]
- [[rlvr]]
- [[rl-sucks-supervision-bits-through-a-straw]]
- [[compute-efficiency]]
- [[scaling-laws]]
- [[gradient-descent]]
- [[reproduce-a-published-model]]
- [[training-diagnostics]]
- [[quick-experiment-loop]]
- [[small-hackable-educational-code]]
- [[sampling-from-language-models]]
- [[llm-tool-use]]
- [[building-for-agents]]
- [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]]
```

## Candidates

### artifact: nanochat
- existing: yes (`wiki/artifacts/nanochat.md`, built from [[github-2026-07-03-nanochat-readme]] and [[blog-2025-12-19-year-in-review-2025]])
- what this source adds to the page (the page has nothing on the stages, the tokenizer, the evals or the costs at launch):
  - It is the launch walkthrough; its goal is "the best ChatGPT that $100 can buy", which he calls a "speedrun", run by `speedrun.sh` start to end on a blank box (§Environment setup). [$100: target]
  - Hardware: an 8×H100 box, e.g. from Lambda, about $24/hour (§intro). [$24/hr: comparison (rental price)]
  - Stages in order: tokenizer training, pretraining, midtraining, SFT, optional RL, then chat by CLI or a FastAPI web UI (§Train the tokenizer through §Reinforcement Learning (RL), §Supervised Finetuning (SFT)).
  - The default model is d20: 20 layers, 1280 channels, 10 heads of dim 128, ~560M parameters (§Pretraining). [setting; 560,988,160 printed by the script]
  - The base model reaches CORE 0.22 for about $72, a little above GPT-2 large and a little below GPT-2 xl (§Pretraining). [CORE 0.22 / 0.2219: measured; $72: estimate (3 h × $24); GPT-2 large 0.21, xl 0.26: comparison]
  - Up to and including SFT the run took 3h51m, $92.4 at $24/hour; with RL closer to 5 hours; "$8 left for ice cream" (§Report card). [3h51m: measured; $92.4: estimate from measured time × price; ~5 h: measured, approximate]
  - The auto-generated `report.md` records run details and a stage-by-stage metric table, plus code size: 333,989 characters, 8,304 lines, 44 files, ~83,497 tokens, 2,004 uv.lock lines (§Report card). [measured, of the codebase]
  - Inference uses a custom `Engine` class with a KV cache, prefill and decode, and Python-interpreter tool use (§Pretraining).
  - `--depth` is the single slider of complexity: channels, learning rates and the rest follow from it, so changing depth sweeps a miniseries; deeper and longer gives strictly better results, he says (§Your turn). For GPT-2 capability, CORE about 0.25, d26 is a good number to try (§Your turn). [d26 / 0.25: target]
  - He says the project is "nowhere near tuned enough" (§Supervised Finetuning (SFT)).
  - He points readers to DeepWiki or their favourite LLM to ask questions of the repo, and to Discussions, Issues and Discord `#nanochat` (§Your turn).
- how it relates to the 2026 README on the page (write dates, not order): the README (2026-07-03) gives GPT-2 grade CORE in ~2 hours for ~$48 and says GPT-2 capability is around depth 26 (README §intro, §Research). The Discussion (2025-10-13) has d20 at CORE 0.22, below GPT-2 xl's 0.26, in 3h51m for $92.4 up to SFT, and suggests d26 to reach ~0.25. Different runs and code states, not a contradiction; both use $24/hour for an 8×H100 node. The README's GPT-2 CORE is 0.256525; the Discussion rounds GPT-2 xl to 0.26.
- the existing line "Its BPE tokenizer in Rust was vibe-coded" (year-in-review §5) now has the launch reason beside it: minbpe too slow, HF tokenizers too bloated (§Environment setup).

### topic: tokenization (rustbpe)
- existing: yes
- statements:
  - He admits a new custom tokenizer is a bit much, but minbpe's Python is way too slow and Hugging Face `tokenizers` too bloated and confusing, so nanochat has its own Rust tokenizer for training, tested equal to the Python, and uses tiktoken for efficient inference (§Environment setup).
  - The training algorithm is identical to OpenAI's: regex splitting, byte-level BPE (§Train the tokenizer).
  - Vocab size 2^16 = 65,536, "a nice number", with a few special tokens reserved for the chat schema; trained on 2B characters in ~1 minute (§Train the tokenizer). [65,536, 2B: setting; ~1 min: measured]
  - Compression ratio about 4.8 characters per token (§Train the tokenizer). [measured]
  - Against GPT-2's tokenizer (50,257 tokens) it compresses better across the board except slightly on math; against GPT-4's (100,277) it is worse, especially multilingual, also code and math, which he attributes to FineWeb's strong English focus; it beats GPT-4 by a tiny bit on FineWeb itself because it was trained on that distribution (§Train the tokenizer). [vocab sizes: comparison; ratios: measured, in images, not in the text]
  - Special tokens follow OpenAI's format; midtraining teaches the conversation tokens, absent in pretraining except `<|bos|>`; `<|python_start|>`/`<|python_end|>` delimit tool calls (§Midtraining).
- relation to claim [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]] (2024-02-20): **supports.** In 2024 he liked tiktoken's byte-level BPE and said the ideal, tiktoken with training code, did not exist ([[youtube-2024-02-20-gpt-tokenizer]] @2:11:45, @2:12:18). Here he trains with OpenAI's algorithm in his own Rust trainer and infers with tiktoken (§Environment setup, §Train the tokenizer): his own build matches the preference. It does not mention SentencePiece, so it is evidence for the tiktoken half only.

### artifact: minbpe
- existing: yes
- statement: he calls the Python minbpe "way too slow" for nanochat's tokenizer training (§Environment setup). **Note:** minbpe's own todos list a faster Python version and a C or Rust version ([[github-2024-04-22-minbpe-readme]] §todos); a connection, not a claim that rustbpe is that todo.

### topic: pretraining-and-finetuning (midtraining, SFT, RL)
- existing: yes; add alias `midtraining`, `GRPO` (no midtraining page; prompt says fold here)
- statements:
  - Pretraining trains the LLM to compress internet web text by predicting the next token, and is where it gains a lot of knowledge about the world; it is the most computationally heavy part (§Pretraining).
  - Pretraining data is FineWeb-EDU, which he re-packaged as `karpathy/fineweb-edu-100b-shuffle` because `datasets.load_dataset()` is too heavy and obscures simple logic: 1822 parquet shards of ~0.25M characters, ~100MB each; d20 needs 240 shards, ~24GB (§Train the tokenizer). [setting / measured sizes]
  - The base model is a fancy autocomplete; his prompts show it knows Paris, Au, Saturday after Friday, cold, the planets, but not the sky's colour or simple maths (§Pretraining).
  - **Midtraining** finetunes on smol-SmolTalk conversations; algorithmically identical to pretraining, it teaches the multi-turn special tokens, adapts to the conversation distribution, teaches multiple choice (100K MMLU auxiliary_train rows) and Python-interpreter tool use, and could target things like context-length extension, not explored yet (§Midtraining).
  - Default mixture: 460K SmolTalk, 100K MMLU auxiliary_train, 8K GSM8K, 568K rows; ~8 minutes against ~3 hours of pretraining (§Midtraining). [rows: setting; times: measured]
  - **SFT** is another round on conversations where ideally you cherry-pick the best data and do safety training such as refusals; it pads rows to mimic the test-time format rather than concatenating them, which fixes a domain mismatch as a small "tightening the screws" boost; ~7 minutes (§Supervised Finetuning (SFT)). [7 min: measured]
  - **RL**, commented out by default: he says RLHF gains a few percent and mitigates sampling-loop failures such as hallucinations and infinite loops, not major at this scale; GSM8K has an objective reward, so a simplified GRPO hill-climbs it (§Reinforcement Learning (RL)).
- relation: the existing page's last date is 2024-07-11 and says llm.c was pretraining only with SFT/RLHF on the roadmap ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Coming up)). This source has his own full pipeline. Topic-level, no claim link. **Note:** the "midtraining" stage is new to the wiki; the 2023 four-stage recipe ([[talk-2023-05-25-state-of-gpt]] @01:07) has no stage between pretraining and SFT.

### claim (existing): pretraining-gives-a-document-completer
- existing: yes (2023-01-17)
- statement: the base model "at this point is a fancy autocomplete" (§Pretraining), and only after midtraining is it "a proper Chat model" (§Midtraining).
- relation: **supports**: the same claim in his own trained model, with the base model completing prompts rather than answering ([[youtube-2023-01-17-gpt-from-scratch]] @1:51:29; §Pretraining). Add this source to the claim's `sources`.

### claim (existing): pretraining-is-lossy-compression-of-the-internet
- existing: yes (2023-11-23)
- statement: pretraining is "training the LLM to compress internet web text by predicting the next token", where it gains knowledge of the world (§Pretraining).
- relation: **supports**: same wording, compression by next-token prediction yielding world knowledge ([[youtube-2023-11-23-intro-to-llms]] @07:10, @07:43). Not in Fed pages above because it is one sentence; merge decides whether to add it (if so, add to Fed pages).

### topic: llm-evaluation
- existing: yes; add aliases `CORE`, `CORE metric`, `ChatCORE`, `bits per byte`, `bpb`, `MMLU`, `GSM8K`, `HumanEval`, `ARC`
- statements:
  - During pretraining the script evaluates the CORE metric from the DCLM paper, which he calls a normalized, broad measure of autocompletion over 22 datasets including HellaSwag, Jeopardy, ARC, COPA, PIQA, LAMBADA, Winograd, BoolQ (§Pretraining). [22: comparison (the benchmark's composition)]
  - Validation bits per byte normalises each token's loss by its byte count, making it tokenizer-invariant and comparable across vocab sizes, unlike raw cross-entropy (§Pretraining).
  - Base d20: train/val bpb ~0.81, CORE 0.22 (§Pretraining). [measured] Step-0 validation bpb 3.3013 in the log (§Pretraining). [measured]
  - Chat evals: ARC-E/C and MMLU are multiple choice with ~25% chance; GSM8K and HumanEval have a 0% baseline (§Midtraining). [baselines: comparison]
  - Mid results: ARC-Easy 0.3561, ARC-Challenge 0.2875, MMLU 0.3111, GSM8K 0.0250, HumanEval 0.0671, ChatCORE 0.0730 (§Midtraining). [measured]
  - SFT results: ARC-Easy 0.3876, ARC-Challenge 0.2807, MMLU 0.3151, GSM8K 0.0455, HumanEval 0.0854, ChatCORE 0.0884, "a small bump" (§Supervised Finetuning (SFT)). [measured] **Note:** ARC-Challenge drops slightly from mid to SFT; he does not comment.
  - RL: GSM8K 0.0758 (§Report card). [measured]
  - ChatCORE is his attempt to extend CORE to chat models: subtract each task's baseline so random is 0, then average; a single-number summary (§Midtraining).
  - He says the evals are still fairly incomplete and many things are not yet measured (§Midtraining).
- relation: on this topic the 2024-07-11 llm.c post says models at GPT-2's capability do not understand multiple choice, which makes good evals harder ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Evals)). This source **supports** that with a fix: teach multiple choice in midtraining (§Midtraining). Topic-level; see the claim below.

### claim: small-models-must-be-taught-multiple-choice
- existing: no (optional; merge may keep it as a sentence on [[llm-evaluation]])
- title: At small scale a model must be taught how multiple choice works to show what it knows
- confidence: stated
- stated_on: 2025-10-13
- quote: "the model doesn't learn it just from random internet data" (§Midtraining)
- statements:
  - At this small scale the model must learn the algorithm of mapping choices to letters and emitting the right one; the issue, he says, is not missing knowledge but not understanding how multiple choice surfaces it (§Midtraining).
  - He mixes in 100K MMLU auxiliary_train questions for this, because common evals like MMLU are multiple choice (§Midtraining). [100K: setting]
  - "Multiple choice is pretty hard for models this small." (§Midtraining)
- relation to existing claims: none as a claim page. The supporting statement is on [[llm-evaluation]] ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Evals)), so a **Note:** there.

### topic: rlvr
- existing: yes (source 2025-12-19 only)
- statements:
  - Of his datasets, GSM8K has a clear, objective reward, the correct answer, so he runs RL that interleaves sampling and training to hill-climb it (§Reinforcement Learning (RL)).
  - His GRPO is highly simplified: no trust region (no reference model or KL), on-policy (no PPO ratios or clip), token-level normalisation, advantage as reward minus mean; closer to REINFORCE but keeping the group-relative advantage (§Reinforcement Learning (RL)).
  - Default run ~1.5 hours; reward, pass@1 and pass@8 rise, and pass@8 >> pass@1 suggests more to gain with more RL; improvements are larger on bigger models, he ran up to d30 (§Reinforcement Learning (RL)). [1.5 h: measured; d30: measured that he ran it, no numbers given]
  - It is commented out by default because it is not well tuned and gives a GSM-specific model, not a general chat model, and there is no full general RLHF (§Reinforcement Learning (RL)).
- **Note:** he does not use the term RLVR in this source; the page's definition (training against automatically checkable rewards such as math) fits GSM8K. Merge should say so. Also check `first_seen` if this becomes a `sources` entry (2025-10-13 would become first_seen).

### claim: rl-sucks-supervision-bits-through-a-straw
- existing: no
- title: Reinforcement learning is sucking supervision bits through a straw
- confidence: stated
- stated_on: 2025-10-13
- quote: "reinforcement learning is sucking supervision bits through a straw" (§Reinforcement Learning (RL))
- context: he gives it as the reason the RL stage runs for quite a while, about 1.5 hours by default (§Reinforcement Learning (RL)). It is said in passing, about run time; keep the title no stronger.
- relation to existing claims: none. **Note (cross-source, both new):** the 2025-10-01 blog says billions of parameters need a "rich, high information density supervision signal", which is why pretraining precedes RL ([[blog-2025-10-01-animals-vs-ghosts]] §intro). The two fit together (RL's signal is thin, so a dense one comes first) but neither text links them; if both claims are created, `supports` is arguable, a **Note:** is safer.

### topic: compute-efficiency
- existing: yes; aliases already include MFU, bfloat16; add `Muon`
- statements:
  - Each GPU processes 32 rows of 2048 tokens, 524,288 ≈ 0.5M tokens per step across 8 GPUs (§Pretraining). [setting]
  - Estimated 3.49e9 FLOPs per token; total ~3.9e19, "a ~4e19 FLOPs capability model" (§Pretraining). [estimate]
  - Each step takes about 0.5 s; MFU "looks good at almost ~half" of bfloat16 compute (§Pretraining). [measured; log shows 47–49% after step 1]
  - Pretraining takes about 3 hours (§Pretraining). [measured]
  - Larger depths need a smaller device batch (16 for d26, 8 for d30); the code then adds gradient accumulation to keep 0.5M tokens per step (§Your turn). [settings]

### topic: scaling-laws
- existing: yes
- statements:
  - To meet the Chinchilla scaling-law recommendation he trains on 20 tokens per parameter: 560M × 20 ≈ 11.2B tokens, ≈ 21,400 steps (§Pretraining). [20: comparison (paper's recommendation); 11.2B, 21,400: setting derived from it]
  - Larger depth and longer training give strictly better results, he says (§Your turn).

### topic: gradient-descent
- existing: yes
- statements:
  - Muon optimises the matrices and AdamW the embedding and unembedding; there are no other trainable parameters, no biases or RMSNorm parameters (§Pretraining).
  - The learning rate is scaled as 1/√dim because larger models prefer smaller learning rates; the log shows 0.774597 for 1280 against 768 (§Pretraining). [setting]
  - `lrm`, the LR decay multiplier, ramps linearly down to 0 near the end of training (§Pretraining). [setting]
- relation to claim [[do-not-decay-the-learning-rate-to-zero]] (2024-06-12): **none; flag for review.** That claim is scoped in its title to the llm.c runs, where after the 774M run he chose to decay to 10% ([[github-2024-06-12-llmc-gpt-2-774m]] §intro (Reflections)). nanochat's default here ramps to 0 (§Pretraining). Different project and optimiser (Muon + AdamW vs AdamW), and he gives no reason or opinion here, so both can be true: not `contradicts`. A **Note:** on the claim page is reasonable; do not write it as a change of mind.

### method: reproduce-a-published-model
- existing: yes
- statements:
  - The eval bundle contains GPT-2 models' CORE scores, which he uses as the comparison: d20's 0.22 sits between GPT-2 large (0.21) and GPT-2 xl, "the" GPT-2 (0.26) (§Pretraining). [0.22: measured; 0.21, 0.26: comparison]
  - To get a GPT-2-capability model, CORE ~0.25, he suggests d26 (§Your turn). [target]
  - He publishes the launch commands, time and cost in the post (§Report card).
- note: nanochat does not reproduce GPT-2's architecture or data; it compares against GPT-2's CORE. Fits the method's "Compare with the released checkpoint" and "Publish the launch command, the time and the cost" steps only.

### method: training-diagnostics
- existing: yes
- statements:
  - In pretraining he watches validation bpb fall and CORE rise (§Pretraining).
  - In RL he watches reward, pass@1 and pass@8, and reads pass@8 >> pass@1 as headroom left for more RL (§Reinforcement Learning (RL)).
  - He shows a midtraining run of a different, bigger model to show what rising metrics look like (§Midtraining).
- note: the method's existing steps are init-era diagnostics (makemore); these are run-level plots. Merge may add a step like "Read validation bpb and benchmark curves together" or keep as sentences.

### method: quick-experiment-loop
- existing: yes (from the 2026 README's d12 loop)
- statements:
  - "With nanochat, you can tune *anything*": tokenizer, data, hyperparameters, optimisation; tune any part, re-run, have fun (§Your turn).
  - `--depth` is the single slider; everything else follows from it (§Your turn).
- note: the Discussion has no d12 or five-minute runs; it invites the loop rather than describing his own. Light support for the method; merge may cite it only on the definition.

### method: small-hackable-educational-code
- existing: yes
- statements:
  - He tried very hard to keep the code readable, commented, clean and accessible (§Your turn).
  - He re-packaged FineWeb-EDU into simple shuffled parquet shards because `datasets.load_dataset()` is heavy, bloated and obscures simple logic (§Train the tokenizer).
  - He wrote his own tokenizer rather than use Hugging Face `tokenizers`, which he calls bloated and confusing (§Environment setup).
  - The report card counts the codebase: 8,304 lines in 44 files, 2,004 uv.lock lines (§Report card). [measured]
- note: the method's step "Keep PyTorch as the only dependency" is from earlier repos; nanochat uses uv, Rust/Cargo, maturin, wandb (optional), FastAPI, tiktoken. Not a contradiction of any claim; merge should not imply nanochat follows that step.

### topic: sampling-from-language-models
- existing: yes
- statement: the `Engine` class uses a KV cache for efficient inference and implements prefill and decode (§Pretraining).

### topic: llm-tool-use
- existing: yes
- statements: the Engine supports a Python-interpreter tool; midtraining teaches it with commands between `<|python_start|>` and `<|python_end|>`, and 8K GSM8K rows teach simple math and calculator tool use (§Pretraining, §Midtraining). [8K: setting]

### topic: building-for-agents
- existing: yes (DeepWiki already cited from the README)
- statement: he suggests packaging the repo for your favourite LLM or using DeepWiki by swapping github.com for deepwiki.com (§Your turn).

## Quotes
- "We wish to train the best ChatGPT that $100 can buy" (§Environment setup)
- "I know - it's a bit much to have a new/custom tokenizer" (§Environment setup)
- "where the LLM gains a lot of knowledge about the world" (§Pretraining)
- "Bits per byte is a much better measure than just the typical cross-entropy loss" (§Pretraining)
- "The model at this point is a fancy autocomplete" (§Pretraining)
- "Multiple choice is pretty hard for models this small." (§Midtraining)
- "the model doesn't learn it just from random internet data" (§Midtraining)
- "The evals are still fairly incomplete" (§Midtraining)
- "Our model isn't even sure about the color of the sky" (§Supervised Finetuning (SFT))
- "this project is nowhere near tuned enough" (§Supervised Finetuning (SFT))
- "reinforcement learning is sucking supervision bits through a straw" (§Reinforcement Learning (RL))
- "it creates a GSM-specific model, not a general chat model" (§Reinforcement Learning (RL))
- "We even have $8 left for ice cream." (§Report card)
- "With nanochat, you can tune *anything*." (§Your turn)
- "I tried very hard to keep it readable, commented, clean and accessible." (§Your turn)

All grep-checked against the raw (one match each).

## Notes for merge
- **Headings** (exact): `§intro`, `§Environment setup`, `§Train the tokenizer`, `§Pretraining`, `§Midtraining`, `§Supervised Finetuning (SFT)`, `§Reinforcement Learning (RL)`, `§Report card`, `§Your turn`. The "$100 can buy" sentence is under Environment setup, not intro.
- **Costs are arithmetic:** $72 for the base model (≈3 h × $24) and $92.4 (3h51m × $24) are his calculations at the rental price, not invoices. The $100 is the budget target. RL is excluded from the 3h51m.
- **Tokenizer comparison numbers** are in images; the text gives only the 4.8 ratio and qualitative comparisons. Do not invent per-domain ratios.
- **The README and the Discussion** report different runs (d20 at CORE 0.22 here; GPT-2 grade CORE 0.256525 in ~2 h for ~$48 there). Write both with their dates; do not write "later", "since launch" or "down from". The README's own "down from 3h" is the README's wording, citable to it.
- **LR to zero:** nanochat's `lrm` ramps to 0; [[do-not-decay-the-learning-rate-to-zero]] is about llm.c. Not a contradiction; flag only.
- "even the planes of the solar system" (§Pretraining) is his typo for planets.
- The chat-format example in §Midtraining (sky "Red. Wait, possibly blue") is an illustrative format sample, not model output.
- `^[` before step 0 in the log is a terminal escape artefact.
- He says RL "is commented out by default right now" and the RL stage is excluded from the wall-clock total; a reader running speedrun.sh at this date would not get the RL column.
- No replies by other people in the raw file. Four later nanochat Discussions (164, 314, 420, 481) are in `raw/github/`, uningested; not read here.
- Merge should add aliases `midtraining`, `GRPO` to [[pretraining-and-finetuning]]; `CORE`, `ChatCORE`, `bits per byte` to [[llm-evaluation]]; `Muon` to [[compute-efficiency]] or [[gradient-descent]]; `rustbpe`, `speedrun` to [[nanochat]].
