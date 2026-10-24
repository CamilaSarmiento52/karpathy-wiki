# Topics

Ideas he explains, each defined in his framing. Alphabetical. Maintained by ingest; do not edit by hand.

- [[activation-functions|Activation functions]] — tanh, sigmoid, ReLU and their local derivatives
- [[backpropagation|Backpropagation]] — recursive chain rule backwards through an expression graph
- [[batch-normalization|Batch normalization]] — standardise pre-activations over the batch, learned gain and bias, running statistics; it couples examples and its state causes bugs
- [[bigram-language-model|Bigram language model]] — one character of context; a 27×27 count table, a one-layer net, or the GPT lecture's embedding-table baseline
- [[broadcasting|Broadcasting]] — PyTorch's shape rules and the keepdim bug
- [[building-for-agents|Building for agents]] — make docs and infrastructure readable and actionable for LLM agents
- [[character-level-language-modeling|Character-level language modeling]] — predict the next character; the makemore task and how he samples from it
- [[embeddings|Embeddings]] — a shared lookup table C, equivalent to a linear layer on one-hot inputs; positional embeddings for attention
- [[gradient-descent|Gradient descent]] — forward, backward, step against the gradient; learning rate and minibatches
- [[jagged-intelligence|Jagged intelligence]] — LLMs as people spirits or ghosts: superhuman in places, broken in others
- [[llm-gui|LLM GUI]] — text suits LLMs, not people; LLMs need a visual interface
- [[llm-knowledge-bases|LLM knowledge bases]] — an LLM compiles and maintains a markdown wiki of your sources
- [[llms-as-operating-systems|LLMs as operating systems]] — utility, fab, and above all a 1960s-era operating system
- [[loss-functions|Loss functions]] — one number to minimise: mean squared error, negative log likelihood, cross-entropy
- [[multilayer-perceptron|Multilayer perceptron]] — neurons, layers and MLPs, from micrograd to the Bengio 2003 language model
- [[overfitting-and-generalization|Overfitting and generalization]] — train/dev/test splits; equal train and dev loss means under-fitting
- [[partial-autonomy-apps|Partial autonomy apps]] — LLM apps with context management, a GUI and an autonomy slider
- [[pretraining-and-finetuning|Pretraining and finetuning]] — pretrain a document completer on the internet, then align it with supervised data, a reward model and PPO
- [[pytorch|PyTorch]] — the production library micrograd mirrors; tensors, autograd, nn.Module-style layers and containers, and its unreliable docs
- [[regularization|Regularization]] — count smoothing and the squared-weight term that does the same job; dropout before scaling up
- [[rlvr|RLVR]] — reinforcement learning from verifiable rewards, the new training stage of 2025
- [[self-attention|Self-attention]] — lower-triangular weighted aggregation made data-dependent by queries, keys and values; scaling, causal mask, multiple heads
- [[softmax|Softmax]] — logits as log counts; exponentiate and normalise; one-hot inputs
- [[software-3-0|Software 3.0]] — prompts as programs, after code (1.0) and weights (2.0)
- [[tokenization|Tokenization]] — text to integers over a vocabulary; characters versus sub-word BPE trades codebook size against sequence length
- [[transformer-architecture|Transformer architecture]] — communication then computation; residual pathway, pre-norm LayerNorm, decoder-only; his notes on the GPT papers
- [[vibe-coding|Vibe coding]] — building by prompting and not reading the code
- [[wavenet-hierarchical-model|WaveNet-style hierarchical model]] — fuse two consecutive elements per level instead of one squashing layer; convolutions only make it efficient
- [[weight-initialization|Weight initialization]] — expected loss at init, confidently wrong logits, divide by the square root of fan-in, Kaiming gain; the GPT lecture code skipped it
