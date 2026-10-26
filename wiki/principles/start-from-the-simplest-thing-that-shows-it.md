---
type: principle
status: promoted
inferred: false
quotes:
  - {text: "I always try to find the first-order terms", source: "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]", location: "@2:17:33"}
  - {text: "we're going to start off with the simplest possible neural network", source: "[[youtube-2023-01-17-gpt-from-scratch]]", location: "@21:57"}
  - {text: "where you add one component at a time", source: "[[blog-2026-02-12-microgpt]]", location: "§Progression"}
  - {text: "Step 2 build the ramp.", source: "[[x-2024-02-21-technical-accessibility]]", location: "#1"}
sources: ["[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]", "[[youtube-2023-01-17-gpt-from-scratch]]", "[[blog-2026-02-12-microgpt]]", "[[x-2024-02-21-technical-accessibility]]"]
---
# Start from the simplest thing that shows the idea working, then add one piece at a time, and show the steps

> "I always try to find the first-order terms" — [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @2:17:33
>
> "where you add one component at a time" — [[blog-2026-02-12-microgpt]] §Progression

## In practice

He describes this as a habit from physics: when he looks at a system, he looks for the first-order component, the simplest thing that shows the effect, and only then adds the other terms ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @2:17:33). In the GPT lecture he starts from a bigram model, which he calls the simplest possible neural network for language modelling, before building up the Transformer ([[youtube-2023-01-17-gpt-from-scratch]] @21:57).

He publishes the build-up, not only the end state. The microgpt post lists a progression of files, from a bigram count table with no neural net up to the full training script, and points to a Gist whose revisions show the diff between each step ([[blog-2026-02-12-microgpt]] §Progression). He puts the same idea as two steps: build the thing, then build the ramp to it ([[x-2024-02-21-technical-accessibility]] #1).

**Note:** for reviewing, this is the wiki's extension, not his words: ask what the first-order version of a change is, and if a change mixes the core idea with efficiency work, suggest landing the simple version first ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @2:17:33).

## Rests on

- [[learn-by-building-and-explaining]], [[spelled-out-build-from-scratch]], [[small-hackable-educational-code]], [[verify-gradients-against-pytorch]]
- [[micrograd-is-all-you-need-everything-else-is-efficiency]], [[microgpt-is-the-full-algorithm-everything-else-is-efficiency]]
- [[build-the-ramp-not-just-the-thing]], [[education-is-building-ramps-to-knowledge]]

## Sources

- [[talk-2025-10-17-dwarkesh-ghosts-not-animals]]
- [[youtube-2023-01-17-gpt-from-scratch]]
- [[blog-2026-02-12-microgpt]]
- [[x-2024-02-21-technical-accessibility]]
