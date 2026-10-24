---
type: topic
aliases: [Jagged intelligence, people spirits, ghosts vs animals, Swiss cheese model, Swiss cheese capabilities, sharp edges, 9.11 vs 9.9]
first_seen: 2025-02-05
last_updated: 2025-12-19
sources: ["[[youtube-2025-06-19-software-is-changing]]", "[[blog-2025-12-19-year-in-review-2025]]", "[[youtube-2025-02-05-deep-dive-into-llms]]", "[[blog-2025-04-07-power-to-the-people]]", "[[blog-2025-10-01-animals-vs-ghosts]]", "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
context: ["[[talk-2023-05-25-state-of-gpt]]", "[[youtube-2023-11-23-intro-to-llms]]"]
related: ["[[rlvr]]", "[[llms-as-operating-systems]]"]
---
# Jagged intelligence
His description of LLM capability as superhuman in some areas and surprisingly broken in others, from a system that simulates people rather than being one ([[youtube-2025-06-19-software-is-changing]] @14:24, @16:04).

## What he says
He calls LLMs "people spirits", stochastic simulations of people produced by an autoregressive transformer fitted to internet text ([[youtube-2025-06-19-software-is-changing]] @14:24, @14:58). They have encyclopedic memory, which he compares to the savant in Rain Man ([[youtube-2025-06-19-software-is-changing]] @15:30).

They also have cognitive deficits: they hallucinate, lack self-knowledge, and make mistakes no human would, such as claiming 9.11 is greater than 9.9 ([[youtube-2025-06-19-software-is-changing]] @16:04). They suffer from something like anterograde amnesia, because nothing consolidates into the weights after training ([[youtube-2025-06-19-software-is-changing]] @16:38). They are gullible and open to prompt injection ([[youtube-2025-06-19-software-is-changing]] @17:44).

In December 2025 he frames this as "summoning ghosts" rather than growing animals, since every part of the LLM stack differs from biology ([[blog-2025-12-19-year-in-review-2025]] §2). Capability spikes near verifiable domains because of RLVR, which produces the jagged shape ([[blog-2025-12-19-year-in-review-2025]] §2). He says this left him with a loss of trust in benchmarks, since benchmarks are verifiable environments that labs can train around ([[blog-2025-12-19-year-in-review-2025]] §2).

**The Swiss cheese model (Deep Dive, 2025-02-05).** In the Deep Dive lecture he describes LLM capabilities with what he calls the Swiss cheese model: incredibly good across many disciplines but failing almost at random in some unique cases, each failure a hole in the cheese, and there are many ([[youtube-2025-02-05-deep-dive-into-llms]] @3:08:39, @3:09:14). He speaks of jagged edges and jagged issues there, but uses the term Swiss cheese for the model, not jagged intelligence ([[youtube-2025-02-05-deep-dive-into-llms]] @2:04:57, @2:07:12, @3:08:39). His example is that models answer Olympiad-grade and PhD-grade questions yet sometimes say 9.11 is bigger than 9.9, not reproducibly ([[youtube-2025-02-05-deep-dive-into-llms]] @2:05:30, @2:06:03). The explanation he gives is not his own: a team that studied the activations told him, and he says he has not read the paper, that neurons associated with Bible verses light up, as if 9.11 were a verse marker that would come after 9.9; he calls it not fully understood ([[youtube-2025-02-05-deep-dive-into-llms]] @2:06:03, @2:06:37). The holes he lists in his recap are too few tokens to think, broken mental arithmetic, letter counting and the 9.11 comparison ([[youtube-2025-02-05-deep-dive-into-llms]] @3:25:55, @3:26:26). His conclusion is to use the models as tools and check their work; see [[use-llms-as-tools-and-check-their-work]] ([[youtube-2025-02-05-deep-dive-into-llms]] @3:09:14). He also notes that a deployed model does not learn at test time, unlike people, who update their parameters, for instance during sleep ([[youtube-2025-02-05-deep-dive-into-llms]] @3:13:05, @3:13:39).

**Versatile but shallow (Power to the people, 2025-04-07).** In the April 2025 essay he describes LLMs' capability profile as merely quasi-expert knowledge and performance, but across a very wide variety of domains at once: "they are simultaneously versatile but also shallow and fallible." ([[blog-2025-04-07-power-to-the-people]] §intro ¶3). He uses this profile to explain why individuals gain more from LLMs than organisations do; see [[technology-diffusion]] ([[blog-2025-04-07-power-to-the-people]] §intro ¶3, ¶4). He does not use the words "jagged" or "people spirits" in the essay ([[blog-2025-04-07-power-to-the-people]] §intro ¶3).

**Ghosts, not animals (Animals vs Ghosts, 2025-10-01).** In his response to Richard Sutton he writes that today's frontier LLM research is not about building animals but about summoning ghosts: entities muddled and engineered by humanity, imperfect replicas that are a statistical distillation of humanity's documents ([[blog-2025-10-01-animals-vs-ghosts]] §intro). He thinks they may be finetuned toward animals or may diverge and stay un-animal-like while still world-altering, and offers planes and birds as a possible analogy; see [[llm-research-summons-ghosts-not-animals]] ([[blog-2025-10-01-animals-vs-ghosts]] §intro). **Note:** the October post keeps open a move toward animals and treats animals as a source of ideas, while the December review says an animal lens is inappropriate for understanding current LLMs; the two are given with their dates, not as a contradiction ([[blog-2025-10-01-animals-vs-ghosts]] §intro; [[blog-2025-12-19-year-in-review-2025]] §2).

**Savant kids without continual learning (Dwarkesh, published 2025-10-17).** He says the models, booted with zero tokens, always restart from scratch; he thinks humans distil the day's context into the weights during sleep, and LLMs have no equivalent phase ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @22:30, @23:09). He imagines something like a per-person neural net, perhaps a LoRA changing a sparse subset of weights, and points to DeepSeek v3.2's sparse attention as an early hint for long context ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @23:47, @24:27). Claude Code and Codex still feel to him like an elementary-grade student: savant kids with perfect memory who can convincingly create slop but don't really know what they are doing ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:42:26, @1:43:07). He also uses the ghosts framing in this interview, recorded on [[llm-research-summons-ghosts-not-animals]] ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @08:49).

**Note:** in May 2023, without the words "jagged" or "people spirits", he described the same mix: LLMs have vast fact-based knowledge and a perfect working memory in the context window, but do not know what they don't know and do not reflect, sanity-check or correct their mistakes ([[talk-2023-05-25-state-of-gpt]] @22:45, @23:22, @23:55). The prompting he recommends around those deficits is on [[prompting-llms]] ([[talk-2023-05-25-state-of-gpt]] @23:55).

**Note:** in November 2023, again without the word "jagged", he gave the reversal curse as an example of how strange and imperfect the knowledge in an LLM is: GPT-4 knows Tom Cruise's mother but not, asked the other way, her son, knowledge accessible from one direction only ([[youtube-2023-11-23-intro-to-llms]] @12:43). The same talk explains prompt injection, the gullibility he lists in 2025, as hijacking the model with what look like new instructions; the attacks are on [[llm-security]] ([[youtube-2023-11-23-intro-to-llms]] @51:27, @51:59).

## Claims
- [[use-llms-as-tools-and-check-their-work]] — the holes are why he checks the work
- [[longer-context-windows-alone-will-not-scale-to-long-multimodal-tasks]] — no learning at test time
- [[llm-research-summons-ghosts-not-animals]] — ghosts, not animals

## Related
- [[rlvr]] — the training stage that makes the spikes
- [[bitter-lesson]] — the Sutton exchange the ghosts framing answers
- [[llms-as-operating-systems]]
- [[llm-knowledge-bases]] — one way to work around the missing long-term memory
- [[technology-diffusion]] — the shallow, fallible profile is his first reason organisations gain less
