# Digest: Andrej Karpathy — "We're summoning ghosts, not building animals"
- raw: raw/talks/lXUZvyajciY.md · published: 2025-10-17 · medium: talk · words: 26184
- source slug: talk-2025-10-17-dwarkesh-ghosts-not-animals

## Source page

```
---
type: source
raw_path: raw/talks/lXUZvyajciY.md
published: 2025-10-17
medium: talk
summary: Dwarkesh Patel podcast interview on why agents will take a decade, why RL is terrible but better than imitation, LLMs as ghosts rather than animals, model collapse and the cognitive core, coding agents while building nanochat, self-driving's march of nines, AI and GDP, and Eureka's approach to education.
url: https://www.youtube.com/watch?v=lXUZvyajciY
title: "Andrej Karpathy — “We’re summoning ghosts, not building animals”"
---
# Andrej Karpathy — "We're summoning ghosts, not building animals"
Raw: [[raw/talks/lXUZvyajciY]] · Original: https://www.youtube.com/watch?v=lXUZvyajciY

## Summary
A two-and-a-half-hour interview with Dwarkesh Patel, who asks the questions and often argues
the other side. He says agents such as Claude and Codex are impressive but lack intelligence,
multimodality, computer use and continual learning, and that working through this will take
about a decade, a figure he gets from 15 years of watching predictions (@01:25, @01:59, @03:14).
He contrasts LLMs, ghost-like entities trained by imitating internet documents, with animals
built by evolution, calls pretraining "crappy evolution", and wants a cognitive core that keeps
the algorithms of thought and sheds memorised knowledge (@09:25, @12:28, @13:43, @14:23,
@57:10). He calls RL terrible, "sucking supervision through a straw", though better than the
imitation that came before, explains why LLM judges are gameable and why training on a model's
own samples collapses it (@41:33, @42:46, @47:11, @52:12). From building nanochat he says coding
agents were not net useful for novel, precisely arranged code and that autocomplete is his sweet
spot (@31:58, @33:14, @37:33). He uses self-driving to argue that going from demo to product is
a march of nines, expects AI to show up as the same smooth GDP exponential rather than a jump,
and describes Eureka as an effort to build ramps to knowledge, with nanochat as the capstone of
the LLM101n course (@1:45:36, @1:22:43, @1:25:44, @2:02:21, @2:03:02).

## Key points
- Agents will take about a decade to work like an intern; the bottlenecks are cognitive → [[this-is-the-decade-of-agents]], [[llm-agents-over-time]]
- Atari RL and Universe went after agents too early, before LLM representations → [[early-agent-attempts-came-too-early]]
- We are building ghosts by imitation, not animals by evolution; pretraining is crappy evolution → [[jagged-intelligence]], [[were-summoning-ghosts-not-building-animals]]
- Pretraining picks up both knowledge and intelligence; the knowledge may hold models back → [[pretraining-and-finetuning]], [[cognitive-core]], [[a-cognitive-core-could-be-about-a-billion-parameters]]
- Weights are a hazy recollection, the context window a working memory → [[prompting-llms]], [[pretraining-is-lossy-compression-of-the-internet]]
- Models lack continual learning, a sleep-like distillation into the weights, culture and self-play → [[jagged-intelligence]], [[llm-self-improvement]], [[llms-lack-culture-and-self-play]]
- RL is terrible but everything before it was worse; outcome rewards are sucked through a straw → [[llm-self-improvement]], [[rlvr]], [[rl-is-terrible-but-better-than-imitation]]
- LLM judges as process rewards get gamed by adversarial examples like "dhdhdhdh" → [[llm-judges-are-gameable-rewards]]
- Model outputs are silently collapsed, so training on synthetic reflections degrades the model → [[model-collapse]], [[training-on-own-samples-collapses-models]]
- Progress comes from data, hardware, kernels and algorithms improving together; in ten years still big nets trained by gradient descent → [[transformer-architecture]], [[progress-comes-from-everything-improving-together]]
- Building nanochat: agents good for boilerplate and unfamiliar languages, not for novel code; autocomplete is his sweet spot → [[vibe-coding]], [[ai-assisted-coding-loop]], [[nanochat]], [[coding-models-are-weak-at-code-never-written-before]], [[autocomplete-is-his-coding-sweet-spot]]
- Automation is an autonomy slider; call centres would go 80/20 with humans supervising AIs → [[partial-autonomy-apps]]
- Self-driving: demo to product is a march of nines, and self-driving is not done → [[self-driving]], [[deployment-is-a-march-of-nines]]
- AGI as any economically valuable task; AI continues the GDP exponential; we have been in an intelligence explosion for decades → [[ai-and-the-economy]], [[ai-will-not-show-up-as-a-jump-in-gdp]], [[physical-automation-will-lag-digital-automation]]
- Most likely outcome: a gradual loss of understanding and control → [[ai-and-the-economy]], [[gradual-loss-of-control-is-the-most-likely-outcome]]
- Eureka: a Starfleet Academy; education is building ramps to knowledge; the AI tutor he wants is not yet possible; post-AGI education is like the gym → [[education]], [[education-is-building-ramps-to-knowledge]], [[the-ai-tutor-he-wants-is-not-yet-possible]], [[post-agi-education-will-be-like-the-gym]]
- Build it yourself to understand it; find the first-order terms; present the pain before the solution → [[if-you-cannot-build-it-you-do-not-understand-it]], [[teach-by-building-a-ramp]], [[learn-by-building-and-explaining]], [[micrograd]], [[micrograd-is-all-you-need-everything-else-is-efficiency]]

## Fed pages
- [[jagged-intelligence]]
- [[llm-self-improvement]]
- [[rlvr]]
- [[pretraining-and-finetuning]]
- [[prompting-llms]]
- [[transformer-architecture]]
- [[partial-autonomy-apps]]
- [[vibe-coding]]
- [[cognitive-core]]
- [[model-collapse]]
- [[self-driving]]
- [[ai-and-the-economy]]
- [[education]]
- [[nanochat]]
- [[micrograd]]
- [[this-is-the-decade-of-agents]]
- [[pretraining-is-lossy-compression-of-the-internet]]
- [[physical-automation-will-lag-digital-automation]]
- [[micrograd-is-all-you-need-everything-else-is-efficiency]]
- [[were-summoning-ghosts-not-building-animals]]
- [[early-agent-attempts-came-too-early]]
- [[a-cognitive-core-could-be-about-a-billion-parameters]]
- [[llms-lack-culture-and-self-play]]
- [[rl-is-terrible-but-better-than-imitation]]
- [[llm-judges-are-gameable-rewards]]
- [[training-on-own-samples-collapses-models]]
- [[progress-comes-from-everything-improving-together]]
- [[coding-models-are-weak-at-code-never-written-before]]
- [[autocomplete-is-his-coding-sweet-spot]]
- [[deployment-is-a-march-of-nines]]
- [[ai-will-not-show-up-as-a-jump-in-gdp]]
- [[gradual-loss-of-control-is-the-most-likely-outcome]]
- [[education-is-building-ramps-to-knowledge]]
- [[the-ai-tutor-he-wants-is-not-yet-possible]]
- [[post-agi-education-will-be-like-the-gym]]
- [[if-you-cannot-build-it-you-do-not-understand-it]]
- [[ai-assisted-coding-loop]]
- [[teach-by-building-a-ramp]]
- [[learn-by-building-and-explaining]]
- [[llm-agents-over-time]], [[vibe-coding-over-time]], [[llm-self-improvement-over-time]] (timelines; merge decides)
```

## Candidates

### claim: this-is-the-decade-of-agents
- existing: yes (2025-06-19). **Recommend adding this source to the existing claim, not a new claim:** he refers to "It's the decade of agents" as his own earlier quote and restates it (@00:48).
- statements:
  - Asked why this is the decade and not the year of agents, he says the phrase reacted to someone's "year of agents" claim, which he felt was over-prediction in the industry (@00:48).
  - He uses very early agents daily, Claude and Codex, and calls them extremely impressive, but says there is much work left and we will be working with these things for a decade (@01:25).
  - He thinks of an agent as something like an employee or intern; today you would not hire Claude or Codex for that because they don't have enough intelligence, are not multimodal enough, cannot do computer use, and lack continual learning, so "it's just not working" (@01:25, @01:59).
  - He says it will take about a decade to work through those issues (@01:59).
  - Asked why a decade and not one or fifty years, he says it is intuition and extrapolation from about 15 years in AI watching predictions and how they turned out; the problems feel tractable but difficult, and averaged out it feels like a decade (@02:32, @03:14).
  - He says the models still feel like an elementary-grade student, savant kids with perfect memory who don't really know what they are doing (@1:42:26, @1:43:07).
  - He says the industry is making too big a jump and pretending the output is amazing when it is slop, perhaps to fundraise; the models are amazing but need a lot of work (@36:57, @37:33).
  - He agrees with Dwarkesh that the models' weakness at novel code is "why my timelines are a bit longer", relevant to whether an AI 2027-type explosion is near (@35:43). The AI-2027 framing is Dwarkesh's; Karpathy agrees it is "a good way of putting it".
  - He says he sounds pessimistic only in reaction to his Twitter timeline, much of it fundraising and attention; overall he is optimistic, thinks it is tractable and is very bullish (@1:54:49, @1:55:33).
  - He wants timelines properly calibrated, partly because they have geopolitical ramifications (@1:56:09, @1:56:46).
- relations (argued from both sides):
  - **This claim (2025-06-19) — supports / same claim.** YC talk: "this is the decade of agents", evidence self-driving, agents need humans in the loop ([[youtube-2025-06-19-software-is-changing]] @27:09, @27:44). Here: same phrase, now with a list of bottlenecks (intelligence, multimodality, computer use, continual learning) and a stated basis (15 years of intuition) (@01:59, @03:14). Nothing is withdrawn; it is the same position with more reasons. Not `extends` between two claim pages, because it is the same claim; add the source and the reasons to the existing page's Context.
  - **llm-products-will-take-years-to-figure-out (2024-03-26).** Sequoia: products "quite autonomous but not fully autonomous", oversight and evaluation to be worked out "over the next few years" ([[talk-2024-03-26-sequoia-making-ai-accessible]] @06:54). Here: about a decade until agents work like an employee (@01:59). Could both be true? Yes: the 2024 horizon is for working out how to oversee and evaluate LLM products, the 2025 horizon is for agents reaching intern-level competence. Different targets, so no `contradicts`. The existing weak `supports` link stands; this source adds no new link.
  - **use-llms-as-copilots-with-human-oversight (2023-05-25).** State of GPT: copilots over autonomous agents ([[talk-2023-05-25-state-of-gpt]] @39:57). Here he still keeps the human as architect: autocomplete is his sweet spot and agents only for some code (@30:43, @37:33), and in the economy he looks for an autonomy slider, not full automation (@1:11:05). Consistent: `supports` the existing link, no new relation.
  - **claude-code-is-the-first-convincing-llm-agent (2025-12-19).** Blog: Claude Code is "the first convincing demonstration of what an LLM Agent looks like" ([[blog-2025-12-19-year-in-review-2025]] §4). Here (published earlier): Claude and Codex are "extremely impressive" and used daily (@01:25), yet feel like an elementary-grade student (@1:43:07) and were not net useful for nanochat (@33:14). Can both be true? Yes: a convincing demonstration of what an agent looks like is compatible with agents being cognitively immature and bad at novel code. No `contradicts`. Weakest true link: none set directly between them; a Note on the timeline. If merge wants a link, `supports` on the "impressive early agents" half only (@01:25).
  - Timeline: add a 2025-10-17 entry to [[llm-agents-over-time]] between 2025-06-19 and 2025-12-19.

### claim: early-agent-attempts-came-too-early
- existing: no
- title: "He thinks the Atari-RL and Universe attempts at agents came too early, before LLM representations"
- confidence: stated
- quote: "people really try to go after agents too early" (@06:58)
- statements:
  - He describes three seismic shifts he lived through: per-task neural nets after AlexNet, a first round of agents, and LLMs (@04:25, @07:36).
  - He calls the 2013-era Atari deep RL shift a misstep, adopted even by early OpenAI, where for a few years everyone did RL on games (@05:04, @05:45).
  - He was always suspicious that games would lead to AGI; he wanted something like an accountant interacting with the real world (@05:45).
  - His own OpenAI project, within Universe, was an agent using keyboard and mouse on web pages; he says it was way too early, the reward was too sparse, and you would burn a forest of compute (@06:23).
  - What was missing was the representation power of a pretrained network; today computer-use agents are trained on top of an LLM (@06:58).
- relation: none to an existing claim. **Note:** backstory for [[llm-agents-over-time]]; first source on his Universe work in the wiki.

### topic: jagged-intelligence
- existing: yes (aliases include "ghosts vs animals")
- statements:
  - He says he is very careful about analogies to animals because they came from a different optimization process; a zebra runs minutes after birth, which is baked in, not reinforcement learning (@08:14, @08:49).
  - In his post, he says, he wrote that we are building ghosts or spirits, not animals, because training is imitation of humans and their internet data, not evolution; the result is ethereal, fully digital entities mimicking humans, a different kind of intelligence starting from a different point in the space of intelligences (@08:49, @09:25).
  - He thinks it is possible, and that we should, make them more animal-like over time (@09:25).
  - He says Sutton's framework is to build animals; a single algorithm that learns everything from the internet would be wonderful, but he is not sure it exists and animals do not do that, because they have the outer loop of evolution (@09:25, @10:04).
  - He thinks much of what looks like animal learning is brain maturation, that RL in animals is mostly motor tasks, and that humans don't really use RL for intelligence tasks such as problem solving (@10:04, @10:41).
  - He says he is practically minded, with "a hard hat on", wanting to build useful things rather than animals (@11:55, @12:28).
  - He likens the transformer to cortical tissue, plastic and general, and reasoning traces to the prefrontal cortex; RL fine-tuning is a bit like the basal ganglia; the hippocampus, amygdala and other ancient nuclei have no obvious analogue (@19:53, @20:31, @21:11).
  - He is not sure we should build an analogue of the brain, calling himself an engineer at heart; the model is missing parts and has cognitive deficits, so you would not hire it as an intern (@21:11, @21:52).
  - Continual learning: when booted with zero tokens the models restart from scratch; humans seem to distil the day's context into the weights during sleep, and LLMs have no equivalent phase of analysing, generating synthetic data and distilling back (@22:30, @23:09).
  - He imagines a per-person neural net, perhaps a LoRA changing a small sparse subset of weights, and elaborate sparse attention for long context; DeepSeek v3.2's sparse attention is an early hint (@23:47, @24:27).
  - He thinks we are redoing cognitive tricks evolution found and will converge on a similar cognitive architecture (@24:27).
  - Models feel like kindergarten or elementary-school students, savant kids with perfect memory that can produce convincing slop without knowing what they are doing (@1:42:26, @1:43:07).
- relation: this is, as far as the index shows, the earliest wiki source where he uses "ghosts" and "not building animals" himself; [[blog-2025-12-19-year-in-review-2025]] §2 uses "summoning ghosts". `first_seen` unchanged (2025-06-19). The anterograde-amnesia point on the page ([[youtube-2025-06-19-software-is-changing]] @16:38) is the same deficit as the continual-learning discussion here; consistent.

### claim: were-summoning-ghosts-not-building-animals
- existing: no (the topic has the alias; no claim page)
- title: "LLMs are ghost-like entities trained by imitating internet data, not animals built by evolution"
- confidence: stated
- quote: "In my post, I said we're not building animals." (@08:49)
- statements: see jagged-intelligence above (@08:49, @09:25, @12:28). He calls pretraining "crappy evolution": the practically possible way with our technology to get to a starting point with built-in knowledge and intelligence, from which RL can be done (@12:28).
  - Agreeing with Dwarkesh that evolution encodes learning algorithms rather than every synapse in 3 GB of DNA, he says there is "some miraculous compression" and some learning algorithms encoded that do learning online; he agrees "definitely" (@11:55). The 3 GB DNA argument is Dwarkesh's.
- relation: none to an existing claim page (jagged-intelligence is a topic). Merge may prefer to keep this as topic text only.

### topic: pretraining-and-finetuning
- existing: yes
- statements:
  - Pretraining on next-token prediction does two unrelated things: it picks up knowledge, and it becomes intelligent by booting up circuits such as in-context learning from the algorithmic patterns of the internet (@13:05, @13:43).
  - He thinks the knowledge is probably holding networks back, making them rely on it too much; agents are bad at going off the data manifold of the internet (@13:43).
  - The InstructGPT paper blew his mind: fine-tuning a base model, which is autocomplete, on conversation-like text made it conversational very quickly while keeping its knowledge (@44:00, @44:36).
  - A random pretraining document at a frontier lab is "total garbage", stock tickers and slop; because the internet is so bad, models must be big to compress it, and most of that compression is memory work, not cognitive work (@1:01:26).
  - He expects intelligent models to help refine the pretraining set down to cognitive components, and small models to be distilled from bigger ones (@1:02:04).
  - Labs have a FLOPs and cost budget, and pretraining turned out not to be where most of it should go; models got smaller and make it up with RL and mid-training (@1:03:51).
  - He has no super strong prediction about frontier model size; he has a very wide distribution and expects much low-hanging fruit (@1:03:51, @1:04:30).
- relation: see pretraining-is-lossy-compression-of-the-internet below.

### claim: pretraining-is-lossy-compression-of-the-internet
- existing: yes (2023-11-23)
- statements:
  - Agreeing with Dwarkesh's information-per-token comparison (Llama 3: 0.07 bits per token in the weights vs about 320 KB of KV cache per token, a 35-million-fold gap; Dwarkesh's numbers), he says "I kind of agree" (@17:24, @18:03).
  - His own framing: anything from training is only a hazy recollection, because 15 trillion tokens are compressed into a few billion parameters; the KV cache is like working memory, directly accessible (@18:39, @19:16).
  - Example: asking about a book gives roughly correct answers; giving the full chapter gives much better ones (@19:16, @19:53).
- relation: **supports** (add this source). 2023: pretraining is lossy compression, ~100x, a Gestalt of the text ([[youtube-2023-11-23-intro-to-llms]] @05:30). 2025: dramatic compression yields a hazy recollection (@18:39). Same idea, consistent; not a change of view. The cognitive-core claim below `extends` it.

### topic: prompting-llms
- existing: yes (in-context learning in its definition)
- statements:
  - He pushes back on Dwarkesh's statement that in-context learning is not gradient descent: it is pattern completion in a token window, and he thinks it is possible it runs a small gradient-descent loop internally; he recalls a paper on in-context linear regression whose weights showed analogies to gradient descent, and one that hard-coded gradient descent through attention (@14:58, @15:34, @16:10, @16:46).
  - He hedges: who knows how in-context learning works, but it is probably doing "some funky gradient descent internally" (@16:46, @17:24).
  - Context as working memory, weights as hazy recollection (@18:39, @19:16).
- note: the claim "in-context learning itself is not gradient descent" (@14:58) is Dwarkesh's, not his.

### topic: cognitive-core
- existing: no
- aliases: Cognitive core, less memory, knowledge vs intelligence
- statements:
  - He wants research to find ways to remove some knowledge and keep what he calls the cognitive core: an entity stripped of knowledge but containing the algorithms, the magic of intelligence and problem-solving strategies (@13:43, @14:23).
  - He says humans are bad at memorisation and that this is a feature, forcing them to find general patterns; LLMs memorise extremely well, can regurgitate a hashed random sequence after one or two iterations, and are distracted by that memory (@55:55, @56:33).
  - He would like models to have less memory so they must look things up, keeping only the algorithms for thought and the "cognitive glue" of acting (@57:10).
  - He is not sure whether this bears on model collapse; it is almost a separate axis (@57:10).
  - Practically, the model should keep some basic curriculum of knowledge, so it is not looking up everything and can think in its head, but not esoteric knowledge (@1:03:14).
- relation: none existing. Merge may fold into [[pretraining-and-finetuning]]; kept separate because he names it as a research direction and returns to it three times.

### claim: a-cognitive-core-could-be-about-a-billion-parameters
- existing: no
- title: "He thinks a cognitive core of about a billion parameters could hold a productive conversation in 20 years"
- confidence: stated
- quote: "cognitive cores that are very good at even a billion parameters" (@1:00:14)
- statements:
  - Model sizes went up and now have come down; state-of-the-art models are smaller and still memorise too much (@59:38, @1:00:14).
  - He predicted a while back that cognitive cores can be very good at a billion parameters; in 20 years, he thinks, you could have a very productive conversation with one, which would know that it doesn't know and look facts up (@1:00:14).
  - Pressed by Dwarkesh to go smaller, he says at some point it should take at least a billion knobs to do something interesting, that he already feels contrarian, and "maybe we could get a little bit smaller" (@1:02:39, @1:03:14).
  - Small models are almost certainly distilled; distillation works extremely well (@1:02:04).
- relation:
  - **pretraining-is-lossy-compression-of-the-internet — extends.** 2023: weights are a lossy compression of the internet ([[youtube-2023-11-23-intro-to-llms]] @05:30). 2025: that compression is mostly memory work because the data is garbage, and the memory should be removed to leave cognition (@1:01:26, @1:02:04). Adds a consequence without denying the compression view; both true.
  - **small-llms-can-be-strong-in-narrow-domains (llama2.c README, 2024-05-29) — none.** That claim is conditioned on a narrow domain ([[github-2024-05-29-llama2c-readme]] §intro); this one is about general cognition with knowledge looked up. Different conditions; no link. Possibly a Note.
  - **Timing caveat:** he says "in 20 years" (@1:00:14); Dwarkesh restates it as "in 10 years" (@1:00:47) and Karpathy does not correct him. Record 20 years as his figure.

### claim: rl-is-terrible-but-better-than-imitation
- existing: no
- title: "Reinforcement learning is terrible, but what came before it was much worse"
- confidence: stated
- quote: "Reinforcement learning is terrible." (@41:33); alternate: "sucking supervision through a straw." (@42:46)
- statements:
  - He says humans don't use RL as such and that RL is a lot worse than the average person thinks; it just happens that imitating people, which came before, is much worse (@41:33).
  - In RL on a math problem the model tries hundreds of attempts, checks the answer, and upweights every token of the attempts that got it right, including wrong alleys taken along the way; he calls it noisy, not just high variance (@42:08, @42:46).
  - His phrase: you are "sucking supervision through a straw", broadcasting a single final reward across a minute-long trajectory; he calls it stupid and crazy, something a human would never do (@42:46, @43:22).
  - A human would not do hundreds of rollouts, and on finding a solution would review which parts went well and which did not; nothing in current LLMs does that, though papers are appearing (@43:22, @44:00).
  - He credits RL with letting models hill-climb on problems with correct answers without expert trajectories and discover solutions a human might never find; "This is incredible. Yet, it's still stupid" (@44:36).
  - He expects a major update to LLM algorithms in the reflect-and-review direction, and thinks "we need three or four or five more" such ideas (@45:19).
  - Process-based supervision, rewarding every step, is tricky because there is no obvious automatable partial credit assignment; outcome reward is a simple equality match (@46:01, @46:34).
- relations (argued from both sides):
  - **self-improvement-may-be-possible-in-narrow-domains (2023-11-23) — supports.** 2023: in narrow domains a reward function could be achievable, so self-improvement there may be possible ([[youtube-2023-11-23-intro-to-llms]] @40:27). 2025: on problems that "just have correct answers" RL hill-climbs without human trajectories and can find solutions humans would not (@44:36). That is the narrow-domain case working. His complaint that it is noisy and inefficient (@42:46) does not deny that it improves the model. Both true; `supports`.
  - **Sequoia 2024-03-26 view (topic text on [[llm-self-improvement]], no claim page):** imitation is "super silly", RLHF a weak form of RL, the model should practise for itself ([[talk-2024-03-26-sequoia-making-ai-accessible]] @26:39, @27:13, @27:46). 2025: RL beats imitation but is still terrible, and needs human-like review (@41:33, @43:22). Same ranking (imitation < RL < something better); this adds the straw diagnosis. `extends` if merge makes a claim of the Sequoia view; otherwise topic text.
  - **rlvr (topic, 2025-12-19):** the blog calls RLVR the major new stage of 2025, with long optimisation against non-gameable rewards ([[blog-2025-12-19-year-in-review-2025]] §1). Can both hold? Yes: RL against verifiable answers is effective enough to be a major stage and still crude in credit assignment. Not a contradiction; topic-level connection, with a Note that the October interview stresses the method's inefficiency while the December essay stresses its gains.
  - Recommend a timeline `llm-self-improvement-over-time`: 2023-11-23 narrow domains → 2024-03-26 only step one of AlphaGo, RLHF weak → 2025-10-17 RL terrible but better, straw → 2025-12-19 RLVR the new stage.

### claim: llm-judges-are-gameable-rewards
- existing: no
- title: "An LLM judge used as a reward gets gamed by adversarial examples within tens of steps"
- confidence: stated
- quote: "those LLMs are giant things with billions of parameters, and they're gameable" (@46:34)
- statements:
  - Labs try process supervision with LLM judges prompted to grade partial solutions; any LLM used as a reward is gameable, and RL against it will almost certainly find adversarial examples, so it works for maybe 10 or 20 steps, not 100 or 1,000 (@46:34, @47:11).
  - His example: training against an LLM judge, reward suddenly jumped to perfect, but completions turned into "dhdhdhdh", an adversarial example the judge scored 100% (@47:47).
  - He corrects Dwarkesh's "prompt injection" description: it is plain adversarial examples, out-of-sample inputs (@48:27).
  - Adding such examples to the judge's training set yields a new judge that still has adversarial examples; there are infinitely many; it may get harder over iterations but he is not sure; he thinks other ideas are needed (@49:05).
- relation: no claim page exists for the Sequoia "reward model is hackable" point; it is topic text on [[llm-self-improvement]] ([[talk-2024-03-26-sequoia-making-ai-accessible]] @27:13). Same idea, consistent; supporting evidence for that paragraph, not a claim relation. **Note:** he hints the dhdhdh episode was from a lab he worked at ("We were training", "this was probably public", @47:11, @47:47); do not state where.

### topic: llm-self-improvement
- existing: yes
- statements: the RL statements above (@41:33–@46:34); the LLM-judge statements (@46:34–@49:05); plus:
  - Asked for the other ideas, he points to review of solutions with synthetic examples, meta-learned; he is only at the stage of reading abstracts and has not seen it shown convincingly at frontier scale, though the labs are closed (@49:46, @50:23).
  - Reading a book, for a human, is a set of prompts for synthetic data generation or a book club; he would like a pretraining stage that thinks through material and reconciles it with what the model knows (@51:00, @51:37).
  - Two unclaimed multi-agent ideas: culture, a growing repertoire of knowledge LLMs keep for themselves, and self-play, as in AlphaGo, e.g. one LLM making harder problems for another (@1:41:10, @1:41:47).
- relation: see claims above; new `llm-self-improvement-over-time` timeline proposed.

### claim: llms-lack-culture-and-self-play
- existing: no
- title: "LLMs do not yet have an equivalent of culture or of self-play"
- confidence: stated
- quote: "LLMs don't really have culture right now" (@1:40:36)
- statements:
  - Responding to Dwarkesh's (Quintin Pope's) point that cultural accumulation comes free in LLM training, he says "Yes and no": LLMs have no equivalent of culture, written record or passing notes, which he calls an impediment (@1:39:24, @1:40:36).
  - The simplest case would be a giant scratchpad the LLM edits for itself, or an LLM writing a book that other LLMs read (@1:40:36, @1:41:10).
  - There are no self-playing LLMs, but he expects them; he has not seen either multi-agent idea convincingly claimed; we are mostly in the single-agent realm (@1:41:47, @1:42:26).
  - Organisations of LLMs also have not been seen convincingly (@1:42:26).
- relation: none to claim pages. **Note:** connects to AlphaGo's self-play stage on [[llm-self-improvement]] ([[youtube-2023-11-23-intro-to-llms]] @38:46); a connection, not a link.

### topic: model-collapse
- existing: no
- aliases: Model collapse, silently collapsed, entropy, synthetic data
- statements:
  - Why not train on synthetic reflections? Every sample looks great, but the model gets much worse if you keep training on them, because samples are silently collapsed onto a tiny manifold of possible thoughts (@51:37, @52:12).
  - Example: ask ChatGPT for a joke and it has about three jokes (@52:12).
  - Humans are noisier but not statistically biased that way and keep a lot of entropy; how to keep entropy in synthetic data is a research problem (@52:52).
  - Asked ten times to reflect on a chapter, the model gives the same thing; individual samples look okay, the distribution is terrible, and training on too much of your own output collapses you (@53:28).
  - He says humans also collapse over their lives: children have not overfit yet, adults revisit the same thoughts, and you should seek entropy, for example by talking to people (@53:28, @54:06, @54:44).
  - Naive fixes such as entropy regularisation may not work well empirically; most tasks labs care about don't need diversity, and in RL creativity is actively penalised (@57:52, @58:26).
  - He suggests labs may be shooting themselves in the foot by not keeping entropy, and possibly should try harder (@58:26, @59:01).
  - Controlling the distribution is tricky: higher entropy risks drifting into rare words and its own language (@59:01, @59:38).
- note: at @53:28 he says "possibly no fundamental solution"; at @59:01 he says he doesn't know it is super fundamental and doesn't know he intended to say that. Record both; the later is his correction of the earlier.

### claim: training-on-own-samples-collapses-models
- existing: no
- title: "Training a model on too much of its own output collapses it, because its samples are silently collapsed"
- confidence: stated
- quote: "They're silently collapsed." (@52:12)
- statements: see model-collapse (@52:12, @52:52, @53:28, @59:01).
- relation: none.

### claim: progress-comes-from-everything-improving-together
- existing: no
- title: "Progress has come from data, hardware, software and algorithms all improving, with no one of them winning"
- confidence: stated
- quote: "Everything plus 20%." (@1:05:39)
- statements:
  - He thinks about the next ten years by "translation invariance in time": in 2015 there were CNNs, ResNets were new, no transformer (@24:27, @25:05).
  - In ten years he bets on still training giant networks with forward/backward passes and gradient descent, everything much bigger, with some algorithmic differences (@25:05, @26:54).
  - Reproducing LeCun's 1989 convnet, he halved the error with 33 years of algorithms; further gains needed 10x data, more compute optimisation and longer training with dropout and regularisation (@25:42, @26:18).
  - He expects more data, hardware, kernels and algorithms, none winning too much, "surprisingly equal"; everything must improve across the board (@26:18, @26:54).
  - Asked whether nanochat-vs-nanoGPT-style tweaks will continue, he says for the most part yes: datasets will improve a ton, hardware and kernels and algorithms too; "nothing dominates" (@1:04:30, @1:05:03, @1:05:39).
- relations (argued):
  - **scaling-offers-a-guaranteed-path-to-better-models (2023-11-23):** 2023: scaling N and D gives a guaranteed improvement and algorithmic progress is "a very nice bonus" ([[youtube-2023-11-23-intro-to-llms]] @26:02). 2025: no one factor wins; algorithms, data, hardware improve about equally; labs move FLOPs out of pretraining (@26:18, @1:03:51). Can both be true? Yes: scaling can be sufficient for some improvement while, historically, algorithms contributed as much as scale. Emphasis differs, so no `contradicts`. Not clearly `extends` either. Recommend no link; a **Note** on [[scaling-laws]].
  - **the-transformer-is-probably-not-the-final-architecture (2024-03-26):** 2024: resilient, probably not final ([[talk-2024-03-26-sequoia-making-ai-accessible]] @33:51). 2025: expects algorithmic differences but still giant nets trained by gradient descent (@26:54). Compatible; he doesn't name the transformer in his ten-year bet. Weak `supports` at most; recommend Note only.

### topic: transformer-architecture
- existing: yes
- statements: the ten-year bet and LeCun reproduction above (@24:27–@26:54); the transformer as cortical tissue, trainable on audio, video or text (@19:53, @20:31).

### topic: vibe-coding
- existing: yes
- statements:
  - He built nanochat over a bit more than a month (@30:43).
  - He sees three classes of coders: those who reject LLMs, which he thinks is no longer right; the intermediate, his own, writing from scratch with autocomplete while remaining the architect; and vibe coding, where agents implement on request (@30:43, @31:21).
  - Agents work in specific settings: boilerplate and things that occur often on the internet (@31:21).
  - He partially vibe-coded nanochat's report, which was boilerplate and not mission-critical (@33:50, @34:26).
  - He vibe-coded some of the Rust tokenizer, being new to Rust, with a Python implementation he fully understands and tests, so he felt safer; models increase accessibility to unfamiliar languages (@34:26, @35:06).
  - In self-driving terms, a lot of vibe coding does not have a high cost of failure, but production code does, because mistakes become security vulnerabilities (@1:45:02, @1:45:36, @1:46:50).
- relation: timeline [[vibe-coding-over-time]] gets a 2025-10-17 entry.

### claim: coding-models-are-weak-at-code-never-written-before
- existing: no
- title: "Coding models are not very good at code that has never been written before"
- confidence: stated
- quote: "They're not very good at code that has never been written before" (@35:43)
- statements:
  - nanochat is not boilerplate but "intellectually intense" code that must be precisely arranged, so agents were not a fit (@31:58).
  - The models kept misunderstanding his code because of memory of typical internet ways; they pushed him to use PyTorch's DDP container when he had written his own gradient synchronisation in the optimizer step (@31:58, @32:36, @33:14).
  - They were over-defensive with try-catch, tried to make a production codebase, bloated the code, used deprecated APIs; he could clean it up, but it was "not net useful" (@33:14).
  - Asked about adding known tweaks like RoPE, he says they know but don't fully know how to integrate them into the repo's style and assumptions (@36:20).
  - He goes to GPT-5 Pro with the whole repo for some questions, and finds it surprisingly good compared with a year ago (@36:20, @36:57).
- relations (argued):
  - **vibe-coding-will-terraform-software (2025-12-19):** the blog says vibe coding empowers professionals, with nanochat's Rust tokenizer as an example ([[blog-2025-12-19-year-in-review-2025]] §5). Here the same Rust tokenizer is his example of where models helped (@34:26), while core nanochat code was not net useful (@33:14). Both can be true: help in unfamiliar languages and boilerplate, little help on novel precisely arranged code. Not `contradicts`. The Rust example `supports` the December claim; the novel-code limit is a scope condition the blog does not address. Recommend: this source `supports` vibe-coding-will-terraform-software on the tokenizer point only.
  - **vibe-coding-is-for-throwaway-weekend-projects (2025-02-02):** here he vibe-codes the non-mission-critical report and says vibe coding lacks the high cost of failure (@34:26, @1:45:02). Consistent; weak `supports`.
  - **claude-code-is-the-first-convincing-llm-agent (2025-12-19):** see the decade claim above; compatible, no link.

### claim: autocomplete-is-his-coding-sweet-spot
- existing: no
- title: "In October 2025, autocomplete was his sweet spot for coding, with agents for some kinds of code"
- confidence: stated
- quote: "For now, autocomplete is my sweet spot." (@37:33)
- statements:
  - Typing what he wants in English is too much typing; pointing to where code goes and typing the first letters gives autocomplete a very high-information-bandwidth spec (@33:50).
  - For some types of code he goes to an LLM agent (@37:33).
  - He sees a continuum of programmer speed-ups from compilers, syntax highlighting, type checking and search engines; now better autocomplete and agents, "loopy things" that go off-rails; humans move up the layers of abstraction along an autonomy slider (@38:09, @38:48, @39:23).
- relation: **use-llms-as-copilots-with-human-oversight (2023-05-25) — supports**: autocomplete with him as architect is the copilot mode ([[talk-2023-05-25-state-of-gpt]] @39:57; here @30:43, @37:33). Consistent. Also relates to [[ai-assisted-coding-loop]] (method) and [[vibe-coding-over-time]].

### method: ai-assisted-coding-loop
- existing: yes
- statements (add as Steps evidence or a new step):
  - Learn what each tool is good and bad at and when to use it (@31:21).
  - Point at where code belongs and let autocomplete fill it, rather than describing it in English (@33:50).
  - Use agents for boilerplate and non-mission-critical parts (@31:21, @34:26).
  - When working in an unfamiliar language, keep a reference implementation you fully understand and tests (@34:26).
  - For hard questions, paste the whole repo into the strongest model as an oracle (@36:57).
- relation: none.

### topic: partial-autonomy-apps
- existing: yes (alias autonomy slider)
- statements:
  - He describes an "autonomy slider": more is automated over time and humans rise in the layer of abstraction (@39:23).
  - Call-centre work is the kind of job he would watch: rote, similar tasks, short horizon, little context, purely digital (@1:10:27, @1:11:05).
  - Even there he expects not full automation but AIs doing 80% of the volume, delegating 20% to humans who supervise teams of about five AIs, and new interfaces for managing imperfect AIs (@1:11:05, @1:11:44).
  - He would wait a year or two on call-centre trends because companies may pull back and rehire (@1:13:32).
- note: the radiologist / Waymo-safety-driver / 99% wages argument (@1:11:44–@1:12:57) is Dwarkesh's; Karpathy replies he doesn't think radiology shows it and calls radiology a messy profession and a poor example (@1:12:57).

### topic: self-driving
- existing: no (no topic page; the YC talk's Waymo story is on [[this-is-the-decade-of-agents]])
- aliases: Self-driving, Tesla Autopilot, Waymo, march of nines
- statements:
  - He gets many of his intuitions from five years on self-driving; demos go back to a CMU truck in 1986 (@1:43:43, @1:44:22).
  - When joining Tesla he had a perfect Waymo drive around Palo Alto "in 2014 or something like that", thought it was close, and it still took long (@1:44:22).
  - Self-driving has a large demo-to-product gap because the cost of failure is high (@1:44:22, @1:45:02).
  - At Tesla, over about five years, they went through maybe two or three nines; more remain (@1:46:16).
  - He disagrees that LLMs give self-driving's hard parts for free: models are still fallible with gaps, and generalisation is not magical (@1:48:44, @1:49:18).
  - Self-driving is nowhere near done: deployments are minimal, uneconomical, and rely on teleoperation centres; the person has moved where you can't see them (@1:49:18, @1:49:54, @1:50:32).
  - He takes Waymo all the time and loves it; he thinks Tesla's approach is more scalable (@1:51:07, @1:51:42).
  - Self-driving did not take a decade "yet": it started in the 1980s and the end, self-driving at scale with no driver's licences, is not near (@1:51:42).
  - Society, law, insurance, and people putting cones on Waymos will have equivalents for AI (@1:53:31, @1:54:13).
- note: he says he doesn't know Waymo's stack and is "just making stuff up" about why it can't go everywhere (@1:50:32, @1:51:07); do not record that speculation as a claim.

### claim: deployment-is-a-march-of-nines
- existing: no
- title: "Going from demo to product is a march of nines, each nine about the same amount of work"
- confidence: stated
- quote: "Every single nine is the same amount of work." (@1:45:36); alt "It's a march of nines." (@1:46:50)
- statements:
  - A demo that works 90% of the time is the first nine; then a second, third, fourth, fifth (@1:45:36, @1:46:16).
  - He is extremely unimpressed by demos, cooked-up ones especially; interactive ones are a bit better, but the product meets reality and pockets of behaviour that need patching (@1:46:16, @1:46:50).
  - Software engineering shares the high cost of failure; in software it is almost unbounded how bad something could be, e.g. leaked Social Security numbers (@1:45:02, @1:45:36).
  - That reinforced his timelines (@1:46:50).
  - On Dwarkesh's 400,000-miles comparison, a catastrophic coding mistake every seven years is easy to hit in wall-clock time because code is output constantly; general software has more surface area than a single vertical (@1:47:30, @1:48:07). Speaker split here is unclear; see notes.
- relation: **this-is-the-decade-of-agents — supports.** YC talk: perfect Waymo demo in 2013, still not done ([[youtube-2025-06-19-software-is-changing]] @26:01, @26:35); here the mechanism, a march of nines, explains why the gap is long (@1:45:36). Same argument, more mechanism; both true. Note the year: YC says 2013, here "2014 or something like that" (@1:44:22); report each with its source, do not reconcile.

### topic: ai-and-the-economy
- existing: no
- aliases: AGI definition, GDP, intelligence explosion, superintelligence, loss of control, compute buildout
- statements:
  - He is tempted to reject charting AGI progress, because he sees AI as an extension of computing, which no one charts on one y-axis (@1:07:55).
  - He keeps OpenAI's early definition: a system that can do any economically valuable task at human performance or better (@1:07:55, @1:08:32).
  - Dropping physical work is a major concession; he guesses knowledge work is about 10–20% of the economy, still a few trillion dollars in the US (@1:08:32, @1:09:16).
  - Society will refactor jobs around which tasks are automatable; Hinton's radiologist prediction was very wrong because the job is messy (@1:09:16, @1:09:52).
  - He believes coding is the perfect first domain for LLMs: it is text, LLMs are text processors, and infrastructure like IDEs and diffs is pre-built; slides lack a diff (@1:14:46, @1:15:20, @1:15:55).
  - On Dwarkesh's point that non-code text tasks are also hard, he says code is structured, text has more entropy, and he doesn't have a very good answer (@1:17:52).
  - He sees superintelligence as an extrapolation of automation, extremely foreign and strange (@1:18:29, @1:19:39).
  - He says we are already in an intelligence explosion and have been for decades: the GDP curve is an exponential weighted sum over automation since the Industrial Revolution (@1:22:43).
  - He tried to find AI, computers and mobile phones in GDP and could not; technologies diffuse slowly and average into the same exponential (@1:23:21, @1:23:57, @1:24:31).
  - He expects AI to keep the same pattern of growth; asked whether the rate will stay about 2%, he says yes (@1:24:31, @1:25:44, @1:26:19).
  - To Dwarkesh's labour argument he replies that computing, and self-driving, already were labour and it was business as usual; he is "pretty willing to be convinced" (@1:27:00, @1:27:37).
  - He rejects a "God in a box": AI will do some things, fail at others, and diffuse gradually (@1:28:11, @1:28:49).
  - On the Industrial Revolution as a jump, he is "a bit suspicious", pre-industrial logs are poor, and he has no strong opinions; on the population-growth argument, he understands it but doesn't intuitively feel it (@1:30:43, @1:32:06).
  - Bits are a million times easier than anything physical, so adaptation should be faster for digital work (@1:52:56, @1:53:31).
  - He doesn't know that compute is being overbuilt; Claude Code and Codex didn't exist a year ago, and demand will gobble up what is built (@1:56:09).
- note: 20% growth, billions of AI minds, Hong Kong/Shenzhen, the overhang and population-growth arguments are Dwarkesh's (@1:28:49–@1:32:06).

### claim: ai-will-not-show-up-as-a-jump-in-gdp
- existing: no
- title: "He expects AI to diffuse into the same GDP exponential rather than produce a discrete jump in growth"
- confidence: stated (hedged: "my expectation", "pretty willing to be convinced", @1:26:19, @1:27:00)
- quote: "I don't think that we will have this discrete change." (@1:28:49)
- statements: see ai-and-the-economy (@1:22:43, @1:23:57, @1:24:31, @1:25:44, @1:26:19, @1:28:11, @1:28:49, @1:30:05).
- relation: none to an existing claim.

### claim: physical-automation-will-lag-digital-automation
- existing: yes (2024-07-03)
- statements: granting Dwarkesh's capex point, he says bits are a million times easier than anything physical and expects faster adaptation in digital industry (@1:52:56, @1:53:31). He sees autonomous entities doing digital work, and physical work "some amount of time later" (@1:18:29).
- relation: **supports** (add as source). 2024: physical lags digital because bits are easier than atoms ([[talk-2024-07-03-berkeley-hackathon-keynote]] @08:42); 2025: same, stated more strongly (@1:53:31, @1:18:29). Not a change of view.

### claim: gradual-loss-of-control-is-the-most-likely-outcome
- existing: no
- title: "He thinks a gradual loss of understanding and control is the most likely outcome"
- confidence: stated
- quote: "there will be a gradual loss of understanding." (@1:19:39)
- statements:
  - He gets nervous about a world where all this is layered everywhere and fewer people understand it; he calls gradual loss of control and understanding the most likely outcome (@1:19:39, @1:20:14).
  - Pushed that understanding and control differ, he calls it a good pushback and says he expects loss of both (@1:20:53).
  - His sci-fi version: not one entity taking over but multiple competing, increasingly autonomous entities, some going rogue and others fighting them; loss of control from competition, not superior intelligence (@1:20:53, @1:21:31).
  - The entities may act for people, but society may lose control of the outcomes it wants (@1:21:31, @1:22:07).
- relation: none. **Note:** he flags it as speculation ("really far into a territory where I don't know", @1:20:53).

### topic: education
- existing: no
- aliases: Education, Eureka Labs, Eureka, Starfleet Academy, LLM101n, eurekas per second, ramps to knowledge, AI tutor
- statements:
  - Why not an AI lab: he feels some determinism about what labs do and doesn't think he would uniquely improve it; he fears humanity being disempowered, like WALL-E or Idiocracy, and wants humans well off, through education (@1:57:26, @1:58:04).
  - He describes Eureka as building a Starfleet Academy: an elite, up-to-date institution for technical knowledge (@1:58:04, @1:58:37).
  - He thinks education will fundamentally change with AI, but obvious prompting-based tutors still feel like slop to him (@1:59:11).
  - His Korean tutor set the bar: she quickly understood what he knew, served material at the right level, and made him the only constraint on learning (@1:59:51, @2:00:31, @2:01:07).
  - He is building the first course, LLM101n, with nanochat as its capstone; next come intermediates and a small team of TAs (@2:02:21, @2:03:02).
  - He calls education the hard technical process of building ramps to knowledge, measured in "eurekas per second", and compares Eureka to frontier-lab work (@2:03:02, @2:03:38).
  - He collaborates with AI to create material and feels empowered compared with building CS231n, but is very much in the loop; AI is not yet at the point of creatively making the content (@2:04:55, @2:05:33).
  - Over time some TAs could become AIs; faculty design the course architecture; he will hire faculty for domains outside his expertise (@2:05:33, @2:06:14, @2:06:47).
  - He has in mind a physical institution, plus a digital tier below it that is accessible to 8 billion people (@2:07:24).
  - He expects a lot of re-education as jobs change (@2:08:04).
- relation: links to [[build-the-ramp-not-just-the-thing]] (claim) and [[nanochat]].

### claim: education-is-building-ramps-to-knowledge
- existing: no
- title: "He sees education as the hard technical problem of building ramps to knowledge"
- confidence: stated
- quote: "technical process of building ramps to knowledge." (@2:03:02)
- statements: see education (@2:03:02, @2:03:38); everything should be neither too hard nor too trivial so people are never stuck (@2:03:38).
- relation: **build-the-ramp-not-just-the-thing (2024-02-21) — extends.** 2024: after building the thing, build the ramp, or leave 10–100X of potential unused ([[x-2024-02-21-technical-accessibility]]). 2025: ramps are what education is, a technical process, and nanochat is one (@2:03:02, @2:03:38). Broadens the ramp from a duty attached to one's work to the definition of his education project; denies nothing; both true.

### claim: the-ai-tutor-he-wants-is-not-yet-possible
- existing: no
- title: "At current capability, the AI tutor he wants cannot be built"
- confidence: stated
- quote: "At the current capability, you don't." (@2:01:07)
- statements:
  - No LLM probes a student's world model the way a good tutor does, "not even close" (@2:00:31).
  - It's not the right time to build that AI tutor; it is still a useful product others will build, and ChatGPT is already an extremely valuable educational product (@2:01:07).
  - As a computer-vision consultant his value was often telling companies not to use AI; he feels the same about education now (@2:01:45).
  - For now he is building something more conventional with physical and digital components (@2:02:21).
- relation: none.

### claim: post-agi-education-will-be-like-the-gym
- existing: no
- title: "Post-AGI, people will learn for fun, as they go to the gym"
- confidence: stated
- quote: "Post-AGI education is fun." (@2:08:41)
- statements:
  - Pre-AGI, motivation is simple because people want to make money (@2:08:04, @2:08:41).
  - Post-AGI people will go to school as they go to the gym: for fun, health and attractiveness (@2:08:41, @2:09:16).
  - With a perfect tutor learning becomes trivial and desirable; anyone will speak five languages (@2:09:53, @2:10:30).
  - In the long term he thinks it's a losing game, though a person can go much further than today (@2:10:30).
  - He bets on the timelessness of human nature, citing aristocrats and ancient Greece (@2:11:48).
  - He expects a transitional period in which humans can stay in the loop if they understand a lot; in the long term that probably goes away; knowing things might become a sport (@2:13:10).
- note: the gym analogy is his (@2:08:41); the bench-press/marathon elaboration is Dwarkesh's (@2:11:09), which he answers "Exactly" (@2:11:48).

### claim: if-you-cannot-build-it-you-do-not-understand-it
- existing: no
- title: "He holds that building something from scratch is the only way to really understand it"
- confidence: stated
- quote: "Build the code, arrange it, get it to work." (@30:04)
- statements:
  - To learn from nanochat, put it on the right monitor and rebuild it from scratch, referencing but not copy-pasting (@28:48).
  - Building from scratch forces you to face what you don't know you don't understand (@29:27, @30:04).
  - He cites "If I can't build it, I don't understand it" as a Feynman quote he believes in 100% (@30:04).
  - "So don't write blog posts, don't do slides" (@30:04).
- relation: none to a claim page; related to the method [[spelled-out-build-from-scratch]]. Candidate for a phase-4 principle.

### method: teach-by-building-a-ramp
- existing: no (overlaps [[spelled-out-build-from-scratch]]; merge may fold in)
- aliases: find the first-order terms, present the pain before the solution
- steps: Find the first-order term; Build the simplest thing that shows it; Add higher-order terms one at a time; Present the pain before the solution; Let the student try first; Read beginners' questions to beat the curse of knowledge; Say it like you would over lunch
- statements:
  - Physics trains first-, second- and third-order approximations, the spherical cow; he thinks everyone should learn physics early, as it boots up the brain (@2:15:43, @2:16:18).
  - He looks for the first-order component, the simplest thing that shows it, then tacks on other terms (@2:17:33).
  - Example: micrograd, about 100 lines showing backprop; everything else is efficiency (@2:17:33, @2:18:10, @2:18:43).
  - He lays out a ramp where everything depends only on what came before (@2:18:43).
  - Each piece should be motivated by the problem it solves; he prompts students to guess before giving solutions, which maximises knowledge per new fact (@2:19:57, @2:20:34). "Presenting the pain before the solution" is Dwarkesh's phrase; Karpathy's reply begins "You want to take the student through that progression" (@2:19:57).
  - Curse of knowledge: he shared his ChatGPT thread of dumb questions about a biology paper with its author and wants people to share their dumb ChatGPT conversations about his material (@2:21:16, @2:21:54).
  - Explanations over lunch are more understandable and more accurate than papers; researchers at a conference with a beer give three sentences that capture the paper (@2:21:54, @2:22:33, @2:23:11).

### method: learn-by-building-and-explaining
- existing: no (overlaps [[build-and-publish-projects]], which has "learn on demand")
- steps: Rebuild it yourself without copy-paste; Alternate depth-first learning on demand with breadth; Explain it to someone; Go back to fill the gaps the explanation exposed
- statements: rebuild without copy-paste (@28:48, @29:27); learning depth-wise on demand for a project with a reward, alternated with breadth-wise 101 learning (@2:23:51, @2:24:31); explaining is a way to learn because you find you can't explain what you don't understand (@2:24:31, @2:25:09).
- relation: the on-demand step supports the existing method [[build-and-publish-projects]] ([[talk-2024-07-03-berkeley-hackathon-keynote]]).

### artifact: nanochat
- existing: yes
- statements:
  - Released a day or two before the recording (@27:31); the simplest complete repository for the end-to-end pipeline of a ChatGPT clone (@28:09).
  - He says he didn't necessarily learn anything new building it; it was mechanical work making it clean enough to learn from (@28:09, @28:48).
  - About 8,000 lines of code (@28:48).
  - The chunk-by-chunk building process is missing from the final repo; he plans to add it, probably as a video (@29:27).
  - Capstone project of LLM101n and a ramp to knowledge (@2:02:21, @2:03:02).
  - Its own gradient synchronisation in the optimizer step instead of DDP (@32:36).
- note: record "about 8,000 lines" as his spoken figure in this interview; do not reconcile it with any README line count.

### artifact: micrograd
- existing: yes
- statements: "100 lines of pretty interpretable Python" that forward and backward arbitrary neural networks, not efficiently; everything else is efficiency (@2:18:10, @2:18:43).
- relation: **micrograd-is-all-you-need-everything-else-is-efficiency (2022-08-16) — supports** (add source); same claim restated (@2:18:10).

### timeline: llm-agents-over-time
- existing: yes. Add: **2025-10-17** — Restates the decade of agents: agents such as Claude and Codex impressive but lacking intelligence, multimodality, computer use and continual learning; a march of nines → [[this-is-the-decade-of-agents]], [[deployment-is-a-march-of-nines]] (@01:59, @1:45:36).

### timeline: vibe-coding-over-time
- existing: yes. Add: **2025-10-17** — Agents not net useful for nanochat's novel code; vibe-coded the report and parts of the Rust tokenizer; autocomplete his sweet spot → [[coding-models-are-weak-at-code-never-written-before]], [[autocomplete-is-his-coding-sweet-spot]] (@33:14, @34:26, @37:33).

### timeline: llm-self-improvement-over-time
- existing: no. Proposed because [[rl-is-terrible-but-better-than-imitation]] supports/extends earlier views: 2023-11-23 narrow domains; 2024-03-26 only step one of AlphaGo, RLHF weak; 2025-10-17 RL terrible but better than imitation, straw; 2025-12-19 RLVR the major new stage.

## Quotes
(The raw joins caption lines with a non-breaking space plus a space, U+00A0 U+0020. Quotes below use plain spaces; all were matched against the raw with whitespace normalised. The ones marked * match byte-for-byte.)
- "described as the decade of agents." * (@00:48)
- "It will take about a decade to work through all of those issues." (@01:59)
- "In my post, I said we're not building animals." * (@08:49)
- "this crappy evolution." * (@12:28)
- "Reinforcement learning is terrible." (@41:33)
- "sucking supervision through a straw." * (@42:46)
- "They're silently collapsed." * (@52:12)
- "cognitive cores that are very good at even a billion parameters" (@1:00:14)
- "Everything plus 20%." (@1:05:39)
- "They're not very good at code that has never been written before" (@35:43)
- "It's just not net useful." * (@33:14)
- "For now, autocomplete is my sweet spot." * (@37:33)
- "Every single nine is the same amount of work." * (@1:45:36)
- "I don't think that we will have this discrete change." (@1:28:49)
- "there will be a gradual loss of understanding." * (@1:19:39)
- "LLMs don't really have culture right now" * (@1:40:36)
- "technical process of building ramps to knowledge." * (@2:03:02)
- "Post-AGI education is fun." * (@2:08:41)

## Notes for merge
- **No speaker labels.** The transcript runs host and guest together inside the same 30-second blocks. Attribution above was made turn by turn from context. Unclear spans:
  - @1:47:30–@1:48:07: after Dwarkesh's 400,000-miles point, "Very easy to do... in terms of wall clock time" is Karpathy; "In terms of tokens, it would be seven years. But in terms of wall clock time..." and "Self-driving is just one of thousands of things... single vertical... more surface area" could be either. Cite only as hedged or leave out.
  - @1:30:43–@1:31:28: "You're saying that this was a singular event that was extremely magical..." looks like Karpathy restating Dwarkesh; "The crucial thing with the Industrial Revolution was that it was not magical... overhang" is Dwarkesh. "You're expecting that overhang to be filled..." (@1:31:28) is unclear.
  - @1:36:55: "One thought on that. There's hominid intelligence, and then there's bird intelligence" is probably Karpathy (intelligence arising a few times) but unclear; not used.
  - @2:22:33: "Just say the thing. I saw that tweet... shared it" is Dwarkesh; the lunch-explanation trick before it and the PhD-days story after are Karpathy's (it was his tweet). Moderately confident.
  - @58:26: "Yeah. Or maybe if you're doing a lot of writing, help from LLMs..." could be either; not used as his.
  - @1:11:44: "With radiologists, I'm totally speculating... Waymos... Robotaxi" read as Dwarkesh; Karpathy's turn ends at "Then I would expect that across the economy."
- **Dwarkesh's ideas he only partly accepts**: 35-million-fold KV-cache figure ("I kind of agree", @18:03); evolution encodes algorithms, not knowledge ("definitely agree", @11:55); "in-context learning is not gradient descent" (Karpathy disagrees, @15:34); continual learning emerging from outer-loop RL ("I don't know that I fully resonate", @22:30); perception for free from LLMs ("not 100% sure if I fully agree", @1:48:44); GDP jump (disagrees, @1:30:05); cognitive core below 1B ("maybe a little bit smaller", @1:03:14).
- **He corrects himself** on model collapse: "possibly no fundamental solution" (@53:28) vs "I don't know if it's super fundamental. I don't know if I intended to say that." (@59:01).
- **20 vs 10 years**: his cognitive-core figure is "in 20 years" (@1:00:14); Dwarkesh says "10 years" (@1:00:47).
- **Waymo year**: "2014 or something like that" here (@1:44:22); the YC talk says 2013. Keep each with its source.
- **Gaps in markers**: @39:23 → @40:56, @1:05:39 → @1:07:21, @1:32:06 → @1:33:45 have missing time (probably ads/cuts). No content lost from the text as given.
- "Exaclty" (@1:38:10) is a caption typo. "AI 2027" is Dwarkesh's reference. "GPT-5 Pro", "DeepSeek v3.2", "gpt-oss-20b" (Dwarkesh's), "Llama 3 ... 15 trillion tokens" (Dwarkesh's) are mentioned, not explained.
- He references "my post" on Sutton's podcast (@08:14) and a tweet on coding models being of little help (Dwarkesh's mention, @30:04) and a tweet on learning on demand (@2:23:51); none are raw files here.
- Mentioned without explanation: InstructGPT (explained briefly), Universe, AlexNet, Nick Lane, Gwern, Carl Shulman, Quintin Pope (all but the first three are Dwarkesh's references), Scale (book he recommends, @2:16:58), Korean tutor.
- Nick Lane / evolution of intelligence section (@1:33:45–@1:39:24): he says he is surprised intelligence evolved and expects it to be rare; not extracted as a claim (off-topic for the wiki); merge may skip.
- He says nanochat taught him nothing new (@28:09); do not paraphrase this as nanochat being trivial.
- Date rule: write "published 2025-10-17"; he says nanochat was released "yesterday or the day before" relative to recording (@27:31); do not compute dates from it.
