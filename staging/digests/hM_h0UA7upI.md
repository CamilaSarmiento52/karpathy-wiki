# Digest: No Priors Ep. 80 | With Andrej Karpathy from OpenAI and Tesla
- raw: raw/talks/hM_h0UA7upI.md · published: 2024-09-05 · medium: talk · words: ~11,000 (wc 11,009 incl. frontmatter)
- source slug: talk-2024-09-05-no-priors-ep-80

## Source page

```
---
type: source
raw_path: raw/talks/hM_h0UA7upI.md
published: 2024-09-05
medium: talk
summary: "No Priors podcast interview with Sarah Guo and Elad Gil covering self-driving as a lesson for AGI, Tesla versus Waymo, humanoid robots, the Transformer as a solved piece with data as the bottleneck, synthetic data and model collapse, a small cognitive core, AI as an exocortex, and his plans for AI-assisted education."
url: https://www.youtube.com/watch?v=hM_h0UA7upI
title: "No Priors Ep. 80 | With Andrej Karpathy from OpenAI and Tesla"
---
# No Priors Ep. 80 | With Andrej Karpathy from OpenAI and Tesla
Raw: [[raw/talks/hM_h0UA7upI]] · Original: https://www.youtube.com/watch?v=hM_h0UA7upI

## Summary
A 44-minute podcast interview with hosts Sarah Guo and Elad Gil. He says self-driving has reached something like AGI a little bit, a decade after a near-perfect Waymo demo, but has not yet spread across the world, and he expects AGI to look similar; he thinks Tesla, with a software problem, is ahead of Waymo, with a hardware problem (@00:36, @01:39, @02:11). He describes Tesla as a robotics company whose car stack transferred to the Optimus humanoid, and argues humanoids should start in their maker's own factory, then go to other businesses, then to consumers (@06:37, @07:11, @08:48). He says the Transformer is no longer the bottleneck, so activity has moved to datasets and loss functions; synthetic data is the future if its entropy is kept, and a cognitive core of a billion parameters or less may suffice (@16:29, @20:13, @27:27, @28:36). He frames AI as an exocortex, asks whether people will accept renting it, and says open models must keep progressing (@22:59, @25:45, @26:53). He closes on education: AI as the front end of a course a teacher designs, education after AGI as something like the gym, and math, physics and CS for children (@32:21, @40:29, @42:08).

## Key points
- Self-driving reached AGI "a little bit", but the demo-to-product gap took a decade and globalisation has not happened; he expects AGI to look similar → [[self-driving]], [[there-is-a-massive-gap-between-demo-and-product]]
- Tesla has a software problem, Waymo a hardware problem; software is easier, so he thinks Tesla is ahead → [[self-driving]], [[tesla-is-ahead-of-waymo-in-self-driving]]
- Tesla uses lidar and extra sensors at training time and distils into a vision-only test-time package → [[self-driving]]
- The neural net eats through the C++ stack piece by piece; intermediate predictions supply the supervision end-to-end needs → [[self-driving]], [[software-3-0]]
- Tesla is a robotics-at-scale company; early Optimus ran the car networks → [[humanoid-robots]]
- Humanoids go to your own factory first, then B2B, then B2C → [[humanoid-robots]], [[humanoid-robots-should-start-in-your-own-factory]]
- One general platform: fixed costs, easy teleoperation, transfer between tasks → [[humanoid-robots]]
- The Transformer is a differentiable computer and scaling laws are largely its property; the architecture is no longer the bottleneck, data and loss function are → [[transformer-architecture]], [[scaling-laws]], [[the-architecture-is-no-longer-the-bottleneck]]
- Internet data is a nearest neighbour of the inner-monologue traces you want; synthetic data must keep its entropy → [[pretraining-and-finetuning]], [[synthetic-data-is-the-future-if-you-keep-its-entropy]]
- Current models help build the next generation, a staircase of improvement → [[llm-self-improvement]]
- Transformers may already be better than the brain in some ways; what holds them back is mostly data → [[transformers-are-in-some-ways-better-than-the-brain]]
- AI as an exocortex, "not your weights, not your brain", open models as the fallback → [[ai-as-exocortex]], [[ai-ecosystem]], [[open-models-must-keep-progressing-as-a-fallback]]
- A cognitive core of about a billion parameters or fewer, using tools to look things up → [[a-cognitive-core-could-be-a-billion-parameters-or-less]], [[llm-tool-use]]
- LLM systems may come to resemble companies of specialised models → [[llms-as-operating-systems]], [[llm-systems-may-come-to-resemble-companies]]
- Teacher on the back end, AI as the front end to the student; the demo is near, the product far → [[ai-for-education]], [[ai-should-be-the-front-end-of-a-teacher-designed-course]]
- After AGI, education like the gym; children should study math, physics and CS → [[ai-for-education]], [[post-agi-education-will-be-like-going-to-the-gym]], [[children-should-mostly-study-math-physics-and-cs]]

## Fed pages
- [[self-driving]]
- [[humanoid-robots]]
- [[ai-as-exocortex]]
- [[ai-for-education]]
- [[transformer-architecture]]
- [[scaling-laws]]
- [[pretraining-and-finetuning]]
- [[llm-self-improvement]]
- [[ai-ecosystem]]
- [[llms-as-operating-systems]]
- [[software-3-0]]
- [[llm-tool-use]] (context only)
- [[there-is-a-massive-gap-between-demo-and-product]]
- [[tesla-is-ahead-of-waymo-in-self-driving]]
- [[humanoid-robots-should-start-in-your-own-factory]]
- [[the-architecture-is-no-longer-the-bottleneck]]
- [[synthetic-data-is-the-future-if-you-keep-its-entropy]]
- [[transformers-are-in-some-ways-better-than-the-brain]]
- [[a-cognitive-core-could-be-a-billion-parameters-or-less]]
- [[open-models-must-keep-progressing-as-a-fallback]]
- [[llm-systems-may-come-to-resemble-companies]]
- [[ai-should-be-the-front-end-of-a-teacher-designed-course]]
- [[post-agi-education-will-be-like-going-to-the-gym]]
- [[children-should-mostly-study-math-physics-and-cs]]
- [[this-is-the-decade-of-agents]], [[llm-products-will-take-years-to-figure-out]], [[small-llms-can-be-strong-in-narrow-domains]], [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]] (only if merge accepts the relations below)
- [[llm-agents-over-time]] (timeline entry)
```

## Candidates

### topic: self-driving
- existing: no (the Tesla Autopilot anecdote is on [[software-3-0]], from the 2025 YC talk)
- aliases: Self-driving, Autopilot, Tesla FSD, Waymo, end-to-end driving, lidar
- statements:
  - He spent about five years on self-driving and draws many analogies from it to AGI, maybe because he is familiar with it (@00:36).
  - He feels self-driving has reached AGI a little bit, because there are systems you can pay to ride, such as Waymo in San Francisco, which he has taken many times (@00:36, @01:07).
  - His first Waymo ride was a demo from a friend who worked there, almost exactly a decade earlier, "2014 or so"; it was basically a perfect drive, and it took ten years to become a city-scale product (@01:07).
  - Asked whether the delay was regulatory or technical, he says you do not see in a 30-minute demo everything they had to deal with for a decade; there is a massive gap between demo and product, and a lot of it is also regulatory (@01:39).
  - Globalisation has not happened at all: the world has not changed yet and that will take a long time; he suspects AGI will look similar (@01:39, @02:11).
  - People think Waymo is ahead of Tesla; he personally thinks Tesla is ahead and is very bullish on its self-driving program (@02:11).
  - Tesla has a software problem and Waymo a hardware problem, software problems are much easier, and Tesla already has cars deployed at scale (@02:11).
  - He drove the latest build the day before and says it did some "miraculous" driving; he expects that in ten years Tesla will be ahead in scale and revenue (@02:45, @03:17).
  - Tesla does use expensive sensors, including lidar, but at training time, on cars that map and do things that do not scale; that is distilled into a vision-only test-time package, an arbitrage on sensor expense he calls brilliant and underappreciated (@03:49).
  - He thinks it will work because the pixels have the information and the network will be capable of using it; sensors help at training time more than at test time (@03:49, @04:21).
  - The plan at Tesla was always for the neural net to eat through the stack: from image-level detection, to multiple images, to predictions over time, discarding C++ code until it outputs steering commands (@04:21, @04:54).
  - His understanding, which he hedges because they do not talk about it, is that current Waymos tried this but did not do it (@04:54).
  - He suspects Tesla's end-to-end system in about ten years will be just a neural net, video in and commands out, built up incrementally (@05:28).
  - The intermediate predictions did not mislead development: imitating humans end to end gives too few bits of supervision for billions of parameters, so intermediate representations develop the features and detectors; he suspects, without being on the team, a lot of pretraining before end-to-end finetuning (@05:28, @06:02).
- relation: **Note:** [[software-3-0]] has his 2025 telling of the neural net eating Autopilot's C++ ([[youtube-2025-06-19-software-is-changing]] @04:56); same story, earlier source. Link the topics.

### topic: humanoid-robots
- existing: no
- aliases: Humanoid robots, Optimus, Tesla Bot, Unitree, G1, teleoperation, robotics
- statements:
  - He worked on the Tesla humanoid before he left; asked what transfers from cars, he says basically everything, and that people do not appreciate it (@06:02, @06:37).
  - Cars are robots, and Tesla is not a car company but a robotics-at-scale company; at scale is a separate variable, since they build the machine that builds the thing (@06:37).
  - The transfer took little work: early Optimus had the same computer and cameras and ran the car networks, trying to recognise drivable space while walking around the office; with some finetuning it generalised a little (@07:11).
  - When Elon said they were doing it, people showed up with the CAD models, supply chain and tools; the same in-house expertise was reconfigured "like a Transformer the movie", and the brains transferred too, networks, labeling team and approach (@07:43, @08:15).
  - He thinks household uses like laundry will come late; B2C is not the right start, because of legal liability and robots that are not perfect yet (@08:15, @08:48).
  - First customer is yourself, incubated in the factory on material handling, then B2B to companies with large warehouses, then B2C (@08:48, @09:21).
  - He expects B2C robots too, says Unitree is making robots he really wants, will probably buy one, and expects an ecosystem building on those platforms (@09:21).
  - He would love an Optimus to pick up individual leaves so we do not need leaf blowers, and hopes it is one of the first applications (@09:54).
  - On the humanoid thesis: people underappreciate the fixed cost of any single platform, so it makes sense to centralise on one that does everything (@10:26, @10:59).
  - A humanoid is easy for people to teleoperate, a data-collection advantage he says is usually overlooked; the world being designed for humans also matters, and he expects variations on the platform (@10:59).
  - You benefit from transfer learning between tasks: in AI you want a single multitasking neural net, as with language models in the text domain, so data collected for leaf-picking benefits every other task (@10:59, @11:33).
  - On cheaper wheeled platforms, he says it makes sense but wonders if it leads to a local minimum; picking one platform and making it perfect is a good long-term bet (@12:06).
  - The human form is familiar and psychologically easy to understand (@12:40, @13:13).
  - He does not claim a good window into what is missing; the lower body is inverted-pendulum control where he doubts imitation learning, while the upper body needs teleoperation and data collection, so systems become hybrid (@13:13, @13:45).
  - He expects teleoperation first, something working 95% of the time, then human-to-robot ratios and people supervising robots, all gradually (@13:45, @14:17).
  - He knows of no single technical impediment; Transformers are a blob of tissue for arbitrary tasks, and the rest is data, training, deployment and iteration, a lot of grunt work (@14:17).
- relation: **Note:** [[physical-automation-will-lag-digital-automation]] (Berkeley, 2024-07-03) says physical automation will probably lag digital; here he expects humanoid deployment to be gradual (@14:17). Compatible; neither compares the two directly, so no relation set.

### topic: transformer-architecture
- existing: yes
- statements:
  - He says the Transformer is not just another neural net but an amazing, extremely general one (@14:49).
  - He thinks of it as a general-purpose training computer, a differentiable computer: given billions of inputs and outputs and trained with backpropagation, it arranges itself into a thing that does the task, "a magical thing" found in algorithm space (@14:49, @15:24).
  - Four or five existing innovations were put together, which he says Google did in its paper: residual connections, layer normalisation, the attention block, and no saturating nonlinearities like tanh, which kill gradient signals (@15:24, @15:56).
  - In the Llama release the Transformer has not changed much: RoPE relative positional encodings are the major change, everything else is about plus 3%, over the last five years or so (@16:29, @17:01).
- relation: see claims below.

### topic: scaling-laws
- existing: yes
- statements:
  - He says scaling laws are to a large extent a property of the Transformer: stacked LSTMs did not give clean scaling laws, and the Transformer was the first thing that just scales (@14:49).
  - On the data wall and the cost of another generation of scale, he says the architecture no longer holds us back fundamentally; the dataset and loss function have become the bottlenecks (@15:56, @16:29).
- relation: **Note:** extends the topic's 2023 account ([[youtube-2023-11-23-intro-to-llms]] @26:02) with a reason scaling laws exist; no claim relation needed.

### topic: pretraining-and-finetuning
- existing: yes
- statements (section "Data as the bottleneck (No Priors, 2024-09-05)"):
  - Internet data is not the data you want, but a nearest neighbour that gets you surprisingly far (@17:33).
  - What you want is the inner thought monologue of a brain solving problems; with a billion of those trajectories, roughly speaking, AGI would be here (@17:33).
  - Internet data happens to contain enough reasoning traces and knowledge, and the Transformer makes it work (@17:33, @18:05).
  - A lot of activity is refactoring the dataset into inner-monologue formats, with a lot of synthetic data generation (@18:05).
  - Synthetic data, its collapse and the Persona dataset: see the synthetic-data claim.
- relation: **Note:** the topic's "RLHF models lose entropy" paragraph ([[talk-2023-05-25-state-of-gpt]] @18:21) is the same phenomenon at a different stage; a connection, not a claim relation.

### topic: llm-self-improvement
- existing: yes
- statements:
  - He says current models are helping create the next generation, a staircase of improvement (@18:05).
- relation: **Note:** not the AlphaGo self-play idea of [[self-improvement-may-be-possible-in-narrow-domains]]; a different mechanism, no relation set. Single sentence; merge may make it a Note.

### topic: ai-as-exocortex
- existing: no
- aliases: Exocortex, human augmentation, AI augmentation, merger, not your weights not your brain
- statements:
  - Asked about augmenting people with AI, he says absolutely, and that we are already kind of merging, limited by the I/O bottleneck, with the models at your fingertips (@22:24).
  - He does not know what a merger looks like yet but wants to decrease the I/O to tool use; he sees it as an exocortex on top of the neocortex, the next layer of the brain, which happens to be in the cloud (@22:59).
  - On the host's Accelerando example, where losing goggles feels like losing part of yourself, he says (speaker likely him) that is very likely, the phone is already almost that, and without your tools you lose part of your intelligence (@23:31).
  - His example is maps: many people can no longer navigate their own city; with a universal translator, which he thinks is not far away, you would lose the ability to speak to people without it (@23:31).
  - A video of a child swiping a magazine shows, to him, that people may stop telling nature from technology when tools are transparent (@24:05).
  - He imagines a world like Disney where objects are alive and you talk to them, and finds it strange you cannot tell a door to open (@24:40, @25:13).
  - Asked about market structure, he describes an oligopoly of a few closed platforms and an open platform, such as Meta's Llama, somewhat behind, mirroring the open-source ecosystem (@25:13, @25:45).
  - Thinking of it as an exocortex, he borrows the crypto saying and asks whether "not your weights, not your brain" holds (@25:45).
  - He sees a trade-off between ownership and renting a better brain; maybe the default is closed models because they are amazing, with an open fallback, as people already fall back to open models when closed APIs go down (@26:19).
- relation: see [[open-models-must-keep-progressing-as-a-fallback]].

### topic: ai-ecosystem
- existing: yes
- statements: the oligopoly/open-platform statements (@25:13, @25:45) and the fallback (@26:19, @26:53) from the exocortex topic, as a dated section "Exocortex and ownership (No Priors, 2024-09-05)".
- relation: **Note:** compatible with Sequoia's open-weights/open-source/proprietary split and "will open keep pace? don't know" ([[talk-2024-03-26-sequoia-making-ai-accessible]] @09:05, @30:33). Here he adds why open must progress; no contradiction.

### topic: llms-as-operating-systems
- existing: yes
- statements (section "Companies of LLMs (No Priors, 2024-09-05)"):
  - He thinks it is probably not a single model: you want a parallel, not sequential, process, and companies parallelise work with a hierarchy for information processing and reduction (@29:09).
  - He thinks it is not unlikely we end up with companies of LLMs (caption "companies for ofms"): models of different capabilities specialised to domains, a programmer, a program manager, working in parallel and orchestrating computation on your behalf (@29:41).
  - It would be like a biological ecosystem with specialised roles and niches, with automatic escalation to other parts of the swarm depending on difficulty (@29:41, @30:13).
- relation: **Note:** the Berkeley keynote pictures many digital entities collaborating ([[talk-2024-07-03-berkeley-hackathon-keynote]] @08:04); that sits in [[physical-automation-will-lag-digital-automation]]'s context, not its own claim. Same direction.

### topic: software-3-0
- existing: yes
- statements: one sentence citing @04:21/@04:54 (neural net eating Tesla's C++ stack) as a **Note:** earlier telling; or `context` only. Merge decides.

### topic: llm-tool-use
- existing: yes; context only
- statements: the cognitive core, he says, is a thing that thinks and, when it needs information, knows how to use tools (@27:27).

### topic: ai-for-education
- existing: no
- aliases: AI for education, education, Eureka Labs, AI tutor, AI TA, perfect tutor, learning vs entertainment
- statements:
  - He says he has always been an educator and loves learning and teaching (@30:13).
  - He sees most AI activity as replacing or displacing people; he is more interested in what empowers people, calls himself "team human", and wants people empowered and more amazing than today rather than sidelined by automation (@30:44, @31:18).
  - He asks how far a person could go with the perfect tutor and curriculum for every subject, noting rich people with tutors go far, and thinks AI can approach or surpass that (@31:18).
  - Asked about The Diamond Age's primer (host's reference), he says he is inspired by aspects of it (@31:50).
  - In practice he is building a single course, the one you would go to if you want to learn AI (@31:50).
  - He taught CS231n at Stanford, which he calls the first deep learning class; the question now is how to scale a course to perhaps 8 billion people in many languages and at all levels (@31:50, @32:21).
  - Currently models are not good enough to create a good course, but they are good enough to be the front end to the student and interpret the course (@32:21).
  - The teacher moves to the back end, designing materials, while the AI is the front end, speaking every language and taking you through the course; an AI TA is one way to think of it (@32:54).
  - He says this is tractable today, does not exist, can be made really good, and can be refactored as capability grows (@32:54, @33:26).
  - He likes to find things matching today's AI capability; many companies, he says, misjudge it and build either too far ahead or not ambitiously enough (@33:26).
  - He says we have not scratched what is possible, with two dimensions: globalisation, everyone having good education, and how far a single person can go (@34:31).
  - Translation is super low-hanging fruit because current models are really good at it; adapting to a person's background, with analogies to things they know, is not low-hanging but not far, though it needs work to actually work rather than demo (@34:31, @35:03, @35:35).
  - Many capabilities are a prompt away so you always get demos, but the demo is near and the product far (@35:35, @36:08).
  - He does not want a world where lab lineage matters too much and hopes AI can destroy that gatekeeping by a scarce resource (@36:40).
  - Communities give education and apprenticeship, but also culture: what is prized, such as the h-index in academia, which strongly shapes motivation and status (@37:13, @37:46).
  - Growing up in Slovakia and studying in Canada, he says, at the University of Toronto starting companies did not occur to you; everyone talked about internships and a fixed set of companies (@37:46, @38:19).
  - He thinks culture may be the dominant variable, because the education is already the easier part, with a ton available (@38:51).
  - He wants to make learning much easier; pre-AGI people learn for practical reasons like jobs, post-AGI education is entertainment to a much larger extent (@39:24, @39:56).
  - He says it is not an accident that two to three hundred years ago science was done by nobility or the wealthy (@39:56, @40:29).
  - First-course audience: roughly undergraduate level in a technical area, any age; the school-then-work model will break down as people return to school more often (@41:01, @41:34).
  - He hoped for late this year, but with distractions expects early next year (@42:08).
- relation: **Note:** [[small-projects-can-snowball]] and [[build-the-ramp-not-just-the-thing]] are earlier education-related claims; no relation set. **Note:** he never says "Eureka Labs"; the host says "Eureka" (@41:01).

### claim: there-is-a-massive-gap-between-demo-and-product
- existing: no
- title: In self-driving, and he expects in AGI, there is a massive gap between a demo and a product, and then between a product and its globalisation
- confidence: stated
- quote: "demo and product there's a massive Gap there" (@01:39)
- statements: Waymo demo to product took ten years (@01:07); the gap and regulation (@01:39); globalisation has not happened and AGI will look similar (@01:39, @02:11); the same phrase applied to AI education, "the demo is near but the product is far" (@36:08); real adaptivity versus something you can demo and that works sometimes (@35:35).
- relation: **supports [[this-is-the-decade-of-agents]]**: both use the decade from a near-perfect Waymo demo to a product as the lesson for AI autonomy (here @01:07, @01:39, @02:11; [[youtube-2025-06-19-software-is-changing]] @26:01, @27:09). Same argument; he does not say "agents" here, he says AGI. **Supports, weakly, [[llm-products-will-take-years-to-figure-out]]** ([[talk-2024-03-26-sequoia-making-ai-accessible]] @06:54): same direction, no horizon given here. Add a 2024-09-05 entry to [[llm-agents-over-time]].

### claim: tesla-is-ahead-of-waymo-in-self-driving
- existing: no
- title: He thinks Tesla, with a software problem, is ahead of Waymo, with a hardware problem
- confidence: stated
- quote: "I think software problems are much easier" (@02:11)
- statements: @02:11, @02:45, @03:17, @03:49 as on the topic.
- relation: none.

### claim: humanoid-robots-should-start-in-your-own-factory
- existing: no
- title: Humanoid robots should start with their maker as first customer, then go B2B, with consumers last
- confidence: stated
- quote: "I think the best customer is yourself first" (@08:48)
- statements: @08:15, @08:48, @09:21.
- relation: none (see Note on the topic about [[physical-automation-will-lag-digital-automation]]).

### claim: the-architecture-is-no-longer-the-bottleneck
- existing: no
- title: The neural-network architecture no longer fundamentally holds progress back; the dataset and loss function have become the bottlenecks
- confidence: stated
- quote: "those have become the bottlenecks almost" (@16:29)
- statements: architecture not the bottleneck anymore, it was before the Transformer (@15:56, @16:29); activity moved to loss function and dataset, companies do not think about the architecture (@16:29); only RoPE since Llama, everyone takes it for granted (@16:29, @17:01).
- relation: **supports [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]**: he again calls it a general-purpose training computer, a differentiable computer, and again says it has barely changed ([[talk-2023-05-19-stanford-cs25-transformers]] @21:39, @59:18; here @15:24, @17:01). **Note, no relation, with [[the-transformer-is-probably-not-the-final-architecture]]**: in Sequoia he expects a pretty big change someday ([[talk-2024-03-26-sequoia-making-ai-accessible]] @33:51); here it is not the bottleneck now. Both can hold; not a contradiction. **Note:** [[with-enough-data-encode-less-inductive-bias]] and [[ai-has-converged-on-one-architecture]] are compatible; no link.

### claim: synthetic-data-is-the-future-if-you-keep-its-entropy
- existing: no
- title: Synthetic data is the way forward, but models are silently collapsed, so its entropy must be kept
- confidence: stated
- quote: "synthetic data absolutely the future" (@20:13); also "these models are silently collapsed" (@18:38)
- statements: synthetic data is the only way to make progress, so we have to make it work (@18:38); ChatGPT asked for a joke knows about three jokes: each output looks fine but the distribution is not diverse (@18:38, @19:10); in synthetic data generation you lose entropy without seeing it, so it silently gets worse (@19:10); one technique: someone's Persona dataset of a billion fictional backgrounds, injected into prompts to explore more of the space (@19:10, @19:42); inject entropy and maintain the distribution, which people may not appreciate (@20:13); his impression is we will not run out of data (@20:13).
- relation: none to a claim page. **Note:** the RLHF-entropy paragraph on [[pretraining-and-finetuning]] ([[talk-2023-05-25-state-of-gpt]] @18:21) is a related observation.

### claim: transformers-are-in-some-ways-better-than-the-brain
- existing: no
- title: He thinks Transformers are in some ways better than the human brain, held back mostly by data
- confidence: stated (hedged: "roughly speaking", "potentially")
- quote: "Transformers are actually better than the human brain in a bunch of ways" (@20:46)
- statements: he would be careful with brain analogies (@20:13); more efficient system, worse mostly from data, as a first approximation (@20:46); a Transformer memorises a sequence from a single forward-backward pass, a human cannot (@20:46); good chance gradient-based optimisation is more efficient than the brain in some ways (@21:18); human working memory is small, Transformers' much bigger (@21:18); not obvious the brain does backprop, it is stochastic and constrained (@21:51); potentially better than the brain, just not there yet (@21:51).
- relation: **Note, no relation, with [[ai-is-far-less-energy-efficient-than-the-brain]]** ([[talk-2024-03-26-sequoia-making-ai-accessible]] @13:27): that is energy per computation, this is learning and memory efficiency. Both can hold; a reviewer may see a tension in the word "efficient", but he does not compare the two.

### claim: a-cognitive-core-could-be-a-billion-parameters-or-less
- existing: no
- title: A "cognitive core" that thinks and uses tools could be about a billion parameters, maybe fewer
- confidence: stated (hedged: "I think", "I don't know we'll see")
- quote: "I think the cognitive core can be extremely small" (@27:27)
- statements: the smallest performant model can be surprisingly small; current models waste capacity remembering things like SHA hashes because datasets are not curated (@26:53, @27:27); the cognitive core thinks and uses tools to look up information; even a billion parameters suffices (@27:27); distillation works surprisingly well, a big model supervising a small one (@27:27, @28:00); the internet is about 0.001% cognition and the rest information (@28:00); "even 1 billion is too much I don't know we'll see" (@28:36).
- relation: **extends [[small-llms-can-be-strong-in-narrow-domains]]**: the llama2.c README says small LLMs can be strong if the domain is narrow and predicts custom micro-LLMs of about 100M–1B up to ~10B ([[github-2024-05-29-llama2c-readme]] §intro, §contributing); here a general cognitive core of about a billion or less, with tools for knowledge (@27:27, @28:36). Broadens, does not deny. **Note:** [[make-it-work-then-make-it-cheap]] mentions distillation (Sequoia); connection only.

### claim: open-models-must-keep-progressing-as-a-fallback
- existing: no
- title: It is important that open models keep progressing, as a fallback people control
- confidence: stated for "100%" importance; the exocortex framing is posed as a question
- quote: "not your weights not your brain" (@25:45)
- statements: @25:45, @26:19, @26:53 (he says "I think so 100%" and that this is not an obvious point people agree on).
- relation: none set. **Note:** [[ai-ecosystem]] Sequoia section; [[open-weights-models-are-not-open-source]] is about naming, not this.

### claim: llm-systems-may-come-to-resemble-companies
- existing: no
- title: He thinks it not unlikely that LLM systems will come to resemble companies of specialised models
- confidence: stated (hedged)
- quote: "it will actually start to resemble companies to a very large extent" (@29:41)
- statements: as on [[llms-as-operating-systems]] (@29:09, @29:41, @30:13).
- relation: none. Merge may fold this into the topic instead.

### claim: ai-should-be-the-front-end-of-a-teacher-designed-course
- existing: no
- title: With current models, the teacher should design the course and AI should be the front end to the student
- confidence: stated
- quote: "I don't think the models are good enough to create a good course" (@32:21)
- statements: @32:21, @32:54, @33:26.
- relation: none.

### claim: post-agi-education-will-be-like-going-to-the-gym
- existing: no
- title: After AGI, he thinks education will be more like entertainment, effortful the way the gym is
- confidence: stated (with "I would hope")
- quote: "learning something is kind of like going to the gym but for the brain" (@40:29)
- statements: pre-AGI practical motives, post-AGI education as entertainment (@39:56); effortful but fun with a payoff, which is what he means by education not being fun (@40:29, @41:01); he hopes people go to the gym mentally and being highly educated is looked up to (@41:01).
- relation: none.

### claim: children-should-mostly-study-math-physics-and-cs
- existing: no
- title: He thinks children should spend most of their study on math, physics and CS
- confidence: stated
- quote: "math physics CS kind of disciplines" (@42:08)
- statements: the best core of thinking skills; physics shaped how he thinks (@42:08, @42:41); useful pre-AGI, and post-AGI you still want empowered humans (@42:41); use the critical period on manipulation-heavy, not memory-heavy, work; other disciplines are fine, but about 80% should be like this (@43:14).
- relation: none.

### timeline: llm-agents-over-time
- existing: yes
- entry: **2024-09-05** — Self-driving reached AGI "a little bit" a decade after a perfect demo, yet has not globalised; he expects AGI to look similar → [[there-is-a-massive-gap-between-demo-and-product]] (@01:39, @02:11). Or put on a new "self-driving lesson" note; merge decides whether AGI belongs on an agents timeline.

### methods
- none. His "match the product to today's capability" (@33:26) is a single remark; it stays a sentence on [[ai-for-education]].

## Quotes
- "demo and product there's a massive Gap there" (@01:39)
- "I think software problems are much easier" (@02:11)
- "the pixels have the information" (@03:49)
- "too few bits of signal to train so many billions of parameters" (@06:02)
- "this is a robotics company robotics at Scale Company" (@06:37)
- "we were running the car networks on the robot" (@07:11)
- "I think the best customer is yourself first" (@08:48)
- "there is a large fixed cost to any platform" (@10:59)
- "Transformers are this beautiful like blob of tissue" (@14:17)
- "it's like a differentiable computer" (@15:24)
- "those have become the bottlenecks almost" (@16:29)
- "what you want is the inner thought monologue of your brain" (@17:33)
- "these models are silently collapsed" (@18:38)
- "synthetic data absolutely the future" (@20:13)
- "Transformers are actually better than the human brain in a bunch of ways" (@20:46)
- "it is the next layer of the brain" (@22:59)
- "not your weights not your brain" (@25:45)
- "I think the cognitive core can be extremely small" (@27:27)
- "it will actually start to resemble companies to a very large extent" (@29:41)
- "I'm kind of on a high level like team human" (@30:44)
- "I don't think the models are good enough to create a good course" (@32:21)
- "the demo is near but the product is far" (@36:08)
- "learning something is kind of like going to the gym but for the brain" (@40:29)
- "math physics CS kind of disciplines" (@42:08)

(24, more than the 8–15 target; merge picks. All grepped: each occurs exactly once in the raw at the marker shown.)

## Notes for merge
- **Speakers.** Hosts are Sarah Guo and Elad Gil; the captions do not label speakers. Unclear or host lines, not to attribute to him:
  - @09:21 "I got one … the G1" is a host; he says he will probably buy one.
  - @09:54 the "n Freedman" leaf-blower challenge is a host's or his framing (likely Nat Friedman, garbled); "even raking", "just very quietly" are mixed.
  - @12:40 the Unitree dog form factor is the host's; "Black Mirror" line unclear.
  - @22:24 "the computer is the bicycle for human mind" is the host's argument, he says "exactly"; the Neuralink pitch and Accelerando are the host's.
  - @24:05 "I'm very comfortable repurposing that part of my brain to do further research" is probably a host.
  - @25:45–@26:19: "a company is effectively controlling your exocortex", "people will care much more about ownership" and "are you willing to give up ownership and control to rent a better brain because I am" are mixed or host; do not quote as his. "not your weights not your brain" follows his "I do think that when … exocortex" and reads as his; a reviewer should listen.
  - @26:53 "it's quite important that the open source stuff continues to progress" is the host; he answers "I think so 100%".
  - @28:36 "maybe a billion parameters gets you sort of like a good cognitive core" is likely the host; "I think probably right I think even 1 billion is too much" is his. "at less than a billion parameters I have my EXO cortex on a local device" (@29:09) is a host.
  - @29:41–@30:13 "maybe it's not correct to think about … more like a swarm", "the CEO is like a really brilliant uh Cloud Model" and "my cost function is different from your cost function" may be a host; I attribute only the companies/ecosystem/escalation lines.
  - @31:18 the Bloom one-to-two standard deviation literature is the host's; he says "yeah exactly".
  - @36:08 onward, lineage and Nobel-lab propagation are the host's question; @38:51 learning vs entertainment and his earlier post are the host's framing; "we will all be nobility learning with Andre" (@40:29) is the host.
  - @43:14 "I did a a math degree … new Grove being carved" is probably a host, not him (he credits physics at @42:41); "we're not efficient memorizers compared to our tools" (@43:48) speaker unclear.
- **Waymo date.** He says the demo was "almost exactly 2014 or so" (@01:07); the YC talk page says 2013 ([[youtube-2025-06-19-software-is-changing]] @26:01). His own hedged recollections; not a correction or change of view. Quote both as he gives them.
- **Caption garbles:** "salt driving"/"Sal driving"/"soft having space" = self-driving; "weo"/"wayo"/"Whos" = Waymo; "liar"/"Lars" = lidar; "neural nut" = neural net; "unit tree"/"unitri" = Unitree; "scaling loss" = scaling laws; "bottom leg" = bottleneck; "Rope" = RoPE; "sha hases" = SHA hashes; "companies for ofms" = companies of LLMs (probably); "EXO cortex" = exocortex; "cryp" = crypto; "ladi's" = Lady's (Diamond Age primer); "231n" = CS231n; "Andre" = Andrej.
- **Mentioned, not explained:** the Persona dataset (one sentence of how it is used, no name of authors); Accelerando; Diamond Age; Demolition Man and I, Robot (as references to talking to objects); Bloom.
- "I would say distillation works" (@27:27) with "it maybe like the only thing" is a garbled aside; paraphrase as "works surprisingly well".
- **Eureka:** the host names "Eureka" (@41:01); he only says he is building "a single course" (@31:50). Do not write "Eureka Labs" as his words. His dates ("late this year … early next year", @42:08) are relative to recording; write them as his words.
- The "first deep learning class" description of CS231n (@31:50) is his claim; keep it attributed.
- "AGI" is used loosely by him and the hosts; the self-driving claim is about AGI, not agents. Merge should decide whether the agents timeline entry fits or a Note on [[this-is-the-decade-of-agents]] is enough.
