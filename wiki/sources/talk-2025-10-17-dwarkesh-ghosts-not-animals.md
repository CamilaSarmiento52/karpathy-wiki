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

The transcript has no speaker labels. Dwarkesh Patel asks the questions and often argues the
other side; wiki pages attribute to Karpathy only turns that are clearly his, and leave out
the spans the digest marks unclear (for example @1:47:30–@1:48:07, @1:30:43–@1:31:28,
@1:36:55 and the second half of @58:26).

## Summary
A two-and-a-half-hour interview with Dwarkesh Patel, who asks the questions and often argues the other side. He says agents such as Claude and Codex are impressive but lack intelligence, multimodality, computer use and continual learning, and that working through this will take about a decade, a figure he gets from 15 years of watching predictions (@01:25, @01:59, @03:14). He contrasts LLMs, ghost-like entities trained by imitating internet documents, with animals built by evolution, calls pretraining "crappy evolution", and wants a cognitive core that keeps the algorithms of thought and sheds memorised knowledge (@09:25, @12:28, @13:43, @14:23, @57:10). He calls RL terrible, "sucking supervision through a straw", though better than the imitation that came before, explains why LLM judges are gameable and why training on a model's own samples collapses it (@41:33, @42:46, @47:11, @52:12). From building nanochat he says coding agents were not net useful for novel, precisely arranged code and that autocomplete is his sweet spot (@31:58, @33:14, @37:33). He uses self-driving to argue that going from demo to product is a march of nines, expects AI to show up as the same smooth GDP exponential rather than a jump, and describes Eureka as an effort to build ramps to knowledge, with nanochat as the capstone of the LLM101n course (@1:45:36, @1:22:43, @1:25:44, @2:02:21, @2:03:02).

## Key points
- Agents will take about a decade to work like an intern; the bottlenecks are cognitive → [[this-is-the-decade-of-agents]], [[llm-agents-over-time]]
- Atari RL and Universe went after agents too early, before LLM representations → [[early-agent-attempts-came-too-early]], [[partial-autonomy-apps]]
- We are building ghosts by imitation, not animals by evolution; pretraining is crappy evolution; Sutton's framework is to build animals → [[llm-research-summons-ghosts-not-animals]], [[pretraining-is-our-crappy-evolution]], [[bitter-lesson]], [[jagged-intelligence]]
- Pretraining picks up both knowledge and intelligence; the knowledge may hold models back → [[cognitive-core]], [[a-cognitive-core-could-be-a-billion-parameters-or-less]]
- Weights are a hazy recollection, the context window a working memory; in-context learning may run gradient descent inside → [[pretraining-is-lossy-compression-of-the-internet]], [[prompting-llms]]
- Models lack continual learning, culture and self-play → [[jagged-intelligence]], [[llms-lack-culture-and-self-play]]
- RL is terrible but everything before it was worse; outcome rewards are sucked through a straw → [[rl-is-terrible-but-better-than-imitation]], [[rl-sucks-supervision-bits-through-a-straw]], [[llm-self-improvement]], [[llm-self-improvement-over-time]]
- LLM judges as process rewards get gamed by adversarial examples → [[llm-judges-are-gameable-rewards]]
- Model outputs are silently collapsed, so training on synthetic reflections degrades the model → [[model-collapse]], [[training-on-own-samples-collapses-models]]
- Progress comes from data, hardware, kernels and algorithms improving together → [[progress-comes-from-everything-improving-together]]
- Building nanochat: agents good for boilerplate and unfamiliar languages, not for novel code; autocomplete is his sweet spot → [[vibe-coding]], [[ai-assisted-coding-loop]], [[nanochat]], [[coding-models-are-weak-at-code-never-written-before]], [[autocomplete-is-his-coding-sweet-spot]], [[vibe-coding-over-time]]
- Automation is an autonomy slider; call centres as the job to watch → [[partial-autonomy-apps]]
- Self-driving: demo to product is a march of nines, and self-driving is not done → [[self-driving]], [[there-is-a-massive-gap-between-demo-and-product]]
- AGI as any economically valuable task; AI continues the GDP exponential; bits are easier than atoms → [[ai-and-the-economy]], [[ai-will-not-show-up-as-a-jump-in-gdp]], [[physical-automation-will-lag-digital-automation]]
- Most likely outcome: a gradual loss of understanding and control → [[gradual-loss-of-control-is-the-most-likely-outcome]]
- Eureka: education is building ramps to knowledge; the AI tutor he wants is not yet possible; post-AGI education is like the gym → [[ai-for-education]], [[education-is-building-ramps-to-knowledge]], [[build-the-ramp-not-just-the-thing]], [[the-ai-tutor-he-wants-is-not-yet-possible]], [[post-agi-education-will-be-like-going-to-the-gym]]
- Build it yourself to understand it; find the first-order terms; explain to learn → [[if-you-cannot-build-it-you-do-not-understand-it]], [[learn-by-building-and-explaining]]

## Fed pages
- [[gpt-2-training-cost-falls-to-about-40-percent-a-year]]
- [[a-cognitive-core-could-be-a-billion-parameters-or-less]]
- [[ai-and-the-economy]]
- [[ai-assisted-coding-loop]]
- [[ai-for-education]]
- [[ai-will-not-show-up-as-a-jump-in-gdp]]
- [[autocomplete-is-his-coding-sweet-spot]]
- [[bitter-lesson]]
- [[build-the-ramp-not-just-the-thing]]
- [[coding-models-are-weak-at-code-never-written-before]]
- [[cognitive-core]]
- [[early-agent-attempts-came-too-early]]
- [[education-is-building-ramps-to-knowledge]]
- [[gradual-loss-of-control-is-the-most-likely-outcome]]
- [[if-you-cannot-build-it-you-do-not-understand-it]]
- [[jagged-intelligence]]
- [[learn-by-building-and-explaining]]
- [[llm-agents-over-time]]
- [[llm-judges-are-gameable-rewards]]
- [[llm-research-summons-ghosts-not-animals]]
- [[llm-self-improvement]]
- [[llm-self-improvement-over-time]]
- [[llms-lack-culture-and-self-play]]
- [[model-collapse]]
- [[nanochat]]
- [[partial-autonomy-apps]]
- [[physical-automation-will-lag-digital-automation]]
- [[post-agi-education-will-be-like-going-to-the-gym]]
- [[pretraining-is-lossy-compression-of-the-internet]]
- [[pretraining-is-our-crappy-evolution]]
- [[progress-comes-from-everything-improving-together]]
- [[prompting-llms]]
- [[rl-is-terrible-but-better-than-imitation]]
- [[rl-sucks-supervision-bits-through-a-straw]]
- [[self-driving]]
- [[self-improvement-may-be-possible-in-narrow-domains]]
- [[the-ai-tutor-he-wants-is-not-yet-possible]]
- [[there-is-a-massive-gap-between-demo-and-product]]
- [[this-is-the-decade-of-agents]]
- [[training-on-own-samples-collapses-models]]
- [[vibe-coding]]
- [[vibe-coding-over-time]]
- [[verifiability-drives-the-jagged-frontier]]
- [[autoresearch-found-real-improvements-to-nanochat]]
- [[he-now-delegates-most-coding-to-agents]]
- [[how-he-explains]]
