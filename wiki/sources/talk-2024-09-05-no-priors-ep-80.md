---
type: source
raw_path: raw/talks/hM_h0UA7upI.md
published: 2024-09-05
medium: talk
summary: "No Priors podcast interview with Sarah Guo and Elad Gil covering self-driving as a lesson for AGI, Tesla versus Waymo, humanoid robots, the Transformer as a solved piece with data as the bottleneck, synthetic data, a small cognitive core, open models as a fallback, companies of LLMs, and his plans for AI-assisted education."
url: https://www.youtube.com/watch?v=hM_h0UA7upI
title: "No Priors Ep. 80 | With Andrej Karpathy from OpenAI and Tesla"
---
# No Priors Ep. 80 | With Andrej Karpathy from OpenAI and Tesla
Raw: [[raw/talks/hM_h0UA7upI]] · Original: https://www.youtube.com/watch?v=hM_h0UA7upI

A podcast interview; the captions do not label speakers. Lines that are the hosts' or unclear are not attributed to him on any page. He never says "Eureka Labs"; a host says "Eureka" (@41:01).

## Summary
A 44-minute podcast interview with hosts Sarah Guo and Elad Gil. He says self-driving has reached something like AGI a little bit, a decade after a near-perfect Waymo demo he dates to "2014 or so", but has not yet spread across the world, and he expects AGI to look similar; he thinks Tesla, with a software problem, is ahead of Waymo, with a hardware problem (@00:36, @01:07, @01:39, @02:11). He describes Tesla as a robotics company whose car stack transferred to the Optimus humanoid, and argues humanoids should start in their maker's own factory, then go to other businesses, then to consumers (@06:37, @07:11, @08:48). He says the Transformer is no longer the bottleneck, so activity has moved to datasets and loss functions; synthetic data is the future if its entropy is kept, and a cognitive core of a billion parameters or less may suffice (@16:29, @20:13, @27:27, @28:36). Asked about augmentation and market structure, he describes an exocortex, an oligopoly of closed platforms with an open one behind, and open models as a fallback (@22:59, @25:13, @26:19). He closes on education: AI as the front end of a course a teacher designs, education after AGI as something like the gym, and math, physics and CS for children (@32:21, @40:29, @42:08).

## Key points
- Self-driving reached AGI "a little bit", but the demo-to-product gap took a decade and globalisation has not happened; he expects AGI to look similar → [[self-driving]], [[there-is-a-massive-gap-between-demo-and-product]], [[llm-agents-over-time]]
- Tesla has a software problem, Waymo a hardware problem; software is easier, so he thinks Tesla is ahead → [[self-driving]], [[tesla-is-ahead-of-waymo-in-self-driving]]
- Tesla uses lidar and extra sensors at training time and distils into a vision-only test-time package → [[self-driving]]
- The neural net eats through the C++ stack piece by piece; intermediate predictions supply the supervision end-to-end needs → [[self-driving]], [[software-3-0]]
- Tesla is a robotics-at-scale company; early Optimus ran the car networks; one general platform, teleoperation, transfer between tasks → [[self-driving]]
- Humanoids go to your own factory first, then B2B, then B2C → [[humanoid-robots-should-start-in-your-own-factory]]
- The Transformer is a differentiable computer and scaling laws are largely its property; the architecture is no longer the bottleneck, data and loss function are → [[transformer-architecture]], [[scaling-laws]], [[the-architecture-is-no-longer-the-bottleneck]], [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]
- Internet data is a nearest neighbour of the inner-monologue traces you want; synthetic data must keep its entropy → [[pretraining-and-finetuning]], [[synthetic-data-is-the-future-if-you-keep-its-entropy]]
- Current models help build the next generation → [[llm-self-improvement]]
- Transformers may already be better than the brain in some ways; what holds them back is mostly data → [[transformer-architecture]]
- Oligopoly of closed platforms, open platforms behind, open models as a fallback → [[ai-ecosystem]]
- An exocortex; LLM systems may come to resemble companies of specialised models → [[llms-as-operating-systems]]
- A cognitive core of about a billion parameters or fewer, using tools to look things up → [[a-cognitive-core-could-be-a-billion-parameters-or-less]], [[small-llms-can-be-strong-in-narrow-domains]], [[llm-tool-use]]
- Teacher on the back end, AI as the front end to the student; the demo is near, the product far → [[ai-for-education]], [[ai-should-be-the-front-end-of-a-teacher-designed-course]]
- After AGI, education like the gym; children should mostly study math, physics and CS → [[ai-for-education]], [[post-agi-education-will-be-like-going-to-the-gym]]
- Same self-driving lesson as the decade-of-agents claim → [[this-is-the-decade-of-agents]]

## Fed pages
- [[self-driving]]
- [[ai-for-education]]
- [[transformer-architecture]]
- [[scaling-laws]]
- [[pretraining-and-finetuning]]
- [[llm-self-improvement]]
- [[ai-ecosystem]]
- [[llms-as-operating-systems]]
- [[software-3-0]]
- [[llm-tool-use]]
- [[there-is-a-massive-gap-between-demo-and-product]]
- [[tesla-is-ahead-of-waymo-in-self-driving]]
- [[humanoid-robots-should-start-in-your-own-factory]]
- [[the-architecture-is-no-longer-the-bottleneck]]
- [[synthetic-data-is-the-future-if-you-keep-its-entropy]]
- [[a-cognitive-core-could-be-a-billion-parameters-or-less]]
- [[ai-should-be-the-front-end-of-a-teacher-designed-course]]
- [[post-agi-education-will-be-like-going-to-the-gym]]
- [[this-is-the-decade-of-agents]]
- [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]
- [[small-llms-can-be-strong-in-narrow-domains]]
- [[llm-agents-over-time]]
- [[cognitive-core]]
- [[model-collapse]]
- [[training-on-own-samples-collapses-models]]
