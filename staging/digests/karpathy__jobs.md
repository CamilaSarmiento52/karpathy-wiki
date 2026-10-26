# Digest: jobs README
- raw: raw/github/karpathy__jobs.md · published: 2026-03-16 · medium: github · words: 684 (frontmatter; `wc -w` 707 with frontmatter) · commit: f51275d8b076bac4159c7370ff3acc2121cf1296
- source slug: github-2026-03-16-jobs-readme

What it is: **about AI and the job market, not a personal tool.** It is a research and visualisation tool for US occupation data. One of its four colour layers is an LLM-estimated "Digital AI Exposure" score per occupation, and the README says what that score does and does not mean.

## Source page
```
---
type: source
raw_path: raw/github/karpathy__jobs.md
published: 2026-03-16
medium: github
summary: "README of his US Job Market Visualizer, a treemap of 342 BLS occupations that can be coloured by growth outlook, pay, education or an LLM-scored AI exposure, with caveats that exposure does not mean a job will disappear."
url: https://github.com/karpathy/jobs
title: jobs README
---
# jobs README
Raw: [[raw/github/karpathy__jobs]] · Original: https://github.com/karpathy/jobs

Read at commit f51275d. Text under the title, before the first `##` heading, is cited as `§intro`.

## Summary
The README describes a research tool for exploring the Bureau of Labor Statistics Occupational Outlook Handbook visually, and says it is not a report, a paper or a serious economic publication (§intro). It covers all 342 OOH occupations as an interactive treemap: each rectangle's area is total employment, and its colour is the selected metric, which can be projected growth, median pay, education or AI exposure (§What's here). The colouring is LLM-powered: a prompt scores every occupation, and the "Digital AI Exposure" layer is one such prompt, estimating how much current, mainly digital AI will reshape each job (§LLM-powered coloring). The README lists what that score is not. It does not predict that a job will disappear, does not account for demand elasticity, latent demand, regulation or social preferences, and is a rough LLM estimate from Gemini Flash via OpenRouter; many high-exposure jobs will be reshaped, not replaced (§LLM-powered coloring). A six-step pipeline goes scrape, parse, tabulate, score, build site data, website, and a `prompt.md` file packs all the data into about 45K tokens to paste into an LLM (§Data pipeline, §LLM prompt).

## Key points
- The treemap, the scoring pipeline and the prompt file → [[jobs]]
- Occupation-level AI exposure, and what it does not predict → [[ai-and-the-economy]]
- High-exposure jobs reshaped, not replaced; software demand could grow → [[many-high-ai-exposure-jobs-will-be-reshaped-not-replaced]]

## Fed pages
- [[jobs]]
- [[ai-and-the-economy]]
- [[many-high-ai-exposure-jobs-will-be-reshaped-not-replaced]]
```

## Candidates

### artifact: jobs
- existing: no (no `jobs`, "job market" or "BLS" in `wiki/index/artifacts.md` or anywhere in `wiki/`)
- repo_url: https://github.com/karpathy/jobs
- language: Python (the pipeline is `.py` scripts run with `uv run python`; the site is a static `site/index.html`). Inferred from the file list; the README does not name a language.
- status: active (no deprecation or archive notice)
- aliases: [US Job Market Visualizer, karpathy.ai/jobs, AI exposure treemap, job market visualizer]
- statements:
  - It is a research tool for visually exploring the BLS Occupational Outlook Handbook. The README calls it a development tool, not a report, a paper or a serious economic publication (§intro)
  - A live demo is at karpathy.ai/jobs (§intro)
  - The OOH covers 342 occupations across every sector of the US economy, with duties, work environment, education, pay and projections; the README says "we" scraped all of it (§What's here)
  - The treemap sizes each rectangle by total employment and colours it by one of four metrics: BLS projected growth outlook, median pay, education requirements and AI exposure (§What's here, §Data pipeline step 6)
  - The colouring is a general mechanism: you write a prompt, the LLM scores each occupation, and the treemap colours accordingly. The README suggests other prompts, such as exposure to humanoid robotics, offshoring risk or climate impact, and says to fork `score.py` for your own (§LLM-powered coloring, §Data pipeline step 4)
  - Pipeline: Playwright scrapes the 342 pages, non-headless because BLS blocks bots; BeautifulSoup converts the HTML to Markdown; structured fields go to a CSV; an LLM gives each occupation a 0–10 AI Exposure score with a rationale; scores and stats are merged into `site/data.json`; a static site renders the treemap (§Data pipeline)
  - The raw BLS HTML (~40MB) is kept as the source of truth (§Key files)
  - `prompt.md` packs aggregate statistics, tier breakdowns, exposure by pay and education, projections and all 342 occupations with scores and rationales into one ~45K-token file to paste into an LLM, for a data-grounded conversation about AI's impact on the job market without running code (§LLM prompt)
  - Setup uses `uv` and Playwright Chromium and needs an OpenRouter API key (§Setup, §Usage)
- relation: **Note** candidates only. `prompt.md`, one file made to paste into an LLM, parallels [[rendergit]]'s LLM View (`github-2025-08-21-rendergit-readme` §Features). Like rendergit, the README says "LLM", not "agent", so link it from [[building-for-agents]] only with the same caveat batch 3 gave rendergit, or not at all.

### topic: ai-and-the-economy (existing; extend)
- existing: yes (`wiki/topics/ai-and-the-economy.md`; sources so far: Dwarkesh only)
- aliases to add: [AI and jobs, AI exposure, job market, occupations]
- proposed section: **AI exposure by occupation (2026-03-16).**
- statements:
  - His job-market tool colours 342 US occupations by an LLM-estimated "Digital AI Exposure", which estimates how much current AI, which the README calls primarily digital, will reshape each occupation (§What's here, §LLM-powered coloring)
  - The README says the exposure score does not predict that a job will disappear. Software developers score 9/10 because AI is transforming their work, yet demand for software "could easily" grow as each developer becomes more productive (§LLM-powered coloring)
  - It says the score does not account for demand elasticity, latent demand, regulatory barriers or social preferences for human workers (§LLM-powered coloring)
  - It calls the scores rough LLM estimates, not rigorous predictions, and says many high-exposure jobs will be reshaped, not replaced (§LLM-powered coloring)
  - It frames the tool as exploration, not a report, paper or serious economic publication (§intro)
- **Note** candidates for this page, each citing both sources:
  - The README's reshaped-not-replaced framing sits next to his Dwarkesh remark that society will refactor jobs around which of their tasks are automatable (`talk-2025-10-17-dwarkesh-ghosts-not-animals` @1:09:16). Both describe jobs changing by task rather than vanishing whole. This is a connection, not his statement.
  - "Digital AI Exposure", on the grounds that current AI is primarily digital (§LLM-powered coloring), with humanoid robotics offered as a different prompt, sits next to [[physical-automation-will-lag-digital-automation]]. The README does not forecast a lag, so it is a Note only.
  - Software developers as the 9/10 example sits next to "coding first" on this page (`talk-2025-10-17-dwarkesh-ghosts-not-animals` @1:14:46). The README gives no reason for the score beyond "AI is transforming their work", so it is a Note, not evidence for coding first.

### claim: many-high-ai-exposure-jobs-will-be-reshaped-not-replaced
- existing: no
- title: "Many jobs highly exposed to AI will be reshaped, not replaced"
- confidence: stated (README text in his repo, under "What 'AI Exposure' is NOT")
- quote: "Many high-exposure jobs will be reshaped, not replaced." (§LLM-powered coloring)
- topic: [[ai-and-the-economy]]
- statements:
  - The README says a high AI exposure score does not predict that a job will disappear (§LLM-powered coloring)
  - Its example: software developers score 9/10 because AI is transforming their work, but demand for software could easily grow as each developer becomes more productive (§LLM-powered coloring). Keep "could easily": it is a possibility, not a forecast.
  - It names what the score leaves out: demand elasticity, latent demand, regulatory barriers and social preferences for human workers (§LLM-powered coloring)
  - It says the scores are rough Gemini Flash estimates, not rigorous predictions (§LLM-powered coloring)
- why a claim, and how strong: a clear position stated as one sentence, but made as a caveat on the tool's own score, not as a forecast argued at length. "Many", not "most" or "all". Do not strengthen it to "AI will not destroy jobs".
- relation to existing claims:
  - [[vibe-coding-will-terraform-software]] (2025-12-19, "terraform software and alter job descriptions"): **none, Note only.** Both describe jobs changing rather than disappearing. That claim is about vibe coding and software, while this one is about AI exposure across occupations, and neither gives evidence for the other. Recommend a labelled **Note:** in Related claims, citing `blog-2025-12-19-year-in-review-2025` §5 and this source §LLM-powered coloring. Do not use `extends`: that would need a timeline, and the README does not present itself as broadening the earlier essay.
  - [[ai-will-not-show-up-as-a-jump-in-gdp]]: none (growth, not occupations).
  - [[physical-automation-will-lag-digital-automation]]: none (see the topic Note above).
  - [[llm-judges-are-gameable-rewards]]: none. Here the LLM scores occupations for a visualisation; it is not a reward signal. Do not link.

## Quotes
- "it is a development tool for exploring BLS data visually" (§intro)
- "This is not a report, a paper, or a serious economic publication" (§intro)
- "You write a prompt, the LLM scores each occupation, and the treemap colors accordingly." (§LLM-powered coloring)
- "it estimates how much current AI (which is primarily digital) will reshape each occupation" (§LLM-powered coloring)
- "The scores are rough LLM estimates (Gemini Flash via OpenRouter), not rigorous predictions." (§LLM-powered coloring)
- "Many high-exposure jobs will be reshaped, not replaced." (§LLM-powered coloring)
- "designed to be pasted into an LLM" (§Key files and §LLM prompt; this string occurs twice in the raw)

All grepped against the raw file and under 15 words. The README's bold and italics ("does **not**", "*grow*") are avoided in quotes so string matches work.

## Notes for merge
- **It feeds more than its own source page:** one new artifact, one new claim, and a section on the existing [[ai-and-the-economy]] topic. It also widens that topic's `last_updated` to 2026-03-16.
- **The README speaks as "we"** ("We scraped all of it"). The repo is his and the raw `author` is Andrej Karpathy. Write "the README says" for its caveats rather than putting the plural into his mouth.
- **The scores are Gemini Flash's estimates, not his judgements.** Never write "he rates software developers 9/10". Write "the tool's LLM scores them 9/10".
- **Later sources talk about this tool. Do not cite them from here.** `raw/talks/kwSVtQ7dziU.md` (published 2026-03-20, "Skill Issue") has him talking about looking at the job market and professions around @38:11. `raw/blog/verifiability.md` (published 2025-11-17) discusses forecasting job-market impact by specifiability. Neither has a source page yet. When they are ingested, they are where his own reasons for building the tool and any wider jobs view belong, and they may support or extend this claim. Do not write order between them and this README.
- **LLM-as-scorer method:** a "score items with an LLM rubric, re-run with another prompt" method is visible here, but from one README. Keep it as an artifact section rather than a method page, unless a later source repeats it.
- `language` and `status` are inferred, as noted on the artifact candidate.
