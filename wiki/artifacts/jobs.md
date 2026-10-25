---
type: artifact
repo_url: https://github.com/karpathy/jobs
language: Python
status: active
sources: ["[[github-2026-03-16-jobs-readme]]"]
aliases: [US Job Market Visualizer, karpathy.ai/jobs, AI exposure treemap, job market visualizer]
context: ["[[github-2025-08-21-rendergit-readme]]"]
---
# jobs
The US Job Market Visualizer: a research tool for exploring the Bureau of Labor Statistics Occupational Outlook Handbook visually, which the README calls a development tool, "not a report, a paper, or a serious economic publication" ([[github-2026-03-16-jobs-readme]] §intro). A live demo is at karpathy.ai/jobs ([[github-2026-03-16-jobs-readme]] §intro). **Note:** `language: Python` is inferred from the pipeline's `.py` scripts run with `uv run python`, and `status: active` from the absence of any archive notice; the README states neither ([[github-2026-03-16-jobs-readme]] §Data pipeline, §Usage).

## What it demonstrates
- **A treemap of the US economy.** The OOH covers 342 occupations across every sector, with duties, work environment, education, pay and projections; the README says "we" scraped all of it and built a treemap whose rectangle areas are total employment and whose colour is one of four metrics: BLS projected growth outlook, median pay, education requirements and AI exposure ([[github-2026-03-16-jobs-readme]] §What's here, §Data pipeline).
- **LLM-powered colouring.** "You write a prompt, the LLM scores each occupation, and the treemap colors accordingly." The "Digital AI Exposure" layer is one such prompt, and the README suggests others, such as exposure to humanoid robotics, offshoring risk or climate impact, by forking `score.py` ([[github-2026-03-16-jobs-readme]] §LLM-powered coloring, §Data pipeline).
- **The scores are the LLM's.** Each occupation's Markdown description goes to an LLM with a rubric and gets an AI Exposure score from 0 to 10 with a rationale; the README calls the scores rough estimates from Gemini Flash via OpenRouter, not rigorous predictions. For example, the tool's LLM scores software developers 9/10; see [[many-high-ai-exposure-jobs-will-be-reshaped-not-replaced]] ([[github-2026-03-16-jobs-readme]] §Data pipeline, §LLM-powered coloring).
- **The pipeline.** Playwright scrapes the 342 pages, run non-headless because BLS blocks bots; BeautifulSoup turns the HTML into Markdown; structured fields go to a CSV; the LLM scores each occupation; scores and stats merge into `site/data.json`; a static site renders the treemap ([[github-2026-03-16-jobs-readme]] §Data pipeline). The raw BLS HTML, about 40MB, is kept as the source of truth ([[github-2026-03-16-jobs-readme]] §Key files).
- **A file to paste into an LLM.** `prompt.md` packs aggregate statistics, tier breakdowns, exposure by pay and education, projections and all 342 occupations with scores and rationales into one file of about 45K tokens, "designed to be pasted into an LLM", for a data-grounded conversation about AI's impact on jobs without running code ([[github-2026-03-16-jobs-readme]] §LLM prompt). **Note:** this parallels [[rendergit]]'s LLM View, one page made for an LLM to read; both READMEs say "LLM", not "agent" ([[github-2025-08-21-rendergit-readme]] §Features; [[github-2026-03-16-jobs-readme]] §LLM prompt).

## Related
- [[ai-and-the-economy]] — occupation-level AI exposure
- [[rendergit]] — another repo that renders something for an LLM to read
