---
type: artifact
repo_url: https://github.com/karpathy/micrograd
language: Python
status: active
sources: ["[[youtube-2022-08-16-micrograd]]", "[[youtube-2022-09-07-makemore-1-bigram]]", "[[github-2024-02-20-nn-zero-to-hero-readme]]", "[[x-2024-02-21-technical-accessibility]]", "[[blog-2026-02-12-microgpt]]"]
context: ["[[youtube-2022-10-11-makemore-4-backprop-ninja]]"]
aliases: [micrograd autograd engine]
---
# micrograd
A scalar-valued autograd engine he released on GitHub about two years before the August 2022 lecture, originally source-only, which he rebuilds from scratch in that video ([[youtube-2022-08-16-micrograd]] @00:00, @00:32, @05:24).

## What it demonstrates
- Two files: `engine.py`, the roughly 100-line autograd engine, and `nn.py`, the neural-net library defining neuron, layer and MLP; roughly 150 lines in total ([[youtube-2022-08-16-micrograd]] @07:03, @07:35).
- It works on individual scalars for pedagogical reasons; he says you would never do this in production ([[youtube-2022-08-16-micrograd]] @05:24, @05:56).
- As of recording, `engine.py` has data, grad, `_backward`, `_prev`, `_op`, add, mul, pow and relu (not tanh, which he intends to add); `nn.py` has a `Module` parent class with `zero_grad`, mirroring PyTorch ([[youtube-2022-08-16-micrograd]] @2:17:07, @2:18:12).
- The repo includes a test comparing forward and backward against PyTorch, and `demo.ipynb`, a larger 2-D binary classifier with batching, max-margin loss, L2 regularisation and learning-rate decay ([[youtube-2022-08-16-micrograd]] @2:18:45, @2:19:18, @2:19:51, @2:20:23).
- In the lecture he uses `_prev` as a set built from a `_children` tuple, which he believes was for efficiency ([[youtube-2022-08-16-micrograd]] @23:02).
- `status: active` rests only on his stated intent to keep developing it; a later GitHub snapshot should decide the real status ([[youtube-2022-08-16-micrograd]] @2:16:34, @2:17:07).

- In the first makemore lecture he presents makemore as the next repo built the same way, and points back to micrograd for backpropagation and the training loop ([[youtube-2022-09-07-makemore-1-bigram]] @00:00, @1:10:02, @1:33:26).

- In the fourth makemore lecture he describes micrograd as an autograd engine only at the level of individual scalars, which he does not think is enough on its own, and refers back to it for the rule that gradients from multiple uses of a node sum, for the tanh backward, and for topological-order backprop ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @02:43, @25:02, @53:30, @1:39:25).

- In the Zero to Hero README it is the companion repo of Lecture 1, which covers backpropagation and training and assumes basic Python and a vague memory of high-school calculus ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 1).

- In a February 2024 post he recalls that the repo, when first published, got some traction on GitHub and then stagnated for many months; after he made the video building it from scratch it went through hockey-stick growth and became an often-cited reference for learning backpropagation, though the code had not changed at all ([[x-2024-02-21-technical-accessibility]]). He describes it there as about 200 lines, extensively commented in the `.py` files and README, getting to the heart of an autograd engine on one page; the 2022 lecture gives roughly 150, and both are his approximations ([[x-2024-02-21-technical-accessibility]]; [[youtube-2022-08-16-micrograd]] @07:35). He says the video almost 100X'd interest and engagement with the same code ([[x-2024-02-21-technical-accessibility]]).

- **microgpt (2026-02-12).** He names micrograd first among the projects microgpt culminates; microgpt's autograd is a scalar `Value` class, and for that part he points readers to his 2.5-hour micrograd video; see [[microgpt]] ([[blog-2026-02-12-microgpt]] §intro, §Autograd). The post does not itself compare the two engines ([[blog-2026-02-12-microgpt]] §Autograd).

## Related
- [[backpropagation]] — what the engine implements
- [[multilayer-perceptron]] — what `nn.py` builds
- [[pytorch]] — the API it is modelled on
- [[spelled-out-build-from-scratch]], [[verify-gradients-against-pytorch]]
- [[micrograd-is-all-you-need-everything-else-is-efficiency]]
- [[nn-zero-to-hero]] — the course it opens
- [[build-the-ramp-not-just-the-thing]] — the lesson he draws from its uptake
- [[understand-backprop-even-with-autograd]] — the tensor-level sequel to the scalar engine
- **Note:** [[nanogpt]] and [[nanochat]] are his later from-scratch training repos; the sources here do not connect them.
- [[microgpt]] — a whole GPT on a scalar autograd engine
