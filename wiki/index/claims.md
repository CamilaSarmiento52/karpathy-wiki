# Claims

Specific positions he takes, dated, with a short quote. Alphabetical. Maintained by ingest; do not edit by hand.

- [[a-buggy-neural-net-can-still-train-on-a-simple-problem|A buggy neural net can still appear to train on a simple problem]] — 2022-08-16; un-zeroed grads acted as a huge step size
- [[approximate-gradient-with-more-steps-beats-exact-gradient|An approximate minibatch gradient with more steps beats an exact one with fewer]] — 2022-09-12; minibatch training
- [[attention-is-a-communication-mechanism|Attention is a communication mechanism between nodes in a directed graph]] — 2023-01-17; no notion of space; the mask makes it a decoder
- [[avoid-batch-normalization-where-possible|He tells learners to avoid batch normalization as much as possible]] — 2022-10-04; coupling examples regularises by accident and causes bugs
- [[backpropagation-is-more-general-than-neural-networks|Backpropagation does not care about neural networks]] — 2022-08-16; it works on arbitrary expressions
- [[batchnorm-train-test-variance-mismatch-is-a-bug|He considers batchnorm's biased-in-training, unbiased-at-test variance a bug]] — 2022-10-11; he uses Bessel's correction throughout
- [[claude-code-is-the-first-convincing-llm-agent|Claude Code is the first convincing LLM agent]] — 2025-12-19; agents belong on your own computer
- [[counting-and-gradient-bigram-models-are-the-same-model|The counting bigram model and the one-layer net are the same model]] — 2022-09-07; W.exp() is the count table
- [[deep-learning-is-largely-shape-gymnastics|Much of deep-learning development is making tensor shapes work]] — 2022-11-21; 2-D, 3-D, 4-D, NCL vs NLC, view and permute
- [[english-is-the-new-programming-language|English is now a programming language]] — 2025-06-19; everyone is now a programmer
- [[forgetting-to-zero-grad-is-a-common-neural-net-bug|Forgetting to zero grad before backward is a common bug]] — 2022-08-16; he made it on camera
- [[gpt-is-not-a-complicated-model|GPT is not a complicated model]] — 2023-01-08; about 300 lines, the complexity is batching
- [[gradient-based-models-scale-where-count-tables-do-not|Gradient-based models scale to longer contexts where count tables do not]] — 2022-09-07; tables blow up with context
- [[micrograd-is-all-you-need-everything-else-is-efficiency|micrograd is all you need; everything else is efficiency]] — 2022-08-16; tensors change nothing in the math
- [[modern-innovations-make-precise-initialization-less-important|Residual connections, normalization layers and better optimisers make exact initialisation less important]] — 2022-10-04; Kaiming is still the most common init
- [[neural-networks-are-just-mathematical-expressions|Neural networks are just a class of mathematical expressions]] — 2022-08-16; data and weights in, loss out
- [[no-rag-needed-for-a-small-wiki|His ~100-article wiki worked without RAG]] — 2026-04-02; one wiki's experience, not a general result
- [[pretraining-gives-a-document-completer|Pretraining alone gives a document completer, not an assistant]] — 2023-01-17; it babbles internet until finetuned
- [[pytorch-documentation-is-unreliable|PyTorch's documentation is unmaintained and will mislead you]] — 2022-11-21; wrong, incomplete, unclear; do your best
- [[the-hockey-stick-loss-means-training-is-wasting-steps|A hockey-stick loss curve means the first iterations are wasted squashing overconfident weights]] — 2022-10-04; fix the output scale at init
- [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers|Only the forward pass changes on the way to transformers]] — 2022-09-07; logits, softmax, NLL and gradient descent stay
- [[this-is-the-decade-of-agents|This is the decade of agents, not the year]] — 2025-06-19; self-driving shows how long autonomy takes
- [[treat-broadcasting-with-respect|Broadcasting deserves respect, not fast-and-loose use]] — 2022-09-07; the bugs are subtle
- [[understand-backprop-even-with-autograd|Autograd being available is no reason to ignore how backpropagation works]] — 2022-10-11; backprop is a leaky abstraction
- [[use-cross-entropy-not-a-hand-rolled-loss|Call F.cross_entropy rather than rolling your own loss]] — 2022-09-12; fused kernels, simpler backward, no overflow
- [[vibe-coding-is-for-throwaway-weekend-projects|Vibe coding is fine for throwaway weekend projects]] — 2025-02-02; extended by the 2025-12-19 claim
- [[vibe-coding-will-terraform-software|Vibe coding will reshape software and jobs]] — 2025-12-19; adds professional uses
- [[weight-regularization-is-equivalent-to-count-smoothing|Pushing weights toward zero is equivalent to count smoothing]] — 2022-09-07; strength plays the role of added counts
