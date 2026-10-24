---
type: topic
aliases: [Jagged intelligence, people spirits, ghosts vs animals, Swiss cheese model, Swiss cheese capabilities, sharp edges, 9.11 vs 9.9]
first_seen: 2025-02-05
last_updated: 2025-12-19
sources: ["[[youtube-2025-06-19-software-is-changing]]", "[[blog-2025-12-19-year-in-review-2025]]", "[[youtube-2025-02-05-deep-dive-into-llms]]"]
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

**Note:** in May 2023, without the words "jagged" or "people spirits", he described the same mix: LLMs have vast fact-based knowledge and a perfect working memory in the context window, but do not know what they don't know and do not reflect, sanity-check or correct their mistakes ([[talk-2023-05-25-state-of-gpt]] @22:45, @23:22, @23:55). The prompting he recommends around those deficits is on [[prompting-llms]] ([[talk-2023-05-25-state-of-gpt]] @23:55).

**Note:** in November 2023, again without the word "jagged", he gave the reversal curse as an example of how strange and imperfect the knowledge in an LLM is: GPT-4 knows Tom Cruise's mother but not, asked the other way, her son, knowledge accessible from one direction only ([[youtube-2023-11-23-intro-to-llms]] @12:43). The same talk explains prompt injection, the gullibility he lists in 2025, as hijacking the model with what look like new instructions; the attacks are on [[llm-security]] ([[youtube-2023-11-23-intro-to-llms]] @51:27, @51:59).

## Claims
- [[use-llms-as-tools-and-check-their-work]] — the holes are why he checks the work
- [[longer-context-windows-alone-will-not-scale-to-long-multimodal-tasks]] — no learning at test time

## Related
- [[rlvr]] — the training stage that makes the spikes
- [[llms-as-operating-systems]]
- [[llm-knowledge-bases]] — one way to work around the missing long-term memory
