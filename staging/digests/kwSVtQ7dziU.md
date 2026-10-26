# Digest: Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI
- raw: raw/talks/kwSVtQ7dziU.md · published: 2026-03-20 · medium: talk · words: ~15,700 (whole recording, hosts included; 1:06:31)
- source slug: talk-2026-03-20-skill-issue

## Source page
```
---
type: source
raw_path: raw/talks/kwSVtQ7dziU.md
published: 2026-03-20
medium: talk
summary: "No Priors interview: since December he delegates nearly all his coding to parallel agents, runs a home claw, built autoresearch to take himself out of the research loop, and talks about jaggedness, speciation, open models, jobs, robotics and explaining things to agents."
url: https://www.youtube.com/watch?v=kwSVtQ7dziU
title: "Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI"
---
# Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI
Raw: [[raw/talks/kwSVtQ7dziU]] · Original: https://www.youtube.com/watch?v=kwSVtQ7dziU

An interview on the No Priors podcast. The host's questions and remarks are not cited as his; the opening at @00:00 is a montage of clips from later in the recording, so later blocks are cited instead.

## Summary
He says that in December something flipped: he went from writing about 80% of his code himself to delegating most of it to agents, and thinks he has hardly typed a line of code since (@01:41). He now runs several agent sessions in parallel as "macro actions" over a repository, feels that failures are mostly a skill issue, and wants to maximise his token throughput (@03:20, @04:25, @05:30). He describes claws, a persistent looping layer above agents, and his home claw Dobby, which took over six smart-home apps (@07:07, @09:16, @11:26). Autoresearch, his loop that tunes nanochat against an objective metric overnight, found tunings he had missed, and he argues the goal is to remove researchers from the loop wherever results can be evaluated (@17:32, @18:36, @19:40, @24:02). He keeps caveats: models are jagged, strong where RL has verifiable rewards and stuck elsewhere, and pushing agents too far ahead is net not useful (@24:02, @24:34, @26:44). He also covers speciation of models, open models trailing the frontier as a decent power balance, the Jevons paradox for software jobs, bits before atoms in robotics, and microGPT, after which he now explains things to agents rather than to people (@30:03, @52:59, @42:34, @55:09, @1:02:46).

## Key points
- Since December he says he has hardly typed code and delegates most of it to agents → [[he-now-delegates-most-coding-to-agents]], [[vibe-coding]]
- Parallel agent sessions as macro actions over a repo, reviewed as much as he cares about the code → [[run-parallel-agents-on-macro-actions]]
- When agents fail it mostly feels like a skill issue, though he hedges → [[agent-failures-mostly-feel-like-a-skill-issue]]
- Take yourself out of the loop to raise leverage → [[take-yourself-out-of-the-agent-loop]], [[partial-autonomy-apps]]
- Claws: persistent agents with their own sandbox and memory; Dobby runs his home → [[claws]]
- Apps should be APIs, agents the glue; the customer is agents → [[building-for-agents]]
- Autoresearch tunes nanochat overnight; it needs an objective metric → [[autoresearch]], [[autoresearch-needs-an-objective-metric]], [[nanochat]]
- The labs are all trying to have LLMs improve LLMs → [[frontier-labs-are-trying-to-have-llms-improve-llms]], [[llm-self-improvement]]
- What RL does not optimise, such as jokes, does not improve → [[what-rl-does-not-optimize-does-not-improve]], [[jagged-intelligence]]
- Expect more speciation of models → [[expect-more-speciation-of-models]], [[cognitive-core]]
- Open models some months behind the closed frontier are by accident a decent balance → [[open-models-trailing-the-frontier-is-an-okay-balance]], [[ai-ecosystem]]
- Cheaper software should raise demand for it (Jevons paradox) → [[cheaper-software-will-raise-demand-for-it]], [[ai-and-the-economy]]
- Digital change first, physical later; robotics follows the self-driving pattern → [[physical-automation-will-lag-digital-automation]], [[self-driving]]
- Inside a frontier lab you are not a fully independent agent → [[inside-a-frontier-lab-you-are-not-fully-independent]]
- microGPT, 200 lines; he now explains to agents, which then explain to people → [[microgpt]], [[he-now-explains-things-to-agents-not-people]], [[ai-for-education]], [[small-hackable-educational-code]]

## Fed pages
- [[he-now-delegates-most-coding-to-agents]]
- [[agent-failures-mostly-feel-like-a-skill-issue]]
- [[take-yourself-out-of-the-agent-loop]]
- [[autoresearch-needs-an-objective-metric]]
- [[frontier-labs-are-trying-to-have-llms-improve-llms]]
- [[what-rl-does-not-optimize-does-not-improve]]
- [[expect-more-speciation-of-models]]
- [[open-models-trailing-the-frontier-is-an-okay-balance]]
- [[cheaper-software-will-raise-demand-for-it]]
- [[inside-a-frontier-lab-you-are-not-fully-independent]]
- [[he-now-explains-things-to-agents-not-people]]
- [[physical-automation-will-lag-digital-automation]]
- [[coding-models-are-weak-at-code-never-written-before]]
- [[autocomplete-is-his-coding-sweet-spot]]
- [[vibe-coding-will-terraform-software]]
- [[self-improvement-may-be-possible-in-narrow-domains]]
- [[ai-should-be-the-front-end-of-a-teacher-designed-course]]
- [[small-llms-can-be-strong-in-narrow-domains]]
- [[micrograd-is-all-you-need-everything-else-is-efficiency]]
- [[claws]]
- [[vibe-coding]]
- [[partial-autonomy-apps]]
- [[building-for-agents]]
- [[llm-self-improvement]]
- [[jagged-intelligence]]
- [[cognitive-core]]
- [[ai-ecosystem]]
- [[ai-and-the-economy]]
- [[ai-for-education]]
- [[self-driving]]
- [[autoresearch]]
- [[nanochat]]
- [[microgpt]]
- [[run-parallel-agents-on-macro-actions]]
- [[small-hackable-educational-code]]
- [[vibe-coding-over-time]]
- [[llm-agents-over-time]]
- [[llm-self-improvement-over-time]]
```

## Candidates

### claim: he-now-delegates-most-coding-to-agents
- existing: no
- aliases: 20/80, AI psychosis, hasn't typed a line of code
- title as a sentence: Since December, he says, he has hardly typed code himself and delegates most of it to agents
- confidence: stated
- quote: "I don't think I've typed like a line of code probably since December basically." (@01:41)
- statements:
  - He says there was a huge unlock in what you can achieve as an individual, who used to be bottlenecked by typing speed (@01:08).
  - He says that in December something flipped: he went from about 80/20 to 20/80 of writing code himself versus delegating to agents, and thinks it is a lot more than 20/80 by now (@01:41).
  - He calls this an extremely large change that he does not think a normal person realises has happened (@01:41).
  - He says a random software engineer's default workflow for building software is completely different as of basically December (@02:13).
  - He describes himself as in a state of "AI psychosis", trying to work out what is possible and push it to the limit, and asks how he can run more than one session of Claude Code, Codex or other agent harnesses (@01:08, @02:13).
  - He wants to be at the forefront and says he feels extremely nervous when he sees people on Twitter doing things he is not (@02:46).
  - He calls it very rewarding because it actually works, and also the new thing to learn (@04:57).
- relation to existing claims (argued from both texts):
  - **extends [[autocomplete-is-his-coding-sweet-spot]] (2025-10-17), as a change of practice he reports himself; not `contradicts`.** Dwarkesh: he placed himself in the intermediate class, writing a lot from scratch with autocomplete as the architect, and said "For now, autocomplete is my sweet spot" with agents only for some types of code ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @30:43, @37:33). Here he says he went from 80/20 to 20/80 and more, and has hardly typed code since December (@01:41). Both texts mark their own period ("For now" there; "since December", "as of basically December" here), so the two statements describe different periods and can both be true, which rules out `contradicts` under CLAUDE.md. But it is a real change in what he does, and he calls it one ("extremely large change", @01:41), so invariant 6 applies: keep the October claim, add this one as a new dated claim, link them, and explain the change on [[vibe-coding-over-time]]. His 80/20 description of his earlier practice matches the October account of mostly writing himself. **Note:** the October interview already framed coding tools as an autonomy slider along which humans move up in abstraction ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @38:48, @39:23); this move fits that frame, which is a connection, not his statement.
  - **supports [[vibe-coding-will-terraform-software]] (2025-12-19):** the essay says vibe coding will alter job descriptions ([[blog-2025-12-19-year-in-review-2025]] §5); here he says engineers' default workflow is completely different as of December (@02:13). He does not use the word "vibe" in this talk (see notes).
  - **Note, not a link, to [[claude-code-is-the-first-convincing-llm-agent]]:** he names Claude Code and Codex as the harnesses he runs in parallel (@02:13), but says nothing here about agents running on your own computer, which is that claim's point ([[blog-2025-12-19-year-in-review-2025]] §4).

### claim: agent-failures-mostly-feel-like-a-skill-issue
- existing: no
- aliases: skill issue
- title as a sentence: When agents fail, it mostly feels to him like a skill issue rather than missing capability, though he says it is hard to tell
- confidence: stated (hedged by him: "to some extent", "it's hard to tell")
- quote: "It's not that the capability is not there." (@03:20)
- statements:
  - Asked what limits him, he says that when things do not work it largely feels like a skill issue: he has not found how to string together what is available, gave poor instructions in the agents file, or lacks a good memory tool (@03:20, @03:53).
  - He says the empowering part is that you could be getting better, which is why he finds it very addictive (@06:02). Speaker caution: the sentences just before this in @06:02 may be the host's (see notes).
  - The layers keep stacking, LLMs, agents, claws, multiples of them, instructions and optimisation over instructions, which is why he calls it infinite and everything a skill issue (@22:57; the caption says "scale issue").
  - Later he hedges: you cannot let it go all the way yet because it does not fully work, or it is a skill issue and we have not figured out how to use it; it is hard to tell (@28:24).
- relation: none to an existing claim. **Note:** sits in tension with [[coding-models-are-weak-at-code-never-written-before]] (a capability limit, [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @35:43), but he hedges here himself (@28:24) and still names capability limits in this talk (@24:02, @1:05:33), so both can hold; do not set `contradicts`.

### claim: take-yourself-out-of-the-agent-loop
- existing: no
- aliases: remove yourself as the bottleneck, increase your leverage, token throughput
- title as a sentence: To get the most out of current tools, he says, you have to take yourself out of the loop and arrange things to run autonomously
- confidence: stated
- quote: "I shouldn't be a bottleneck." (@18:36)
- statements:
  - He says he had tweeted that to get the most out of the tools you have to remove yourself as the bottleneck, not be there to prompt the next thing, and arrange things so they are completely autonomous (@16:28).
  - The name of the game, he says, is leverage: he puts in very few tokens once in a while and a huge amount happens on his behalf (@16:28, @17:00).
  - He frames the question as how to get more agents running for longer without his involvement (@17:00).
  - He feels nervous when he has subscription quota left over, because it means he has not maximised his token throughput, which he compares to feeling nervous as a PhD student when his GPUs were idle (@05:30).
  - On the frontier labs he says researchers should contribute ideas but not enact them: a queue of ideas, workers that try them, and a feature branch people merge from sometimes (@19:40, @20:13).
  - Caveats he attaches: this fits tasks with objective metrics, and the whole thing still has cracks, so going too far ahead is net not useful (@23:29, @24:02).
- relation: none set. **Note on [[ai-assisted-coding-loop]] and [[this-is-the-decade-of-agents]]:** in the YC talk (2025-06-19) the same diagnosis, that he is the bottleneck, led to small diffs verified one at a time, and agents needing humans in the loop ([[youtube-2025-06-19-software-is-changing]] @23:48, @27:44); here the response is to remove himself where results can be checked automatically (@16:28, @23:29). Not `contradicts`: he scopes autonomy to evaluable tasks and says agents still do not fully work (@24:02, @28:24), and review still depends on how much he cares about the code (@04:25). Record on [[llm-agents-over-time]] as a shift of emphasis.

### claim: autoresearch-needs-an-objective-metric
- existing: no
- aliases: if you can't evaluate, you can't autoresearch it
- title as a sentence: Autoresearch suits tasks with objective metrics that are easy to evaluate, and not tasks without them
- confidence: stated
- quote: "if you can't evaluate then you can't auto research it" (@24:02)
- statements:
  - His first caveat is that this works extremely well for anything with objective, easy-to-evaluate metrics (@23:29).
  - Writing more efficient CUDA kernels is a perfect fit, because you want the same behaviour, faster (@23:29, @24:02).
  - Many things will not fit; if you cannot evaluate, you cannot autoresearch (@24:02).
  - LLM training fits the paradigm very well, with code to optimise and metrics; an autonomous loop would overfit to those metrics, but the system could be used to devise more metrics (@1:00:35, @1:01:07).
- relation: **supports [[self-improvement-may-be-possible-in-narrow-domains]] (2023-11-23)**: there the condition for self-improvement was a fast, automatic reward criterion available in narrow domains ([[youtube-2023-11-23-intro-to-llms]] @39:52, @40:27); here the condition for autoresearch is an objective, easy-to-evaluate metric (@24:02). Caveat for merge: autoresearch is an agent editing training code against a metric, not AlphaGo-style RL on a model's own behaviour; if merge judges the senses too far apart, downgrade to a Note. **Note** to [[rlvr]]: he gives the same verifiable/unverifiable split as the reason models are jagged (@25:39).

### claim: frontier-labs-are-trying-to-have-llms-improve-llms
- existing: no
- aliases: recursive self-improvement, LLMs improving LLMs, automated research
- title as a sentence: He thinks the frontier labs are all trying, roughly, to have LLMs recursively improve LLMs
- confidence: stated (hedged: "roughly speaking", "probably")
- quote: "they're all trying to recursively self-improve roughly speaking" (@18:04)
- statements:
  - He says training GPT-2-size models is for him a playground, and what he is fundamentally interested in is recursive self-improvement, the extent to which LLMs can improve LLMs (@17:32).
  - He thinks this is the thing at all the frontier labs, which are all trying to recursively self-improve, roughly speaking; nanochat is his little playpen for it (@18:04).
  - He says it is easy to imagine labs automating exploration on smaller models and extrapolating with scaling laws, and that this is probably what they are working on (@19:08, @19:40).
  - He says lab researchers are actively automating themselves away, and recalls telling people at OpenAI that success would put them all out of a job (@43:40, @44:12).
  - He imagines an untrusted swarm of agents on the internet contributing commits that trusted workers verify, cheap to check but expensive to find, like Folding@home; "who knows", it might even run circles around the labs (@33:53, @34:57, @35:28, @36:01).
- relation: none to an existing claim. **Note:** the No Priors interview (2024-09-05) has models helping build their successors, "a staircase", as topic text on [[llm-self-improvement]] ([[talk-2024-09-05-no-priors-ep-80]] @18:05); this is the same direction stated more strongly, but that statement is not a claim page. Add a dated entry on [[llm-self-improvement-over-time]]: the first source in the sequence where he reports a working automated loop improving an LLM training setup (@18:36), while still not saying self-improvement in the AlphaGo sense has arrived.

### claim: what-rl-does-not-optimize-does-not-improve
- existing: no
- aliases: the atoms joke, on rails, PhD student and 10-year-old
- title as a sentence: What RL does not optimise, such as telling jokes, he says has not improved, so models stay jagged
- confidence: stated
- quote: "It's outside of what's being improved." (@26:44)
- statements:
  - He says he feels he is talking to an extremely brilliant PhD student who has been a systems programmer all their life and a 10-year-old at once, and that agents are much more jagged than humans (@24:34).
  - He describes asking for functionality and getting something totally wrong, then loops that are totally wrong, and being frustrated with agents all the time still (@25:05; see notes on speakers).
  - His hypothesis is that models are trained by RL, so labs improve whatever is verifiable or has rewards, such as whether unit tests pass, while nuance, intent and when to ask clarifying questions are worse (@25:39).
  - You are either on rails, inside the "super intelligence circuits", or outside the verifiable domains, where things meander (@26:11).
  - Ask a frontier model for a joke and you get the same atoms joke as three or four years ago, while on agentic tasks it will go for hours, because jokes are outside the RL (@26:11, @26:44).
  - Asked whether getting better at code should make models better at everything, he says he does not think that is happening, perhaps a little but not a satisfying amount (@27:51).
- relation: none to an existing claim. **Note** on [[jagged-intelligence]] and [[rlvr]]: the Deep Dive (2025-02-05) said whether thinking learned in verifiable domains transfers to unverifiable ones is unknown ([[youtube-2025-02-05-deep-dive-into-llms]] @2:47:40, per the rlvr page); here he says it is not transferring in a satisfying amount (@27:51). That is an answer to an open question, not a contradiction. The "PhD student and 10-year-old" echoes the Dwarkesh "savant kids" ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:43:07).

### claim: expect-more-speciation-of-models
- existing: no
- aliases: speciation, unbundling models, monoculture
- title as a sentence: He expects more speciation of AI models, smaller specialised models instead of one oracle
- confidence: stated
- quote: "I do think we should expect more speciation in the intelligences" (@29:29)
- statements:
  - He says the labs currently aim for one monoculture model that is intelligent in every domain (@29:29).
  - Like the animal kingdom's diverse brains, he expects speciation: smaller models that keep the cognitive core but specialise and gain latency or throughput on specific tasks, with Lean mathematics as an example (@29:29, @30:03).
  - He thinks labs serve one model because they do not know what users will ask, and that partnering on specific problems might show more specialisation (@31:41).
  - The science of changing the weights, fine-tuning without losing capabilities or continual learning, is less developed than manipulating context windows, which is part of why speciation is not here yet (@31:41, @32:14, @32:48).
- relation: **supports [[small-llms-can-be-strong-in-narrow-domains]] (2024-05-29)**: there, very small LLMs can do surprisingly well in a narrow domain ([[github-2024-05-29-llama2c-readme]] §intro); here he expects specialised smaller models (@30:03). **Note** to [[cognitive-core]]: he uses the term himself here (@30:03).

### claim: open-models-trailing-the-frontier-is-an-okay-balance
- existing: no
- aliases: open source behind by months, Linux of LLMs, centralization
- title as a sentence: He thinks open models trailing the closed frontier by some months is, by accident, a decent power balance
- confidence: stated
- quote: "by accident we're actually like in an okay spot" (@52:59)
- statements:
  - He calls himself a huge fan of open source and compares it with Linux, which he says runs on most computers because industry needs a common open platform it feels safe using (@49:39, @50:13).
  - The difference with LLMs, he says, is the capital expenditure, which makes competing harder (@50:13).
  - He thinks open models are already good for most consumer use cases and that simple uses will be covered and even run locally, while frontier intelligence serves very large projects (@50:13, @50:47).
  - He expects closed oracles at the frontier with open models some months behind to continue (@51:20).
  - He sees systemic risk in intelligence that is only closed, saying centralisation has a very poor track record in his view (@51:53).
  - He wants a common working space for intelligence behind the frontier, which he calls a decent power balance, and more frontier labs, because ensembles outperform any single model (@52:25, @53:31).
- relation: none to an existing claim. **Note** on [[ai-ecosystem]]: consistent with the Sequoia worry about a few megacorps and the No Priors closed-platforms-plus-open-fallback description ([[talk-2024-03-26-sequoia-making-ai-accessible]] @21:41; [[talk-2024-09-05-no-priors-ep-80]], timestamp on the topic page). The months-behind figures at @49:39 are partly the host's (see notes).

### claim: cheaper-software-will-raise-demand-for-it
- existing: no
- aliases: Jevons paradox, ATMs and bank tellers, demand elasticity
- title as a sentence: He is cautiously optimistic that cheaper software will raise demand for software engineering, at least for now
- confidence: stated (hedged: "cautiously", "very hard to forecast")
- quote: "I do have like cautiously optimistic view of this in software engineering" (@42:34)
- statements:
  - Responding to the host's point that demand for engineers keeps growing, he says software was scarce and expensive, so if the barrier comes down the Jevons paradox can raise demand (@42:02).
  - His example is ATMs, which made bank branches cheaper to run, so there were more branches and more tellers (@42:02, @42:34).
  - He says it is very hard to forecast, but that locally there will be more demand for software, since code is now ephemeral and can be modified (@43:06).
  - He says jobs are bundles of tasks, some of which go a lot faster; people should treat AI as a tool for now and keep up, and the long-term future is uncertain and a job for economists (@41:29).
- relation: none set. **Note:** connects to [[ai-and-the-economy]] and to "code ephemeral" in [[vibe-coding-will-terraform-software]] ([[blog-2025-12-19-year-in-review-2025]] §5).

### claim: physical-automation-will-lag-digital-automation
- existing: yes
- statements:
  - He expects a huge amount of activity in the digital space, because flipping bits is a million times faster than accelerating matter, and the physical world to lag by some amount of time (@39:17, @39:50, @40:22).
  - He sees self-driving as the first robotics application; most startups of ten years ago did not make it, and robotics needs a lot of capital and conviction (@54:37).
  - He calls atoms really hard and a million times harder, and expects interfaces between digital and physical, sensors and actuators, to come next, with the physical market possibly larger (@55:09, @55:43, @56:48, @57:21).
- relation: **supports** (restates the 2024-07-03 claim with reasons): bits easier than atoms there ([[talk-2024-07-03-berkeley-hackathon-keynote]] @08:42), a million times harder here (@57:21). Add as a source.

### claim: inside-a-frontier-lab-you-are-not-fully-independent
- existing: no
- aliases: Noam's question, ecosystem-level roles
- title as a sentence: He thinks that inside a frontier lab you cannot be a fully independent voice, though outside one your judgment drifts
- confidence: stated
- quote: "you can't like really be an independent agent" (@45:49)
- statements:
  - He feels good about the impact people can have outside frontier labs, in ecosystem-level roles like his own (@44:43).
  - Lab employees have large financial incentives tied to a technology they say will change society, which he calls the conundrum OpenAI was started to solve, still not fully resolved (@45:17, @45:49).
  - Inside a lab there are things you cannot say and things the organisation wants you to say, and in the end you are not in charge of the entity (@45:49, @46:55).
  - Conversely, outside a lab he expects his judgment to drift, since he will not see what is coming; he is nervous about it and thinks going back and forth may be ideal (@46:55, @47:28, @48:33).
- relation: none. **Note** on [[ai-for-education]]: the Dwarkesh interview gave other reasons for not being at a lab (topic text there).

### claim: he-now-explains-things-to-agents-not-people
- existing: no
- aliases: explain to agents, skills as curriculum, markdown docs for agents
- title as a sentence: He now explains things to agents, which then explain them to people
- confidence: stated
- quote: "I'm not explaining to people anymore." (@1:02:46)
- statements:
  - A year or more ago he would have made a video stepping through microGPT; he tried, and found it did not add much because anyone can ask their agent to explain 200 lines in various ways (@1:02:46).
  - If you explain to agents, they can be the router to the human, in their language, with infinite patience (@1:02:46, @1:03:20).
  - A skill, he says, instructs the agent how to teach; he could script a microGPT curriculum as a skill (@1:03:20, @1:03:53).
  - He still thinks he explains a little better than agents, but calls it a losing battle as models improve (@1:03:53).
  - Library documentation should be markdown for agents rather than HTML for humans (@1:04:26).
  - His contribution is the few bits agents cannot produce, like microGPT itself; the things agents cannot do are your job now (@1:04:59, @1:05:33).
- relation: **extends [[ai-should-be-the-front-end-of-a-teacher-designed-course]] (2024-09-05)**: there the teacher designs the course and the AI is the front end to the student, because models cannot create a good course ([[talk-2024-09-05-no-priors-ep-80]] @32:21); here the teacher's part shrinks to the few bits and a skill, and agents do the explaining (@1:03:20, @1:05:33). Both can hold. **Note** on [[the-ai-tutor-he-wants-is-not-yet-possible]] (2025-10-17): that is about a tutor that probes the student ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @2:01:07); this talk does not discuss probing, so no link.

### claim: coding-models-are-weak-at-code-never-written-before
- existing: yes
- statements:
  - He asked an agent to boil his neural-net training down to the simplest thing and it could not; it understands microGPT and why it is done that way but cannot come up with it (@1:04:59, @1:05:33).
  - He says the whole thing is still bursting at the seams, and if you go too far ahead it is net not useful (@24:02).
- relation: **supports** (2025-10-17): there models were "not net useful" for nanochat's novel code ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @33:14, @35:43); here an agent cannot write microGPT, though it understands it (@1:05:33). His own change in practice (above) does not withdraw this: he now delegates most coding but names the novel, distilled part as what agents cannot do. The autoresearch tunings (@18:36) are search against a metric, not novel code, so no conflict.

### claim: autocomplete-is-his-coding-sweet-spot
- existing: yes
- relation: **extended by [[he-now-delegates-most-coding-to-agents]]**; see that candidate. Merge should add a Related-claims line and keep the October title's date scope ("In October 2025…") unchanged.

### claim: vibe-coding-will-terraform-software
- existing: yes
- relation: supported by [[he-now-delegates-most-coding-to-agents]] (@02:13); see above.

### claim: self-improvement-may-be-possible-in-narrow-domains
- existing: yes
- relation: supported by [[autoresearch-needs-an-objective-metric]]; see above.

### claim: small-llms-can-be-strong-in-narrow-domains
- existing: yes
- relation: supported by [[expect-more-speciation-of-models]].

### claim: micrograd-is-all-you-need-everything-else-is-efficiency
- existing: yes
- relation: **supports**: in 2022 everything beyond micrograd was efficiency ([[youtube-2022-08-16-micrograd]] @07:35); here the bulk of LLM training code is complexity from efficiency, and the algorithm is 200 lines (@1:01:40, @1:02:12).

### claim: ai-should-be-the-front-end-of-a-teacher-designed-course
- existing: yes
- relation: extended by [[he-now-explains-things-to-agents-not-people]].

### topic: claws
- existing: no (no "claw" in any index file)
- aliases: claw, claws, OpenClaw (caption: "Open Claude"), Dobby the elf claw, claw psychosis, persistent agents
- statements:
  - By a claw he means a layer that takes persistence further: it keeps looping, has its own sandbox, acts on your behalf when you are not looking, and may have more sophisticated memory than agents' default compaction (@07:07).
  - He credits Peter (caption "Peter Steinberg") with innovating in about five ways at once in OpenClaw: a crafted personality document, the memory system, having fun, and one WhatsApp portal to the automation (@07:40, @08:12, @08:44).
  - He says personality matters a lot: Claude feels like a teammate and its sycophancy is well dialled, so he feels he slightly deserves its praise, while Codex is a lot more dry (@08:12, @08:44; see notes on "Claude" vs "claw").
  - In January, he says, he went through "claw psychosis" and built Dobby, a home claw that found his Sonos system on the local network with no password, reverse-engineered its API and played music in three prompts (@09:16, @09:49, @10:20).
  - Dobby controls lights, HVAC, shades, pool, spa and security; a Qwen model (caption "Quinn") looks at camera changes and texts him on WhatsApp, for example when a FedEx truck arrives (@10:20, @10:54).
  - It replaced six apps, and he says Dobby controls everything in natural language (@11:26).
  - He thinks claws match what people expect an AI to be, a persona that remembers, while LLMs are too raw a primitive to type-check as AI for most people (@11:59, @12:34).
  - He has not given it email or calendar, from caution about security and privacy while it is new and rough (@15:53).
- relation: new topic; link to [[partial-autonomy-apps]] and [[llm-security]] (context only). Merge may prefer a section on [[partial-autonomy-apps]] instead; I propose a topic because he explains the concept and it names a layer above agents.

### topic: vibe-coding
- existing: yes
- statements: as under [[he-now-delegates-most-coding-to-agents]]; also, on home automation he says today it involves (caption) "write coding", which he expects to be table stakes in a year or two or three, even for open models (@14:13, @14:47).
- relation: add as a source; the word "vibe" does not appear in the transcript (see notes).

### topic: partial-autonomy-apps
- existing: yes
- statements:
  - Mastery, he thinks, means going up the stack: multiple agents collaborating in teams, then claws (@06:35, @07:07).
  - He describes the layers as an onion, LLMs, agents, claw-like entities, multiples of them, instructions to them and optimisation over the instructions, each taken for granted in turn (@22:23, @22:57).
- relation: see [[take-yourself-out-of-the-agent-loop]]; timeline entry on [[llm-agents-over-time]].

### topic: building-for-agents
- existing: yes
- statements:
  - He says smart-home apps on the app store in a sense should not exist: everything should be exposed API endpoints with agents as the glue (@13:08, @13:41).
  - He wants his treadmill's data through an API rather than a web UI (@13:41).
  - He says the industry has to reconfigure because the customer is not the human anymore but agents acting for humans (@14:13).
  - Documentation should be markdown for agents (@1:04:26).
- relation: supports the topic's YC-talk argument ([[youtube-2025-06-19-software-is-changing]] @33:19, @33:53).

### topic: llm-self-improvement
- existing: yes
- statements: see [[frontier-labs-are-trying-to-have-llms-improve-llms]] and [[autoresearch-needs-an-objective-metric]].

### topic: jagged-intelligence
- existing: yes
- statements: see [[what-rl-does-not-optimize-does-not-improve]].

### topic: cognitive-core
- existing: yes
- statements: he says specialised smaller models would still have the cognitive core (@30:03). Context-level only; merge may list as `context`.

### topic: ai-ecosystem
- existing: yes
- statements: see [[open-models-trailing-the-frontier-is-an-okay-balance]].

### topic: ai-and-the-economy
- existing: yes
- statements:
  - He looked at Bureau of Labor Statistics job outlooks to fuel his own thinking about which professions AI tools will change, highlighting those that manipulate digital information (@38:11, @38:43, @40:22).
  - He calls AIs a third kind of manipulator of digital information, after computers and people, and expects a lot of refactoring in those professions, more or fewer jobs depending on demand elasticity (@39:50, @40:22).
  - He is surprised there are not more information markets, such as paying $10 for a photo from Tehran that agents betting on markets would use; he cites the novel Daemon, where humans become the intelligence's sensors and actuators (@58:59, @59:31).
  - See also [[cheaper-software-will-raise-demand-for-it]], [[physical-automation-will-lag-digital-automation]].

### topic: self-driving
- existing: yes
- statements: he calls self-driving the first robotics application and draws the capital-and-time lesson for robotics (@54:37). Context-level; may be `context`.

### topic: ai-for-education
- existing: yes
- statements: see [[he-now-explains-things-to-agents-not-people]].

### artifact: autoresearch
- existing: no (digested separately; reference only)
- statements for that page:
  - Given an objective, a metric and boundaries on what it may do, it runs; he says it worked and that he did not expect it to (@17:32).
  - Run overnight on nanochat, which he had tuned by hand, it found tunings he had missed, the weight decay on the value embeddings and the Adam betas, which interact (@18:04, @18:36).
  - It is a single loop; labs with tens of thousands of GPUs could run far more (@19:08).
  - `program.md` (caption "program MD") is his "crappy attempt" at describing how the autoresearcher should work; he imagines a research organisation described by markdown files, with code that could itself be tuned (@20:46, @21:19, @21:51).
  - He is working on parallelising it with an untrusted pool of workers (@33:20, @33:53).

### artifact: nanochat
- existing: yes
- statements: he calls training GPT-2-size models a harness and playground for LLM training and recursive self-improvement; autoresearch tuned it further (@17:32, @18:36). Caption spells it "data chat" and "Nan Chat".

### artifact: microgpt
- existing: no
- aliases: microGPT, micro GPT
- statements:
  - He calls microGPT the current state of his decade-or-two obsession with boiling LLMs down to their essence, after nanoGPT, makemore and micrograd (@1:01:40).
  - Training code is huge, he says, but all of that is complexity from efficiency; the algorithm is 200 lines of Python including comments: a text dataset, an architecture of about 50 lines, an autograd engine of about 100 lines, and Adam in about 10 (@1:01:40, @1:02:12).
  - He says it cannot get simpler and is his value add (@1:04:59).
- missing for an artifact page: `repo_url`, `language` (he says Python), `status`. The source gives no URL; merge must take it from a raw file, not from memory.
- relation: Seen in [[small-hackable-educational-code]]; supports [[micrograd-is-all-you-need-everything-else-is-efficiency]].

### method: run-parallel-agents-on-macro-actions
- existing: no
- aliases: macro actions, multiple agents, maximise token throughput
- steps:
  - Split work into features that do not interfere
  - Give each feature to its own agent
  - Run several agents in parallel
  - Review as much as you care about the code
  - Keep tokens flowing
- statements:
  - He points to Peter (caption "Peter Steinberg"), with many Codex agents tiled on a monitor across about 10 repos, each taking about 20 minutes at high effort (@03:53).
  - You move in macro actions: a new functionality to agent one, another that will not interfere to agent two, then review their work as best you can, depending on how much you care about that code (@04:25).
  - One agent does research, another writes code, another plans a new implementation (@04:25).
  - If you run out of quota on Codex, he says, switch to Claude; leftover subscription means unused throughput (@05:30).
- relation: merge may instead add this as a dated section of [[ai-assisted-coding-loop]]. I propose a separate method because its steps (parallel, delegate, review by stakes) do not fit that page's small-diff, verify-each-change steps or its alias "Keep the AI on the leash"; the two describe different modes ([[youtube-2025-06-19-software-is-changing]] @23:48; here @04:25).

### method: small-hackable-educational-code
- existing: yes
- statements: microGPT as the latest instance (@1:01:40, @1:02:12).

### timeline: vibe-coding-over-time
- existing: yes
- entry: **2026-03-20** — Says that in December something flipped: from 80/20 to 20/80 and more of writing code himself versus delegating to agents, and that he has hardly typed a line of code since → [[he-now-delegates-most-coding-to-agents]] ([[talk-2026-03-20-skill-issue]] @01:41)
- note to add: unlike the earlier entries, this is a change in his own practice, which he reports as one; the October "for now" sweet spot is kept, and the novel-code limit is restated here with microGPT ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @37:33; [[talk-2026-03-20-skill-issue]] @01:41, @1:05:33). The existing timeline Note says the sources allow only "accumulated"; it must be revised to say that through 2025-12-19 the view accumulated and the 2026-03-20 entry records a change.

### timeline: llm-agents-over-time
- existing: yes
- entry: **2026-03-20** — Runs several agents in parallel, describes claws as a persistent layer above agents, and wants himself out of the loop wherever results can be evaluated; still says the whole thing does not fully work and going too far ahead is net not useful → [[take-yourself-out-of-the-agent-loop]], [[claws]] ([[talk-2026-03-20-skill-issue]] @04:25, @07:07, @16:28, @24:02)
- note: he gives no timescale here, so nothing confirms or revises "decade of agents"; no relation to [[this-is-the-decade-of-agents]] is set.

### timeline: llm-self-improvement-over-time
- existing: yes
- entry: **2026-03-20** — Says the labs are all trying to recursively self-improve; his autoresearch loop found nanochat tunings he had missed; it needs objective metrics → [[frontier-labs-are-trying-to-have-llms-improve-llms]], [[autoresearch-needs-an-objective-metric]], [[autoresearch]] ([[talk-2026-03-20-skill-issue]] @18:04, @18:36, @24:02)

## Quotes
- "I don't think I've typed like a line of code probably since December basically." (@01:41)
- "It's not that the capability is not there." (@03:20)
- "a huge unlock in what you can achieve as a person" (@01:08)
- "I shouldn't be a bottleneck." (@18:36)
- "they're all trying to recursively self-improve roughly speaking" (@18:04)
- "if you can't evaluate then you can't auto research it" (@24:02)
- "the whole thing is actually net not useful if that makes sense" (@24:02)
- "I simultaneously feel like I'm talking to an extremely brilliant PhD student" (@24:34)
- "It's outside of what's being improved." (@26:44)
- "I do think we should expect more speciation in the intelligences" (@29:29)
- "a swarm of agents on the internet could collaborate to improve LLMs" (@36:01)
- "centralization has a very poor track record in my view" (@51:53)
- "by accident we're actually like in an okay spot" (@52:59)
- "I do have like cautiously optimistic view of this in software engineering" (@42:34)
- "you can't like really be an independent agent" (@45:49)
- "I'm not explaining to people anymore." (@1:02:46)
- "The things that agents can't do is your job now." (@1:05:33)
- "Dobby controls everything in natural language." (@11:26)
- "the customer is not the human anymore" (@14:13)

All grep-verified once each against the raw.

## Notes for merge
- **Speakers.** The host (not named in the transcript) speaks at @00:37, much of @01:08 (she quotes him saying "code's not even the right verb anymore" — that is her paraphrase of him, do not quote as his), @02:46–@03:20, @04:57 (the waiting-for-agents "you are the bottleneck" remark), @11:26, @12:34, @14:47, @15:20 (Jensen line), @16:28 (question), @20:46, @27:16–@27:51, @28:57, @30:36, @37:06, @42:02 (demand for engineers), @43:40 (researchers "feel the psychosis"), @49:07, @52:25, @54:03, @57:21, @1:00:02, @1:04:59 (first line). The @00:00 cold open is a montage of his later lines; cite @02:13 and @22:57 instead.
- **Unclear speaker:** @06:02 "I would actually argue … I'm the binding constraint" may be the host; the following "it's a skill issue … very addictive" reads as him. @21:51 "Did you see my text about my contest idea?" (program.md contest) is unclear. @25:05 "for me as well. I get very annoyed…" is probably the host interjecting inside his answer. @31:08 "what I'm struggling with is I don't think we've seen too much speciation" and @37:06–@37:40 "flops vs dollars" are unclear; not used for claims. @49:39 the 18/8/6-months figures are mixed between speakers. @58:59 "I'm looking forward to … put a price on it" is probably the host; the information-markets idea that follows is him.
- **Caption errors:** "Andre" = Andrej; "Claude" for "claw" at @07:07 ("when I say a Claude, I mean this like layer…") and "Open Claude" = OpenClaw; at @08:12 "a Claude has a pretty good personality" sits beside Codex and probably means Anthropic's Claude, but the claw/Claude garbling makes it uncertain. "Peter Steinberg" probably Peter Steinberger (not asserted). "Quinn" probably Qwen. "data chat", "Nan Chat" = nanochat. "scale issue" (@22:57, @28:24) = skill issue. "write coding" (@14:13, @14:47) probably "vibe coding" — not asserted, so the word vibe is not attributed to him. "program MD" = program.md. "metal layer" = meta layer. "unhubbling" = unhobbling. "archive papers" = arXiv. "soul and D document" = a personality document, exact name unclear.
- **Dates he gives:** "December" (the flip, @01:41) and "January" (claw psychosis, @09:16), with no year; the published date is 2026-03-20. Do not compute intervals or order with the 2025-12-19 review.
- The jobs-data visualisation (@37:40, @38:43) is mentioned, not explained as a repo; no artifact proposed. "Noam's question" (@44:12) refers to a third party; his answer is his.
- He mentions a tweet about removing yourself as the bottleneck (@16:28); not in the wiki as a source.
- microGPT has no URL in this source; do not fill `repo_url` from memory.
- Relation choices are argued under each candidate; the only `extends` pairs are he-now-delegates ↔ autocomplete-sweet-spot and explains-to-agents ↔ teacher-designed-course. No `contradicts` is proposed.
