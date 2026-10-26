# Verification: phase 4, rule candidates

Verified 2026-10-26 by a fresh reader who did not write the candidates. Input:
`staging/rules/candidates.md` (11 rules). Checked against CLAUDE.md invariants 7–9 and §3,
the phase 4 plan §1 (independence), `scripts/independence.json`, and the raw files.

## Coverage

- **Quotes: 41 of 41 checked.** A script normalised curly quotes and whitespace, split each raw
  file at its `[mm:ss]` markers, and searched for each quote. Every quote is verbatim, occurs
  once, and sits in the block the candidate names; text sources are in the named section.
  Every quote is at most one sentence and under 15 words (longest: 14). I read each quote with
  about 400 characters on either side to check who is speaking and what the quote means.
- **Speakers.** All quotes are his. Talk transcripts: CUDA MODE and Skill Issue are clearly
  his turns. The Dwarkesh raw has no speaker labels. @29:27, @2:17:33 and @33:14 are his from
  context (first-person accounts of his repos and training). For @2:19:57 see F5.
- **AI-written text.** None is used. Neither `github-2026-03-08-autoresearch-session-report`
  nor the Sequoia blog summary is cited. The Sequoia *talk* (`raw/talks/96jN2OCOfLs.md`) is
  his recording, not the Codex summary, so I use it below as counter-evidence.
- **Independence.** No pair falls under `same_text` or `ai_written`. Separate Zero to Hero
  lectures count separately under the plan, and so do the separate llm.c discussions. The
  status column below follows from that.
- **Links.** Every `[[slug]]` in the candidates resolves to an existing wiki page.

## Findings

### F1 — overstated — rule keep-model-written-changes-small-and-check-them
- problem: The title is timeless and absolute ("check each one before trusting it"), but every
  quote that says *he* checks dates from February to June 2025. The rule needs to be dated.
  1. **2026 practice differs in kind.** Since December 2025 he hands agents whole
     functionalities ("macro actions") in parallel. He reviews them only as best he can,
     depending on how much he cares about the code.
  2. **His trust has grown.** He says he can't remember the last time he corrected the
     agent, and that he trusted the system more and more.
  3. **Oversight has moved up a level.** Checking now happens at the level of the spec and
     the quality bar, not of every diff.
  4. **What still holds.** The quality bar stays: you are still responsible for your
     software, so you check it. The "small" part is supported for 2025 and for autoresearch's
     single-file design, not for his 2026 agent workflow in general.

  Nothing in 2026 withdraws checking. But "each one" and "small" are contradicted for his
  current practice. The candidate's caveat ("the rule stands for code that matters") is
  right, but it sits only in the status note, and the title an agent reads does not carry it.
- evidence:
  - talk-2026-03-20-skill-issue `raw/talks/kwSVtQ7dziU.md` @04:25: he delegates a new
    functionality to each agent and will "review their work as best as you can", depending
    on how much he cares about the code.
  - talk-2026-04-29-sequoia-ascent-2026 `raw/talks/96jN2OCOfLs.md`:
    - @01:08: "I can't remember the last time I corrected it".
    - @15:49: agentic engineering preserves the quality bar, and you are still responsible.
    - @20:44: people must own the spec and the oversight while agents do the details under
      the hood.
  - For 2025: the YC talk `raw/youtube/LCEmiRjPEtQ.md` @23:48 has a stronger first-person line
    than the leash quote: "I always go in small incremental chunks." (7 words).
- fix:
  - title: "Keep model-written code reviewable and check it before you trust it, more
    carefully the more the code matters."
  - Add to the rule body a dated line: "2025: small diffs, check everything (YC, Deep Dive,
    How I use LLMs). Since December 2025 he delegates whole features to parallel agents and
    reviews them as best he can, depending on how much he cares about the code. Oversight
    sits at the spec and quality-bar level (Skill Issue @04:25; Sequoia talk @01:08,
    @15:49, @20:44)."
  - Add the YC @23:48 quote, and keep the other four. Status stays **promoted**.
  - In practice: keep the reviewing bullet. Add "do not claim he reads every line of agent
    code in 2026". Its "defensive bloat" and "deprecated APIs" items are supported
    (Dwarkesh @33:14; `raw/blog/vibe-coding-menugen.md`).

### F2 — status — rule show-the-instructive-bug-failing-then-explain-it
- problem: Of the two sources, only one is a deliberate demonstration:
  - **makemore 1 is deliberate.** He removes `keepdim`, runs it, gets garbage, and asks
    viewers to pause and think why.
  - **micrograd is an accident he kept.** It is the forgotten zero_grad, "embarrassing" and
    "for the 20th time in my life… on camera", left in because it is funny.

  The micrograd line supports "keep real mistakes in rather than hide them". It does not
  support "show the bug failing" as a technique. On this evidence the deliberate move rests
  on one quoted source, which would make it **bench**. A second deliberate source is in raw,
  though. In the tokenizer lecture he knowingly flags a flaw in his own decode function,
  asks viewers to work out why it errors, then shows it failing on token 128. With that
  quote added, two independent lectures support the rule and it stays **promoted**.
  The micrograd quote also says nothing about explaining. The prior verifier found the same
  split on `how-he-explains` step 6 (`staging/verify/phase-4-how-he-explains.md` F3).
- evidence:
  - micrograd `raw/youtube/VMj-3S1tku0.md` @2:10:28: "kind of embarrassing… a really terrible
    bug". The same pattern appears at @1:15:05, "i should just leave the error in here".
  - makemore 1 `raw/youtube/PaCmpygFfXo.md` @46:21–@46:57: deliberate. He runs it, gets a
    wrong result, then invites viewers to pause and think about why.
  - tokenizer `raw/youtube/zduSFxRajkE.md` @45:16: "try to think figure out why this code
    could actually result in an error" (14 words). Shorter alternative: "let me demonstrate
    the issue" (5 words).
- fix:
  - title: "When a bug is instructive, show it failing, then explain it; keep real mistakes in
    rather than hide them."
  - quotes: replace the micrograd quote with the tokenizer @45:16 quote. Keep the micrograd
    quote only as support for the "keep real mistakes in" clause, labelled as an accident.
  - status: **promoted**, on makemore 1 and the tokenizer lecture.
  - In practice: "drop keepdim" is a fair deliberate example. "Skip zero_grad" comes from an
    accident, so label it "the bug he made by accident in micrograd". The agent may still use
    it as a planted bug.

### F3 — overstated — rule let-the-learner-try-before-you-show-the-answer
- problem: The rule holds in a weaker form, and status **promoted** is right: there are four
  independent sources. But the title and the in-practice line ("wait for the learner's
  attempt before giving it") describe withholding the answer, and his lectures do not do that.
  - **In the lectures the invitation is brief and optional.** micrograd says "maybe pause the
    video here", and the solution follows straight away. The tokenizer lecture says "if you'd
    like a fun exercise uh and pause here otherwise I'm going to start putting in my
    solution".
  - **Only the Zero to Hero README asks for real work first.** Even there the answer is on
    tap: unpause and see the answer whenever you are stuck.
  - **The Dwarkesh line is about good educators.** It describes what good educators do, said
    in the educator's voice while he discusses tutoring, not a description of his own
    lectures (see F5).

  An agent that holds back the answer until the learner guesses would do something his
  recordings never show.
- evidence:
  - micrograd `raw/youtube/VMj-3S1tku0.md` @1:33:56: "maybe pause the video here and see if
    you can figure it out yourself".
  - tokenizer `raw/youtube/zduSFxRajkE.md` @48:38: the try-it invitation is conditional, and
    the solution comes in the same breath.
  - `raw/github/karpathy__nn-zero-to-hero.md` §Lecture 5: unpause when stuck and "see me give
    away the answer".
  - Dwarkesh `raw/talks/lXUZvyajciY.md` @2:19:57: "a lot of good educators will do this".
- fix:
  - title: "Invite the learner to try a step before you show the answer."
  - In practice, replace the first bullet with: "Teaching: pose the next step as a question and
    offer the learner a chance to try. Give the answer as soon as they ask for it or are
    stuck, and never make them guess before they may proceed. For a longer exercise, like the
    README's backprop exercise, set the work first and keep the solution available."
  - Keep the Dwarkesh quote, with the gloss "describing what good educators do", and the
    attribution note in F5. Status **promoted**.

### F4 — overstated — rule surface-assumptions-and-ask-when-unclear
- problem: Status **inferred** is right: no quote states the rule, and the candidate says so
  plainly ("this wiki's reading of those complaints"). The candidate also flags the DESIGN.md
  "top complaint" wording correctly.
  - **The Dwarkesh quote cuts the other way.** It is listed as support, but it is his defence
    of *deliberate* assumptions in his code against agents. Agents could not accept his custom
    implementation, made the code over-defensive and turned it into a production code base.
  - **The reviewing bullet repeats that failure.** "Name the implicit assumptions in the code…
    and ask whether each was intended" invites the agent to do what he complains about:
    query, and implicitly guard against, assumptions he made on purpose.
- evidence: Dwarkesh `raw/talks/lXUZvyajciY.md` @33:14: agents were "way too over-defensive"
  and made try-catch statements; "I have a bunch of assumptions in my code, and it's okay."
- fix:
  - Relabel the Dwarkesh quote as a *limit* on the rule, not support for it.
  - Replace the reviewing bullet with: "Reviewing: name the assumptions that silently change a
    result (a filled-in missing value, an assumed dimension or default). Do not ask the author
    to justify, or guard against, deliberate simplifying assumptions, and do not suggest
    defensive code for them."
  - Add the line the plan requires as a separate opening body sentence: "This rule is
    inferred: no source states it."

### F5 — minor — rule let-the-learner-try-before-you-show-the-answer (attribution)
- problem: The @2:19:57 quote is very likely his, but the transcript cannot prove it.
  - **Speaker turns from context.** The sentence before ("You're presenting the pain before you
    present a solution…") is Dwarkesh. The passage from "You want to take the student through
    that progression" carries on into @2:20:34 ("before I give you a shot"). The next turn,
    "Why do you think… experts… are often bad at explaining", is Dwarkesh's question, and the
    answer "I suffered from it myself" is his. So the quoted sentence sits inside his turn.
  - **Whose "I" it is.** The "I" is a role-played educator, not a report of his own lectures.
- evidence: `raw/talks/lXUZvyajciY.md` @2:19:57–@2:21:16; no speaker labels in the file.
- fix: keep the quote, with the note "speaker inferred from turn structure; the 'I' is the
  educator he describes". The rule does not depend on it: the other three sources still
  promote it.

### F6 — overstated — rule report-every-result-with-its-baseline-and-caveats
- problem: The title reaches further than the quotes. All four quotes caveat a *comparison*
  against PyTorch or OpenAI's GPT-2: 2024, llm.c and the GPT-2 lecture. None is about results
  in general. "Every result" also turns a habit into an absolute.
  Independence holds, and so does **promoted**. #481 and the GPT-2 lecture caveat the same
  FineWeb comparison, but they are different texts and neither summarises the other. That
  makes them two sources of one caveat, which is worth noting.
- evidence:
  - `raw/github/karpathy__llm.c__discussion-224.md` §intro: "~6.4% faster than PyTorch, in this
    constrained setting".
  - `raw/github/karpathy__llm.c__discussion-481.md` §intro and `raw/youtube/l8pRSuU81PU.md`
    @3:44:15: the same FineWeb caveat.
- fix:
  - slug, if renamed: `report-a-comparison-with-its-setting-and-caveats`.
  - title: "When you compare a result with a baseline, state the setting and what might make
    the comparison unfair."
  - In practice: change the building bullet's "every reported number" to "every number
    compared with a baseline".

### F7 — overstated — rule cut-complexity-that-does-not-pay-for-itself
- problem: The quotes are well chosen and the "complexity must pay" reading is right. But
  every quote is about his own reference or educational repos (llama2.c, llm.c mainline,
  minGPT). Those repos send production and deployment needs to forks or to other projects.
  - **The second reviewing bullet overreaches.** "Prefer one hackable file and config in code
    over flags and frameworks" would push that style onto client production code. He does not
    advise that; he sets his repos apart from production code bases.
- evidence:
  - `raw/github/karpathy__llama2.c.md` §contributing: applications are expected to fork, and
    deployment efficiency points to llama.cpp.
  - `raw/talks/lXUZvyajciY.md` @33:14: he contrasts his code with "a production code base".
- fix:
  - Title: unchanged.
  - In practice: scope the second reviewing bullet to "in educational or reference code, prefer
    one hackable file…". For other code, keep only the cost/benefit question in the first
    bullet.

### F8 — overstated — rule build-it-yourself-to-understand-it
- problem: The title holds on three sources. "Without copy-paste" comes from one of them
  (Dwarkesh), where the context is learning from the nanochat repo. That is acceptable inside
  a title that is otherwise well supported, but it should stay scoped to learning.
  - **The reviewing bullet goes further than any source.** "Flag code the author cannot explain
    line by line" turns a learning method into a review standard.
  - **His 2026 view cuts against it.** He says he no longer remembers API details such as
    keepdim versus keep_dim, and needn't, though the fundamentals still matter.
- evidence:
  - Dwarkesh `raw/talks/lXUZvyajciY.md` @29:27: the context is how to learn from nanochat.
  - Sequoia talk `raw/talks/96jN2OCOfLs.md` @21:16: he says he no longer remembers details like
    keep dims versus keep dim, but you still need the fundamentals.
- fix:
  - title: "To learn something, build it yourself, without copy-paste."
  - In practice: change the reviewing bullet to "flag code that misuses something the author
    evidently has not understood (what a call does to memory, gradients or shapes), not API
    trivia".

### F9 — minor — rule check-every-shape-and-be-explicit
- problem: The quote "And I encourage you to treat this with respect." does not name what
  "this" is. In context it is broadcasting semantics.
  - **Absolute.** "Check every shape" is stronger than "be careful with the shapes".
  - **Scope and date.** The candidate correctly scopes the rule to 2022 array code. A 2026 note
    helps: he now leaves API-level details to agents but keeps the fundamentals.
- evidence:
  - `raw/youtube/PaCmpygFfXo.md` @44:10: "read through broadcasting semantics" comes just before
    the quote.
  - `raw/youtube/q8SA3rM6ckI.md` @22:12: "be careful with the shapes".
  - `raw/talks/96jN2OCOfLs.md` @21:16.
- fix:
  - title: "Be careful with shapes and broadcasting, and write array code explicit enough that a
    wrong assumption raises an error."
  - Gloss the first quote as "(broadcasting)".
  - Status **promoted**.

## Checked and correct

- **start-from-the-simplest-thing-that-shows-it.** All four quotes are his and in place, and the
  sources are independent. The title matches Dwarkesh @2:17:33 ("simplest thing that shows
  that thing… then I can tack on the other terms"). The reviewing bullet (land the simple
  version first) is an extension, mild enough to keep.
- **predict-the-number-before-you-run.** All four quotes are in place. The micrograd quote is
  correctly labelled as supporting the reason, not the procedure.
- **check-against-a-known-good-reference.** All four quotes are in place and his, including the
  rustbpe LLM Assistance note, which is his own text. The CUDA MODE keynote and #454 are
  different texts.
- **Hypothesis handling.** The rejected and merged hypotheses are reasoned correctly. "Silently
  work a bit worse" and "top complaint about coding agents" indeed do not appear in raw.

## Table

| # | slug | verified status | result |
|---|---|---|---|
| 1 | build-it-yourself-to-understand-it | promoted | F8 |
| 2 | start-from-the-simplest-thing-that-shows-it | promoted | ok |
| 3 | predict-the-number-before-you-run | promoted | ok |
| 4 | check-every-shape-and-be-explicit | promoted | F9 |
| 5 | check-against-a-known-good-reference | promoted | ok |
| 6 | report-every-result-with-its-baseline-and-caveats | promoted | F6 |
| 7 | keep-model-written-changes-small-and-check-them | promoted (dated) | F1 |
| 8 | cut-complexity-that-does-not-pay-for-itself | promoted | F7 |
| 9 | let-the-learner-try-before-you-show-the-answer | promoted (softened) | F3, F5 |
| 10 | show-the-instructive-bug-failing-then-explain-it | promoted only with the tokenizer quote; bench otherwise | F2 |
| 11 | surface-assumptions-and-ask-when-unclear | inferred | F4 |

Totals: 9 findings: 6 overstated, 1 status, 2 minor, 0 wrong, 0 mis-cited. No rule needs to be
dropped.
