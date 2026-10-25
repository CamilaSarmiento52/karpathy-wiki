---
type: claim
stated_on: 2026-02-12
confidence: stated
sources: ["[[blog-2026-02-12-microgpt]]"]
context: ["[[youtube-2022-08-16-micrograd]]"]
topic: "[[transformer-architecture]]"
supports: ["[[micrograd-is-all-you-need-everything-else-is-efficiency]]"]
---
# microgpt's 200 lines hold the full algorithmic content of a GPT; everything else is efficiency
> "Everything else is just efficiency." — [[blog-2026-02-12-microgpt]] §intro

## Context
He says the 200-line file contains the full algorithmic content of what is needed, dataset, tokenizer, autograd engine, GPT-2-like network, Adam, training loop and inference loop, that everything else is just efficiency, and that "I cannot simplify this any further." ([[blog-2026-02-12-microgpt]] §intro). Between microgpt and a production LLM like ChatGPT a long list of things change, but none, he says, alters the core algorithm and overall layout; they are what makes it work at scale ([[blog-2026-02-12-microgpt]] §Real stuff). Tensor autograd on GPUs is the same math over many scalars in parallel, and his scalar `Value` backward is the same algorithm as PyTorch's `loss.backward()`, "algorithmically identical, significantly smaller and simpler, but of course a lot less efficient" ([[blog-2026-02-12-microgpt]] §Real stuff, §Autograd). Production inference is still next-token prediction with a lot of engineering spent on speed ([[blog-2026-02-12-microgpt]] §Real stuff). He concludes "if you understand microgpt, you understand the algorithmic essence." ([[blog-2026-02-12-microgpt]] §Real stuff). Asked why it is slow, he says it processes one scalar at a time in pure Python, while a GPU runs the same math on millions of scalars in parallel ([[blog-2026-02-12-microgpt]] §FAQ).

## Related claims
- Supports [[micrograd-is-all-you-need-everything-else-is-efficiency]]: in 2022 he said a scalar autograd engine is all you need to train neural nets, tensors being purely for efficiency ([[youtube-2022-08-16-micrograd]] @05:56, @06:30); microgpt runs a whole GPT, from dataset to inference, on a scalar `Value` engine and says everything else is just efficiency ([[blog-2026-02-12-microgpt]] §intro, §Autograd). Evidence for the earlier claim; the map sets `supports` as the weakest true link, with no timeline.
- **Note:** microgpt is also a source for [[gpt-is-not-a-complicated-model]], running a GPT with no batch dimension and no parallel time steps, and for [[neural-net-training-should-not-be-complicated]], a five-step training loop in pure Python ([[blog-2026-02-12-microgpt]] §Architecture, §Training loop). No relation is set from this claim to them.
