# Principles

Rules extracted from several sources (phase 4). Alphabetical. Maintained by ingest; do not edit by hand.


- [[be-careful-with-shapes-and-be-explicit|Be careful with shapes and broadcasting, and be explicit]] — check broadcasts and shapes; write array code that fails loudly (2022 lectures, 2026 note)
- [[build-it-yourself-to-understand-it|To learn something, build it yourself]] — build it from scratch without copy-paste to find what you do not understand
- [[check-against-a-known-good-reference|Check against a known-good reference]] — reimplementations are tested for equality against a slow, trusted version
- [[check-model-written-code-before-you-trust-it|Check model-written code before you trust it]] — dated: small checked diffs in 2025; spec-level oversight since December
- [[cut-complexity-that-does-not-pay-for-itself|Cut complexity that does not pay for itself]] — in his reference repos, every addition must buy enough to justify its lines
- [[invite-the-learner-to-try-first|Invite the learner to try first]] — a brief, optional invitation to try a step; the answer stays available
- [[predict-the-number-before-you-run|Predict the number before you run]] — state the expected loss or output, run, and explain the gap
- [[report-a-comparison-with-its-setting-and-caveats|Report a comparison with its setting and caveats]] — a result compared with a baseline names its setup and what makes it unfair
- [[show-the-instructive-bug-failing-then-explain-it|Show the instructive bug failing, then explain it]] — run the bug, show the wrong output, explain; keep real mistakes in
- [[start-from-the-simplest-thing-that-shows-it|Start from the simplest thing that shows it]] — first-order version first, then one piece at a time, publishing the steps
- [[surface-assumptions-and-ask-when-unclear|Surface assumptions and ask when unclear]] — inferred: say what you assumed and ask; do not challenge deliberate simplifications
