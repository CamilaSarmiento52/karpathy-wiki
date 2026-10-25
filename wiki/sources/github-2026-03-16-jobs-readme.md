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

Read at commit f51275d. Text under the title, before the first `##` heading, is cited as `§intro`. The AI exposure scores are produced by the tool's LLM (Gemini Flash via OpenRouter), not by him; the README speaks as "we".

## Summary
The README describes a research tool for exploring the Bureau of Labor Statistics Occupational Outlook Handbook visually, and says it is not a report, a paper or a serious economic publication (§intro). It covers all 342 OOH occupations as an interactive treemap: each rectangle's area is total employment, and its colour is the selected metric, which can be projected growth, median pay, education or AI exposure (§What's here). The colouring is LLM-powered: a prompt has an LLM score every occupation, and the "Digital AI Exposure" layer is one such prompt, estimating how much current, mainly digital AI will reshape each job (§LLM-powered coloring). The README lists what that score is not: it does not predict that a job will disappear, does not account for demand elasticity, latent demand, regulation or social preferences, and is a rough LLM estimate from Gemini Flash via OpenRouter; many high-exposure jobs will be reshaped, not replaced (§LLM-powered coloring). A six-step pipeline goes scrape, parse, tabulate, score, build site data, website, and a `prompt.md` file packs all the data into about 45K tokens to paste into an LLM (§Data pipeline, §LLM prompt).

## Key points
- The treemap, the scoring pipeline and the prompt file → [[jobs]]
- Occupation-level AI exposure, and what it does not predict → [[ai-and-the-economy]]
- High-exposure jobs reshaped, not replaced; software demand could grow → [[many-high-ai-exposure-jobs-will-be-reshaped-not-replaced]]

## Fed pages
- [[jobs]]
- [[ai-and-the-economy]]
- [[many-high-ai-exposure-jobs-will-be-reshaped-not-replaced]]
- [[cheaper-software-will-raise-demand-for-it]]
