---
type: claim
stated_on: 2024-07-11
confidence: stated
sources: ["[[github-2024-07-11-llmc-gpt-2-1-6b]]"]
context: ["[[youtube-2022-10-04-makemore-3-activations-batchnorm]]"]
topic: "[[weight-initialization]]"
---
# He judged llm.c not yet careful enough about initialisation, activation ranges and stability for long runs
> "I think we're not yet being sufficiently careful with our initialization" — [[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (400B token run)

## Context
He trained the 1558M model for 420B tokens, more than GPT-3's 300B for this size; the run looked great until about step 330,000, reaching about 61% on HellaSwag, then became unstable and exploded ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (400B token run)). Smaller spikes along the way were handled by detecting simple instantaneous instability and skipping the update (`-sl 5.0 -sg 5.0`), which he says mitigates and defers the issues ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (400B token run)). He thinks llm.c is not yet careful enough with initialisation, activation ranges and overall training stability, and that deeper issues gradually drift the model into instability, especially for larger models and long training; he asks readers for ideas ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (400B token run)). The same caveat opens the post: llm.c is not yet sufficiently stabilised and still sees loss spikes and bad activation ranges now and then ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro). Training and scaling stability is item 2 of his roadmap ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Coming up)).

## Related claims
- **Note:** [[modern-innovations-make-precise-initialization-less-important]] (2022) says exact initialisation matters less than it did, while also saying the field has not solved it ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @36:26, @1:54:48). Both can hold, one about small networks and the other about long runs of large ones, so this is not a contradiction and no relation is set ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (400B token run)).
