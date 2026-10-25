# Verification: batch 4, group E3 (nanochat 2h post, autoresearch Discussion #43, autoresearch round-1 post, jobs README, Skill Issue, autoresearch README)
Verified 2026-10-25 by a fresh reader. Sources: [[x-2026-03-05-nanochat-gpt-2-in-two-hours]], [[github-2026-03-08-autoresearch-session-report]], [[x-2026-03-09-autoresearch-tuning-nanochat]], [[github-2026-03-16-jobs-readme]], [[talk-2026-03-20-skill-issue]], [[github-2026-03-21-autoresearch-readme]]

## Coverage
- pages checked: 44. That is the 6 source pages; 17 claim pages; 3 timelines (vibe-coding-over-time, llm-agents-over-time, llm-self-improvement-over-time); 4 artifacts (autoresearch, jobs, nanochat, microgpt); 11 topics (claws, partial-autonomy-apps, building-for-agents, vibe-coding, llm-self-improvement, jagged-intelligence, ai-ecosystem, ai-and-the-economy, pretraining-and-finetuning, llm-evaluation, compute-efficiency); and 3 methods (ai-assisted-coding-loop, quick-experiment-loop, small-hackable-educational-code).
- claim pages fully checked: 11 (the ten E3 claims plus autocomplete-is-his-coding-sweet-spot). On the other six claim pages (coding-models-are-weak…, vibe-coding-will-terraform-software, physical-automation-will-lag…, micrograd-is-all-you-need…, software-2-0-automates…, verifiability-drives…), every sentence that cites an E3 source was checked, along with its supports/extends back-link.
- timeline entries checked: 5 dated entries citing E3 sources, plus all 5 Notes that cite them, including the rewritten closing Note on vibe-coding-over-time.
- other sentences checked: about 120 of about 230. Every quote was grepped against the raw file.
- Skill Issue: I read the whole transcript, not only the cited blocks. I re-checked who is speaking against the digest's Notes for merge.

## Findings
### F1 — overstated — [[talk-2026-03-20-skill-issue]], [[vibe-coding-over-time]], [[llm-agents-over-time]]
- sentences: source page Summary "He now runs several agent sessions in parallel as "macro actions" over a repository"; frontmatter summary "delegates nearly all his coding to parallel agents"; vibe-coding-over-time 2026-03-20 entry "he now runs several agents in parallel"; llm-agents-over-time 2026-03-20 entry "Runs several agents in parallel".
- cited: @04:25 (and @01:41)
- raw says: Parallel running is something he aspires to, and he describes it in general terms. At @02:13 he asks "how can I have more of them?". At @03:53–@04:25 he describes Peter's tiled Codex agents, then the macro-action mode in the second person ("delegate it to agent one… agent two"). At @01:41 he says he delegates most of his coding, but he never says he himself runs several in parallel. ai-assisted-coding-loop phrases this correctly, as a mode he describes.
- fix: Summary: "He describes running several agents in parallel as "macro actions" over a repository, asks how he can run more of them, feels that failures are mostly a skill issue…". Frontmatter summary: "…he delegates nearly all his coding to agents and wants to run many in parallel…". vibe-coding-over-time: "…hardly typing a line of code since; he describes running several agents in parallel on macro actions". llm-agents-over-time: "Describes running several agents in parallel on macro actions, describes claws…".

### F2 — minor — [[all-frontier-labs-will-autoresearch]]
- sentence: "all the frontier labs, he says, "are all trying to recursively self-improve roughly speaking""
- cited: [[talk-2026-03-20-skill-issue]] @18:04
- raw says: "they're all trying to recursively self-improve roughly speaking". The quoted words are not verbatim: the raw has "they're", the quote has "are".
- fix: "…all the frontier labs, he says, "they're all trying to recursively self-improve roughly speaking"…", or move the quotation mark to start at "trying".

### F3 — minor — [[expect-more-speciation-of-models]]
- sentence: "The host's remark at @31:08 that little speciation has been seen is not his"
- cited: [[talk-2026-03-20-skill-issue]] @31:08
- raw says: The line opens "The question makes sense and I guess… I don't think we've seen too much speciation just yet". That reads as the answer to the host's "Does that question make sense to you?", so it may well be his. The digest and the source page both mark the speaker as unclear. Leaving it out is right; calling it the host's is not supported.
- fix: "The remark at @31:08 that little speciation has been seen has an unclear speaker and is not attributed to him ([[talk-2026-03-20-skill-issue]] @31:08)."

### F4 — minor — [[small-hackable-educational-code]]
- sentence: "He declines to add other platforms because it would bloat the code"
- cited: [[github-2026-03-21-autoresearch-readme]] §Platform support
- raw says: Support for other platforms is "quite possible" but would bloat the code, and he is "not 100% sure" he wants to take it on personally right now. He also invites forks.
- fix: "He hesitates to add other platforms himself because it would bloat the code, and points to forks instead ([[github-2026-03-21-autoresearch-readme]] §Platform support)."

### F5 — minor — [[claws]]
- sentence: "His word for a layer above coding agents that takes persistence much further…"
- cited: [[talk-2026-03-20-skill-issue]] @07:07
- raw says: He uses "claw" for this layer and names OpenClaw (Peter's project). He does not claim to have coined the word, and "His word for" can read as coinage.
- fix: "The word he uses for a layer above coding agents…"

### F6 — minor — [[vibe-coding-over-time]] (first Note; existing text, now ambiguous)
- sentence: "…the April "not for anything important" is stated as of today, beside the December view that it will reshape software."
- cited: [[blog-2025-12-19-year-in-review-2025]]
- raw says: This "December" means the 2025-12-19 review. The rewritten closing Note now uses "December" for the yearless flip he describes in Skill Issue, so a reader can run the two together.
- fix: "…beside the 2025-12-19 view that it will reshape software."

## Checked and correct
- [[he-now-delegates-most-coding-to-agents]]: all sentences supported. The quote is verbatim at @01:41, and the 80/20 → 20/80 figures are at @01:41. "Something flipped" is his own wording. "December" carries no year anywhere on the page. The host's "code's not even the right verb" is not attributed to him. The extends link is real on both sides. He states the change himself (@01:41), and the Dwarkesh text gives "For now, autocomplete is my sweet spot" (lXUZvyajciY @37:33) with the three classes at @30:43. The two describe different periods ("for now" and "since December"), so not setting contradicts is correct.
- [[autocomplete-is-his-coding-sweet-spot]]: the extends entry and the Skill Issue context are supported.
- [[vibe-coding-over-time]]: the 2026-03-20 entry is correct apart from F1. The rewritten closing Note is correct. "December" has no year there. It calls this a change he states himself (@01:41), not an editorial reading. It says the October claim is kept, cites the microGPT restatement correctly (@1:04:59, @1:05:33), and correctly says he does not call the new practice vibe coding.
- [[llm-agents-over-time]]: the 2026-03-05 entry is correct; "the feeling of post-agi :)" is verbatim and the 110 changes are labelled as the agents'. The 2026-03-09 entry is correct. Both Notes are correct, including the "not RL on the model" framing.
- [[llm-self-improvement-over-time]]: the 2026-03-09 and 2026-03-20 entries are correct. Both Notes are correct. Autoresearch is described as an agent editing training code against a metric, not RL on the model, and the 2026-03-09 post indeed does not call it RL or self-improvement.
- [[autoresearch-found-real-improvements-to-nanochat]], [[agent-failures-mostly-feel-like-a-skill-issue]], [[take-yourself-out-of-the-agent-loop]], [[autoresearch-needs-an-objective-metric]], [[what-rl-does-not-optimize-does-not-improve]], [[cheaper-software-will-raise-demand-for-it]], [[many-high-ai-exposure-jobs-will-be-reshaped-not-replaced]]: titles, quotes (all verbatim), Context, Related and confidence are all supported. The ~700 and ~20 counts are labelled as the agent's run and the transfer test as his own. The 9/10 score is always "the tool's LLM scores". The supports back-links from software-2-0-automates… and verifiability-drives… are present.
- [[all-frontier-labs-will-autoresearch]], [[expect-more-speciation-of-models]]: all other sentences are supported.
- [[github-2026-03-08-autoresearch-session-report]] / Discussion #43 rule: no page other than the autoresearch artifact and its own source page cites it, and every sentence there is labelled as the agent's. I checked the figures against the raw: 126/23/102/1, about 10.5 h, H100 80GB, 0.997900 → 0.969686, 0.0282. The ~0.0028 claim and the log sums (about 0.0017; about 0.0022 with the embedding-LR and lm_head rows) are both correct, and the mismatch is stated, not reconciled.
- [[jobs]], [[ai-and-the-economy]] (both jobs paragraphs): the scores are never presented as his ratings. The "we" and the "not a report" framing are correct.
- [[autoresearch]] artifact: all README, X-post and Skill Issue sentences are supported. The italic opening is treated as a joke, and its quote is verbatim.
- [[nanochat]], [[microgpt]], [[quick-experiment-loop]], [[ai-assisted-coding-loop]], [[building-for-agents]], [[partial-autonomy-apps]], [[vibe-coding]], [[llm-self-improvement]], [[jagged-intelligence]], [[ai-ecosystem]], [[pretraining-and-finetuning]], [[llm-evaluation]], [[compute-efficiency]]: every sentence I checked is supported, and the quotes are verbatim ("tries out ideas, merges them when they work and iterates"; "I am slightly suspicious about about goodharting"; "centralization has a very poor track record in my view"; "I'm not explaining to people anymore."; "the customer is not the human anymore").
- The cited Skill Issue sentences on [[coding-models-are-weak-at-code-never-written-before]], [[vibe-coding-will-terraform-software]], [[physical-automation-will-lag-digital-automation]], [[micrograd-is-all-you-need-everything-else-is-efficiency]], [[software-2-0-automates-what-you-can-verify]] and [[verifiability-drives-the-jagged-frontier]] are all supported.
- Source pages for the 2026-03-05 post, the 2026-03-09 post, the jobs README and the autoresearch README: Summaries and Key points are supported.
