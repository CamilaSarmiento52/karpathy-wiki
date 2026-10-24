---
type: source
raw_path: raw/talks/c3b-JASoPi0.md
published: 2024-03-26
medium: talk
summary: "Sequoia fireside interview with Stephanie Zhan covering the LLM OS, open-weights versus open-source models, scale, energy efficiency, how Elon Musk runs companies, RLHF versus AlphaGo-style RL, and his wish for a vibrant AI ecosystem."
url: https://www.youtube.com/watch?v=c3b-JASoPi0
title: "Making AI accessible with Andrej Karpathy and Stephanie Zhan"
---
# Making AI accessible with Andrej Karpathy and Stephanie Zhan
Raw: [[raw/talks/c3b-JASoPi0]] · Original: https://www.youtube.com/watch?v=c3b-JASoPi0

An interview. Stephanie Zhan asks the main questions and audience members the rest; their framings (for example "scale is all that matters" at @09:05, the rowing-team joke at @15:06, "democratizing access to AI education" at @20:35, "graduate school for AI models" at @27:46) are theirs, not his, and the wiki does not attribute them to him. The "making AI accessible" title is the event's. The clause "it's not just one agent it's many agents" at @04:39 runs into the host's next question and is not quoted.

## Summary
A 37-minute interview at Sequoia, with Stephanie Zhan asking the questions and a few audience questions at the end. He describes what everyone is building as an LLM OS, with the LLM as a CPU, modalities as peripherals and existing software as the rest of the machine, and expects a few default apps from the big labs alongside an ecosystem of others (@04:05, @05:48, @06:20). He separates open-weights models such as Llama and Mistral from fully open-source ones, ranks scale first among the things that matter while stressing that money alone does not produce a model, and names unifying diffusion and autoregressive models and a thousand- to millionfold energy-efficiency gap as open problems (@07:27, @09:38, @11:15, @12:22, @13:27). He describes how Elon Musk runs companies (small technical teams, no non-technical middle management, direct contact with engineers, removing bottlenecks), and says founders can copy it if they set it up from the start (@16:13, @18:25, @20:02, @22:46). He argues the field has done only the imitation step of AlphaGo and that RLHF is a weak form of RL, recommends getting an LLM product to work before making it cheap, and says the Transformer has been remarkably resilient but is probably not the final architecture (@24:59, @26:39, @29:28, @33:51, @35:30). Throughout, he says he cares about a healthy ecosystem of startups more than any one company (@21:10, @36:06).

## Key points
- Everyone is building an LLM OS: the LLM as CPU, modalities as peripherals, wired into existing software → [[llms-as-operating-systems]]
- Big labs will ship a few default apps, like a browser bundled with Windows, beside an ecosystem of others → [[llms-as-operating-systems]], [[ai-ecosystem]]
- LLM products are "quite autonomous but not fully autonomous", so oversight and evaluation still have to be worked out over the next few years → [[llm-products-will-take-years-to-figure-out]], [[partial-autonomy-apps]], [[this-is-the-decade-of-agents]], [[llm-agents-over-time]]
- Llama and Mistral are open weights, not open source; finetuning without the data and training loop regresses other skills → [[open-weights-models-are-not-open-source]], [[ai-ecosystem]], [[pretraining-and-finetuning]]
- Scale is the first principal component, but data, algorithms and infrastructure expertise also matter → [[scaling-laws]], [[scaling-offers-a-guaranteed-path-to-better-models]], [[compute-efficiency]]
- Diffusion and autoregressive models sit apart with nothing in between → [[sampling-from-language-models]], [[he-does-not-love-autoregressive-sampling]]
- Models are a thousand to a million times less energy-efficient than a brain; precision, sparsity and new hardware are the levers → [[compute-efficiency]], [[ai-is-far-less-energy-efficient-than-the-brain]]
- Elon Musk runs "the biggest startups": small technical teams, intensity, direct contact with engineers; founders can copy it if they start that way → [[elon-musk-management-style]]
- He cares about the ecosystem, a coral reef of startups, more than any one company, and worries about a few megacorps → [[ai-ecosystem]]
- LLMs have done AlphaGo's imitation step, not its RL step; models must practise for themselves; RLHF is a weak form of RL → [[llm-self-improvement]], [[self-improvement-may-be-possible-in-narrow-domains]]
- Get it to work with the best model first, then make it cheaper, for example by distilling → [[make-it-work-then-make-it-cheap]]
- Many build the thing; far fewer build the ramp → [[build-the-ramp-not-just-the-thing]], [[ai-ecosystem]]
- The Transformer is designed for the GPU, remarkably resilient, and probably not the final network → [[transformer-architecture]], [[the-transformer-is-probably-not-the-final-architecture]], [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]

## Fed pages
- [[llms-as-operating-systems]]
- [[partial-autonomy-apps]]
- [[ai-ecosystem]]
- [[pretraining-and-finetuning]]
- [[transformer-architecture]]
- [[compute-efficiency]]
- [[elon-musk-management-style]]
- [[scaling-laws]]
- [[scaling-offers-a-guaranteed-path-to-better-models]]
- [[sampling-from-language-models]]
- [[he-does-not-love-autoregressive-sampling]]
- [[llm-self-improvement]]
- [[self-improvement-may-be-possible-in-narrow-domains]]
- [[llm-products-will-take-years-to-figure-out]]
- [[this-is-the-decade-of-agents]]
- [[open-weights-models-are-not-open-source]]
- [[ai-is-far-less-energy-efficient-than-the-brain]]
- [[the-transformer-is-probably-not-the-final-architecture]]
- [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]
- [[build-the-ramp-not-just-the-thing]]
- [[make-it-work-then-make-it-cheap]]
- [[llm-agents-over-time]]
- [[llm-os-over-time]]
