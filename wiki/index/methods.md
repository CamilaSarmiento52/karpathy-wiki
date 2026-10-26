# Methods

How he builds, debugs, explains and evaluates. Alphabetical. Maintained by ingest; do not edit by hand.

- [[ai-assisted-coding-loop|AI-assisted coding loop]] — small concrete diffs, verified fast; keep the AI on the leash
- [[append-and-review-note|Append-and-review note]] — one note, append at the top, no metadata, skim and rescue, rarely delete
- [[build-and-publish-projects|Build and publish projects]] — end to end, learn on demand, remix, publish, let the audience raise the bar, count the hours
- [[check-shapes-and-broadcasting|Check shapes and broadcasting]] — walk the shapes through the rules, verify a row sums to one, print every layer's output shape
- [[choose-a-model-tier|Choose a model tier]] — check the model, compare tiers, most powerful that works, non-thinking first, an LLM council, know each model's tools
- [[diagnose-under-or-overfitting|Diagnose under- or overfitting]] — overfit a small batch first, compare train and dev loss, match parameter counts before comparing architectures
- [[digital-hygiene-checklist|Digital hygiene checklist]] — fifteen practices from password manager and hardware keys to a network monitor and work-life separation
- [[fit-your-own-scaling-law|Fit your own scaling law]] — fix a FLOP budget, sweep depth, fit the optima, read off the tokens-to-parameters ratio, check the family does not cross
- [[how-he-explains|How he explains]] — blank file, tiny numbers, one piece at a time, predict the loss, show shapes, show a bug on purpose, invite the learner to try, compare with a reference, analogies, say what is left out
- [[learn-by-building-and-explaining|Learn by building and explaining]] — rebuild without copy-paste, find the first-order term, ramp up, let the learner try, explain to find the gaps
- [[learning-rate-sweep|Learning-rate sweep]] — exponentially spaced rates over 1,000 steps, read the valley in the plot
- [[llm-wiki-workflow|LLM wiki workflow]] — collect, compile, browse, ask, file back, lint
- [[make-it-work-then-make-it-cheap|Make it work, then make it cheap]] — most capable model and heavy prompting first, then cheaper models and distillation
- [[port-a-pytorch-model-to-c-and-cuda|Port a PyTorch model to C and CUDA]] — explicit PyTorch, hand-written backward, C on float arrays, one file, then CUDA kernels and library swaps
- [[prototype-in-jupyter-then-repo|Prototype in Jupyter, then move to the repo]] — read the docs for shapes, prototype in a notebook, paste into VS Code, run experiments from the repo, have a harness
- [[quick-experiment-loop|Quick experiment loop]] — change one thing, re-run a five-minute d12, read the same plots
- [[read-with-an-llm|Read with an LLM]] — raw text into the context, summary first, ask as you read, diagram the chapter
- [[reproduce-a-published-model|Reproduce a published model]] — GPT-2 with released weights, GPT-3's recipe, from scratch on open data, compare with the checkpoint, publish the bill, scale up
- [[small-hackable-educational-code|Small, hackable, educational code]] — one file, PyTorch only, a few hundred lines, published with its git history; know when it needs teeth
- [[spelled-out-build-from-scratch|Spelled-out build from scratch]] — blank notebook, by hand first, then code, then the real repo; one addition at a time, one validation number each
- [[start-a-new-chat-per-topic|Start a new chat per topic]] — wipe the context window when switching topic; tokens are a precious resource
- [[teach-a-capability-with-synthetic-tasks|Teach a capability with synthetic tasks]] — synthetic conversations in midtraining and SFT, randomised prompts, answers shaped around the tokenizer, a drill for the weak part
- [[training-diagnostics|Training diagnostics]] — expected loss at init, hockey stick, activation/gradient histograms, update-to-data ratio against -3; average the loss over batches
- [[verify-against-a-reference-implementation|Verify against a reference implementation]] — run the same input through a known-good implementation and match its output exactly
- [[verify-citations|Verify citations]] — primary sources, follow citations, first drafts, read the code, transcribe images first
- [[verify-gradients-against-pytorch|Verify gradients against PyTorch]] — numerical bump check, then PyTorch parity
- [[voice-input|Voice input]] — phone microphone, a system-wide dictation key, type the hard names, read-aloud for output
