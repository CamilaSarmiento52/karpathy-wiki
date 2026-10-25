# Verification: batch 3, group D4 (Animals vs Ghosts blog, Sutton X post, nanochat Discussion 1, Dwarkesh interview)
Verified 2026-10-25 by a fresh reader. Sources: [[blog-2025-10-01-animals-vs-ghosts]], [[x-2025-10-01-sutton-podcast]], [[github-2025-10-13-nanochat-discussion-introducing]], [[talk-2025-10-17-dwarkesh-ghosts-not-animals]]

## Coverage
- Fed pages: the four `## Fed pages` lists match the pages that cite each source (blog 11, X 4, nanochat 13, Dwarkesh 41).
- Claim pages fully checked: 17 new D4 claims (frontier-llms-are-not-platonically-bitter-lesson-pilled, pretraining-is-our-crappy-evolution, llm-research-summons-ghosts-not-animals, rl-sucks-supervision-bits-through-a-straw, early-agent-attempts-came-too-early, rl-is-terrible-but-better-than-imitation, llm-judges-are-gameable-rewards, llms-lack-culture-and-self-play, training-on-own-samples-collapses-models, progress-comes-from-everything-improving-together, coding-models-are-weak-at-code-never-written-before, autocomplete-is-his-coding-sweet-spot, ai-will-not-show-up-as-a-jump-in-gdp, gradual-loss-of-control-is-the-most-likely-outcome, education-is-building-ramps-to-knowledge, the-ai-tutor-he-wants-is-not-yet-possible, if-you-cannot-build-it-you-do-not-understand-it). Also the D4 sentences on 11 existing claims: this-is-the-decade-of-agents, a-cognitive-core-could-be-a-billion-parameters-or-less, post-agi-education-will-be-like-going-to-the-gym, there-is-a-massive-gap-between-demo-and-product, physical-automation-will-lag-digital-automation, pretraining-is-lossy-compression-of-the-internet, pretraining-gives-a-document-completer, he-prefers-tiktoken-byte-level-bpe-to-sentencepiece, do-not-decay-the-learning-rate-to-zero, build-the-ramp-not-just-the-thing, self-improvement-may-be-possible-in-narrow-domains. Every quote was grepped in the raw file; every `supports` link was checked on both pages (rl-is-terrible ↔ self-improvement-may-be-possible…, rl-is-terrible ↔ rl-sucks…, education-is-building-ramps ↔ build-the-ramp: all set on both sides).
- Timeline entries checked: 4 D4 entries (llm-agents-over-time 2025-10-17; vibe-coding-over-time 2025-10-17; llm-self-improvement-over-time 2025-10-13 and 2025-10-17), plus the closing Note on each of the three timelines.
- Other pages checked: bitter-lesson (every sentence citing the blog/X/Dwarkesh), jagged-intelligence, llm-self-improvement, prompting-llms, model-collapse (all), cognitive-core (all), ai-and-the-economy (all), ai-for-education, self-driving, partial-autonomy-apps, vibe-coding, pretraining-and-finetuning, tokenization, llm-evaluation, rlvr, scaling-laws, llm-knowledge-bases, nanochat, minbpe, ai-assisted-coding-loop, learn-by-building-and-explaining, and the four source pages' Summary and Key points. Other sentences checked: about 120 of ~210. For Dwarkesh that is well above one in five.

## Findings

### F1 — overstated — [[llm-judges-are-gameable-rewards]] (title), also [[llm-self-improvement]] and [[llm-self-improvement-over-time]]
- sentence: title "An LLM judge used as a reward gets gamed by adversarial examples within tens of steps"; llm-self-improvement: "Process supervision with LLM judges is gameable within tens of steps"; timeline 2025-10-17: "LLM judges used as rewards are gamed within tens of steps"
- cited: [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @46:34, @47:11
- raw says: you can do "maybe 10 steps or 20 steps, and maybe it will work, but you can't do 100 or 1,000". That is a limit on how long RL against a judge stays useful. He does not say gaming happens within tens of steps.
- fix: title → "An LLM judge used as a reward gets gamed by adversarial examples, so RL against it works for only tens of steps"; llm-self-improvement → "Process supervision with LLM judges is gameable, so RL against a judge works for maybe 10 or 20 steps, not hundreds; see …"; timeline → "LLM judges used as rewards get gamed, so RL against them works for only tens of steps".

### F2 — minor — [[progress-comes-from-everything-improving-together]]
- sentence: "So he expects more data, better hardware, kernels and software, and better algorithms, with "no one of them winning too much""
- cited: @26:18
- raw says: "it's almost like no one of them is winning too much". The quote leaves out "is", so it is not verbatim.
- fix: quote it as "no one of them is winning too much".

### F3 — minor — [[ai-assisted-coding-loop]] step 8
- sentence: "He uses agents … in an unfamiliar language, Rust, only with a Python implementation he fully understands and tests"
- cited: @31:21, @34:26
- raw says: he had a Python implementation he fully understands and tests, "so I feel safer doing that stuff". He does not set it as a condition.
- fix: "… and in an unfamiliar language, Rust, where having a Python implementation he fully understands, plus tests, made him feel safer".

### F4 — minor — [[self-driving]]
- sentence: "Deployments are minimal and uneconomical, and the cars rely on elaborate teleoperation centres, so the person has been moved somewhere you cannot see them"
- cited: @1:49:18, @1:49:54, @1:50:32
- raw says: there are "very elaborate teleoperation centers of people kind of in a loop". He hedges this ("I don't have the full extent of it"; he does not know if they are fully in the loop; "Some of the time they are").
- fix: "… and he says there are elaborate teleoperation centres with people in the loop some of the time, though he does not know the full extent; in some sense the person has been moved somewhere you cannot see them".

### F5 — minor — [[frontier-llms-are-not-platonically-bitter-lesson-pilled]] Context ¶1
- sentence: "… "is not inadequate", a double negative that reads as agreement rather than strong endorsement"
- cited: [[blog-2025-10-01-animals-vs-ghosts]] §intro
- raw says: only "his criticism of LLMs as not bitter lesson pilled is not inadequate". The reading of the double negative is the wiki's, but it sits in a cited sentence.
- fix: end the sentence at "is not inadequate" (citation unchanged), and add "**Note:** the double negative reads as agreement rather than strong endorsement."

### F6 — minor — [[training-on-own-samples-collapses-models]] Context ¶1
- sentence: "Asked why a model cannot train on its own reflections, he says every synthetic sample looks great …"
- cited: @51:37, @52:12
- raw says: Dwarkesh does not ask this. He asks himself ("If I can just describe one: why can't we just synthetically generate and train on it?").
- fix: "Explaining why a model cannot simply train on its own reflections, he says …".

### F7 — minor — [[llm-self-improvement]] ¶Terrible, also [[llm-self-improvement-over-time]] 2025-10-17
- sentence: "He says RL is terrible and just happens to beat the imitation that came before, because it broadcasts a single final reward across a whole trajectory"; timeline: "calls RL terrible but better than the imitation before it, because one final reward is broadcast across a whole trajectory"
- cited: @41:33, @42:46
- raw says: the broadcast reward is his reason RL is terrible (@42:46–@43:22). It is not why RL beats imitation. Imitation is worse because "previously we were just imitating people" (@41:33). As written, "because" can be read as attached to "beat".
- fix: "He says RL is terrible, because it broadcasts a single final reward across a whole trajectory, and just happens to beat the imitation that came before"; same reorder in the timeline entry.

### F8 — minor — [[pretraining-and-finetuning]] ¶Midtraining (nanochat)
- sentence: "d20 needs 240 shards, about 24GB (setting)"
- cited: [[github-2025-10-13-nanochat-discussion-introducing]] §Train the tokenizer
- raw says: 240 shards is the configuration. "about ~24GB download" is his estimate of the download size, not a chosen value.
- fix: "d20 needs 240 shards (setting), about 24GB to download (estimate)".

## Checked and correct
- Attribution. Sutton's positions on [[bitter-lesson]], [[pretraining-and-finetuning]], [[llm-self-improvement]], [[scaling-laws]] and [[frontier-llms-are-not-platonically-bitter-lesson-pilled]] are attributed to Sutton ("as he reports it", "in Sutton's view"), including the squirrel line, the finite-data question and the TD-learning answer. Dwarkesh's points are attributed to Dwarkesh: in-context learning is not gradient descent (@14:58), the 0.07 bits/token vs KV-cache figures, the 3 GB DNA argument, AI 2027, AGI-as-labour and population growth, the radiologist/safety-driver argument, presenting the pain before the solution, the 10-year cognitive-core horizon, and the in-context test-time-learning point in the blog Appendix. None of the unclear-speaker spans the digest flags is attributed to him: @1:47:30–@1:48:07, @1:30:43–@1:31:28, @1:36:55 and the second half of @58:26 are not cited. The @58:26 citation on model-collapse is for the first half, which is his. @2:22:33 on learn-by-building-and-explaining step 7 is used only for his lunch-explanation point, not the "Just say the thing" tweet line.
- Model collapse. [[model-collapse]] and [[training-on-own-samples-collapses-models]] give "possibly no fundamental solution" (@53:28), then the walk-back (@59:01), in that order and both as his. They also say the later statement corrects the earlier.
- Cognitive core horizon. [[a-cognitive-core-could-be-a-billion-parameters-or-less]] and [[cognitive-core]] give 20 years as his figure (@1:00:14) and 10 years as Dwarkesh's restatement (@1:00:47). Correct.
- Folded claims. this-is-the-decade-of-agents: 6 Dwarkesh sentences, all supported (@00:48 quote verbatim; @01:25, @01:59, @02:32/@03:14, @1:43:07, @1:55:33). post-agi-education-will-be-like-going-to-the-gym: 4, all supported (@2:08:41 quote verbatim; the gym-culture elaboration is not attributed to him). there-is-a-massive-gap-between-demo-and-product: the march-of-nines paragraph, 6 sentences, all supported (@1:45:36 quote verbatim; Tesla "two or three nines" @1:46:16). physical-automation-will-lag-digital-automation: 3, all supported (the capex point is correctly Dwarkesh's). pretraining-is-lossy-compression-of-the-internet: 4, all supported. pretraining-gives-a-document-completer, he-prefers-tiktoken-byte-level-bpe-to-sentencepiece, build-the-ramp-not-just-the-thing, self-improvement-may-be-possible-in-narrow-domains: D4 sentences all supported.
- New claims not listed in Findings: all titles, quotes (verbatim at the cited block), Context sentences and `confidence: stated` are supported. That is 15 of the 17; F1, F2, F5 and F6 are the only problems on claim pages.
- Timelines. llm-agents-over-time: the 2025-10-17 entry and the closing Note ("six sources" is correct) are supported. vibe-coding-over-time: the 2025-10-17 entry and both closing Notes are supported. llm-self-improvement-over-time: the 2025-10-13 entry (1.5 h, measured) is supported, the 2025-10-17 entry is fine apart from F1/F7, and the closing D4 Note (hill-climbs yet "still stupid", "three or four or five more", nothing withdrawn) is supported. No ordering is written from published dates alone.
- nanochat numbers and tags (nanochat, tokenization, llm-evaluation, rlvr, pretraining-and-finetuning, rl-sucks…). All values match the raw: $100 (target), ~$24/hr, d20 / 1280 channels / 10 heads / ~560M (setting), CORE 0.22 (measured) vs 0.21 / 0.26 (comparison), $72, 3h51m (measured), $92.4 (estimate), ~5 h with RL, 8,304 lines / 44 files, d26 for CORE ~0.25 (target), 65,536 vocab and 2B chars (setting), ~1 min and 4.8 chars/token (measured), 50,257 / 100,277 (comparison), 0.81 bpb, ChatCORE 0.0730 → 0.0884, GSM8K 0.0758 after RL, 568K-row mixture (setting), 8 min / 7 min / 1.5 h (measured). The only tag problem is F8. The interview's "about 8,000 lines" is kept separate from 8,304.
- do-not-decay-the-learning-rate-to-zero: the Note correctly says `lrm` "will linearly ramp down to 0 near the end of training" (§Pretraining), tags it as a setting, keeps the claim scoped to llm.c, and correctly says he gives no opinion on the schedule in nanochat. Muon/AdamW is stated in the raw. No contradiction is implied. Correct.
- X post: everywhere it is cited, it is cited as the same words as the blog §intro, never as independent evidence. Its source page's diff Note is accurate (the post has no Appendix).
- Source pages: the Summary and Key points of all four are supported. Dwarkesh summary timestamps checked: @01:59, @03:14, @12:28, @41:33, @42:46, @52:12, @33:14, @37:33, @1:45:36, @1:22:43, @2:03:02.
- Other pages: cognitive-core (8 sentences), model-collapse (12), ai-and-the-economy (13), ai-for-education (9), partial-autonomy-apps (6), vibe-coding (5), jagged-intelligence (6 D4), prompting-llms (5), bitter-lesson (22), learn-by-building-and-explaining (9), nanochat (16), plus 4–6 each on tokenization, llm-evaluation, rlvr and pretraining-and-finetuning. All supported apart from F3, F4, F7 and F8.
