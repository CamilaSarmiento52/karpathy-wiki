# Digest: Animals vs Ghosts
- raw: raw/blog/animals-vs-ghosts.md · published: 2025-10-01 · medium: blog · words: 1768 (frontmatter; `wc -w` on the file gives 1790)
- source slug: blog-2025-10-01-animals-vs-ghosts

## Source page
```
---
type: source
raw_path: raw/blog/animals-vs-ghosts.md
published: 2025-10-01
medium: blog
summary: "His response to Richard Sutton on the Dwarkesh podcast: he grants Sutton that frontier LLMs are full of human input and not cleanly bitter-lesson pilled, but doubts animals learn from scratch, calls pretraining a crappy stand-in for evolution, and says today's LLM research summons ghosts rather than building animals."
url: https://karpathy.bearblog.dev/animals-vs-ghosts/
title: Animals vs Ghosts
---
# Animals vs Ghosts
Raw: [[raw/blog/animals-vs-ghosts]] · Original: https://karpathy.bearblog.dev/animals-vs-ghosts/

The body before the one heading is cited `§intro`; the bullets after it, `§Appendix`. The
same text, without the Appendix, is his X post [[x-2025-10-01-sutton-podcast]].

## Summary
He writes up his reaction to the Dwarkesh podcast with Richard Sutton, whose "The Bitter Lesson" he says has become near-biblical among frontier LLM researchers, and whom he reports as doubting that LLMs are bitter-lesson pilled because they train on human, finite data (§intro). He summarises Sutton's alternative, a child machine that learns only by interacting with the world through reinforcement learning, with intrinsic rewards and learning at test time, and no pretraining or supervised finetuning (§intro). He agrees with Sutton that frontier LLMs carry human input at every stage and that no clean "turn the crank" algorithm exists, and that animals do not do supervised learning (§intro, §Appendix). He disagrees that the two usual existence proofs carry over: Go is a simple closed environment, and animal brains are not blank slates, since much "learning" is maturation or finetuning on an initialization evolution encoded in DNA (§intro). So pretraining is "our crappy evolution", one practical answer to the cold-start problem, followed by RL finetuning; LLM research summons ghosts, statistical distillations of human documents, which may move toward animals or stay different, like planes and birds (§intro). The Appendix adds that in-context learning and memory files are test-time learning, and that he does not find Sutton's temporal-difference answer to long-horizon sparse rewards compelling (§Appendix).

## Key points
- Sutton's position, as he reports it: LLMs trained on human, finite data are not bitter-lesson pilled; learn from experience by RL like an animal → [[bitter-lesson]]
- He agrees frontier LLMs are not cleanly bitter-lesson pilled; the bitter lesson is correct but platonic, perhaps practically met → [[frontier-llms-are-not-platonically-bitter-lesson-pilled]]
- Animal brains are no blank slate: maturation plus finetuning on an evolved initialization; Go is closed and simple → [[animal-brains-are-not-a-blank-slate]]
- Pretraining as a crappy evolution, a candidate solution to cold start, then RL → [[pretraining-is-our-crappy-evolution]], [[pretraining-and-finetuning]]
- Frontier research summons ghosts, not animals; ghosts:animals :: planes:birds → [[llm-research-summons-ghosts-not-animals]], [[jagged-intelligence]]
- Animals do not do supervised learning; the human analogue is RL with an example in context → [[animals-do-not-do-supervised-learning]]
- Ideas to borrow from animals: intrinsic motivation, curiosity, empowerment, multi-agent self-play, culture; TD learning not compelling for long-horizon rewards → [[llm-self-improvement]]
- In-context learning and memory files as test-time learning → [[prompting-llms]], [[llm-knowledge-bases]]
- Researchers assume LLMs are bitter-lesson pilled because of scaling laws → [[scaling-laws]]

## Fed pages
- [[bitter-lesson]]
- [[frontier-llms-are-not-platonically-bitter-lesson-pilled]]
- [[animal-brains-are-not-a-blank-slate]]
- [[pretraining-is-our-crappy-evolution]]
- [[llm-research-summons-ghosts-not-animals]]
- [[animals-do-not-do-supervised-learning]]
- [[pretraining-and-finetuning]]
- [[jagged-intelligence]]
- [[llm-self-improvement]]
- [[prompting-llms]]
- [[llm-knowledge-bases]]
- [[scaling-laws]]
```

## Candidates

### topic: bitter-lesson
- existing: no (grep for "bitter lesson", "Sutton", "AlphaZero" across `wiki/` finds nothing)
- aliases: [The Bitter Lesson, bitter lesson pilled, Richard Sutton, child machine, learning from experience]
- fallback if merge wants coarser pages: a section on [[llm-self-improvement]] (its "beyond imitation / AlphaGo step two" framing is the nearest existing idea)
- statements (Sutton's positions marked as his; Karpathy reports them):
  - He says Sutton's "The Bitter Lesson" has become a bit of biblical text in frontier LLM circles, where researchers ask whether an idea is "bitter lesson pilled", meaning arranged to benefit from added computation for free, as a proxy for whether it will work (§intro).
  - He reports the researchers' assumption that LLMs are highly bitter-lesson pilled, citing scaling laws where more compute makes the number go up (§intro).
  - [Sutton] Sutton, as he reports it, is not sure LLMs are bitter-lesson pilled at all, since they train on human-generated and finite data; he lists Sutton's questions, what to do when it runs out and how to prevent human bias (§intro).
  - He says Dwarkesh and Sutton partly speak past each other because Sutton has a very different architecture in mind, one LLMs break many principles of (§intro).
  - [Sutton] Sutton calls himself a "classicist" and evokes Turing's "child machine", learning through experience by interacting with the world, with no pretraining on web pages and no supervised finetuning, which Sutton points out is absent in animals (§intro).
  - [Sutton] Even treating pretraining as a prior before RL finetuning, Sutton sees the approach as tainted with human bias and off course, comparable, in Karpathy's paraphrase, to AlphaZero (no human games) beating AlphaGo (initialized from them) (§intro).
  - [Sutton] In Sutton's world view there is only RL interaction with a world, with rewards partly environment-specific and partly intrinsic (fun, curiosity, prediction quality in a world model), and the agent always learning at test time (§intro).
  - [Sutton] Sutton is more interested in what humans share with animals than what differentiates them (§intro).
  - He calls Sutton a great guest and likes that the field keeps entropy of thought, since AI has gone through too many discrete transitions of dominant approach to lose that (§intro).
  - He calls the pod solid "real talk" for frontier researchers who may be gear-shifted too much into exploit mode, and says there is a very good chance of more powerful paradigms than exhaustive benchbuilding and benchmaxxing (§intro).

### claim: frontier-llms-are-not-platonically-bitter-lesson-pilled
- existing: no
- title: He agrees with Sutton that frontier LLMs are not platonically bitter-lesson pilled, though perhaps practically so
- confidence: stated
- stated_on: 2025-10-01
- quote: "They are not platonically bitter lesson pilled" (§intro)
- statements:
  - He thinks Sutton's criticism of LLMs as not bitter-lesson pilled "is not inadequate": pretraining data is all human text, finetuning data is human and curated, and the RL environment mixture is tuned by human engineers (§intro).
  - We do not have a single clean, bitter-lesson-pilled "turn the crank" algorithm that learns from experience alone; finding one would be a huge breakthrough (§intro).
  - He still thinks the bitter lesson is correct, but more as something platonic to pursue than necessarily reach in practice, and says this with double-digit percent uncertainty (§intro).
  - LLMs are perhaps "practically" bitter-lesson pilled compared with much of what came before (§intro).
  - Probably we are still not sufficiently bitter-lesson pilled, he concludes (§intro).
- relation to existing claims:
  - [[scaling-offers-a-guaranteed-path-to-better-models]] (2023-11-23): **none, Note only.** The 2023 claim says a bigger model on more text improves next-word accuracy with high confidence and algorithmic progress is a bonus ([[youtube-2023-11-23-intro-to-llms]] @26:02, @27:10). Here he reports the scaling-law argument as the researchers' assumption and says more powerful paradigms are likely (§intro), but he does not say scaling stops working; the finite-data question is Sutton's (§intro). Both can hold, and the 2025 text neither builds on nor gives evidence for the 2023 one, so `extends` would overstate it. A reviewer could argue `extends` (a caveat added later); I recommend a **Note:** on [[scaling-laws]] instead.
  - [[with-enough-data-encode-less-inductive-bias]] (2023-05-19): **none, Note only.** That claim is about hand-coded inductive biases hurting with enough data ([[talk-2023-05-19-stanford-cs25-transformers]] @1:06:28); here the "humanness" he concedes is in data and engineering choices, and the bitter lesson's content is given only as "benefits from added computation for free" (§intro). Related in spirit, but neither text says one supports the other.

### claim: animal-brains-are-not-a-blank-slate
- existing: no
- title: He doubts animals learn from scratch: much of their "learning" is maturation or finetuning on an evolved initialization
- confidence: stated
- stated_on: 2025-10-01
- quote: "Animal brains are nowhere near the blank slate they appear to be at birth." (§intro)
- statements:
  - Two "example proofs" are commonly offered that a learn-from-experience algorithm exists, AlphaZero and animals; he doubts both transfer (§intro).
  - Go is such a simple, closed environment that the analogous formulation in messy reality is hard to see; he loves Go but calls it essentially a harder tic tac toe (§intro).
  - Animals arise by a very different computational process, under constraints the industry does not have (§intro).
  - Much of what is called "learning" is in his view "maturation", and what clearly is learning is more "finetuning" on something powerful and preexisting (§intro).
  - His example: a baby zebra runs and follows its mother within a few dozen minutes of birth, which he says cannot be learned tabula rasa; animal brains have a powerful initialization encoded in DNA, trained by evolution's "outer loop" (§intro). A zebra spasming at random, as an RL policy at initialization would, would not get far (§intro).
- relation to existing claims: none. **Note:** the "outer loop" wording echoes the outer/inner-loop distinction on [[prompting-llms]] ([[talk-2023-05-19-stanford-cs25-transformers]] @56:34), but the uses differ (evolution vs gradient descent); do not link as evidence.

### claim: pretraining-is-our-crappy-evolution
- existing: no
- title: Pretraining is our crappy evolution, one candidate solution to the cold-start problem
- confidence: stated
- stated_on: 2025-10-01
- quote: "Pretraining is our crappy evolution." (§intro)
- statements:
  - Our AIs also have billions of parameters, which need their own rich, high-information-density supervision signal; we will not re-run evolution, but we have mountains of internet documents (§intro).
  - He grants that this is basically supervised learning, which is ~absent in animals, but says it practically gathers enough soft constraints over billions of parameters to avoid starting from scratch (§intro).
  - Pretraining is one candidate solution to the cold-start problem, followed by finetuning on tasks that look more correct, for example within RL, as he says frontier labs now do pervasively (§intro).
- relation to existing claims:
  - [[pretraining-is-lossy-compression-of-the-internet]] (2023-11-23): **extends.** The 2023 claim says what pretraining produces: a lossy compression of internet text into the parameters, where predicting the next word forces the network to learn about the world ([[youtube-2023-11-23-intro-to-llms]] @05:30, @07:43). The 2025 claim keeps that picture, calling LLMs "a kind of statistical distillation of humanity's documents" (§intro), and adds what pretraining is for: an initialization, in the role evolution plays for animals, before RL (§intro). Neither denies the other. If merge prefers the weakest link, `supports` is defensible only for the "distillation" sentence; `extends` fits the claim as a whole. Timeline: needs a `wiki/timeline/` page if `extends` is set (e.g. `pretraining-over-time`).
  - [[pretraining-gives-a-document-completer]] (2023-01-17): **none, Note only.** Both say pretraining alone is not the end product ([[youtube-2023-01-17-gpt-from-scratch]] @1:51:29), but the 2025 text is about initialization for RL, not about assistant behaviour.
  - Sequoia, 2024-03-26 (on [[llm-self-improvement]], a topic page, not a claim): he called imitation "a good initializer" for something agent-like ([[talk-2024-03-26-sequoia-making-ai-accessible]] @26:04, @26:39). The 2025 claim is the same idea with evolution as the analogy. Topic-level, so a **Note:** on [[llm-self-improvement]], no claim link.

### claim: llm-research-summons-ghosts-not-animals
- existing: no as a claim; the idea is on topic [[jagged-intelligence]] (alias "ghosts vs animals"), from [[blog-2025-12-19-year-in-review-2025]] §2. Merge may fold this into that topic instead of creating a claim.
- title: Today's frontier LLM research is not about building animals but summoning ghosts
- confidence: stated
- stated_on: 2025-10-01
- quote: "It is about summoning ghosts." (§intro)
- statements:
  - Ghosts are a fundamentally different kind of point in the space of possible intelligences, muddled by humanity and thoroughly engineered by it (§intro).
  - They are imperfect replicas, a statistical distillation of humanity's documents with some sprinkle on top (§intro).
  - It seems possible to him that we can finetune ghosts more and more toward animals, a matter of initialization rather than fundamental incompatibility; it is also quite possible they diverge further and stay un-animal-like but still very helpful and world-altering (§intro).
  - He offers the analogy ghosts:animals :: planes:birds as a possibility (§intro).
  - He still thinks it worth being inspired by animals: LLM agents are algorithmically missing multiple powerful ideas that could be adapted from animal intelligence (§intro).
  - On ghosts being scary: not necessarily, citing Casper, his childhood favourite (§Appendix).
- relation to existing pages:
  - No claim page covers ghosts vs animals. The year-in-review text on [[jagged-intelligence]] (2025-12-19) says "summoning ghosts" not growing animals, every part of the stack differs from biology, and the entities are inappropriate to think about through an animal lens ([[blog-2025-12-19-year-in-review-2025]] §2; raw §2 links this blog post). **Not a contradiction:** the October text leaves open that ghosts may be finetuned toward animals and says animals are a source of algorithmic inspiration (§intro); the December text is about understanding the shape of current LLMs. Both can hold. If merge makes this a claim, the topic gets a sentence and a **Note:**, and no `extends`/`contradicts` is needed (there is no earlier claim page). Do not write an order between the two dates.

### claim: animals-do-not-do-supervised-learning
- existing: no
- title: He agrees with Sutton that animals do not do supervised learning
- confidence: stated
- stated_on: 2025-10-01
- quote: "I agree with Sutton that animals don't do supervised learning." (§Appendix)
- statements:
  - [Sutton] Sutton points out that supervised finetuning is absent in the animal kingdom; Karpathy calls it a subtle point and says Sutton is right in the strong sense: animals observe demonstrations, but their actions are not forced or "teleoperated" by other animals (§intro).
  - The closest case he can think of is holding a child's hand to show a spoon motion, and even then it may be observation rather than training; such cases are very rare, while for LLMs it is the default mode in pretraining and SFT (§Appendix).
  - The LLM analogue of what humans do, he suggests, is: given a math problem and a human example solution in context, solve it, reward 1 if correct; "It's not SFT, it's RL." (§Appendix)
- relation to existing claims:
  - [[rlhf-works-better-because-comparing-is-easier-than-generating]] (2023-05-25): none. That claim is about why RLHF beats SFT in human preference ([[talk-2023-05-25-state-of-gpt]] @17:16); this one is about animals. No link.
  - [[llms-want-to-imitate-not-succeed]] (2023-05-25): none; about prompting, not training. **Note:** possible.
  - Topic-level: his Sequoia remark that imitation learning is "super silly" ([[talk-2024-03-26-sequoia-making-ai-accessible]] @27:13) sits with this on [[llm-self-improvement]]; a **Note:**, not a claim link.

### topic: pretraining-and-finetuning
- existing: yes
- statements:
  - Frontier LLMs have human input at every stage: pretraining data is all human text, finetuning data is human and curated, the RL environment mixture is tuned by engineers (§intro).
  - He casts pretraining as a practical way to gather soft constraints over billions of parameters, a candidate answer to cold start, followed by RL finetuning that frontier labs now do pervasively (§intro).
  - [Sutton] Sutton rejects even pretraining-as-prior followed by RL as tainted by human bias (§intro).
  - Supervised learning with actions is the default mode for LLMs in pretraining and SFT, and nearly absent in animals (§Appendix).

### topic: jagged-intelligence
- existing: yes (alias "ghosts vs animals")
- statements: the ghost statements under [[llm-research-summons-ghosts-not-animals]] above (§intro), whichever way merge places them. `first_seen` stays 2025-06-19; `last_updated` stays 2025-12-19.

### topic: llm-self-improvement
- existing: yes
- statements:
  - [Sutton] AlphaZero, never shown human games, beating AlphaGo, initialized from them, is the comparison he uses for Sutton's view that a human-data prior is off course (§intro). **Note:** the topic's 2023 account has AlphaGo's two stages, imitation then self-play ([[youtube-2023-11-23-intro-to-llms]] @38:14); this is the next step in the same analogy, from Sutton's side.
  - He names ideas LLM agents might adapt from animals: intrinsic motivation, fun, curiosity, empowerment, multi-agent self-play, culture (§intro).
  - On very long-horizon sparse rewards, raised by Dwarkesh (e.g. building a startup), Sutton offered temporal-difference learning and future-reward discounting, which Karpathy does not find particularly compelling; he thinks something else is going on and that it is not reinforcement learning (§Appendix).
  - He says there was a lot of discussion of "gradient descent will not make you generalize well" that he did not follow (§Appendix). [mention only; nothing to extract]

### topic: prompting-llms
- existing: yes (alias "in-context learning")
- statements:
  - Dwarkesh briefly argued that LLMs do learn continually at test time, not in the weights; Karpathy thinks Sutton did not fully react to it (§Appendix). [the point is Dwarkesh's; his own view follows]
  - He calls in-context learning a form of test-time adaptation and the reason few-shot prompting works (§Appendix).
- relation: supports the CS25 statement on the same page that the Transformer learns in its activations, unlike finetuning ([[talk-2023-05-19-stanford-cs25-transformers]] @56:34). Topic-level; a **Note:** or a plain sentence.

### topic: llm-knowledge-bases
- existing: yes
- statements:
  - He says a lot of recent work is interested in memory, "think CLAUDE.md files", as test-time learning with text and context as the substrate instead of weights (§Appendix).
- note: also connects to the "anterograde amnesia" sentence on [[jagged-intelligence]] ([[youtube-2025-06-19-software-is-changing]] @16:38); a **Note:** at most.

### topic: scaling-laws
- existing: yes
- statements:
  - He reports that frontier researchers assume LLMs are highly bitter-lesson pilled because LLM scaling laws go up and to the right with compute on the x-axis (§intro). [the researchers' assumption as he reports it, not his own claim]
  - [Sutton] Sutton's counterpoint, as reported: the data is human and finite (§intro).

### topic: rlvr (context only, optional)
- existing: yes
- He does not use the term RLVR. His math-problem example with "reward of 1 if correct" (§Appendix) and RL finetuning "as state of the art frontier LLM labs now do pervasively" (§intro) are close to it. If used at all, a **Note:** on [[rlvr]] with this source in `context`.

## Quotes
- "Pretraining is our crappy evolution." (§intro)
- "It is about summoning ghosts." (§intro)
- "today's frontier LLM research is not about building animals" (§intro)
- "They are muddled by humanity." (§intro)
- "It's possible that ghosts:animals :: planes:birds." (§intro)
- "Animal brains are nowhere near the blank slate they appear to be at birth." (§intro)
- "a lot of what is commonly attributed to "learning" is imo a lot more "maturation"" (§intro)
- "it is essentially a harder version of tic tac toe" (§intro)
- "his criticism of LLMs as not bitter lesson pilled is not inadequate" (§intro)
- "They are not platonically bitter lesson pilled" (§intro)
- "I still think the bitter lesson is correct" (§intro)
- "Probably we are still not sufficiently bitter lesson pilled" (§intro)
- "I agree with Sutton that animals don't do supervised learning." (§Appendix)
- "It's not SFT, it's RL." (§Appendix)
- "In context learning is a form of test time adaptation" (§Appendix)
- "which I don't find particularly compelling" (§Appendix)

All grep-checked against the raw (one match each).

## Notes for merge
- **Duplicate text.** The X post [[x-2025-10-01-sutton-podcast]] (raw `x/1973435013875314729.md`) is this blog body word for word, minus link markup, minus "Dwarkesh" in the first sentence, and minus the two "Also available as" bullets and the whole Appendix (checked with `diff`). The blog links the tweet. Every `§intro` statement above can cite both sources; `§Appendix` statements are blog-only. Suggest each fed page cite both for shared sentences, e.g. `([[blog-2025-10-01-animals-vs-ghosts]] §intro; [[x-2025-10-01-sutton-podcast]])`.
- **Attribution.** Many sentences report Sutton's position, and one (continual learning at test time) reports Dwarkesh's. These are marked [Sutton] above. "If we understood a squirrel, we'd be almost done" is Sutton's line as he quotes it; do not quote it as his. The AlphaZero vs AlphaGo comparison is his paraphrase of Sutton's view ("a bit like"), not necessarily Sutton's own example.
- **Hedges to keep:** "double digit percent uncertainty" on both "worth being inspired by animals" and "the bitter lesson is correct"; "It seems possibly to me" and "quite possible" for the ghosts-toward-animals and ghosts-diverge outcomes; "Probably" on "not sufficiently bitter lesson pilled".
- "I wrote about this a bit more previously" (§Appendix, on long-horizon rewards) refers to writing not in this file; do not supply its content.
- "his criticism ... is not inadequate" is a double negative; paraphrase as agreement, not strong endorsement.
- He says "It seems possibly to me" (sic).
- The ChatGPT-share bullet says the conversation has the podcast transcript, the bitter-lesson post and this blog; not a source.
- No dates between sources: the year-in-review (2025-12-19) links this post in §2; write dates, not "later".
- Raw blogs `the-space-of-minds.md` and `verifiability.md` sit in `raw/blog/` uningested and may touch the same ideas; not read for this digest.
