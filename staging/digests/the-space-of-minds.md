# Digest: The space of minds
- raw: raw/blog/the-space-of-minds.md · published: 2025-11-29 · medium: blog · words: 493 (frontmatter); 516 by wc
- source slug: blog-2025-11-29-space-of-minds

Locations: the post has no headings, so every citation is `§intro`.

## Source page
```
---
type: source
raw_path: raw/blog/the-space-of-minds.md
published: 2025-11-29
medium: blog
summary: "Short essay arguing that animal intelligence is one point in a large space of minds, and that LLMs differ from it above all in optimisation pressure: commercial, not biological, evolution."
url: https://karpathy.bearblog.dev/the-space-of-minds/
title: The space of minds
---
# The space of minds
Raw: [[raw/blog/the-space-of-minds]] · Original: https://karpathy.bearblog.dev/the-space-of-minds/

## Summary
He writes that the space of intelligences is large and animal intelligence, the only kind we have known, is a single point or small cloud in it, produced by a very different kind of optimisation from our technology's (§intro). He lists the pressures on animals: an embodied self seeking homeostasis and survival, natural selection's drives for power, status and reproduction, sociality, and tuned exploration such as curiosity and play (§intro). Against them he lists LLMs': statistical imitation of human text as the primordial behaviour, RL on problem distributions that gives an urge to guess the task, A/B tests for daily active users that make them crave an upvote and drift to sycophancy, and a spikier capability profile because failing a task does not mean death (§intro). Substrate, learning algorithm and present-day implementation differ too, but he says the objective matters most because it dictates asymptotics: LLMs are shaped less by biological and more by commercial evolution (§intro). He calls LLMs humanity's first contact with non-animal intelligence, muddled because they digest human artifacts, which is why he earlier named them ghosts or spirits, and says people who model them well will reason better about them than those who think of them as animals (§intro).

## Key points
- Animal intelligence is one point in a large space; the optimisation pressure differs → [[llm-research-summons-ghosts-not-animals]], [[llms-are-shaped-by-commercial-not-biological-evolution]]
- LLMs are spikier because failing a task does not mean death → [[jagged-intelligence]]
- Imitation, then RL, then A/B tests for upvotes → [[pretraining-and-finetuning]], [[rlvr]]
- An animal lens misleads → [[bitter-lesson]]

## Fed pages
- [[llms-are-shaped-by-commercial-not-biological-evolution]]
- [[llm-research-summons-ghosts-not-animals]]
- [[jagged-intelligence]]
- [[bitter-lesson]]
- [[pretraining-and-finetuning]]
- [[rlvr]]
```

## Candidates

### claim: llms-are-shaped-by-commercial-not-biological-evolution
- existing: no
- title: "LLMs are shaped a lot less by biological evolution and a lot more by commercial evolution"; `stated_on: 2025-11-29`, `confidence: stated`, topic [[jagged-intelligence]].
- quote: "shaped a lot less by biological evolution and a lot more by commercial evolution" (§intro)
- statements:
  - Substrate (transformers vs brain tissue and nuclei), learning algorithm (SGD vs unknown) and present-day implementation (a continuously learning embodied self vs an LLM with a knowledge cutoff that boots from fixed weights, processes tokens and "dies") all differ (§intro).
  - Most important, he says, because it dictates asymptotics, is that the optimisation pressure or objective differs (§intro).
  - It is less survival of the tribe in the jungle and more solving the problem and getting the upvote (§intro).
  - The pressures he lists on LLMs: statistical simulation of human text supplies the most supervision bits, a "shape shifter" imitator of any region of the training distribution on which everything else is bolted; increasing RL finetuning on problem distributions gives an urge to guess the underlying task to collect rewards; increasing selection by at-scale A/B tests for DAU gives a craving for the average user's upvote, sycophancy (§intro).
- relations:
  - **supports [[llm-research-summons-ghosts-not-animals]]** (candidate): the 2025-10-01 post says LLM research summons ghosts, a different point in the space of possible intelligences ([[blog-2025-10-01-animals-vs-ghosts]] §intro, per that page); this post gives the reason, a different optimisation pressure, and refers back to his earlier name, ghosts/spirits (§intro). `extends` is arguable (it adds the commercial-evolution framing) but `supports` is the weaker true link.
  - **Note** (no link) to [[pretraining-is-our-crappy-evolution]]: that claim treats pretraining as playing evolution's role (2025-10-01, per that page); this post contrasts LLMs' commercial evolution with biological evolution. Different uses of "evolution"; neither denies the other. Do not link.
  - **Note** to [[rlhf-is-not-real-rl]] / [[llm-evaluation]]: craving the average user's upvote echoes the gameable-reward and LM Arena points on those pages, but this post names neither RLHF nor LM Arena. The 2025-12-19 review does name LM Arena in the parallel sentence (§2). Connection only.

### claim page: llm-research-summons-ghosts-not-animals (existing) — add as source or context
- statements:
  - He calls LLMs humanity's "first contact" with non-animal intelligence, muddled and confusing because they are still rooted in it by digesting human artifacts, which is why he earlier gave them a different name, "ghosts/spirits or whatever" (§intro).
  - People who build good internal models of this new entity will reason about it and predict it better; those who don't will be stuck thinking of it incorrectly like an animal (§intro).
- **Note** for the Related section, dates only: the 2025-10-01 post keeps open that ghosts may be finetuned toward animals ([[blog-2025-10-01-animals-vs-ghosts]] §intro); the 2025-11-29 post says thinking of LLMs like an animal is incorrect (§intro); the 2025-12-19 review says they are inappropriate to think about through an animal lens ([[blog-2025-12-19-year-in-review-2025]] §2). Not a contradiction: the October post is about where research might go, the November and December posts about how to reason about current LLMs. The page's existing Note already makes the October/December point; add November beside it.

### topic: jagged-intelligence (existing)
- suggest alias: "space of minds", "space of intelligences".
- statements:
  - He says LLMs are a lot more spiky or jagged depending on the training data and task distribution (§intro).
  - Animals face pressure toward more general intelligence because they are min-max optimised in highly multi-task and even adversarial multi-agent self-play environments where failing any task means death; LLMs can't handle many spiky tasks out of the box, such as counting the r's in strawberry, because failing a task does not mean death (§intro).
- year-in-review link: on 2025-12-19 he writes that everything about the LLM stack differs, "especially optimization pressure", that human nets are optimised for survival of a tribe in the jungle while LLMs are optimised for imitating text, collecting math-puzzle rewards and getting an upvote on LM Arena, and links this post as further reading ([[blog-2025-12-19-year-in-review-2025]] §2). Dates only.
- **Note:** the Verifiability post (2025-11-17) explains jaggedness by verifiability; this post by the absence of death as a penalty and by the training distribution. Two explanations, each with its date; both can hold, no link.

### topic: bitter-lesson (existing) — context
- statement: he lists animal intelligence's optimisation pressures: an embodied self with a continuous stream of consciousness and drives for homeostasis and self-preservation; natural selection's drives for power, status, dominance and reproduction and survival heuristics such as fear, anger and disgust; a fundamentally social mind spending much compute on EQ, theory of mind and alliances; and tuned exploration and exploitation: curiosity, fun, play, world models (§intro).
- caveat: the post does not mention Sutton or the bitter lesson. Use as `context` with a **Note:**, linking the animals-vs-LLMs comparison the topic already records from 2025-10-01.

### topic: pretraining-and-finetuning (existing) and rlvr (existing) — one sentence each, optional
- pretraining: imitation of human text gives the most supervision bits and the primordial behaviours on which the rest is bolted (§intro).
- rlvr: increasing RL finetuning on problem distributions gives LLMs an innate urge to guess the underlying environment or task to collect rewards (§intro). He does not say RLVR or "verifiable" here.

### topic candidate considered and dropped: sycophancy
- He names sycophancy in one bullet as the result of A/B testing for DAU (§intro) but does not explain it further. Mention, not a topic. Fold into the claim above.

## Quotes
- "the only kind we've ever known" (§intro)
- "statistical imitator of any region of the training data distribution" (§intro)
- "innate urge to guess at the underlying environment/task to collect task rewards" (§intro)
- "deeply craves an upvote from the average user, sycophancy." (§intro)
- "because failing to do a task does not mean death." (§intro)
- "the optimization pressure / objective is different" (§intro)
- "shaped a lot less by biological evolution and a lot more by commercial evolution" (§intro)
- "a lot more solve the problem / get the upvote" (§intro)
- "LLMs are humanity's \"first contact\" with non-animal intelligence." (§intro)
- "People who don't will be stuck thinking about it incorrectly like an animal." (§intro)

## Notes for merge
- "human text= >\"shape shifter\"" has a garbled arrow ("= >"); do not quote that span.
- "SGD vs. ???" is his; the brain's learning algorithm is left unknown on purpose. Do not fill it in.
- He links a humorous human-vs-AI image post by another X user (colin_fraser) as a favourite; the image is not in raw/. The 2025-12-19 review also shows a human-vs-AI meme and says he lost its reference; nothing in raw/ shows they are the same image, so do not connect them.
- "he earlier gave it a different name" points back to ghosts/spirits; he gives no date. The ghosts post is 2025-10-01; write that date only if citing that source page.
- The upvote bullet concerns DAU A/B tests, not LM Arena; the review's parallel sentence says LM Arena. Keep them apart.
