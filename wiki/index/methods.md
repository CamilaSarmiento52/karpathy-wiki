# Methods

How he builds, debugs, explains and evaluates. Alphabetical. Maintained by ingest; do not edit by hand.

- [[ai-assisted-coding-loop|AI-assisted coding loop]] — small concrete diffs, verified fast; keep the AI on the leash
- [[build-and-publish-projects|Build and publish projects]] — end to end, learn on demand, remix, publish, let the audience raise the bar, count the hours
- [[check-shapes-and-broadcasting|Check shapes and broadcasting]] — walk the shapes through the rules, verify a row sums to one, print every layer's output shape
- [[diagnose-under-or-overfitting|Diagnose under- or overfitting]] — overfit a small batch first, compare train and dev loss, match parameter counts before comparing architectures
- [[learning-rate-sweep|Learning-rate sweep]] — exponentially spaced rates over 1,000 steps, read the valley in the plot
- [[llm-wiki-workflow|LLM wiki workflow]] — collect, compile, browse, ask, file back, lint
- [[make-it-work-then-make-it-cheap|Make it work, then make it cheap]] — most capable model and heavy prompting first, then cheaper models and distillation
- [[prototype-in-jupyter-then-repo|Prototype in Jupyter, then move to the repo]] — read the docs for shapes, prototype in a notebook, paste into VS Code, run experiments from the repo, have a harness
- [[quick-experiment-loop|Quick experiment loop]] — change one thing, re-run a five-minute d12, read the same plots
- [[reproduce-a-published-model|Reproduce a published model]] — GPT-2 with released weights, GPT-3's recipe, from scratch on open data, compare with the checkpoint, publish the bill, scale up
- [[small-hackable-educational-code|Small, hackable, educational code]] — one file, PyTorch only, a few hundred lines, published with its git history; know when it needs teeth
- [[spelled-out-build-from-scratch|Spelled-out build from scratch]] — blank notebook, by hand first, then code, then the real repo; one addition at a time, one validation number each
- [[training-diagnostics|Training diagnostics]] — expected loss at init, hockey stick, activation/gradient histograms, update-to-data ratio against -3; average the loss over batches
- [[verify-against-a-reference-implementation|Verify against a reference implementation]] — run the same input through a known-good implementation and match its output exactly
- [[verify-gradients-against-pytorch|Verify gradients against PyTorch]] — numerical bump check, then PyTorch parity
