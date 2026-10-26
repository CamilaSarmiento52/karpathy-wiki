---
type: topic
aliases: [Agentic engineering, agent-assisted engineering, agentic engineer]
first_seen: 2026-04-29
last_updated: 2026-04-29
sources: ["[[talk-2026-04-29-sequoia-ascent-2026]]"]
context: ["[[youtube-2025-06-19-software-is-changing]]"]
related: ["[[vibe-coding]]", "[[ai-assisted-coding-loop]]", "[[vibe-coding-over-time]]"]
---
# Agentic engineering
The discipline, as he defines it at Sequoia Ascent, of coordinating fallible, stochastic but extremely powerful coding agents to go faster while keeping the quality bar of professional software; the host said "agentic engineering" first in her question, and he adopted the term and defined it ([[talk-2026-04-29-sequoia-ascent-2026]] @15:49, @16:22).

## What he says
Asked how vibe coding differs from what the host called agentic engineering, he says vibe coding is about raising the floor for everyone in what they can do in software, and agentic engineering is about preserving the quality bar of professional software: you may not introduce vulnerabilities through vibe coding and "you're still responsible for your software just as before", and the question is whether you can go faster; "spoiler is you can" ([[talk-2026-04-29-sequoia-ascent-2026]] @15:49, @16:22). He calls it that because he thinks it is an engineering discipline: agents are spiky entities, a bit fallible and a little stochastic but extremely powerful, and the work is coordinating them to go faster without sacrificing the quality bar; see [[agentic-engineering-keeps-the-quality-bar-while-going-faster]] ([[talk-2026-04-29-sequoia-ascent-2026]] @16:22).

He sees the two as different, one raising the floor and the other "extrapolating", and sees a very high ceiling on agentic-engineer capability: the old 10x engineer is magnified a lot, and people very good at this peak at a lot more than 10x, "from my perspective right now" ([[talk-2026-04-29-sequoia-ascent-2026]] @16:22, @16:55). Asked what separates an AI-native coder from a mediocre one, he says getting the most out of the available tools, using their features and investing in your own setup, as engineers always did with Vim or VS Code ([[talk-2026-04-29-sequoia-ascent-2026]] @17:28, @18:01). Most hiring processes, he says, have not been refactored for this; see [[hiring-should-test-building-a-big-project-with-agents]] ([[talk-2026-04-29-sequoia-ascent-2026]] @18:34).

**What the human still owns.** He says you still have to be in charge of the aesthetics, the judgment, the taste and a little oversight ([[talk-2026-04-29-sequoia-ascent-2026]] @19:38). His example: for MenuGen his agent matched Stripe purchases to Google sign-ups by email address, though the two can differ, so funds would not be associated; there was no persistent user ID, the kind of mistake he says agents still make ([[talk-2026-04-29-sequoia-ascent-2026]] @19:38, @20:10). People have to be in charge of the spec and plan; he says he does not even like plan mode, though it is obviously useful, and prefers working with the agent to design a very detailed spec, maybe basically the docs, then getting the agents to write them ([[talk-2026-04-29-sequoia-ascent-2026]] @20:10, @20:44). You are in charge of oversight and the top-level categories while agents do a lot under the hood ([[talk-2026-04-29-sequoia-ascent-2026]] @20:44). He has forgotten tensor API details such as keepdims versus keepdim or dim versus axis, which are "handled by the intern because they have very good recall", but you still need fundamentals such as views versus separate storage so as not to copy memory unnecessarily ([[talk-2026-04-29-sequoia-ascent-2026]] @21:16). You own the taste, the engineering and the design, such as insisting on unique user IDs, and the agents fill in the blanks: "that's currently kind of like where we are" ([[talk-2026-04-29-sequoia-ascent-2026]] @21:51).

**Taste and code quality.** He hopes taste improves in the models, and thinks it probably does not now because it is not part of the RL, with probably no aesthetics reward ([[talk-2026-04-29-sequoia-ascent-2026]] @22:25). Looking at agent code sometimes gives him "a little bit of a heart attack": bloated, lots of copy-paste, brittle awkward abstractions, working but really gross ([[talk-2026-04-29-sequoia-ascent-2026]] @22:25). Prompting an LLM to simplify microGPT further failed, which felt like being outside the RL circuits; he sees nothing fundamental preventing it, "the labs haven't done it yet almost" ([[talk-2026-04-29-sequoia-ascent-2026]] @22:58). **Note:** this is close to [[coding-models-are-weak-at-code-never-written-before]], which this source is not added to ([[talk-2026-04-29-sequoia-ascent-2026]] @22:58).

**Note:** in the YC talk, published 2025-06-19, he already separated vibe coding from how he works "if I'm actually trying to get work done": small incremental chunks, keeping the AI on the leash and checking for bugs and security issues, the steps on [[ai-assisted-coding-loop]] ([[youtube-2025-06-19-software-is-changing]] @23:16, @23:48). He did not use the term agentic engineering there; at Sequoia he names and defines the discipline and adds that you can go faster without lowering the bar ([[talk-2026-04-29-sequoia-ascent-2026]] @16:22).

## Claims
- [[agentic-engineering-keeps-the-quality-bar-while-going-faster]] — vibe coding raises the floor; agentic engineering keeps the bar (2026-04-29)
- [[hiring-should-test-building-a-big-project-with-agents]] — not puzzles (2026-04-29)
- [[understanding-cannot-be-outsourced]] — he becomes the bottleneck in directing agents (2026-04-29)
- [[he-now-delegates-most-coding-to-agents]] — since December

## Related
- [[vibe-coding]] — what agentic engineering is set against
- [[ai-assisted-coding-loop]] — his earlier small-diff practice
- [[vibe-coding-over-time]]
- [[claws]]
