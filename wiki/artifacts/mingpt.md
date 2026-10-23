---
type: artifact
repo_url: https://github.com/karpathy/minGPT
language: Python
status: superseded
sources: ["[[github-2023-01-08-mingpt-readme]]"]
aliases: [minGPT]
---
# minGPT
A PyTorch re-implementation of GPT, both training and inference, that tries to be small, clean, interpretable and educational because he found most available GPT implementations somewhat sprawling ([[github-2023-01-08-mingpt-readme]] §intro). As of January 2023 he describes it as semi-archived, with his rewrite nanoGPT as the place for more recent developments ([[github-2023-01-08-mingpt-readme]] §intro).

## What it demonstrates
- The model is about 300 lines of code in `mingpt/model.py`; all that happens, he says, is that a sequence of indices feeds into a Transformer and a probability distribution over the next index comes out, with most of the complexity in batching for efficiency ([[github-2023-01-08-mingpt-readme]] §intro).
- Three files: `model.py` (the Transformer definition), `bpe.py` (a mildly refactored Byte Pair Encoder that matches OpenAI's GPT) and `trainer.py` (GPT-independent PyTorch training boilerplate) ([[github-2023-01-08-mingpt-readme]] §intro).
- Demos: `projects/adder` trains a GPT from scratch to add numbers, inspired by the GPT-3 paper's addition section; `projects/chargpt` trains a character-level model on a text file; `demo.ipynb` is a sorting example; `generate.ipynb` loads a pretrained GPT-2 and generates from a prompt ([[github-2023-01-08-mingpt-readme]] §intro).
- Installable with `pip install -e .`; the README shows a GPT-2 (124M) configuration (vocabulary 50,257, block size 1,024) and a Trainer with learning rate, max iterations and batch size ([[github-2023-01-08-mingpt-readme]] §Library Installation, §Usage).
- He describes the unit-test coverage as not great yet, and lists open todos: finetuning and dialog demos, mixed precision, distributed training, reproducing benchmarks, proper logging, a requirements file, and loading weights beyond gpt2-* ([[github-2023-01-08-mingpt-readme]] §Unit tests, §todos).
- Reference code he points to: openai/gpt-2 (model but no training code), openai/image-gpt, and huggingface/transformers' language-modeling example, which he calls full-featured but hard to trace ([[github-2023-01-08-mingpt-readme]] §References).
- Why it was frozen: minGPT became referenced across notebooks, blogs, courses and books, which made him less willing to make the bigger changes he wanted; he also wanted to change direction from a sole focus on education to something still simple and hackable but with teeth, reproducing medium-sized industry benchmarks and accepting some tradeoffs for runtime efficiency; he points to his rewrite nanoGPT for more recent developments ([[github-2023-01-08-mingpt-readme]] §intro). `status: superseded` rests on this note ([[github-2023-01-08-mingpt-readme]] §intro).
- Licensed MIT ([[github-2023-01-08-mingpt-readme]] §License).

## Related
- [[nanogpt]] — the rewrite that superseded it; its own README calls itself a rewrite of minGPT
- [[gpt-is-not-a-complicated-model]]
- [[transformer-architecture]] — the model it implements, and his notes on the GPT papers
- [[small-hackable-educational-code]] — the design goal
- [[tokenization]] — `bpe.py`
- **Note:** [[makemore]] is his other one-file educational repo of the same period; neither README mentions the other.
