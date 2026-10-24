---
type: claim
stated_on: 2023-05-19
confidence: stated
sources: ["[[talk-2023-05-19-stanford-cs25-transformers]]"]
topic: "[[transformer-architecture]]"
---
# He would have called the Transformer a general-purpose, efficient, optimizable computer
> "I probably would have called the Transformer a general purpose efficient optimizable computer" — [[talk-2023-05-19-stanford-cs25-transformers]] @59:18

## Context
Reading his own earlier tweets off a slide, which he says were written for general consumption and are a bit hyped, he argues the Transformer optimizes three properties at once: an expressive forward pass, possibly even meta-learning; optimizability thanks to residual connections and layer norms; and efficiency ([[talk-2023-05-19-stanford-cs25-transformers]] @58:12, @58:44). It is a shallow, wide computational graph suited to GPU parallelism; he thinks it was designed deliberately for GPUs, and he likes the earlier Neural GPU work that designs nets backwards from hardware constraints ([[talk-2023-05-19-stanford-cs25-transformers]] @58:44). In hindsight he would have used this name for the paper instead of "Attention Is All You Need" ([[talk-2023-05-19-stanford-cs25-transformers]] @59:18).

Efficiency is less talked about but, he says, extremely important, because scale matters in deep learning and being efficient on current hardware means the model can be made bigger ([[talk-2023-05-19-stanford-cs25-transformers]] @1:03:35, @1:04:09). He calls the observation that RNNs can implement arbitrary programs a somewhat useless statement, since they are not optimizable or efficient ([[talk-2023-05-19-stanford-cs25-transformers]] @1:02:29).

Earlier in the lecture he says the architecture has proven remarkably resilient: papers have tried changing its details and nothing sticks except moving the layer norms to the pre-norm position, so today's GPTs are basically the 2017 architecture ([[talk-2023-05-19-stanford-cs25-transformers]] @21:39, @22:11).

## Related claims
- **Note:** compatible with [[gpt-is-not-a-complicated-model]] (simple to write down) and [[ai-has-converged-on-one-architecture]] (why everyone copies it); neither link is set as support ([[talk-2023-05-19-stanford-cs25-transformers]] @59:18).
