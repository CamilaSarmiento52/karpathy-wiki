# Batch 4 merge map

Decided 2026-10-25 from the digest candidate lists. Same rules as batches 1–3: merge creates
ONLY the pages named here (plus source pages); everything else becomes cited sentences on
the page its "→" names; existing pages are extended. Four batch 4 raw files were compiled in
phase 1 (nanoGPT README, year in review, LLM knowledge bases, nanochat README); they are
linked, not re-ingested. Relations: CLAUDE.md's weakest true link; `extends` only where the
map says, each on a timeline.

## AI-written sources (CLAUDE.md §3)

- **`github-2026-03-08-autoresearch-session-report`** (autoresearch Discussion #43) was
  written by the agent, not by him. Its source page says so in the Summary. It feeds only
  the `autoresearch` artifact, as "the agent's session report", with its numbers labelled
  as the agent's (its claimed ~0.0028 gain does not match its own log; say so, do not
  reconcile). No claim cites it.
- **`blog-2026-04-30-sequoia-ascent-2026-summary`**: only §intro (~130 words) is his. The
  first-person summary and the cleaned transcript were produced by Codex. Cite the talk
  (`talk-2026-04-29-sequoia-ascent-2026`) for everything he said at the event. The blog is
  cited only for its intro (he made his content legible to LLMs, and his verdict on the
  Codex text), and its source page names the AI-written parts and what they add or soften.

## Source pages and merge groups

| group | raw stem | source slug |
|---|---|---|
| E1 | karpathy__nanochat__discussion-164 | github-2025-10-24-nanochat-strawberry-guide |
| E1 | verifiability | blog-2025-11-17-verifiability |
| E1 | karpathy__reader3 | github-2025-11-18-reader3-readme |
| E1 | 1990577951671509438 | x-2025-11-18-reading-with-llms |
| E1 | karpathy__nanochat__discussion-314 | github-2025-11-20-nanochat-d34-model |
| E1 | karpathy__llm-council | github-2025-11-22-llm-council-readme |
| E1 | the-space-of-minds | blog-2025-11-29-space-of-minds |
| E2 | auto-grade-hn | blog-2025-12-10-auto-grade-hn |
| E2 | karpathy__hn-time-capsule | github-2025-12-10-hn-time-capsule-readme |
| E2 | chemical-hygiene | blog-2025-12-18-chemical-hygiene |
| E2 | karpathy__rustbpe | github-2026-01-03-rustbpe-readme |
| E2 | karpathy__nanochat__discussion-420 | github-2026-01-07-nanochat-miniseries-v1 |
| E2 | karpathy__nanochat__discussion-481 | github-2026-01-31-nanochat-beating-gpt-2 |
| E2 | microgpt | blog-2026-02-12-microgpt |
| E3 | 2029701092347630069 | x-2026-03-05-nanochat-gpt-2-in-two-hours |
| E3 | karpathy__autoresearch__discussion-43 | github-2026-03-08-autoresearch-session-report |
| E3 | 2031135152349524125 | x-2026-03-09-autoresearch-tuning-nanochat |
| E3 | karpathy__jobs | github-2026-03-16-jobs-readme |
| E3 | kwSVtQ7dziU | talk-2026-03-20-skill-issue |
| E3 | karpathy__autoresearch | github-2026-03-21-autoresearch-readme |
| E4 | karpathy__gist-442a6bf555914893e9891c11519de94f | github-2026-04-04-llm-wiki-gist |
| E4 | 96jN2OCOfLs | talk-2026-04-29-sequoia-ascent-2026 |
| E4 | sequoia-ascent-2026 | blog-2026-04-30-sequoia-ascent-2026-summary |
| E4 | karpathy__micrograd | github-2026-08-03-micrograd-readme |

## New topics (3)

| slug | aliases | group |
|---|---|---|
| chemical-hygiene | Chemical hygiene, edible food-like substances, food additives, personal health choices | E2 (the grocery post `x-2025-07-08-ideal-grocery-store` joins its `sources`; it stays `context` on calorie). Health lines are his choices, with his hedges; never medical fact |
| claws | Claws, agent harnesses (use the digest's aliases; captions write "Claude" for "claw") | E3 |
| agentic-engineering | Agentic engineering, agent-assisted engineering | E4 (the host says the term first; he adopts and defines it) |

## New claims

| slug | from | group | relation |
|---|---|---|---|
| software-2-0-automates-what-you-can-verify | verifiability | E1 | Sequoia talk's llms-automate-what-you-can-verify folds in as a second source (E4) |
| verifiability-drives-the-jagged-frontier | verifiability | E1 | topic jagged-intelligence |
| code-is-ephemeral-now-and-libraries-are-over | reader3 README; llm-council README | E1 | supports [[vibe-coding-will-terraform-software]] |
| writers-may-increasingly-write-for-llms | X reading post | E1 | topic building-for-agents |
| llms-are-shaped-by-commercial-not-biological-evolution | space of minds | E1 | supports [[llm-research-summons-ghosts-not-animals]] |
| future-llms-are-watching | auto-grade-hn | E2 | |
| us-chemical-regulation-lags-the-industry | chemical hygiene | E2 | Note to user-hostile-technology |
| nanochat-reproduces-chinchillas-equal-scaling-of-parameters-and-tokens | nanochat 420 | E2 | topic scaling-laws; each source's tokens-to-parameters ratio stated with its own source, not reconciled |
| only-actual-metrics-are-real-and-comparable | nanochat 420 | E2 | topic llm-evaluation |
| gpt-2-training-cost-falls-to-about-40-percent-a-year | nanochat 481 | E2 | topic compute-efficiency |
| small-scale-tuning-does-not-always-transfer | nanochat 481 | E2 | Note to quick-experiment-loop |
| microgpt-is-the-full-algorithm-everything-else-is-efficiency | microgpt; micrograd README in E4 | E2 | supports [[micrograd-is-all-you-need-everything-else-is-efficiency]] (weakest true; no timeline) |
| autoresearch-found-real-improvements-to-nanochat | X 2026-03-09 | E3 | the improvements are the agents' results as he reports them |
| all-frontier-labs-will-autoresearch | X 2026-03-09; Skill Issue | E3 | folds frontier-labs-are-trying-to-have-llms-improve-llms |
| many-high-ai-exposure-jobs-will-be-reshaped-not-replaced | jobs README | E3 | topic ai-and-the-economy; the scores are the tool's LLM's, never "he rates" |
| he-now-delegates-most-coding-to-agents | Skill Issue; Sequoia talk in E4 (coding-agents-became-reliable-for-him-in-december folds in) | E3 | **extends** [[autocomplete-is-his-coding-sweet-spot]]: a change he states himself ("something flipped" in December; the October claim said "for now"). Both claims on vibe-coding-over-time. "December" has no year in either source; write "December" as he does |
| agent-failures-mostly-feel-like-a-skill-issue | Skill Issue | E3 | topic claws |
| take-yourself-out-of-the-agent-loop | Skill Issue | E3 | topic partial-autonomy-apps; entry on llm-agents-over-time |
| autoresearch-needs-an-objective-metric | Skill Issue | E3 | supports [[software-2-0-automates-what-you-can-verify]] |
| what-rl-does-not-optimize-does-not-improve | Skill Issue | E3 | supports [[verifiability-drives-the-jagged-frontier]] |
| expect-more-speciation-of-models | Skill Issue | E3 | topic ai-ecosystem |
| cheaper-software-will-raise-demand-for-it | Skill Issue | E3 | topic ai-and-the-economy |
| a-wiki-compounds-where-rag-rediscovers | llm-wiki gist | E4 | topic llm-knowledge-bases |
| an-index-file-avoids-rag-at-moderate-scale | llm-wiki gist | E4 | supports [[no-rag-needed-for-a-small-wiki]] (weakest true; no timeline) |
| llms-make-wiki-maintenance-nearly-free | llm-wiki gist | E4 | topic llm-knowledge-bases |
| agentic-engineering-keeps-the-quality-bar-while-going-faster | Sequoia talk | E4 | **extends** [[vibe-coding-is-for-throwaway-weekend-projects]]; Note to vibe-coding-will-terraform-software (both hold); entry on vibe-coding-over-time |
| in-software-3-0-some-apps-should-not-exist | Sequoia talk | E4 | topic software-3-0 |
| neural-nets-may-become-the-host-process | Sequoia talk | E4 | **extends** [[llms-are-the-kernel-of-an-emerging-operating-system]] (a hedged extrapolation; say so); entry on llm-os-over-time |
| hiring-should-test-building-a-big-project-with-agents | Sequoia talk | E4 | topic agentic-engineering |
| understanding-cannot-be-outsourced | Sequoia talk | E4 | he takes the line from someone else's tweet; the claim is that he endorses it |

(30 rows.) Dropped as claims (cited sentences on the named page): the hallucination aside in
microgpt → llm-hallucinations; the forward-future-predictor remark → hn-time-capsule;
open-models-trailing-the-frontier-is-an-okay-balance and inside-a-frontier-lab-you-are-not-fully-independent
→ ai-ecosystem; he-now-explains-things-to-agents-not-people → building-for-agents;
physical-automation and the other existing claims Skill Issue mentions → add it as a
source only where the passage restates them.

Existing claims gaining sources: a-lot-of-llm-oddness-traces-back-to-tokenization,
transformers-need-tokens-to-think, synthetic-data-is-the-future-if-you-keep-its-entropy
(strawberry guide); he-prefers-tiktoken-byte-level-bpe-to-sentencepiece,
coding-models-are-weak-at-code-never-written-before (rustbpe, for the Rust help only;
Skill Issue @1:05:33); progress-comes-from-everything-improving-together (nanochat 481);
gpt-is-not-a-complicated-model, neural-net-training-should-not-be-complicated,
attention-is-a-communication-mechanism, pretraining-gives-a-document-completer (microgpt);
vibe-coding-will-terraform-software (Skill Issue); english-is-the-new-programming-language
(Sequoia talk); use-llms-as-tools-and-check-their-work (Sequoia talk). Notes only, no
relation: his-gpt-2-reproductions… (nanochat is scored on CORE), do-not-decay… (nanochat
decays to 0 again; he gives no view), this-is-the-decade-of-agents (no timescale in
batch 4 sources).

## New methods (2)

| slug | from | group |
|---|---|---|
| teach-a-capability-with-synthetic-tasks | strawberry guide | E1 |
| fit-your-own-scaling-law | nanochat 420, 481 | E2 |

run-parallel-agents-on-macro-actions → a section of ai-assisted-coding-loop (E3). The
2025-11-18 reading order (read first, then summary, then Q&A) is a dated variant on
read-with-an-llm, not a change of mind.

## New artifacts (7)

| slug | group | notes |
|---|---|---|
| reader3 | E1 | link from read-with-an-llm |
| llm-council | E1 | remove the alias "LLM council" from choose-a-model-tier and link the artifact instead |
| hn-time-capsule | E2 | |
| rustbpe | E2 | "the missing tiktoken training code"; link from tokenization, minbpe, nanochat |
| microgpt | E2 | repo_url = the gist URL the post gives; micrograd README (E4) adds the "better engine" statement |
| jobs | E3 | |
| autoresearch | E3 | the README's italic opening is a signed joke set in an imagined future, not a prediction |

Extended: nanochat (all its Discussions and the X post; each cost and time figure with its
own source and date, no ordering written between sources; the inconsistencies the digest
lists stay unreconciled), minbpe, micrograd (E4: first README source).

## Timelines (extend only)

- **vibe-coding-over-time**: he-now-delegates-most-coding-to-agents (E3),
  agentic-engineering-keeps-the-quality-bar… (E4), code-is-ephemeral… (E1). Rewrite its
  closing Note in E3: his own words state a change in his practice in December; earlier
  entries only accumulated.
- **llm-agents-over-time**: X 2026-03-05 and take-yourself-out-of-the-agent-loop (E3).
- **llm-os-over-time**: neural-nets-may-become-the-host-process (E4).
- **llm-self-improvement-over-time**: autoresearch as a dated entry (E3), with a Note that it
  is an agent editing training code against a metric, not RL on the model.
