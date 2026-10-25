# Digest: Andrej Karpathy: From Vibe Coding to Agentic Engineering w/ Stephanie Zhan
- raw: raw/talks/96jN2OCOfLs.md · published: 2026-04-29 · medium: talk · words: 6346 (wc, incl. host; 29:49)
- source slug: talk-2026-04-29-sequoia-ascent-2026

## Source page

```
---
type: source
raw_path: raw/talks/96jN2OCOfLs.md
published: 2026-04-29
medium: talk
summary: "Sequoia Ascent fireside chat with Stephanie Zhan: the December step change in coding agents, Software 3.0 and apps that should not exist, neural computers, verifiability and jaggedness, vibe coding versus agentic engineering, hiring, taste, ghosts, agent-native infrastructure, and why understanding cannot be outsourced."
url: https://www.youtube.com/watch?v=96jN2OCOfLs
title: "Andrej Karpathy: From Vibe Coding to Agentic Engineering w/ Stephanie Zhan"
---
# Andrej Karpathy: From Vibe Coding to Agentic Engineering w/ Stephanie Zhan
Raw: [[raw/talks/96jN2OCOfLs]] · Original: https://www.youtube.com/watch?v=96jN2OCOfLs

## Summary
A half-hour fireside chat at Sequoia Ascent in which Stephanie Zhan asks the questions. He
says that in December the chunks of code his agents produced started coming out fine, he
trusted them more and more and has been coding side projects all the time since (@01:08,
@01:39, @02:11). He restates Software 3.0 as prompting, with the context window as the lever
over an LLM interpreter, and gives an agent-pasted installer and a one-prompt Gemini version
of MenuGen as examples, the second of which makes his own app "spurious" (@03:18, @03:50,
@05:59); he extrapolates to neural nets as the host process with CPUs as coprocessors
(@08:40). He explains jaggedness as verifiability plus what the labs care about, with a
car-wash question and chess data as examples (@09:47, @11:24, @12:00, @12:32). He separates
vibe coding, which raises the floor, from agentic engineering, which keeps professional
software's quality bar while going faster, and says hiring, spec-writing and human taste have
to follow (@15:49, @16:22, @18:34, @19:38, @21:51). He closes on agent-native infrastructure
and a tweet he endorses, that thinking can be outsourced but understanding cannot (@25:41,
@26:47, @27:55).

## Key points
- December was a stark transition: agent output came out fine, he trusted it and kept asking for more → [[coding-agents-became-reliable-for-him-in-december]], [[vibe-coding]], [[llm-agents-over-time]]
- Software 3.0: prompting, the context window as lever over the LLM interpreter; the installer as text for your agent → [[software-3-0]], [[english-is-the-new-programming-language]]
- The Software 3.0 MenuGen is one prompt to Gemini; his app "shouldn't exist"; LLM wikis are information processing no code could do → [[in-software-3-0-some-apps-should-not-exist]], [[software-3-0]], [[llm-knowledge-bases]]
- Neural computers: the neural net may become the host process and CPUs coprocessors → [[neural-nets-may-become-the-host-process]], [[llms-as-operating-systems]], [[llm-os-over-time]]
- Traditional computers automate what you can specify, LLMs what you can verify; jaggedness is verifiable plus labs care → [[llms-automate-what-you-can-verify]], [[jagged-intelligence]], [[rlvr]]
- Treat jagged models as tools and stay in the loop → [[use-llms-as-tools-and-check-their-work]]
- Vibe coding raises the floor; agentic engineering keeps the quality bar and goes faster, with a ceiling far above 10x → [[agentic-engineering]], [[agentic-engineering-keeps-the-quality-bar-while-going-faster]], [[vibe-coding-over-time]]
- Hire by having candidates build and harden a big project with agents → [[hiring-should-test-building-a-big-project-with-agents]]
- Humans own taste, the spec and identity design; agents handle API recall; models still write bloated code and cannot simplify microGPT → [[ai-assisted-coding-loop]], [[coding-models-are-weak-at-code-never-written-before]]
- The MenuGen Stripe-email bug as an agent mistake → [[agentic-engineering]], [[vibe-coding]]
- Ghosts not animals: a little philosophizing; be suspicious and learn empirically → [[llm-research-summons-ghosts-not-animals]], [[jagged-intelligence]]
- Docs written for humans are his pet peeve; sensors and actuators; build-MenuGen-and-deploy as a test; agents representing people → [[building-for-agents]], [[deploying-a-vibe-coded-app-is-harder-than-writing-it]]
- You can outsource thinking, not understanding; knowledge bases as tools for understanding → [[understanding-cannot-be-outsourced]], [[llm-knowledge-bases]], [[ai-for-education]]

## Fed pages
- [[vibe-coding]]
- [[agentic-engineering]]
- [[software-3-0]]
- [[llms-as-operating-systems]]
- [[jagged-intelligence]]
- [[rlvr]]
- [[building-for-agents]]
- [[llm-knowledge-bases]]
- [[ai-for-education]]
- [[ai-assisted-coding-loop]]
- [[coding-agents-became-reliable-for-him-in-december]]
- [[agentic-engineering-keeps-the-quality-bar-while-going-faster]]
- [[in-software-3-0-some-apps-should-not-exist]]
- [[neural-nets-may-become-the-host-process]]
- [[llms-automate-what-you-can-verify]]
- [[hiring-should-test-building-a-big-project-with-agents]]
- [[understanding-cannot-be-outsourced]]
- [[coding-models-are-weak-at-code-never-written-before]]
- [[deploying-a-vibe-coded-app-is-harder-than-writing-it]]
- [[llm-research-summons-ghosts-not-animals]]
- [[use-llms-as-tools-and-check-their-work]]
- [[english-is-the-new-programming-language]]
- [[vibe-coding-over-time]]
- [[llm-agents-over-time]]
- [[llm-os-over-time]]
```

## Candidates

### topic: agentic-engineering
- existing: no (no slug or alias in `wiki/index/`; grep for "agentic engineering" in wiki/ finds nothing)
- aliases: Agentic engineering, agentic engineer, agent engineering
- statements:
  - Asked the difference between vibe coding and what Zhan calls "more agentic engineering", he says vibe coding raises the floor for everyone in what they can do in software, and agentic engineering is about preserving the quality bar of professional software (@15:49).
  - Under agentic engineering you may not introduce vulnerabilities through vibe coding and are still responsible for your software as before; the question is whether you can go faster, and he says you can (@15:49, @16:22).
  - He calls it that because he thinks it is an engineering discipline: coordinating agents, which are spiky, a bit fallible, a little stochastic but extremely powerful, to go faster without sacrificing the quality bar (@16:22).
  - He sees the two as different: one raises the floor, the other is about "extrapolating" (the ceiling, by context), and he sees a very high ceiling on agentic-engineer capability (@16:22, @16:55).
  - The old 10x engineer is magnified a lot; people very good at this peak a lot more than 10x, from his perspective right now (@16:55).
  - The AI-native coder gets the most out of the tools, uses their features and invests in their own setup, as engineers always did with Vim or VS Code (@17:28, @18:01).
  - Humans must stay in charge of aesthetics, judgment, taste and some oversight (@19:38). His example: a MenuGen agent matched Stripe purchases to Google sign-ups by email address, which can differ, so funds would not be associated; there was no persistent user ID (@19:38, @20:10).
  - People have to be in charge of the spec and plan; he does not even like "plan mode", though it is useful, and prefers working with the agent to design a very detailed spec, maybe basically the docs, then having agents write them (@20:10, @20:44).
  - He has forgotten tensor API details (keepdims vs keepdim, dim vs axis, reshape, permute, transpose) because the "intern" with good recall handles them, but you still need the fundamentals, such as storage versus views, so you are not copying memory unnecessarily (@20:44, @21:16).
  - You own taste, engineering and design, for example insisting on unique user IDs, and the agents fill in the blanks; "that's currently kind of like where we are" (@21:51).
- relation to an existing page: new topic; links to [[vibe-coding]], [[ai-assisted-coding-loop]], [[vibe-coding-over-time]]. See the claim below for extends-vs-rename.
- alternative for merge: if a new topic is too fine-grained, make it a section of [[vibe-coding]] (not an alias: he says the two are different, @16:22) with the method steps on [[ai-assisted-coding-loop]]. I recommend the new topic, because he names and defines a discipline distinct from vibe coding.

### claim: agentic-engineering-keeps-the-quality-bar-while-going-faster
- existing: no
- title: "Vibe coding raises the floor; agentic engineering keeps professional software's quality bar while going faster"
- confidence: stated
- quote: "agentic engineering is about preserving the quality bar" (@15:49)
- statements: as in the topic (@15:49, @16:22, @16:55).
- **extends or only renames?** Argued from both texts:
  - *What is a rename.* The YC talk (published 2025-06-19) already split vibe coding from the way he works "when trying to get real work done": small diffs, verify each, keep the AI on the leash ([[ai-assisted-coding-loop]], [[youtube-2025-06-19-software-is-changing]] @23:16, @23:48). Treating agents as fallible and keeping a human responsible for quality is that stance under a new name. Also, the term is first spoken by the host in her question (@15:49); he adopts and defines it ("I call it that because...", @16:22). The blog's AI-written summary presents it as his distinction ("I distinguish two related but different ideas", blog §7); do not write that he coined the term.
  - *What extends.* Three things in the talk are not on any existing page: (1) that you *can* go faster without lowering the quality bar, "spoiler is you can" (@16:22); (2) a ceiling well beyond 10x (@16:55); (3) the human's job recast as owning the spec/docs, top-level categories and identity design while agents fill in the blanks and API recall is offloaded (@20:44, @21:16, @21:51). Earlier sources set vibe coding's scope (weekend projects, not for anything important) but say nothing about a professional discipline with a quality bar that goes faster.
  - *Verdict:* `extends` [[vibe-coding-is-for-throwaway-weekend-projects]] (2025-02-02): the February post bounded vibe coding to low-stakes work; the talk keeps vibe coding as floor-raising ("everyone can vibe code anything, and that's amazing", @15:49) and adds a named professional counterpart, denying nothing. Not `contradicts`.
  - vs [[vibe-coding-will-terraform-software]] (2025-12-19): **no field; a Note.** December says vibe coding empowers trained professionals too (Rust tokenizer, bug-finding apps). The talk reserves the professional quality bar to agentic engineering ("You're not allowed to introduce uh vulnerabilities due to vibe coding", @15:49). Both can hold: professionals can vibe-code throwaway or tested side code while production code needs the quality bar. **Note** (editorial, label it): the December Rust-tokenizer example, done with tests and a reference implementation ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @34:26), looks more like what he now calls agentic engineering; he does not say so.
  - vs [[vibe-coding-full-web-apps-is-not-yet-for-anything-important]] (2025-04-27): `supports`, weakly, or a Note only: the talk's line that vibe coding must not introduce vulnerabilities into professional software is consistent with "not for anything of actual importance"; the April claim is about web apps "today". I'd set a Note, not a field.
  - vs [[deploying-a-vibe-coded-app-is-harder-than-writing-it]]: none; the Stripe email bug (@19:38) is the same incident the MenuGen post reports, now used as an example of agent mistakes; a Note on that page.

### claim: coding-agents-became-reliable-for-him-in-december
- existing: no
- title: "In December, the code chunks his agents produced started coming out fine, and he began trusting them with more"
- confidence: stated
- quote: "I can't remember the last time I corrected it" (@01:08)
- statements:
  - He had used agentic tools for maybe the last year; they were good at chunks of code but sometimes messed up and needed editing (@00:36, @01:08).
  - December was a clear point for him; on a break, he noticed the chunks from the latest models came out fine, kept asking for more, trusted the system more and more, "And then I was vibe coding." (@01:08).
  - He calls it a very stark transition: people who experienced AI as a ChatGPT-adjacent thing had to look again as of December, because the agentic, coherent workflow really started to work (@01:39).
  - Since then his side-projects folder is extremely full and he has been coding all the time (@02:11).
  - Feeling more behind as a programmer (the host's quote of his post) was, he says, a mixture of exhilarating and unsettling (@00:36).
- relation:
  - vs [[autocomplete-is-his-coding-sweet-spot]] (2025-10-17, "For now, autocomplete is my sweet spot."): **not `contradicts`**: the October claim is explicitly "for now" and dated; both are true at their dates. But this is a change in his reported practice (invariant 6 "he changed his mind" case): keep the October claim, link the two in Related claims with a Note, and add a vibe-coding-over-time entry. No `supports`/`extends` field is honestly true; I recommend no field. He does not himself say that autocomplete stopped being his sweet spot; write "he describes trusting agents with more", not "he abandoned autocomplete".
  - vs [[claude-code-is-the-first-convincing-llm-agent]] (2025-12-19): `supports`: the same month in his account; the agents he names in the cleaned transcript are Claude Code and Codex (blog §The December 2025 Agentic Inflection). In the raw talk the name is garbled as "Alpha code" (@00:36); cite the talk only for "agentic tools", not for "Claude Code".
  - vs [[coding-models-are-weak-at-code-never-written-before]]: no conflict; the same talk still says models cannot simplify microGPT and write bloated code (see below).
  - vs [[this-is-the-decade-of-agents]]: **none.** The talk gives no timescale for agents; do not cite it for or against the decade.

### claim: in-software-3-0-some-apps-should-not-exist
- existing: no
- title: "In the Software 3.0 version, an app like MenuGen should not exist"
- confidence: stated
- quote: "all of my menu gen is spurious" (@05:59)
- statements:
  - MenuGen photographs a menu, OCRs the titles, generates an image for each with an image generator and re-renders the menu; it runs on Vercel (@04:54, @05:26).
  - The Software 3.0 version he saw, which blew his mind, gives the photo to Gemini and asks Nano Banana to overlay the dishes; the returned image is his menu with the dishes rendered into the pixels (@05:26).
  - His MenuGen is "working in the old paradigm", that app shouldn't exist; the neural net does more and more of the work, the input and output are images, with no app in between (@05:59).
  - People should not only think of AI as a speed-up of what exists; new things are available now (@05:59, @06:32).
- relation: no existing claim. Topic [[software-3-0]]. **Note** to [[deploying-a-vibe-coded-app-is-harder-than-writing-it]]: the same app that was a slog to deploy is here one he says need not exist (@05:59, @26:47). No field.

### claim: neural-nets-may-become-the-host-process
- existing: no
- title: "He imagines neural nets becoming the host process, with CPUs as coprocessors"
- confidence: stated (he frames it as an extrapolation that "looks very weird" and is "TBD")
- quote: "the neural net becomes kind of like the host process" (@08:40)
- statements:
  - Extrapolating from MenuGen, a lot of code shouldn't exist and neural nets do most of the work; one could imagine completely neural computers, a device taking raw video or audio into a neural net that renders a moment-specific UI with diffusion (@08:07).
  - In the 1950s and 60s it was not obvious whether computers would look like calculators or neural nets; we went the calculator way, and neural nets now run virtualised on classical computers (@08:40).
  - He imagines a flip: the neural net as host process and CPUs as coprocessors, with intelligence compute becoming the dominant spend of flops ("we saw the diagram", a slide not in the transcript) (@08:40).
  - Neural nets would do the heavy lifting and use tools as a historical appendage for deterministic tasks; we will probably get there piece by piece and the progression is TBD (@09:13).
- relation:
  - vs [[llms-are-the-kernel-of-an-emerging-operating-system]] (2023-11-23): `extends`. 2023: the LLM is the kernel process coordinating memory and tools. 2026: the neural net as host process is the same direction, and the talk adds the flip of classical compute into a coprocessor, tools as appendage, and fully neural UIs. Not a rename: kernel-coordinating-tools does not say CPUs become coprocessors. Add a 2026-04-29 entry to [[llm-os-over-time]].
  - **Note** to [[llms-as-operating-systems]]: in 2025 he said the model is like the CPU ([[youtube-2025-06-19-software-is-changing]] @10:01); here CPUs become the coprocessor. Wording, extrapolation, not a stated change.
  - **Note** to [[llm-gui]]: diffusion-rendered UI is related; no field.
  - Do **not** link [[technology-could-be-like-the-calculator]]: "calculator" here means classical deterministic computing, not the self-contained-device ideal.

### claim: llms-automate-what-you-can-verify
- existing: no (the verifiability blog post, raw/blog/verifiability.md, exists but has no wiki page yet; he refers to "writing about verifiability" here, @09:47)
- title: "Traditional computers automate what you can specify; LLMs automate what you can verify"
- confidence: stated
- quote: "some kind of combination of verifiable plus labs care" (@12:00)
- statements:
  - Traditional computers can easily automate what you can specify in code; this round of LLMs can easily automate what you can verify (@09:47).
  - Labs train LLMs in giant RL environments with verification rewards, so models become jagged entities that peak in verifiable domains like math and code and stay rougher outside them (@10:19).
  - Jaggedness also comes from the labs' focus and data distribution: economically valuable settings get more environments, code being an example; other verifiable environments just don't make it into the mix (@10:52).
  - He thinks it is some combination of verifiable plus labs care (@12:00).
  - Verifiability makes something tractable because you can throw a lot of RL at it, even if labs are not focusing on it; with diverse RL environments a founder can fine-tune, technology that "just works" (@14:10, @14:43). He declines to name the domain he has in mind (@14:43).
  - Almost everything can ultimately be made verifiable to some extent, even writing, with a council of LLM judges; it is more about easy or hard (@15:17).
- relation:
  - Topics [[rlvr]], [[jagged-intelligence]]: supports the 2025-12-19 statement that capability spikes near verifiable domains because of RLVR ([[blog-2025-12-19-year-in-review-2025]] §2). No claim page exists for that; statements go on the topics.
  - vs [[llm-judges-are-gameable-rewards]] (2025-10-17): **no field; Note.** There he says RL against an LLM judge gets gamed within 10–20 steps; here a council of judges could get "something reasonable" for writing. Both can hold (reasonable vs robust); flag for a Note.
  - vs [[self-improvement-may-be-possible-in-narrow-domains]] (2023): Note only; RL on verifiable rewards is not self-improvement as that claim states it.
  - When the verifiability raw is ingested, that source should become the primary for this claim; the talk is a spoken restatement.

### claim: hiring-should-test-building-a-big-project-with-agents
- existing: no
- title: "Hiring should test building and securing a big project with agents, not puzzles"
- confidence: stated
- quote: "if you're giving out puzzles to solve, then this is still the old paradigm" (@18:34)
- statements:
  - Most hiring processes have not been refactored for agentic-engineer capability; puzzles are the old paradigm (@18:34).
  - He would give a big project, such as a Twitter clone for agents, made good and secure, with agents simulating activity, then use many top Codex agents to try to break the deployed site, which should hold (@18:34, @19:06).
- relation: none. Topic [[agentic-engineering]].

### claim: understanding-cannot-be-outsourced
- existing: no
- title: "He endorses the line that you can outsource your thinking but not your understanding"
- confidence: stated (as his endorsement; the line is from a tweet by someone else)
- quote: the line itself is the tweet's, so quote his reaction instead, or attribute: "you can outsource your thinking, but you can't outsource your understanding" (@27:55; a tweet he read, author not named)
- statements:
  - A recent tweet blew his mind, roughly that you can outsource your thinking but not your understanding; he finds it nicely put (@27:55).
  - He is still part of the system; information still has to reach his brain, and he feels he is becoming the bottleneck in knowing what to build, why, and how to direct his agents (@27:55, @28:27).
  - Something still has to direct the thinking, and that is constrained by understanding (@28:27).
  - LLMs "certainly don't excel at understanding", so you remain uniquely in charge of it, and tools that enhance understanding excite him (@28:59).
- relation: none set. **Note** to [[ai-assisted-coding-loop]] step 3: in 2025 he said he is still the bottleneck for verifying diffs ([[youtube-2025-06-19-software-is-changing]] @22:43); here the bottleneck is understanding. Topic: [[ai-for-education]] (the answer to the education question) and [[llm-knowledge-bases]].

### topic: vibe-coding (existing)
- statements:
  - In December, trusting the agents more and more, he says "And then I was vibe coding." (@01:08).
  - Vibe coding raises the floor for everyone; everyone can vibe code anything, which he calls amazing (@15:49).
  - Retelling the MenuGen bug: the agent matched Stripe and Google accounts by email, a kind of mistake agents still make (@19:38, @20:10).
- relation: see claims above; timeline entry on [[vibe-coding-over-time]] (2026-04-29: the December step change; the floor/quality-bar split).

### topic: software-3-0 (existing)
- statements:
  - Software 1.0 is writing code; 2.0 is programming by arranging datasets, objectives and architectures and training networks (@02:46). (The "explicit rules / learned weights" phrasing at @02:11 is the host's.)
  - Training on the internet forces models to multitask, so they become a programmable computer in a certain sense (@02:46, @03:18).
  - In Software 3.0 programming turns to prompting, and what is in the context window is the lever over the LLM interpreter performing computation in digital information space (@03:18).
  - The OpenClaw installer is a block of text to give your agent rather than a ballooning shell script; the agent looks at the environment and debugs in the loop; "That's the programming paradigm now." (@03:50, @04:22).
  - It is not only programming getting faster: general information processing over unstructured data is now automatable, e.g. compiling a knowledge base, which no code could do before (@06:32, @07:04). He finds the new possibilities more exciting than the speed-ups (@07:04, @07:35).
- relation: supports [[english-is-the-new-programming-language]] (the copy-paste text as program, @04:22). Restatement of the 2025-06-19 definition, not a change.

### topic: llms-as-operating-systems (existing)
- statements: neural computers and the host-process flip (@08:07, @08:40, @09:13); see claim.
- relation: [[llm-os-over-time]] entry 2026-04-29.

### topic: jagged-intelligence (existing)
- statements:
  - The strawberry letter count was the old example and is patched; the new one: models tell you to walk to a car wash 50 m away to wash your car (@10:52, @11:24).
  - He finds it insane that Opus 4.7 can refactor a 100,000-line codebase or find zero-day vulnerabilities yet tells him to walk (@11:24).
  - Jaggedness means either something is slightly off, or you must stay in the loop, treat them as tools and stay in touch with what they do (@12:00).
  - From GPT-3.5 to GPT-4 chess improved a lot, which he attributes, "I think this is public information, I think I saw it on the internet", to a lot of chess data added to pretraining (@12:00, @12:32). Keep the hedge.
  - We are at the mercy of the labs' mix; the model has no manual; inside the RL circuits you fly, outside the data distribution you struggle and may need fine-tuning (@12:32, @13:04).
  - Models do not improve at taste probably because there is no aesthetics reward in RL (@22:25).
- relation: supports [[use-llms-as-tools-and-check-their-work]] (@12:00 vs Deep Dive @3:09:14).

### topic: rlvr (existing)
- statements: RL environments with verification rewards make capability peak in verifiable domains (@10:19); founders can build their own RL environments and fine-tune (@14:10, @14:43).

### topic: building-for-agents (existing)
- statements:
  - Everything is still written for humans and has to be rewritten; docs for frameworks still tell humans what to do, his favorite pet peeve; he wants to know what to copy-paste to his agent (@25:41).
  - Workloads should be decomposed into sensors and actuators over the world and described to agents first; he keeps a lot of automation around data structures legible to LLMs (@25:41, @26:15). The host says she had not thought of the sensors/actuators analogy (@27:20), which confirms it is his.
  - MenuGen's trouble was deploying on Vercel, stringing services, settings and DNS, not writing the code; a good test of agent-native infrastructure would be prompting "build MenuGen" and having it deployed without touching anything (@26:15, @26:47).
  - He expects agent representation for people and organisations: "my agent talks to your agent" about meeting details (@26:47, @27:20).
- relation: [[deploying-a-vibe-coded-app-is-harder-than-writing-it]] gets the talk as a further source (supports; the same story retold, @26:15, @26:47).

### topic: llm-knowledge-bases (existing)
- statements:
  - Getting LLMs to create wikis for an organisation or a person is not a program in the old sense; no code could create a knowledge base from a bunch of facts, but LLMs can recompile and reorder documents into a new reframing of the data (@06:32, @07:04).
  - He is excited about knowledge bases as a way to process information: every different projection onto information gives him insight; "a lot of prompts for me to do synthetic data generation" over fixed data (@28:27).
  - He has a wiki built up from the articles he reads and loves asking it questions; these are tools to enhance understanding (@28:59).
- relation: extends the topic's 2026-04-02 description with the understanding framing; no claim relation ([[no-rag-needed-for-a-small-wiki]] is not discussed).

### topic: ai-for-education (existing)
- statements: asked what remains worth learning deeply, he answers with the understanding line and knowledge bases (@27:55, @28:27, @28:59). Fine as a short section; merge may prefer only [[llm-knowledge-bases]].

### method: ai-assisted-coding-loop (existing)
- proposed new steps: "Write a detailed spec with the agent, then let it fill in the blanks"; "Own the design decisions such as identity"; "Offload API recall, keep the fundamentals"; "Invest in your own tool setup".
- statements: @17:28/@18:01 (setup), @20:10/@20:44 (spec, plan mode), @20:44/@21:16 (API details vs storage and views), @21:51 (unique user IDs, agents fill in blanks).
- relation: this method page is what "agentic engineering" partly renames (see above).

### claim: coding-models-are-weak-at-code-never-written-before (existing; add talk as source)
- statements:
  - When he looks at agent code he sometimes gets "a little bit of a heart attack": bloated, copy-paste, brittle awkward abstractions; it works but is gross; he hopes future models improve (@22:25).
  - Trying to get an LLM to simplify microGPT further, "The models hate this. They can't do it."; it felt like being outside the RL circuits, like pulling teeth (@22:58).
  - He sees nothing fundamental preventing it; the labs haven't done it yet (@22:58).
- relation: `supports` (same limit: off-distribution, code-style work; October also listed bloat). Add as further source, not a new claim.

### claim: llm-research-summons-ghosts-not-animals (existing; add talk as source)
- statements:
  - He wrote about animals and ghosts to wrap his head around what these things are, since a good model of them makes you more competent at using them (@24:04).
  - He is not sure the framing has real power, "a little bit of philosophizing" (@24:04).
  - They are not animal intelligences: yelling at them changes nothing; they are statistical simulation circuits on a pretraining substrate with RL bolted on (@24:36).
  - It is a mindset of being suspicious of them and figuring things out over time, not five obvious ways to improve a system (@24:36, @25:09).
- relation: `supports` (restatement), with a new hedge on its practical value. The list "intrinsic motivation, fun, curiosity, empowerment" at @23:30 is the **host's** summary; do not attribute it to him.

### claim: use-llms-as-tools-and-check-their-work (existing; add talk as source)
- statement: to the extent models stay jagged, you need to be in the loop, treat them as tools and stay in touch with what they are doing (@12:00).
- relation: `supports`.

### timeline: vibe-coding-over-time (existing)
- 2026-04-29 entry: December step change → [[coding-agents-became-reliable-for-him-in-december]]; vibe coding raises the floor, agentic engineering keeps the quality bar → [[agentic-engineering-keeps-the-quality-bar-while-going-faster]] (@01:08, @15:49, @16:22). Note: a change in his reported practice relative to [[autocomplete-is-his-coding-sweet-spot]]; vibe coding's own description is not withdrawn.

### timeline: llm-agents-over-time (existing)
- 2026-04-29 entry: agents started working for him as of December; still spiky, fallible, stochastic, needing humans in charge of spec and oversight (@01:39, @16:22, @20:44). No timescale given; do not tie to the decade claim.

### timeline: llm-os-over-time (existing)
- 2026-04-29 entry: neural net as host process, CPUs as coprocessors → [[neural-nets-may-become-the-host-process]] (@08:40).

### not fed: partial-autonomy-apps, this-is-the-decade-of-agents
- The talk never uses "autonomy slider", "partial autonomy" or "decade". The closest content (humans in charge of oversight and top-level categories, @20:44) belongs on [[agentic-engineering]]; at most a **Note** on [[partial-autonomy-apps]] linking it. Do not cite the talk as evidence on either page.

## Quotes
- "I can't remember the last time I corrected it" (@01:08)
- "That's the programming paradigm now." (@04:22)
- "all of my menu gen is spurious" (@05:59)
- "that app shouldn't exist" (@05:59)
- "the neural net becomes kind of like the host process" (@08:40)
- "some kind of combination of verifiable plus labs care" (@12:00)
- "you need to treat them as tools" (@12:00)
- "vibe coding is about raising the floor for everyone" (@15:49)
- "agentic engineering is about preserving the quality bar" (@15:49)
- "you're still responsible for your software just as before" (@15:49)
- "I do think it's kind of like an engineering discipline" (@16:22)
- "handled by the intern because they have very good recall" (@21:16)
- "It's just the labs haven't done it yet almost." (@22:58)
- "I think it's a little bit of philosophizing." (@24:04)
- "This is my favorite pet peeve." (@25:41)
- "What is the thing I should copy paste to my agent?" (@25:41)
- "the LLMs certainly don't excel at understanding" (@28:59)
- (a tweet he quotes, not his line) "you can outsource your thinking, but you can't outsource your understanding" (@27:55)

## Notes for merge
- **Host vs him.** No speaker labels. Stephanie Zhan's turns: @00:02–@00:36 intro, "Software 1.0 was explicit rules, software 2.0 was learned weights" (@02:11), the 2026-equivalent question with "last October to early January, February" (@07:35), verifiability question (@09:13–@09:47), founder question (@13:37), "automatable only from a distance" (@14:43), the vibe-coding-vs-"agentic engineering" question (@15:17–@15:49), Sam Altman generations anecdote (@17:28, Altman's claim reported by her), the ghosts summary listing intrinsic motivation, fun, curiosity, empowerment (@23:30), "agents that have real permissions..." (@25:09), sensors/actuators reaction (@27:20), education question and closing "fully automated out of the loop" (@27:20, @29:32). None of these are his.
- **Unclear speaker:** @15:17 "I think uh Everything. >> [laughter] >> Everything is automatable. Amazing. Okay." "Everything." is probably him; "Everything is automatable. Amazing." is probably the host echoing. Do not quote "Everything is automatable" as his; cite only "almost everything can be made verifiable to some extent" (@15:17).
- **"Agentic engineering" is first spoken by the host** (@15:49); he adopts and defines it. The YouTube title, set by Sequoia, is not his phrasing either.
- **Caption errors:** "Alpha code" (@00:36) is Claude Code per the blog's cleaned transcript; "Open Claw"/"OpenClaw" (@03:18, @17:28); "cloud code" = Claude Code (@17:28, @18:01); "Nana Banana" (@05:26) = Nano Banana; "menu gen" lowercase; "agent engineer" (@16:55) for agentic engineer; "the agents are catalog these internal entities" (@19:38) is garbled (the cleaned transcript renders it "like interns"; the raw does say "intern" at @21:16); "a race or tensors" (@20:44) = arrays or tensors; "10 codex 5.4 x high" (@19:06) is probably ten Codex 5.4 xhigh agents; "AI sent" (@17:28) = Ascent; "Andre" = Andrej.
- **Models named, not explained:** Opus 4.7 (@11:24), GPT-3.5/GPT-4 (@12:00), Gemini, Nano Banana (@05:26), Codex 5.4 (@19:06), microGPT (@22:58; a raw file raw/blog/microgpt.md exists, not yet a wiki page).
- **Dates:** he says "December" and "last year" without a year; the blog's AI summary writes "December 2025" (blog §1). From the talk alone write "December", or cite the blog summary for the year with its AI-written caveat. Do not compute intervals from the host's "last October to early January, February".
- **Chess anecdote is hedged** ("I think this is public information, I think I saw it on the internet", @12:32); keep the hedge, it is not his inside knowledge.
- **Hedges to keep:** neural computers "very weird", "TBD", "piece by piece" (@08:07, @09:13); ghosts framing "not sure if it actually has like real power" (@24:04); hiring "maybe it looks like that" (@19:06); 10x "from my perspective right now" (@16:55); taste "that's currently kind of like where we are" (@21:51).
- **He refers to "a slide/diagram"** (@08:40, "we saw the diagram") shown earlier at the event; not in the transcript.
- **Overlap with the blog (raw/blog/sequoia-ascent-2026.md, published 2026-04-30).** The blog is three parts: (a) a ~130-word intro in his own words (§intro); (b) a ~2,050-word **AI-written** first-person summary ("Codex 5.5", given all his recent posts and tweets plus this transcript; he says he read it and it "reads ok without glaring mistakes"); (c) a ~3,930-word **AI-cleaned transcript** of this same conversation. Part (c) overlaps this talk almost completely; it is one statement in two places, not two sources. Part (b) restates every topic of the talk except the neural-computers extrapolation, which it omits. Cite **this talk** (with timestamps) as the evidence for anything he said at the event; use the blog only as a second location, for its §intro, or explicitly as "the AI-written summary he posted".
- **Only in the talk (not in the blog summary):** neural computers / host process (@08:07–@09:13); car wash and Opus 4.7 (@11:24); council of LLM judges and almost everything verifiable (@15:17); Vim/VS Code and investing in setup (@18:01); dislike of plan mode (@20:10); code "heart attack" and no aesthetics reward (@22:25); yelling at models (@24:36); agent-to-agent meeting scheduling (@26:47); that the outsourcing line comes from a tweet (@27:55). All of these are also in the cleaned transcript, except the model names.
- **Only in the blog summary (not said in the talk):** see the blog digest's list; none of it should be cited as something he said at Sequoia.
- **Wording differences, talk vs blog cleaned transcript:** "certainly don't excel at understanding" (@28:59) vs "do not fully excel" (blog §Education and Understanding), a softening by the cleaner; "will tell you to walk" (@11:24) vs "may tell you to walk"; "Opus 4.7" vs "a state-of-the-art model"; "10 codex 5.4 x high" vs "ten Codex agents"; "extrapolating" the ceiling (@16:22) vs the summary's "Agentic engineering raises the ceiling" (blog §7). Prefer the talk's wording.
- Existing slug check: no page for verifiability, microGPT, OpenClaw, agentic engineering. raw/blog/verifiability.md and raw/blog/microgpt.md exist without wiki pages; when ingested they should be linked (verifiability → [[llms-automate-what-you-can-verify]]; microgpt → an artifact, plus the simplification anecdote here).
- The same host interviewed him in [[talk-2024-03-26-sequoia-making-ai-accessible]]; different event, no shared content beyond the LLM-OS theme.
