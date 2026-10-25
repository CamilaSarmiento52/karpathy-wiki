---
type: artifact
repo_url: https://gist.github.com/karpathy/8627fe009c40f57531cb18360106ce95
language: Python
status: active
sources: ["[[blog-2026-02-12-microgpt]]", "[[talk-2026-03-20-skill-issue]]", "[[talk-2026-04-29-sequoia-ascent-2026]]", "[[github-2026-08-03-micrograd-readme]]"]
context: ["[[github-2026-07-03-nanochat-readme]]"]
aliases: [microgpt, microgpt.py, build_microgpt]
---
# microgpt
What he calls his new art project: a single file of 200 lines of pure Python, with no dependencies, that trains and runs inference on a GPT ([[blog-2026-02-12-microgpt]] §intro). It is a GitHub gist, not a repository ([[blog-2026-02-12-microgpt]] §intro).

## What it demonstrates
- **The whole algorithm in one file.** It holds a dataset of documents, a tokenizer, an autograd engine, a GPT-2-like architecture, the Adam optimizer, a training loop and an inference loop; "Everything else is just efficiency.", and he says he cannot simplify it any further; see [[microgpt-is-the-full-algorithm-everything-else-is-efficiency]] ([[blog-2026-02-12-microgpt]] §intro).
- **A culmination.** He calls it the culmination of multiple projects, naming micrograd, makemore and nanoGPT, and of "a decade-long obsession to simplify LLMs to their bare essentials"; he thinks it is beautiful and notes it breaks perfectly across three columns ([[blog-2026-02-12-microgpt]] §intro).
- **Where it lives.** A GitHub gist, a web page at karpathy.ai/microgpt.html, a Google Colab notebook where readers can ask Gemini about it, and a triptych print on his art store ([[blog-2026-02-12-microgpt]] §intro, §Run it).
- **Data and tokens.** The default dataset is about 32,000 names from the makemore repo, one per line, each name a document (the run prints 32,033); a character tokenizer plus a BOS token gives a vocabulary of 27 ([[blog-2026-02-12-microgpt]] §Dataset, §Tokenizer, §Run it).
- **A tiny GPT.** One layer, 16-dimensional embeddings, 4 heads and a block size of 16 give 4,192 parameters, against GPT-2's 1.6 billion and hundreds of billions for modern LLMs, in his figures ([[blog-2026-02-12-microgpt]] §Parameters). It follows GPT-2 with three simplifications, RMSNorm instead of LayerNorm, no biases and ReLU instead of GeLU, and processes one token at a time with no batch dimension, so it builds the KV cache explicitly ([[blog-2026-02-12-microgpt]] §Architecture).
- **Training and sampling.** 1,000 steps of one document each take the loss from about 3.3, random guessing among 27 tokens, to about 2.37; it then samples 20 new names at temperature 0.5, which he calls hallucinated names ([[blog-2026-02-12-microgpt]] §Training loop, §Inference, §Run it).
- **Running it.** It needs only Python, no pip install, and the script takes about 1 minute on his MacBook ([[blog-2026-02-12-microgpt]] §Run it). Separately, his FAQ says a single training step takes seconds, because it processes one scalar at a time in pure Python while a GPU runs the same math on millions of scalars in parallel ([[blog-2026-02-12-microgpt]] §FAQ). The two figures are his; no per-step time is derived from them.
- **Try it on other data.** He suggests another dataset, longer training or a bigger model, "the same knobs that matter at scale"; for a new dataset the rest of the code does not need to change ([[blog-2026-02-12-microgpt]] §Run it, §FAQ).
- **Six versions.** The build_microgpt.py gist keeps train0.py to train5.py as revisions, each adding one component, train5.py being train.py; see [[spelled-out-build-from-scratch]] ([[blog-2026-02-12-microgpt]] §Progression).
- **Note:** its autograd is a scalar `Value` class, for which he points readers to his 2.5-hour micrograd video; see [[micrograd]] ([[blog-2026-02-12-microgpt]] §Autograd).
- **Note:** the post never mentions nanochat. Both are his from-scratch GPT code, nanochat a full harness that trains a ChatGPT-style model end to end and microgpt the algorithm alone in one file; the comparison is the wiki's ([[github-2026-07-03-nanochat-readme]] §intro; [[blog-2026-02-12-microgpt]] §intro).
- **Note:** `status: active` because nothing in the post marks it otherwise; `repo_url` is the gist URL the post gives ([[blog-2026-02-12-microgpt]] §intro).

**In the Skill Issue interview (2026-03-20).** He calls microGPT the current state of a decade-or-two obsession with boiling LLMs down to their essence, after nanoGPT, makemore and micrograd: training code is huge only because of efficiency, while the algorithm is 200 lines of Python, comments included, with an architecture of about 50 lines, an autograd engine of about 100 and Adam in about 10 ([[talk-2026-03-20-skill-issue]] @1:01:40, @1:02:12). He tried to make a video stepping through it and found it adds little, since anyone can ask an agent to explain it; see [[building-for-agents]] ([[talk-2026-03-20-skill-issue]] @1:02:46). An agent he asked to boil his training code down to the simplest thing could not write it, though it understands it ([[talk-2026-03-20-skill-issue]] @1:04:59, @1:05:33).

**In the micrograd README (commit dated 2026-08-03).** The README points to microgpt as the more advanced example, a full GPT-2-like transformer trained and sampled in pure, dependency-free Python, built on a more efficient and better version of micrograd's engine that stores local gradients at forward time instead of per-op backward closures ([[github-2026-08-03-micrograd-readme]] §Training a GPT). **Note:** the post's `Value` class likewise records each operation's children and local gradients; the judgement "better" is the README's ([[blog-2026-02-12-microgpt]] §Autograd; [[github-2026-08-03-micrograd-readme]] §Training a GPT).

**At Sequoia Ascent (2026-04-29).** He says that trying to simplify LLM training to be as simple as possible with microGPT, he kept prompting an LLM to simplify more and "The models hate this. They can't do it.", which felt like being outside the RL circuits; he sees nothing fundamental preventing it ([[talk-2026-04-29-sequoia-ascent-2026]] @22:58). See [[agentic-engineering]] ([[talk-2026-04-29-sequoia-ascent-2026]] @22:58).

## Related
- [[microgpt-is-the-full-algorithm-everything-else-is-efficiency]]
- [[micrograd]] — the scalar autograd engine it builds on
- [[makemore]] — the names dataset and the task
- [[nanogpt]] — named among the projects it culminates
- [[nanochat]] — not mentioned in the post; see the Note above
- [[small-hackable-educational-code]], [[spelled-out-build-from-scratch]]
