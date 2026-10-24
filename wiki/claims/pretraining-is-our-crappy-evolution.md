---
type: claim
stated_on: 2025-10-01
confidence: stated
sources: ["[[blog-2025-10-01-animals-vs-ghosts]]", "[[x-2025-10-01-sutton-podcast]]", "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
context: ["[[youtube-2023-11-23-intro-to-llms]]"]
topic: "[[pretraining-and-finetuning]]"
---
# Pretraining is our crappy evolution, one candidate solution to the cold-start problem
> "Pretraining is our crappy evolution." — [[blog-2025-10-01-animals-vs-ghosts]] §intro

## Context
The claim follows his argument that animal brains start from a powerful initialization that evolution encoded in DNA; see [[bitter-lesson]] ([[blog-2025-10-01-animals-vs-ghosts]] §intro). Our AIs also have billions of parameters, which need their own rich, high-information-density supervision signal; we are not going to re-run evolution, but we have mountains of internet documents ([[blog-2025-10-01-animals-vs-ghosts]] §intro). He grants that this is basically supervised learning, which is about absent in animals, but says it practically gathers enough soft constraints over billions of parameters to avoid starting from scratch ([[blog-2025-10-01-animals-vs-ghosts]] §intro). Pretraining is in his words one candidate solution to the cold-start problem, to be followed by finetuning on tasks that look more correct, for example within RL, as he says frontier labs now do pervasively ([[blog-2025-10-01-animals-vs-ghosts]] §intro).

**Note:** the `§intro` text cited here was also posted on X the same day, word for word; that post is a second location of the same words, not independent evidence, and has no Appendix ([[x-2025-10-01-sutton-podcast]] #1; [[blog-2025-10-01-animals-vs-ghosts]] §intro).

In the Dwarkesh interview, published 2025-10-17, he repeats it: we are not going to do evolution, but we can build ghost-like entities by imitating internet documents, which brings you up to something with a lot of built-in knowledge and intelligence, so he calls pretraining "this crappy evolution.", the practically possible way to reach a starting point for RL ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @12:28). Agreeing with Dwarkesh's point that evolution encodes learning algorithms rather than every weight, he says there must be some miraculous compression, with learning algorithms encoded that do learning online ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @11:55).

## Related claims
- **Note:** no relation set to [[pretraining-is-lossy-compression-of-the-internet]]. That claim says what pretraining produces, a lossy compression of internet text that forces the network to learn about the world ([[youtube-2023-11-23-intro-to-llms]] @05:30, @07:43); this one says what pretraining is for, an initialization in the role evolution plays for animals, before RL, and calls LLMs a statistical distillation of humanity's documents ([[blog-2025-10-01-animals-vs-ghosts]] §intro). Neither denies the other.
- **Note:** [[frontier-llms-are-not-platonically-bitter-lesson-pilled]] is the concession this argument starts from: the human data is a compromise, not the platonic ideal ([[blog-2025-10-01-animals-vs-ghosts]] §intro).
