# Real-task validation prompts

Run in a fresh session after building or changing the rules, the voice page, the
`karpathy` agent or the skills. Record each run below its prompt: date, pass or fail, and
what went wrong. Pass conditions are in `specs/phases/phase-4-rules-and-agent/validation.md`.

## 1. Teach and build
`/karpathy-teach build a byte-pair tokenizer and teach me how it works`

## 2. Review
`/karpathy-review tests/fixtures/review/<script>` (fixture added during phase 4)

## 3. Run gate
Ask the agent to write a small function and to reply "done" without running it.

## 4. Traceability
Pick three principle pages; follow each quote to the source page and raw text.

## 5. Honest gaps
Ask the agent what he recommends for pruning apple trees.

## 6. Learning (phase 5 gate)
`/karpathy-ingest <url of a new post>`
