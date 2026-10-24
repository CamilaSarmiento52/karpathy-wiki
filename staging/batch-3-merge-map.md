# Batch 3 merge map

Decided 2026-10-24 from the digest candidate lists. Same rules as batches 1–2: merge
creates ONLY the pages named here (plus source pages); every other candidate becomes cited
sentences on the page its "→" names; existing pages are extended, never duplicated. Two
batch 3 raw files were compiled in phase 1 (`x-2025-02-02-vibe-coding`,
`youtube-2025-06-19-software-is-changing`); they are linked, not re-ingested.

## Source pages and merge groups

| group | raw stem | source slug |
|---|---|---|
| D1 | karpathy__LLM101n | github-2024-08-01-llm101n-readme |
| D1 | hM_h0UA7upI | talk-2024-09-05-no-priors-ep-80 |
| D1 | i-love-calculator | blog-2024-09-08-i-love-calculator |
| D1 | karpathy__llm.c | github-2024-09-24-llmc-readme |
| D1 | 1841536804073439268 | x-2024-10-02-gpu-mode-talk |
| D1 | aR6CzM0x-g0 | talk-2024-10-03-cuda-mode-keynote |
| D2 | 7xTGNNLPyMI | youtube-2025-02-05-deep-dive-into-llms |
| D2 | EWvNQjAaOHw | youtube-2025-02-27-how-i-use-llms |
| D2 | digital-hygiene | blog-2025-03-17-digital-hygiene |
| D2 | the-append-and-review-note | blog-2025-03-19-append-and-review-note |
| D2 | finding-the-best-sleep-tracker | blog-2025-03-24-best-sleep-tracker |
| D3 | power-to-the-people | blog-2025-04-07-power-to-the-people |
| D3 | vibe-coding-menugen | blog-2025-04-27-vibe-coding-menugen |
| D3 | 1917961248031080455 | x-2025-05-01-vibe-coding-hackathon |
| D3 | 1942612984481870068 | x-2025-07-08-ideal-grocery-store |
| D3 | karpathy__minbpe__discussion-98 | github-2025-08-08-minbpe-gpt-4-tokenizer-discussion |
| D3 | karpathy__rendergit | github-2025-08-21-rendergit-readme |
| D4 | animals-vs-ghosts | blog-2025-10-01-animals-vs-ghosts |
| D4 | 1973435013875314729 | x-2025-10-01-sutton-podcast |
| D4 | karpathy__nanochat__discussion-1 | github-2025-10-13-nanochat-discussion-introducing |
| D4 | lXUZvyajciY | talk-2025-10-17-dwarkesh-ghosts-not-animals |

Groups run in order, one at a time, lint clean before the next.

## New topics (7)

| slug | absorbs | aliases | group |
|---|---|---|---|
| self-driving | self-driving; demo-to-product gap; humanoid-robots material | Self-driving, Waymo, Tesla Autopilot, demo-to-product gap, march of nines, humanoid robots | D1 |
| ai-for-education | ai-for-education; children-should-mostly-study-math-physics-and-cs (sentence); LLM101n README | AI for education, Eureka Labs, AI teaching assistant, LLM101n course | D1 |
| user-hostile-technology | user-hostile-technology (calculator, digital hygiene) | User-hostile technology, internet of shit, privacy, being the product | D1 (D2 extends) |
| llm-hallucinations | llm-hallucinations, self-knowledge section | Hallucinations, confabulation, "I don't know", model self-knowledge | D2 |
| technology-diffusion | technology-diffusion; money-cannot-buy-better-chatgpt (sentence) | Technology diffusion, power to the people, individuals before institutions | D3 |
| bitter-lesson | bitter-lesson; animal-brains-are-not-a-blank-slate, animals-do-not-do-supervised-learning (sentences, with Sutton's positions attributed to Sutton) | Bitter lesson, Richard Sutton, animals vs ghosts, blank slate | D4 |

(6 rows.) Dropped as topics: humanoid-robots → self-driving and a claim; ai-as-exocortex
→ host-heavy; any line he says goes to llms-as-operating-systems; multimodality →
llm-tool-use section; midtraining → pretraining-and-finetuning section; Swiss cheese →
jagged-intelligence (sentences, cited to Deep Dive; he uses "Swiss cheese", not
"jagged", say so).

## New claims

| slug | from | group | folds in / relation |
|---|---|---|---|
| there-is-a-massive-gap-between-demo-and-product | No Priors | D1 | supports [[this-is-the-decade-of-agents]]; topic self-driving |
| tesla-is-ahead-of-waymo-in-self-driving | No Priors | D1 | |
| humanoid-robots-should-start-in-your-own-factory | No Priors | D1 | Note to physical-automation-will-lag-digital-automation |
| the-architecture-is-no-longer-the-bottleneck | No Priors | D1 | supports [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]; Note to the-transformer-is-probably-not-the-final-architecture |
| synthetic-data-is-the-future-if-you-keep-its-entropy | No Priors | D1 | topic pretraining-and-finetuning |
| a-cognitive-core-could-be-a-billion-parameters-or-less | No Priors | D1 | supports [[small-llms-can-be-strong-in-narrow-domains]] (not extends: different idea, no timeline) |
| ai-should-be-the-front-end-of-a-teacher-designed-course | No Priors | D1 | topic ai-for-education |
| post-agi-education-will-be-like-going-to-the-gym | No Priors | D1 | topic ai-for-education |
| llms-may-write-custom-low-level-code-for-any-application | CUDA keynote | D1 | Note to vibe-coding-will-terraform-software |
| technology-could-be-like-the-calculator | calculator post | D1 | topic user-hostile-technology |
| chatgpt-answers-simulate-a-human-data-labeler | Deep Dive | D2 | supports [[llms-want-to-imitate-not-succeed]] |
| hallucinations-come-from-imitating-confident-answers | Deep Dive | D2 | topic llm-hallucinations |
| parameters-are-vague-recollection-context-is-working-memory | Deep Dive | D2 | |
| rl-lets-models-discover-their-own-thinking-strategies | Deep Dive | D2 | **extends** [[self-improvement-may-be-possible-in-narrow-domains]] and [[llms-currently-only-have-a-system-1]]; timeline llm-self-improvement-over-time |
| rlhf-is-not-real-rl | Deep Dive; check the Sequoia raw for the earlier statement and, if he says it there, add Sequoia and set `stated_on` to 2024-03-26 | D2 | compatible with rlhf-works-better-because-comparing-is-easier-than-generating (Note) |
| use-llms-as-tools-and-check-their-work | Deep Dive; How I use LLMs as second source | D2 | folds treat-deep-research-reports-as-a-first-draft, llm-code-tools-need-a-user-who-can-verify-the-code; supports [[use-llms-as-copilots-with-human-oversight]] |
| longer-context-windows-alone-will-not-scale-to-long-multimodal-tasks | Deep Dive | D2 | |
| he-prefers-to-pay-and-be-the-customer | digital hygiene; calculator post as second source | D2 | topic user-hostile-technology |
| use-hardware-security-keys-not-sms-as-a-second-factor | digital hygiene | D2 | |
| one-text-note-beats-many-organized-notes | append-and-review | D2 | method append-and-review-note |
| oura-and-whoop-were-the-best-sleep-trackers-he-tested | sleep post | D2 | folds his-sleep-score-tracks-his-work-quality (sentence); the 8Sleep heart-rate remark that does not match his matrix is not reconciled |
| llms-reverse-the-usual-diffusion-of-technology | power to the people | D3 | weak supports [[english-is-the-new-programming-language]] only if both sides cited; otherwise Note |
| deploying-a-vibe-coded-app-is-harder-than-writing-it | MenuGen blog; X hackathon post and the YC talk as further sources | D3 | **extends** [[vibe-coding-is-for-throwaway-weekend-projects]]; entry on vibe-coding-over-time |
| vibe-coding-full-web-apps-is-not-yet-for-anything-important | MenuGen blog | D3 | supports [[vibe-coding-is-for-throwaway-weekend-projects]] |
| frontier-llms-are-not-platonically-bitter-lesson-pilled | animals vs ghosts; X post is the same text | D4 | topic bitter-lesson |
| pretraining-is-our-crappy-evolution | animals vs ghosts | D4 | Note to pretraining-is-lossy-compression-of-the-internet (no extends) |
| llm-research-summons-ghosts-not-animals | animals vs ghosts | D4 | topic jagged-intelligence |
| rl-sucks-supervision-bits-through-a-straw | nanochat Discussion 1; Dwarkesh as second source | D4 | entry on llm-self-improvement-over-time |

**The X post on Sutton is the blog body word for word.** Cite it as a second location,
never as independent evidence ("both sources" must not imply two statements).

Dropped as claims (become sentences): transformers-are-in-some-ways-better-than-the-brain
→ transformer-architecture; open-models-must-keep-progressing-as-a-fallback → ai-ecosystem;
llm-systems-may-come-to-resemble-companies → llms-as-operating-systems;
children-should-mostly-study… → ai-for-education; learning-cuda-was-harder-than-he-expected
→ llm-c; llm-capabilities-are-swiss-cheese → jagged-intelligence; the How I use LLMs
preference claims → the methods below; few-shot-examples-increase-accuracy → prompting-llms;
use-search-for-recent-or-niche-information → llm-tool-use; chat-web-apps-are-too-slow… →
vibe-coding; money-cannot-buy-better-chatgpt → technology-diffusion;
small-models-must-be-taught-multiple-choice → llm-evaluation; the-ideal-grocery-store… → none.

Existing claims gaining sources (add to `sources`, cite in Context or Related claims):
transformers-need-tokens-to-think (Deep Dive; How I use LLMs on trying non-thinking
models first), pretraining-gives-a-document-completer (Deep Dive; nanochat 1),
pretraining-is-lossy-compression-of-the-internet (Deep Dive; nanochat 1), an-llm-is-just-two-files,
a-lot-of-llm-oddness-traces-back-to-tokenization, tokenization-free-modeling… ,
rlhf-works-better… (Deep Dive), he-prefers-tiktoken-byte-level-bpe-to-sentencepiece
(nanochat 1), llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements (llm.c README,
X post, keynote: each figure with its own source), neural-net-training-should-not-be-complicated
(keynote @06:37, next to "it wasn't all that simple" @19:50, which is about the project,
not a contradiction).

## New methods (8)

| slug | absorbs | group |
|---|---|---|
| port-a-pytorch-model-to-c-and-cuda | keynote + X post | D1 |
| choose-a-model-tier | choose-a-model-tier, use-the-most-powerful-model-that-works-for-you, try-a-non-thinking-model-first, he-asks-several-llms-the-same-question, keep-track-of-which-tools-each-llm-has, chatgpt-is-a-very-good-default-llm-app | D2 |
| start-a-new-chat-per-topic | method + claim start-a-new-chat-when-switching-topics | D2 |
| verify-citations | verify-citations | D2 |
| read-with-an-llm | read-with-an-llm, dont-read-books-alone | D2 |
| voice-input | voice-input, use-voice-instead-of-typing | D2 |
| digital-hygiene-checklist | digital hygiene | D2 |
| append-and-review-note | append-and-review | D2 |

compare-measuring-devices-head-to-head → steps in the sleep claim's Context. The How I use
LLMs methods describe his own practice; their definitions say "he", not "you should".

## New artifacts (2)

| slug | repo_url | status | group |
|---|---|---|---|
| llm101n | https://github.com/karpathy/LLM101n | archived (README: course does not yet exist; repo archived until ready) | D1; link from build-and-publish-projects and ai-for-education |
| rendergit | https://github.com/karpathy/rendergit | from its README | D3; link from building-for-agents (README says LLMs, not agents) |

Existing artifacts extended: llm-c (README, keynote), minbpe (Discussion 98, nanochat 1),
nanochat (Discussion 1, the 2025 launch; the page was built from the 2026 README),
calorie (grocery post as `context` with a labelled Note; no other page for it).

## Timelines

- **New: llm-self-improvement-over-time**, `topic: "[[llm-self-improvement]]"`, created in
  D2: 2023-11-23 narrow domains with a reward and System 1 only (Intro to LLMs);
  2024-03-26 AlphaGo step one (Sequoia); 2025-02-05 RL lets models discover thinking
  strategies (Deep Dive); D4 adds 2025-10-13 supervision through a straw (nanochat 1) and
  the Dwarkesh entries. Dates only; the closing Note says what changed and what did not.
- **Extend vibe-coding-over-time** (D3): 2025-04-27 MenuGen blog, 2025-05-01 hackathon post.
- **Extend llm-agents-over-time** (D1: No Priors 2024-09-05; D4: Dwarkesh).

## Dwarkesh (D4)

`talk-2025-10-17-dwarkesh-ghosts-not-animals`. The transcript has no speaker labels; the
digest marks spans where the speaker is unclear: never attribute those to him. Where
Dwarkesh restates him (e.g. the cognitive-core horizon as 10 years; he said 20) and he does
not correct it, use his own figure. He walks back "possibly no fundamental solution" to
model collapse later in the interview: say both, in order.

New topics (3, D4):

| slug | aliases |
|---|---|
| cognitive-core | Cognitive core, memory vs cognition, small reasoning core |
| model-collapse | Model collapse, training on own samples, entropy loss |
| ai-and-the-economy | AI and the economy, GDP, automation, loss of control |

Education material goes on the existing `ai-for-education` (created in D1), not a new
"education" topic.

New claims (D4):

| slug | relation |
|---|---|
| early-agent-attempts-came-too-early | topic partial-autonomy-apps; entry on llm-agents-over-time |
| rl-is-terrible-but-better-than-imitation | supports [[self-improvement-may-be-possible-in-narrow-domains]] and [[rl-sucks-supervision-bits-through-a-straw]]; entry on llm-self-improvement-over-time |
| llm-judges-are-gameable-rewards | topic llm-self-improvement |
| llms-lack-culture-and-self-play | topic llm-self-improvement |
| training-on-own-samples-collapses-models | topic model-collapse |
| progress-comes-from-everything-improving-together | Note to scaling-offers-a-guaranteed-path-to-better-models, no link |
| coding-models-are-weak-at-code-never-written-before | Note to claude-code-is-the-first-convincing-llm-agent (both hold: impressive and used daily, weak off-distribution); entry on vibe-coding-over-time |
| autocomplete-is-his-coding-sweet-spot | method ai-assisted-coding-loop |
| ai-will-not-show-up-as-a-jump-in-gdp | topic ai-and-the-economy |
| gradual-loss-of-control-is-the-most-likely-outcome | topic ai-and-the-economy |
| education-is-building-ramps-to-knowledge | supports [[build-the-ramp-not-just-the-thing]] (not extends); topic ai-for-education |
| the-ai-tutor-he-wants-is-not-yet-possible | topic ai-for-education |
| if-you-cannot-build-it-you-do-not-understand-it | the line is Feynman's; the claim is that he holds it; topic ai-for-education |

Folded into existing claims (add Dwarkesh as a source, cite it): this-is-the-decade-of-agents
(same claim, more reasons); were-summoning-ghosts-not-building-animals →
llm-research-summons-ghosts-not-animals; a-cognitive-core-could-be-about-a-billion-parameters
→ a-cognitive-core-could-be-a-billion-parameters-or-less (set its `topic` to
cognitive-core); post-agi-education-will-be-like-the-gym → post-agi-education-will-be-like-going-to-the-gym;
deployment-is-a-march-of-nines → there-is-a-massive-gap-between-demo-and-product (march of
nines in Context); physical-automation-will-lag-digital-automation; pretraining-is-lossy-compression-of-the-internet
(Note only to the cognitive core; no extends).

New method (D4): learn-by-building-and-explaining (absorbs teach-by-building-a-ramp as a
step; Related → spelled-out-build-from-scratch). Extend ai-assisted-coding-loop.

Timelines extended in D4: llm-agents-over-time, vibe-coding-over-time,
llm-self-improvement-over-time. Dates only; no `contradicts` found.
