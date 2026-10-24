---
type: topic
aliases: [Jagged intelligence, people spirits, ghosts vs animals]
first_seen: 2025-06-19
last_updated: 2025-12-19
sources: ["[[youtube-2025-06-19-software-is-changing]]", "[[blog-2025-12-19-year-in-review-2025]]"]
context: ["[[talk-2023-05-25-state-of-gpt]]", "[[youtube-2023-11-23-intro-to-llms]]"]
related: ["[[rlvr]]", "[[llms-as-operating-systems]]"]
---
# Jagged intelligence
His description of LLM capability as superhuman in some areas and surprisingly broken in others, from a system that simulates people rather than being one ([[youtube-2025-06-19-software-is-changing]] @14:24, @16:04).

## What he says
He calls LLMs "people spirits", stochastic simulations of people produced by an autoregressive transformer fitted to internet text ([[youtube-2025-06-19-software-is-changing]] @14:24, @14:58). They have encyclopedic memory, which he compares to the savant in Rain Man ([[youtube-2025-06-19-software-is-changing]] @15:30).

They also have cognitive deficits: they hallucinate, lack self-knowledge, and make mistakes no human would, such as claiming 9.11 is greater than 9.9 ([[youtube-2025-06-19-software-is-changing]] @16:04). They suffer from something like anterograde amnesia, because nothing consolidates into the weights after training ([[youtube-2025-06-19-software-is-changing]] @16:38). They are gullible and open to prompt injection ([[youtube-2025-06-19-software-is-changing]] @17:44).

In December 2025 he frames this as "summoning ghosts" rather than growing animals, since every part of the LLM stack differs from biology ([[blog-2025-12-19-year-in-review-2025]] §2). Capability spikes near verifiable domains because of RLVR, which produces the jagged shape ([[blog-2025-12-19-year-in-review-2025]] §2). He says this left him with a loss of trust in benchmarks, since benchmarks are verifiable environments that labs can train around ([[blog-2025-12-19-year-in-review-2025]] §2).

**Note:** in May 2023, without the words "jagged" or "people spirits", he described the same mix: LLMs have vast fact-based knowledge and a perfect working memory in the context window, but do not know what they don't know and do not reflect, sanity-check or correct their mistakes ([[talk-2023-05-25-state-of-gpt]] @22:45, @23:22, @23:55). The prompting he recommends around those deficits is on [[prompting-llms]] ([[talk-2023-05-25-state-of-gpt]] @23:55).

**Note:** in November 2023, again without the word "jagged", he gave the reversal curse as an example of how strange and imperfect the knowledge in an LLM is: GPT-4 knows Tom Cruise's mother but not, asked the other way, her son, knowledge accessible from one direction only ([[youtube-2023-11-23-intro-to-llms]] @12:43). The same talk explains prompt injection, the gullibility he lists in 2025, as hijacking the model with what look like new instructions; the attacks are on [[llm-security]] ([[youtube-2023-11-23-intro-to-llms]] @51:27, @51:59).

## Related
- [[rlvr]] — the training stage that makes the spikes
- [[llms-as-operating-systems]]
- [[llm-knowledge-bases]] — one way to work around the missing long-term memory
