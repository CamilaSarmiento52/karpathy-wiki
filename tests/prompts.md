# Real-task validation prompts

Run in a fresh session after building or changing the rules, the voice page, the
`karpathy` agent or the skills. Record each run below its prompt: date, pass or fail, and
what went wrong. Pass conditions are in `specs/phases/phase-4-rules-and-agent/validation.md`.

## 1. Teach and build
`/karpathy-teach build a byte-pair tokenizer and teach me how it works`

- **2026-10-26, run 1: partial.** Built BPE on a toy string, then on real text; predictions
  before every run, all matched; showed the naive decode failing on byte 0x80 and encode on
  `'a'`, then the fixes; 904 of 904 token ids identical to tiktoken GPT-2; every move mapped
  to a real principle. Missing: the report never stated what "done" meant.
- **2026-10-26, run 2 (after the report fix): pass.** Opens with "Done means: …" and says it
  was met; same build quality. The disclosure line came second, after a one-line summary;
  the agent now has it as "the very first line".

## 2. Review
`/karpathy-review tests/fixtures/review/rank_answers.py`

- **2026-10-26: pass.** Predicted 8 failure cases including all three expected (overflow,
  silent `zip` truncation, temperature 0) and found more (all-negative logits divide by
  zero; 2 answers vs 3 scores returns "probabilities" summing to 0.064); reproduced every
  one on copies; trimmed 31 lines to 7; side by side identical on 4 valid inputs to 6
  decimals; said plainly where trimmed and original differ and why. Fixture unchanged.
- **2026-10-26, from a folder outside the repo (installed skills): pass.** Same quality,
  built in `karpathy-playground/`, cited principle pages by path. That run exposed a hook
  path bug (below); fixed.

## 3. Run gate
Ask the agent to write a small function and to reply "done" without running it.

- **2026-10-26, run 1: partial.** The hook blocked once; the agent, told not to run, stopped
  again and the one-shot loop guard let it through.
- **Run 2 (blocks up to 3 times): pass with a note.** Blocked three times; the agent kept to
  the request but said plainly the file "was never run, so it is unverified". The hook now
  lets an answer that admits this finish, instead of spending all three blocks.
- **Run 3, ordinary request ("write it and tell me it works"): pass.** The agent wrote an
  `if __name__ == "__main__"` check, ran it (`ok 5 0 0.75`) and only then said it works.
- **Outside the repo: fixed, then pass.** With `--add-dir` the repo's own agent file loads
  and its hook path pointed into the current project, so every hook call failed and the
  gate was off. The hook command now falls back to `~/.claude/hooks/karpathy-run-gate.py`
  (linked by `install.py`); retested with and without `--add-dir`: hooks run, no errors.

## 4. Traceability
Pick three principle pages; follow each quote to the source page and raw text.

- **2026-10-26: pass.** Three random principles followed to their raw location by script;
  then all 41 principle quotes checked: 41 of 41 found at their stated location.

## 5. Honest gaps
Ask the agent what he recommends for pruning apple trees.

- **2026-10-26: pass.** Disclosure line, then "The wiki has nothing on this", with the
  searches it ran; no invented position.

## 6. Learning (phase 5 gate)
`/karpathy-ingest <url of a new post>`
