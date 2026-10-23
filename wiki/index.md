# Index

Every wiki page, grouped by type. Maintained by ingest; do not edit by hand.

## Sources
- [[blog-2025-12-19-year-in-review-2025|2025 LLM Year in Review]] — six 2025 paradigm changes: RLVR, jagged intelligence, LLM apps, Claude Code, vibe coding, LLM GUI
- [[github-2025-11-12-nanogpt-readme|nanoGPT README]] — his earlier training/finetuning repo, marked deprecated in favour of nanochat
- [[github-2026-07-03-nanochat-readme|nanochat README]] — minimal single-node harness that trains a GPT-2-grade chat model, set by one depth dial
- [[x-2025-02-02-vibe-coding|There's a new kind of coding I call "vibe coding"]] — the post that coined vibe coding
- [[x-2026-04-02-llm-knowledge-bases|LLM Knowledge Bases]] — his workflow for an LLM-compiled Obsidian wiki, the pattern this project follows
- [[youtube-2022-08-16-micrograd|The spelled-out intro to neural networks and backpropagation: building micrograd]] — builds a scalar autograd engine from a blank notebook and trains a tiny MLP
- [[youtube-2022-09-07-makemore-1-bigram|The spelled-out intro to language modeling: building makemore]] — bigram character model built by counting and as a one-layer net; they are the same model
- [[youtube-2022-09-12-makemore-2-mlp|Building makemore Part 2: MLP]] — the Bengio 2003 MLP character model; minibatches, learning-rate sweep, train/dev/test splits
- [[youtube-2022-10-04-makemore-3-activations-batchnorm|Building makemore Part 3: Activations & Gradients, BatchNorm]] — initial loss and the hockey stick, saturated tanh, Kaiming init, batch normalization, and his activation/gradient/update-ratio plots
- [[youtube-2022-10-11-makemore-4-backprop-ninja|Building makemore Part 4: Becoming a Backprop Ninja]] — the MLP's backward pass written by hand at tensor level, checked against PyTorch; cross-entropy and batchnorm gradients in closed form
- [[youtube-2025-06-19-software-is-changing|Andrej Karpathy: Software Is Changing (Again)]] — YC keynote on Software 3.0, the LLM OS, partial autonomy and building for agents

## Topics
- [[activation-functions|Activation functions]] — tanh, sigmoid, ReLU and their local derivatives
- [[backpropagation|Backpropagation]] — recursive chain rule backwards through an expression graph
- [[batch-normalization|Batch normalization]] — standardise pre-activations over the batch, learned gain and bias, running statistics; it couples examples
- [[bigram-language-model|Bigram language model]] — one character of context; a 27×27 count table or a one-layer net
- [[broadcasting|Broadcasting]] — PyTorch's shape rules and the keepdim bug
- [[building-for-agents|Building for agents]] — make docs and infrastructure readable and actionable for LLM agents
- [[character-level-language-modeling|Character-level language modeling]] — predict the next character; the makemore task and how he samples from it
- [[embeddings|Embeddings]] — a shared lookup table C, equivalent to a linear layer on one-hot inputs
- [[gradient-descent|Gradient descent]] — forward, backward, step against the gradient; learning rate and minibatches
- [[jagged-intelligence|Jagged intelligence]] — LLMs as people spirits or ghosts: superhuman in places, broken in others
- [[llm-gui|LLM GUI]] — text suits LLMs, not people; LLMs need a visual interface
- [[llm-knowledge-bases|LLM knowledge bases]] — an LLM compiles and maintains a markdown wiki of your sources
- [[llms-as-operating-systems|LLMs as operating systems]] — utility, fab, and above all a 1960s-era operating system
- [[loss-functions|Loss functions]] — one number to minimise: mean squared error, negative log likelihood, cross-entropy
- [[multilayer-perceptron|Multilayer perceptron]] — neurons, layers and MLPs, from micrograd to the Bengio 2003 language model
- [[overfitting-and-generalization|Overfitting and generalization]] — train/dev/test splits; equal train and dev loss means under-fitting
- [[partial-autonomy-apps|Partial autonomy apps]] — LLM apps with context management, a GUI and an autonomy slider
- [[pytorch|PyTorch]] — the production library micrograd mirrors; tensors, autograd, nn.Module
- [[regularization|Regularization]] — count smoothing and the squared-weight term that does the same job
- [[rlvr|RLVR]] — reinforcement learning from verifiable rewards, the new training stage of 2025
- [[softmax|Softmax]] — logits as log counts; exponentiate and normalise; one-hot inputs
- [[software-3-0|Software 3.0]] — prompts as programs, after code (1.0) and weights (2.0)
- [[vibe-coding|Vibe coding]] — building by prompting and not reading the code
- [[weight-initialization|Weight initialization]] — expected loss at init, confidently wrong logits, divide by the square root of fan-in, Kaiming gain

## Claims
- [[a-buggy-neural-net-can-still-train-on-a-simple-problem|A buggy neural net can still appear to train on a simple problem]] — 2022-08-16; un-zeroed grads acted as a huge step size
- [[approximate-gradient-with-more-steps-beats-exact-gradient|An approximate minibatch gradient with more steps beats an exact one with fewer]] — 2022-09-12; minibatch training
- [[avoid-batch-normalization-where-possible|He tells learners to avoid batch normalization as much as possible]] — 2022-10-04; coupling examples regularises by accident and causes bugs
- [[backpropagation-is-more-general-than-neural-networks|Backpropagation does not care about neural networks]] — 2022-08-16; it works on arbitrary expressions
- [[batchnorm-train-test-variance-mismatch-is-a-bug|Using the biased variance in training and the unbiased one at test time is a bug in batchnorm]] — 2022-10-11; he uses Bessel's correction throughout
- [[claude-code-is-the-first-convincing-llm-agent|Claude Code is the first convincing LLM agent]] — 2025-12-19; agents belong on your own computer
- [[counting-and-gradient-bigram-models-are-the-same-model|The counting bigram model and the one-layer net are the same model]] — 2022-09-07; W.exp() is the count table
- [[english-is-the-new-programming-language|English is now a programming language]] — 2025-06-19; everyone is now a programmer
- [[forgetting-to-zero-grad-is-a-common-neural-net-bug|Forgetting to zero grad before backward is a common bug]] — 2022-08-16; he made it on camera
- [[gradient-based-models-scale-where-count-tables-do-not|Gradient-based models scale to longer contexts where count tables do not]] — 2022-09-07; tables blow up with context
- [[micrograd-is-all-you-need-everything-else-is-efficiency|micrograd is all you need; everything else is efficiency]] — 2022-08-16; tensors change nothing in the math
- [[modern-innovations-make-precise-initialization-less-important|Residual connections, normalization layers and better optimisers make exact initialisation less important]] — 2022-10-04; Kaiming is still the most common init
- [[neural-networks-are-just-mathematical-expressions|Neural networks are just a class of mathematical expressions]] — 2022-08-16; data and weights in, loss out
- [[no-rag-needed-for-a-small-wiki|His ~100-article wiki worked without RAG]] — 2026-04-02; one wiki's experience, not a general result
- [[the-hockey-stick-loss-means-training-is-wasting-steps|A hockey-stick loss curve means the first iterations are wasted squashing overconfident weights]] — 2022-10-04; fix the output scale at init
- [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers|Only the forward pass changes on the way to transformers]] — 2022-09-07; logits, softmax, NLL and gradient descent stay
- [[this-is-the-decade-of-agents|This is the decade of agents, not the year]] — 2025-06-19; self-driving shows how long autonomy takes
- [[treat-broadcasting-with-respect|Broadcasting deserves respect, not fast-and-loose use]] — 2022-09-07; the bugs are subtle
- [[understand-backprop-even-with-autograd|Autograd being available is no reason to ignore how backpropagation works]] — 2022-10-11; backprop is a leaky abstraction
- [[use-cross-entropy-not-a-hand-rolled-loss|Call F.cross_entropy rather than rolling your own loss]] — 2022-09-12; fused kernels, simpler backward, no overflow
- [[vibe-coding-is-for-throwaway-weekend-projects|Vibe coding is fine for throwaway weekend projects]] — 2025-02-02; extended by the 2025-12-19 claim
- [[vibe-coding-will-terraform-software|Vibe coding will reshape software and jobs]] — 2025-12-19; adds professional uses
- [[weight-regularization-is-equivalent-to-count-smoothing|Pushing weights toward zero is equivalent to count smoothing]] — 2022-09-07; strength plays the role of added counts

## Artifacts
- [[makemore|makemore]] — character-level name generator built across the makemore lectures
- [[micrograd|micrograd]] — ~150-line scalar autograd engine and neural-net library
- [[nanochat|nanochat]] — train and talk to your own GPT-2-grade model for about $48
- [[nanogpt|nanoGPT]] — his earlier training/finetuning repo, deprecated in favour of nanochat

## Methods
- [[ai-assisted-coding-loop|AI-assisted coding loop]] — small concrete diffs, verified fast; keep the AI on the leash
- [[check-shapes-and-broadcasting|Check shapes and broadcasting]] — walk the shapes through the rules, verify a row sums to one
- [[diagnose-under-or-overfitting|Diagnose under- or overfitting]] — overfit a small batch first, then compare train and dev loss
- [[learning-rate-sweep|Learning-rate sweep]] — exponentially spaced rates over 1,000 steps, read the valley in the plot
- [[llm-wiki-workflow|LLM wiki workflow]] — collect, compile, browse, ask, file back, lint
- [[quick-experiment-loop|Quick experiment loop]] — change one thing, re-run a five-minute d12, read the same plots
- [[spelled-out-build-from-scratch|Spelled-out build from scratch]] — blank notebook, by hand first, then code, then the real repo
- [[training-diagnostics|Training diagnostics]] — expected loss at init, hockey stick, activation/gradient histograms, update-to-data ratio against -3
- [[verify-gradients-against-pytorch|Verify gradients against PyTorch]] — numerical bump check, then PyTorch parity

## Timelines
- [[vibe-coding-over-time|Vibe coding over time]] — weekend projects (Feb 2025), then professional uses added (Dec 2025)

## Principles

## Syntheses
