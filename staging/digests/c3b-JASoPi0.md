# Digest: Making AI accessible with Andrej Karpathy and Stephanie Zhan
- raw: raw/talks/c3b-JASoPi0.md · published: 2024-03-26 · medium: talk · words: 7965
- source slug: talk-2024-03-26-sequoia-making-ai-accessible

## Source page

```
---
type: source
raw_path: raw/talks/c3b-JASoPi0.md
published: 2024-03-26
medium: talk
summary: Sequoia fireside interview with Stephanie Zhan, weeks after he left OpenAI, covering the LLM OS, open-weights versus open-source models, scale, energy efficiency, how Elon Musk runs companies, RLHF versus AlphaGo-style RL, and his wish for a vibrant AI ecosystem.
url: https://www.youtube.com/watch?v=c3b-JASoPi0
title: "Making AI accessible with Andrej Karpathy and Stephanie Zhan"
---
# Making AI accessible with Andrej Karpathy and Stephanie Zhan
Raw: [[raw/talks/c3b-JASoPi0]] · Original: https://www.youtube.com/watch?v=c3b-JASoPi0

## Summary
A 37-minute interview at Sequoia, with Stephanie Zhan asking the questions and a few audience
questions at the end. He describes what everyone is building as an LLM OS, with the LLM as a
CPU, modalities as peripherals and existing software as the rest of the machine, and expects a
few default apps from the big labs alongside an ecosystem of others (@04:05, @05:48, @06:20).
He separates open-weights models such as Llama and Mistral from fully open-source ones, ranks
scale first among the things that matter while stressing that money alone does not produce a
model, and names unifying diffusion and autoregressive models and a thousand- to millionfold
energy-efficiency gap as open problems (@07:27, @09:38, @11:15, @12:22, @13:27). He describes
how Elon Musk runs companies (small technical teams, no non-technical middle management, direct
contact with engineers, removing bottlenecks), and says founders can copy it only if they set it
up from the start (@16:13, @18:25, @20:02, @22:46). He argues the field has done only the
imitation step of AlphaGo and that RLHF is a weak form of RL, recommends getting an LLM product
to work before making it cheap, and says the Transformer has been remarkably resilient but is
probably not the final architecture (@24:59, @26:39, @29:28, @33:51, @35:30). Throughout, he
says he cares about a healthy ecosystem of startups more than any one company (@21:10, @36:06).

## Key points
- Everyone is building an LLM OS: the LLM as CPU, modalities as peripherals, wired into existing software → [[llms-as-operating-systems]]
- Big labs will ship a few default apps, like a browser bundled with Windows, beside an ecosystem of others → [[llms-as-operating-systems]], [[ai-ecosystem]]
- LLM products are "quite autonomous but not fully autonomous", so oversight and evaluation still have to be worked out → [[partial-autonomy-apps]], [[llm-products-will-take-years-to-figure-out]]
- Llama and Mistral are open weights, not open source; finetuning without the data and training loop regresses other skills → [[ai-ecosystem]], [[open-weights-models-are-not-open-source]], [[pretraining-and-finetuning]]
- Scale is the first principal component, but data, algorithms and infrastructure expertise also matter → [[scale-matters-most-but-is-not-enough]]
- Diffusion and autoregressive models sit apart with nothing in between → [[diffusion-and-autoregressive-models-should-meet]]
- Models are a thousand to a million times less energy-efficient than a brain; precision, sparsity and new hardware are the levers → [[compute-efficiency]], [[ai-is-far-less-energy-efficient-than-the-brain]]
- Elon Musk runs "the biggest startups": small technical teams, intensity, direct contact with engineers → [[elon-musk-management-style]], [[founders-can-copy-elons-style-only-from-the-start]]
- He cares about the ecosystem, a coral reef of startups, more than any one company, and worries about a few megacorps → [[ai-ecosystem]], [[he-cares-about-the-ecosystem-more-than-any-company]]
- LLMs have done AlphaGo's imitation step, not its RL step; models must practice for themselves → [[pretraining-and-finetuning]], [[llms-have-done-only-step-one-of-alphago]]
- RLHF is a vibe check against a hackable reward model, a weak form of RL → [[rlhf-is-a-weak-form-of-rl]]
- Get it to work with the best model first, then make it cheaper, for example by distilling → [[make-it-work-then-make-it-cheap]]
- Build the thing, and also build the ramp so others can understand it → [[ai-ecosystem]], [[build-the-ramp-not-just-the-thing]]
- The Transformer is designed for the GPU, remarkably resilient, and probably not the final network → [[transformer-architecture]], [[the-transformer-is-probably-not-the-final-architecture]]

## Fed pages
- [[llms-as-operating-systems]]
- [[partial-autonomy-apps]]
- [[ai-ecosystem]]
- [[pretraining-and-finetuning]]
- [[transformer-architecture]]
- [[compute-efficiency]]
- [[elon-musk-management-style]]
- [[llm-products-will-take-years-to-figure-out]]
- [[open-weights-models-are-not-open-source]]
- [[scale-matters-most-but-is-not-enough]]
- [[diffusion-and-autoregressive-models-should-meet]]
- [[ai-is-far-less-energy-efficient-than-the-brain]]
- [[founders-can-copy-elons-style-only-from-the-start]]
- [[he-cares-about-the-ecosystem-more-than-any-company]]
- [[llms-have-done-only-step-one-of-alphago]]
- [[rlhf-is-a-weak-form-of-rl]]
- [[build-the-ramp-not-just-the-thing]]
- [[the-transformer-is-probably-not-the-final-architecture]]
- [[make-it-work-then-make-it-cheap]]
- [[this-is-the-decade-of-agents]] (only if merge accepts the `supports` link below)
```

## Candidates

### topic: llms-as-operating-systems
- existing: yes (aliases LLM OS, LLMs are operating systems)
- aliases to add: none needed
- statements:
  - A few years ago he felt it was unclear how AGI would happen and the question was academic; now he thinks it is very clear, with a lot of space everyone is trying to fill (@03:30).
  - He says everyone is trying to build what he calls an LLM OS (@03:30, @04:05).
  - In this OS, modalities such as text, images and audio are peripherals plugged into a new CPU, the LLM Transformer itself, which is also connected to the Software 1.0 infrastructure already built (@04:05).
  - Everyone is trying to make it available and customisable for all the nooks and crannies of the economy (@04:05, @04:39).
  - He expects to bring up and down relatively self-contained agents that can be given high-level tasks and specialised in various ways (@04:39).
  - He sees OpenAI as building out this LLM OS as a platform on which companies and verticals can be positioned (@05:48).
  - As Windows ships with a default browser, OpenAI or other companies may ship a few default apps, but different apps, like different browsers or chat agents, can still run on the infrastructure (@05:48, @06:20).
  - He extends the analogy to the ecosystem: an oligopoly of proprietary systems like Windows and macOS, plus Linux with an infinity of distributions; he thinks LLMs may look something like that (@07:27).
  - Being handed open weights is like being tossed a binary of an operating system, while fully open releases give the infrastructure needed to compile it (@07:27, @07:59).
- relation: extends the existing page's 2025 framing (Windows/macOS vs a possible Linux, [[youtube-2025-06-19-software-is-changing]] @08:54, @09:28) backwards in time; this is now the earliest source for the topic, so `first_seen` moves to 2024-03-26. Same analogy, no change of view.

### topic: partial-autonomy-apps
- existing: yes
- statements:
  - He compares the current moment to early iPhone apps, which were mostly jokes and took time to develop (@06:20).
  - People are still working out what LLMs are good and bad at, how to program, debug and get them to do real tasks, and what oversight and evaluation should look like, because the systems are quite autonomous but not fully (@06:20, @06:54).
  - He expects this to take time and to play out over the next few years (@06:54).
- relation: context for the 2025 autonomy-slider framing; not the same vocabulary. **Note:** he does not use the terms "partial autonomy" or "autonomy slider" here.

### topic: ai-ecosystem
- existing: no
- aliases: AI ecosystem, open weights, open-source LLMs, open vs closed models, coral reef, build the ramp
- statements:
  - He says names matter: models such as Llama and Mistral are not, in his view, open source (@07:27).
  - He names Pythia, LLM360 and OLMo (caption "Almo") as fully open-source LLMs that release the whole infrastructure, from gathering data to training the model (@07:59).
  - Weights alone let you finetune, but the more you finetune the more the model regresses on everything else (@07:59, @08:32).
  - To add a capability without regressing others you may want to train on a mixture of the old and new data distributions, which needs the training loop and the dataset, not just the weights (@08:32).
  - He proposes three categories: open-weights models, open-source models and proprietary models, and expects the ecosystem to look like today's operating systems (@09:05).
  - Asked whether open source will keep pace, he says he does not really know, because the models are so capital-intensive (@30:33).
  - He reasons that Meta can afford to train at scale while its money printer is unrelated, giving it an incentive to release models to empower the ecosystem and borrow its best ideas (@30:33, @31:06).
  - He says Meta has so far only released open weights and should go further, possibly by constraining itself to data sources that are easy to use (@31:06, @31:40).
  - He credits Meta for publishing a paper and a logbook and says it could do much better at fostering the ecosystem (@31:40).
  - He wants the ecosystem healthy and thriving, a coral reef of startups in all the nooks and crannies of the economy (@21:10).
  - He is more hesitant about five megacorps taking over, worried because AGI magnifies power, and says he has to think it through more (@21:41).
  - What would make the ecosystem more vibrant, he says, is what is available: his tweet "build the thing, build the ramp" says many build things and far fewer build ramps so people can understand them (@32:13).
  - He wants people to be more open about what they learned, how they trained, and what worked and did not (@32:45).
  - He sees quite a bit of momentum in the open ecosystems already (@32:45).
  - His parting message to founders is a question of how to keep a vibrant ecosystem of startups that continue to win against big tech (@36:06).
- relation: none to an existing claim. **Note:** the operating-system framing links this to [[llms-as-operating-systems]].

### topic: compute-efficiency
- existing: no
- aliases: energy efficiency, precision, sparsity, hardware co-design, von Neumann bottleneck
- statements:
  - His brain runs on roughly 20 watts, while the supercomputers Jensen described at GTC are measured in megawatts (@12:55).
  - He thinks it is safe to say we are probably off by a factor of a thousand to a million in the efficiency of running these models (@12:55, @13:27).
  - Part of the gap is that computers were not designed for this workload, which needs massive parallelism rather than data-dependent sequential computation; he calls Nvidia GPUs a good step (@13:27).
  - His levers: adapt computer architecture to the workload; lower precision, which has come down from 64-bit to a few bits or even 1.58 depending on the paper; and sparsity, since the brain is not always fully activated (@13:59).
  - The last lever is the von Neumann architecture, whose shuttling of data between memory and cores he calls broken and unlike how the brain works (@14:33).
  - He says he is not a computer architect, but expects an exciting time in computer architecture (@14:33).
  - He returns to precision, sparsity and hardware co-design as levers for changing the Transformer (@34:24).
- relation: none.

### topic: elon-musk-management-style
- existing: no
- aliases: Elon Musk, Tesla culture, how Elon runs companies
- statements:
  - He says Elon runs companies in an extremely unique style that people do not appreciate even from reading about it, and finds it hard to describe (@16:13).
  - First, Elon likes very small, strong, highly technical teams (@16:13).
  - Elon pushed against team growth: he had to plead to hire, and had to fight to keep people because Elon by default wanted to remove low performers (@16:48).
  - No non-technical middle management (@16:48, @17:21).
  - Second, the vibe: Elon wants a vibrant office, dislikes stagnation and large meetings, and encourages people to walk out of meetings where they are not contributing or learning (@17:21, @17:53).
  - There is less pampering than at bigger companies; you are there to do your best technical work, with intensity (@17:53).
  - Third, Elon is unusually connected to the team, talking directly to engineers in meetings of about 50 people rather than mostly to VPs (@17:53, @18:25).
  - With a small strong team, the engineers and the code are the source of truth, and Elon talks to them to learn the actual state of things (@18:57).
  - Fourth, Elon uses a "large hammer": his example is Elon hearing twice about a GPU shortage, ordering the cluster doubled with daily updates, and offering to call Jensen when told of a six-month delay (@18:57, @19:29, @20:02).
  - He says that after leaving, a normal company misses aspects of this (@20:02).
- note: the rowing-team joke (@15:06, @15:39) is told by Stephanie Zhan, attributed to Elon; it is not his.

### claim: llm-products-will-take-years-to-figure-out
- existing: no
- title: "Working out how to oversee and evaluate LLM products will take the next few years"
- confidence: stated
- quote: "it's quite autonomous but not fully autonomous" (@06:54)
- statements: see partial-autonomy-apps above (@06:20, @06:54); plus he expects many self-contained agents given high-level tasks (@04:39).
- relation: **supports [[this-is-the-decade-of-agents]]**, weakly. In 2025 he says agents need humans in the loop and that autonomy took twelve years in self-driving ([[youtube-2025-06-19-software-is-changing]] @27:09, @27:44); in 2024 he already says LLM systems are not fully autonomous, need oversight still to be designed, and will take years to figure out (@06:54). Both point the same way. Caveat: the 2024 horizon is "the next few years", for an app ecosystem to develop, not a decade, and he does not discuss self-driving here; do not record this as the origin of the decade claim. Merge may prefer to treat it as context only.

### claim: open-weights-models-are-not-open-source
- existing: no
- title: "Llama and Mistral are open-weights models, not open source"
- confidence: stated
- quote: "I wouldn't actually say they're open source right" (@07:27)
- statements: @07:27, @07:59, @08:32, @09:05 (see ai-ecosystem).
- relation: none.

### claim: scale-matters-most-but-is-not-enough
- existing: no
- title: "Scale is the main factor in LLM capability, but money and GPUs alone do not produce a model"
- confidence: stated
- quote: "I would say scale is definitely number one" (@09:38)
- statements:
  - Scale is number one, the first principal component; dataset preparation and algorithms are compute-efficiency gains that also matter (@09:38, @10:10).
  - Scale sets something like a speed limit: without it you cannot train the massive models, though fine-tuning may need less (@10:10).
  - Even with money and scale, training is a hard distributed-optimisation problem on tens of thousands of GPUs failing at random; the infrastructure is creaking and the talent is scarce (@10:43, @11:15).
  - It is not obvious to him that someone given a ton of money or GPUs could produce one of these models; it takes expertise in infrastructure, algorithms and data (@11:15).
- relation: none. **Note:** [[pretraining-and-finetuning]] already says training GPT-3 is a massive infrastructure challenge ([[youtube-2023-01-17-gpt-from-scratch]] @1:50:56); a Note link, not a claim relation.

### claim: diffusion-and-autoregressive-models-should-meet
- existing: no
- title: "He finds it odd that nothing sits between diffusion and autoregressive models"
- confidence: stated
- quote: "different modalities are apparently a good fit for one of the two" (@12:22)
- statements: on the algorithm side he is thinking about the split between diffusion and autoregressive models, both ways of representing probability distributions; he thinks there is probably space to unify or connect them or find a hybrid, and says it feels wrong that there is nothing in between (@12:22, @12:55). He returns to it as "some fruit there probably" (@34:24).
- relation: none.

### claim: ai-is-far-less-energy-efficient-than-the-brain
- existing: no
- title: "Running these models is probably a thousand to a million times less efficient than a brain"
- confidence: stated (he hedges: "I don't know how much you need exactly")
- quote: "probably off by a factor of a thousand to like a million" (@13:27)
- statements: see compute-efficiency (@12:55, @13:27, @14:33).
- relation: none.

### claim: founders-can-copy-elons-style-only-from-the-start
- existing: no
- title: "A founder can run a company Elon's way if it is set up front and kept consistent"
- confidence: stated
- quote: "as long as you do it from the start and you're consistent" (@22:46)
- statements: asked by audience member Brian whether founders should copy Elon, he says it depends on the founder's DNA; making it clear when hiring lets people happily sign up, but changing it later is very messy; it has pros and cons and is a consistent model of company building (@22:14, @22:46).
- relation: none. Alternative: fold into elon-musk-management-style as a section and skip the claim page.

### claim: he-cares-about-the-ecosystem-more-than-any-company
- existing: no
- title: "He cares more about a healthy AI ecosystem than about any one company"
- confidence: stated
- quote: "I care a lot more about the ecosystem" (@21:10)
- statements: @21:10, @21:41, @36:06 (see ai-ecosystem).
- relation: none. Caution: the framing "what you care most about is democratizing access to AI education tools" (@20:35) is Stephanie Zhan's; he agrees with her description in general terms ("I think you've described it on in the right way", @21:10) but then talks about the ecosystem, not education. Do not record education as his stated motive from this source.

### claim: llms-have-done-only-step-one-of-alphago
- existing: no
- title: "LLMs have done AlphaGo's imitation-learning step but not its RL step"
- confidence: stated
- quote: "I think we've done step one of alpha go" (@24:59)
- statements:
  - Current models are not good enough, and he thinks people have not seen what is possible; there are big rocks in capability still to turn (@24:59, @25:32).
  - The field has done AlphaGo's imitation-learning step, not its RL step, which is the part that made AlphaGo work and become superhuman (@24:59, @25:32).
  - Data collection for ChatGPT-like models is terrible: a human writes an ideal solution, but what is easy or hard for the human differs from the model, so some steps are trivial to it and others are leaps it does not understand (@25:32, @26:04).
  - The model needs to practise for itself and learn what works for it, for example falling back to a calculator if it is bad at four-digit addition (@26:04, @26:39).
  - He calls imitation a good initializer for something agent-like (@26:39).
  - Learning from a textbook involves exercises, note-taking and rephrasing; he says nothing equivalent exists in LLMs yet and it is super early days (@28:19).
- relation: none to an existing claim. **Note for merge:** the 2025 RLVR description, that models develop reasoning-like strategies because they find what works for them through optimisation ([[blog-2025-12-19-year-in-review-2025]] §1), reads like this 2024 call being answered. The rlvr page has no claim page to link, so this is a Note on [[rlvr]] (as `context`), not a supports/extends edge. Also a possible Note on [[jagged-intelligence]]: "human psychology is different from the model psychology" (@26:04).

### claim: rlhf-is-a-weak-form-of-rl
- existing: no
- title: "RLHF is a super weak form of reinforcement learning"
- confidence: stated
- quote: "that's like a super weak form of reinforcement learning" (@26:39)
- statements:
  - He says RLHF barely counts as RL; its reward model is a "vibe check" (@26:39, @27:13).
  - An AlphaGo trained by RLHF would ask people which of two boards they prefer, train on those labels and do RL against that; that trains against the vibes of the board (@27:13).
  - A neural-net reward model is easy for the optimised model to overfit and find spurious ways to hack (@27:13).
  - AlphaGo avoids this with a clear objective function; he calls imitation learning super silly and RLHF a nice improvement that is still silly, and wants training where the model is in the loop with its own psychology (@27:46).
- relation: none to an existing claim. **Note:** consistent with the 2025 statement that RLVR, unlike RLHF, allows long optimisation against non-gameable rewards ([[blog-2025-12-19-year-in-review-2025]] §1); could seed a timeline on RL for LLMs later. Not a contradiction of [[pretraining-gives-a-document-completer]].

### claim: build-the-ramp-not-just-the-thing
- existing: no
- title: "Many people build the thing; far fewer build the ramp to understand it"
- confidence: stated
- quote: "number one build the thing number two build the ramp" (@32:13)
- statements: @32:13, @32:45.
- relation: none. **Note:** possible Note link to [[small-hackable-educational-code]] (his repos as ramps), but this talk does not mention his code or courses, so it is not evidence for that method.

### claim: the-transformer-is-probably-not-the-final-architecture
- existing: no
- title: "The Transformer has been remarkably resilient but is probably not the final neural network"
- confidence: stated
- quote: "I don't know that it's like the final neural network" (@33:51)
- statements:
  - He calls the Transformer amazing and says he did not see it coming; before it he expected an insane diversification of neural networks, and the opposite happened (@33:51).
  - Given the field's history he finds it hard to say this is the end, says "absolutely it's not", and is optimistic someone will find a big change (@34:24).
  - He sees fruit in the autoregressive-vs-diffusion modelling setup and in precision, sparsity and hardware co-design (@34:24, @34:57).
  - The Transformer was designed for the GPU: the paper's leap was an extremely parallelisable architecture, breaking the RNN's sequential dependencies through attention, with predecessors like the Neural GPU (@34:57, @35:30).
  - It has proven remarkably resilient: the original and today's are not super different (@35:30).
- relation: none to an existing claim. [[gpt-is-not-a-complicated-model]] is about size, not longevity; no edge. Statements also go on [[transformer-architecture]].

### topic: pretraining-and-finetuning
- existing: yes (aliases include RLHF, finetuning)
- statements:
  - Finetuning a model regresses its other capabilities; adding knowledge without regression wants a mix of old and new data, which needs the dataset and training loop (@08:32).
  - Neural nets are less composable than traditional code, but they compose through pretraining components separately, plugging them in and finetuning through the whole, for example adding images to a ChatGPT-like system (@23:53, @24:26).
  - He sees papers on model merges but does not know that anything has really stuck (@23:21, @23:53).
  - The AlphaGo and RLHF points above (@24:59–@27:46).

### topic: transformer-architecture
- existing: yes
- statements: as under the-transformer-is-probably-not-the-final-architecture (@33:51–@35:30). Update `last_updated` to 2024-03-26.

### method: make-it-work-then-make-it-cheap
- existing: no
- aliases: performance first, then cost; distill the expensive pipeline
- steps:
  1. Start with the most capable model regardless of cost (his examples: GPT-4, heavy prompting, RAG) (@28:56).
  2. Get it to work at all, even with many prompts, picking the best one, or a debate flow (@29:28, @30:01).
  3. Then make concessions: check which queries can fall back to GPT-3.5 (@29:28).
  4. Distill: run the expensive pipeline over a large distribution of problems to get labels, then finetune a smaller, cheaper model on them (@30:01).
- note: he frames it as the paradigm a few people he talked to say works for them, then as his own suggestion (@29:28, @30:01).

## Quotes
- "trying to build what I refer to as kind of like this llm OS" (@04:05)
- "you have a CPU which is the llm Transformer itself" (@04:05)
- "it's quite autonomous but not fully autonomous" (@06:54)
- "I wouldn't actually say they're open source right" (@07:27)
- "there's open weights models open source models and then um proprietary models" (@09:05)
- "I would say scale is definitely number one" (@09:38)
- "different modalities are apparently a good fit for one of the two" (@12:22)
- "probably off by a factor of a thousand to like a million" (@13:27)
- "he runs the biggest startups" (@16:13)
- "Elon was always like a force against growth" (@16:48)
- "I care a lot more about the ecosystem" (@21:10)
- "I want it to be like a coral reef" (@21:10)
- "especially with AGI being such a magnifier of power" (@21:41)
- "as long as you do it from the start and you're consistent" (@22:46)
- "I think we've done step one of alpha go" (@24:59)
- "the model needs to practice itself" (@26:04)
- "that's like a super weak form of reinforcement learning" (@26:39)
- "go after performance first and then you make it cheaper later" (@29:28)
- "number one build the thing number two build the ramp" (@32:13)
- "I don't know that it's like the final neural network" (@33:51)
- "Transformer is kind of designed for the GPU by the way" (@34:57)

All grepped: each matches exactly once in the raw, in the block cited.

## Notes for merge
- **Speakers.** Stephanie Zhan asks every main question; audience members (Brian, Alex, Nick, Yi, Sam, Peter, Michael) ask the rest. Host lines not to attribute to him: the intro and career backstory (@00:03–@02:54; "trained by Jeff Hinton", poached by Elon, six autopilot leaders); "AGI even seven years ago seemed like an incredibly impossible task" (@02:54/@03:30); "OpenAI is dominating the ecosystem" (@05:14); "scale is all that matters" (@09:05); the rowing-team joke (@15:06); "what you care most about is democratizing access to AI education tools" (@20:35); "genuinely Andre dreams about coral reefs" (@21:10); "graduate school for AI models… sit in a room with a book and quietly question itself for a decade" (@27:46), which he only answers "I think that would be part of it"; "sounds like you should become an investor" (@36:40); Nick's physicist / faster-than-light question (@24:26).
- **Speaker boundary unclear @04:39:** "it's not just one agent it's many agents and what does that look like" runs straight into the host's next question; the first clause is probably his, but treat it as uncertain and do not quote it.
- **What the source does not contain.** No criteria for what he looks for in founders (only the Elon-style question and a parting message about the startup ecosystem). No discussion of his own courses, YouTube videos or educational code; the "making AI accessible" title is the event's framing. No mention of `llms.txt`, docs for agents or anything on [[building-for-agents]]; do not feed that page. Nothing on [[small-hackable-educational-code]] beyond a possible Note via "build the ramp".
- **His career facts he states himself:** OpenAI's first office (after Greg's apartment) was across from Sequoia's SF office, above a chocolate factory; about two years there; team of 10–20+; Jensen delivered the first DGX there and they signed it (@01:12, @01:46). Fine as source-page colour; no page needs them.
- **Caption spellings:** "Andre karpathy" = Andrej Karpathy; "llm OS" = LLM OS; "Lama mrone" = Llama, Mistral; "Pia models llm 360 Almo" = Pythia, LLM360, OLMo (my reading; only "llm 360" is unambiguous); "mol" in the host's list = Mistral; "alpha go / alphao / Alo" = AlphaGo; "rhf / rlf / RL HF" = RLHF; "V noyman" = von Neumann; "autoaggressive" = autoregressive; "sparity / sparcity" = sparsity; "primary efficient training" = probably parameter-efficient training (@23:53); "log book" = logbook (Meta's OPT logbook, he does not name the model); "gp4" = GPT-4; "chpt" = ChatGPT; "neural lots" = neural nets; "ARL" = RL.
- **Numbers:** precision "456 or even 1.58" (@13:59) is garbled; read as "4, 5, 6 or even 1.58 bits"? Safer to write "down to a few bits or even 1.58". "Factor of a thousand to a million" is consistent across @13:27 and @14:33. Transformer age "six seven" years (@35:30).
- **Dated context:** recorded 2024-03-26, weeks after he left OpenAI (host says so, @00:03, @02:54). His claims about Meta releasing "only open weights" and about RL not yet being done for LLMs are dated to that moment; RLVR (2025) is later.
- **Possible relation to [[this-is-the-decade-of-agents]]:** proposed as weak `supports` from [[llm-products-will-take-years-to-figure-out]]; see the caveat there. If merge judges the horizons too different ("next few years" vs "decade"), downgrade to a **Note:** on the decade claim and drop it from Fed pages.
