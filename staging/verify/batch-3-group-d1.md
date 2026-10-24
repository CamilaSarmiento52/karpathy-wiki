# Verification: batch 3, group D1 (LLM101n README, No Priors ep. 80, I love calculator, llm.c README, GPU MODE post, CUDA MODE keynote)
Verified 2026-10-24 by a fresh reader. Sources: [[github-2024-08-01-llm101n-readme]], [[talk-2024-09-05-no-priors-ep-80]], [[blog-2024-09-08-i-love-calculator]], [[github-2024-09-24-llmc-readme]], [[x-2024-10-02-gpu-mode-talk]], [[talk-2024-10-03-cuda-mode-keynote]]

## Coverage
- pages checked: 43. Six source pages; claims there-is-a-massive-gap-between-demo-and-product, tesla-is-ahead-of-waymo-in-self-driving, humanoid-robots-should-start-in-your-own-factory, the-architecture-is-no-longer-the-bottleneck, synthetic-data-is-the-future-if-you-keep-its-entropy, a-cognitive-core-could-be-a-billion-parameters-or-less, ai-should-be-the-front-end-of-a-teacher-designed-course, post-agi-education-will-be-like-going-to-the-gym, llms-may-write-custom-low-level-code-for-any-application, technology-could-be-like-the-calculator, this-is-the-decade-of-agents, the-transformer-is-a-general-purpose-efficient-optimizable-computer, small-llms-can-be-strong-in-narrow-domains, llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements, his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag, neural-net-training-should-not-be-complicated; timeline llm-agents-over-time; topics self-driving, ai-for-education, user-hostile-technology, ai-ecosystem, llm-self-improvement, llm-tool-use, llms-as-operating-systems, pretraining-and-finetuning, scaling-laws, software-3-0, transformer-architecture, prompting-llms, pytorch, compute-efficiency; artifacts llm101n, llm-c, nanogpt, nn-zero-to-hero; methods port-a-pytorch-model-to-c-and-cuda (Fed list only), reproduce-a-published-model, small-hackable-educational-code, verify-against-a-reference-implementation, build-and-publish-projects, spelled-out-build-from-scratch.
- claim pages fully checked: 16 (the 10 D1 claims in full; the other 6 for every sentence citing a D1 source, plus both sides of each `supports` link).
- timeline entries checked: 1 of 1 D1 entry (2024-09-05), plus the closing Note.
- other sentences checked: about 75 of about 120 (all of self-driving, ai-for-education, user-hostile-technology and llm101n; all D1-cited lines on the other pages).
- Fed pages: every source page's `## Fed pages` matches exactly the pages that cite it (checked by grep).
- Quotes: all 10 D1 claim quotes are verbatim at the cited block and are his. Host checks: "exocortex" first appears in his own line (@22:59); the hosts use it later (@25:13, @29:09) and no page gives him their lines. The cognitive-core "billion parameters gets you a good core" line (@28:36) is credited to a host on the claim page. "Eureka" is a host's word (@41:01) and is never given to him.

## Findings
### F1 — overstated — [[ai-for-education]]
- sentence: "His planned first course, LLM101n, is being developed by Eureka Labs, according to its README"
- cited: [[github-2024-08-01-llm101n-readme]] §intro
- raw says: the README says only that the course does not yet exist and is being developed by Eureka Labs. It never says "first". "First course" is a host's phrase in No Priors (@41:01), and that interview never names LLM101n. Treating the two as the same course is the wiki's inference.
- fix: "His planned course LLM101n is being developed by Eureka Labs, according to its README ([[github-2024-08-01-llm101n-readme]] §intro)." If the link to the No Priors course is wanted, add it as a **Note:**.

### F2 — mis-cited (host's words given to him) — [[self-driving]]
- sentence: "He worked on the Tesla humanoid before he left and says basically everything transfers from cars: cars are robots, and Tesla is a robotics-at-scale company"
- cited: [[talk-2024-09-05-no-priors-ep-80]] @06:02, @06:37
- raw says: "you worked on the um Tesla humanoid robot before you left" is the host's question (@06:02). He does not restate it. "Everything transfers", "cars are robots" and "robotics at scale company" are his lines (@06:37).
- fix: "A host notes that he worked on the Tesla humanoid before leaving; he says basically everything transfers from cars: cars are robots, and Tesla is a robotics-at-scale company ([[talk-2024-09-05-no-priors-ep-80]] @06:02, @06:37)."

### F3 — overstated — [[post-agi-education-will-be-like-going-to-the-gym]]
- sentence (title): "After AGI, he hopes education will be more like entertainment, effortful the way the gym is"
- cited: [[talk-2024-09-05-no-priors-ep-80]] @39:56, @41:01
- raw says: the entertainment part is a prediction: "I think education is entertainment to a much larger extent" (@39:56). Only the gym part is a hope: "what I would hope happens is people … go to the gym a lot" (@41:01). The title turns the prediction into a hope.
- fix: title "After AGI, he thinks education will be largely entertainment, and hopes people will go to a mental gym". The slug can stay.

### F4 — minor — [[there-is-a-massive-gap-between-demo-and-product]]
- sentence (title): "In self-driving, and he expects in AGI, there is a massive gap between a demo and a product, and then between a product and its globalisation"
- cited: [[talk-2024-09-05-no-priors-ep-80]] @01:39, @02:11
- raw says: he frames the second gap as "going from a demo to an actual globalization of it … a big gap". He says "I suspect" AGI will look similar, not "expects".
- fix: "In self-driving, and he suspects in AGI, there is a massive gap between a demo and a product, and a big gap between a demo and its globalisation"

### F5 — minor (wrong reading) — [[transformer-architecture]]
- sentence: "Since the Llama release the major change is RoPE positional encodings; everything else is about plus 3%, over the last five years or so"
- cited: [[talk-2024-09-05-no-priors-ep-80]] @16:29, @17:01
- raw says: he uses the Llama release as an example of how little the Transformer has changed in about five years. RoPE is the one major change in it. Nothing has changed "since" Llama.
- fix: "In the Llama release, he says, the Transformer has changed little: RoPE positional encodings are the major change in about five years, and everything else is about plus 3% ([[talk-2024-09-05-no-priors-ep-80]] @16:29, @17:01)."

### F6 — mis-cited — [[llm-agents-over-time]]
- sentence: "**2024-09-05** — Self-driving reached AGI "a little bit" a decade after a near-perfect demo, yet has not spread across the world; he expects AGI to look similar. … ([[talk-2024-09-05-no-priors-ep-80]] @01:39, @02:11)"
- raw says: the decade after the near-perfect Waymo demo is in the @01:07 block, which is not cited. His verb is "suspect".
- fix: cite "@01:07, @01:39, @02:11" and change "he expects AGI" to "he suspects AGI".

### F7 — minor (mis-cited) — [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]
- sentence: "…he again calls the Transformer a general-purpose training computer, a differentiable computer, … ([[talk-2024-09-05-no-priors-ep-80]] @15:24, @17:01)"
- raw says: "general purpose training computer" is at the end of the @14:49 block. "differentiable computer" is at @15:24.
- fix: cite "@14:49, @15:24, @17:01", as the other side of the link already does.

### F8 — minor (overstated) — [[user-hostile-technology]]
- sentence: "His name for technology drifting toward the "complex, dependency-bloated, user-hostile" products he contrasts with the pocket calculator…"
- cited: [[blog-2024-09-08-i-love-calculator]] §intro
- raw says: "user-hostile" is one adjective in a list ("complex, dependency-bloated, user-hostile, anti-pattern-ridden mess"). He does not offer it as a name.
- fix: "Technology drifting toward what he calls a "complex, dependency-bloated, user-hostile" mess, which he contrasts with the pocket calculator…"

## Points asked about
- **Ten D1 claims:** all quotes are verbatim and his, and every `confidence: stated` is right. Fixes needed only on titles (F3, F4).
- **llm-agents-over-time 2024-09-05 entry and closing Note:** the entry correctly flags "AGI here, not agents" but needs F6. The closing Note starts with **Note:**, calls itself an editorial reading, and does not hide a claim. Its point that the 2023 caution is never withdrawn holds for the No Priors entry. Correct.
- **`supports` links:** all three are set on both sides, and each Related line cites both sources.
  - this-is-the-decade-of-agents ↔ there-is-a-massive-gap-between-demo-and-product: real. It is the same Waymo-decade argument, and both pages say AGI versus agents and 2014 versus 2013.
  - the-transformer-is-a-general-purpose-efficient-optimizable-computer ↔ the-architecture-is-no-longer-the-bottleneck: real. He again calls it a general-purpose, differentiable computer that has barely changed. The CS25 citations @21:39 and @59:18 check out. Only the timestamp in F7 needs fixing.
  - small-llms-can-be-strong-in-narrow-domains ↔ a-cognitive-core-could-be-a-billion-parameters-or-less: weak but defensible, and both pages say the ideas differ. The llama2.c "~100M - ~1B" line is verbatim in §contributing.
- **llm.c speed figures:** each figure is tied to its own source.
  - README: about 7%, with no setting given, and the Note correctly refuses to merge it with the 2024-05-03 ~7%.
  - X post: 29% less memory and 19% faster, "(at the time)".
  - Keynote @19:17: 30% and 20%, with his hedges. Compile and run speed is @19:50.
  - The Note calling 30%/20% rounded versions of 29%/19% is labelled and cites both sources.
  - The $672 (X post) and "roughly $600" (keynote) figures are also kept apart on reproduce-a-published-model and llm-c.
- **`llm101n` status `archived`:** this rests on the README text itself: "Until it is ready I am archiving this repo" (§intro banner). The artifact does not add Eureka Labs facts beyond the banner. The Berkeley @13:01 mention and the 2024-08-01 commit date are given as dates with no interval between them. Correct.

## Checked and correct
- [[talk-2024-09-05-no-priors-ep-80]] (source page): Summary and Key points, 14 sentences checked, all supported. The host and Eureka note is accurate.
- [[talk-2024-10-03-cuda-mode-keynote]], [[x-2024-10-02-gpu-mode-talk]], [[github-2024-09-24-llmc-readme]], [[blog-2024-09-08-i-love-calculator]], [[github-2024-08-01-llm101n-readme]] (source pages): Summaries, all supported. The "very likely the same talk" inference is a labelled Note on both pages.
- [[tesla-is-ahead-of-waymo-in-self-driving]], [[humanoid-robots-should-start-in-your-own-factory]], [[the-architecture-is-no-longer-the-bottleneck]], [[synthetic-data-is-the-future-if-you-keep-its-entropy]], [[a-cognitive-core-could-be-a-billion-parameters-or-less]] (cognitive core and exocortex lines attributed correctly), [[ai-should-be-the-front-end-of-a-teacher-designed-course]], [[llms-may-write-custom-low-level-code-for-any-application]], [[technology-could-be-like-the-calculator]]: every sentence supported.
- [[there-is-a-massive-gap-between-demo-and-product]] and [[post-agi-education-will-be-like-going-to-the-gym]]: body sentences all supported. The titles need F4 and F3.
- [[this-is-the-decade-of-agents]], [[small-llms-can-be-strong-in-narrow-domains]], [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]], [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]] (@18:44), [[neural-net-training-should-not-be-complicated]] (@06:37, @07:09, @19:50): every D1-cited sentence supported.
- [[self-driving]]: 22 sentences; all supported except F2.
- [[ai-for-education]]: 20 sentences; all supported except F1. Host lines (Diamond Age, Bloom, lineage question, Eureka) are correctly attributed.
- [[user-hostile-technology]]: 12 sentences; all supported except F8. The shareholder-value point is correctly written as questions.
- [[ai-ecosystem]] ("not your weights, not your brain" given to him, as the digest reads it; "100%" answer correct), [[llms-as-operating-systems]] (exocortex @22:59 his; companies and swarm lines), [[llm-self-improvement]], [[llm-tool-use]], [[pretraining-and-finetuning]], [[scaling-laws]], [[software-3-0]], [[prompting-llms]], [[pytorch]], [[compute-efficiency]]: D1 sentences all supported.
- [[transformer-architecture]]: D1 sentences all supported except F5.
- [[llm101n]], [[llm-c]] (about 20 forks: the raw lists 19), [[nanogpt]], [[nn-zero-to-hero]], [[reproduce-a-published-model]], [[small-hackable-educational-code]], [[verify-against-a-reference-implementation]], [[build-and-publish-projects]], [[spelled-out-build-from-scratch]]: D1 sentences all supported.
