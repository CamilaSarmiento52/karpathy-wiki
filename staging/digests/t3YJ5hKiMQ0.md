# Digest: Building makemore Part 5: Building a WaveNet
- raw: raw/youtube/t3YJ5hKiMQ0.md · published: 2022-11-21 · medium: youtube · words: 10487
- source slug: youtube-2022-11-21-makemore-5-wavenet

## Source page

```
---
type: source
raw_path: raw/youtube/t3YJ5hKiMQ0.md
published: 2022-11-21
medium: youtube
summary: Fifth makemore lecture, in which he grows the character-level MLP into a WaveNet-like hierarchical model, rebuilds torch.nn-style containers, fixes a BatchNorm bug on 3-D inputs, and reflects on how he develops deep learning code.
url: https://www.youtube.com/watch?v=t3YJ5hKiMQ0
title: "Building makemore Part 5: Building a WaveNet"
---
# Building makemore Part 5: Building a WaveNet
Raw: [[raw/youtube/t3YJ5hKiMQ0]] · Original: https://www.youtube.com/watch?v=t3YJ5hKiMQ0

## Summary
A 56-minute lecture, recorded from a hotel room in Kyoto, continuing the makemore character-level language model (@00:00). He wants more context than three characters and a deeper network that fuses that context progressively rather than squashing it into one hidden layer, which leads to an architecture like the 2016 WaveNet paper (@00:33, @01:05). Along the way he "pytorchifies" the code: Embedding and Flatten modules, a Sequential container, and a model object replacing a bare list of layers (@09:24, @12:42, @13:16). Scaling the block size from 3 to 8 alone takes validation loss from 2.10 to 2.02 (@20:29, @21:01); the hierarchical version, with hidden units chosen so the parameter count matches, initially gives no gain (@37:47, @38:20), until he finds that his BatchNorm1d reduced over the wrong dimensions on 3-D inputs (@38:53, @40:32, @42:49). After the fix and a larger model he reaches 1.993 (@45:01, @46:08). He closes with notes on convolutions as an efficiency device, PyTorch documentation, shape wrangling, his Jupyter-to-repository workflow, and the missing experimental harness (@47:46, @52:51, @53:24, @53:57, @54:32).

## Key points
- Fuse two consecutive elements per level in a tree-like hierarchy instead of crushing all characters into the first layer → [[hierarchical-progressive-fusion]]
- Matrix multiply in PyTorch acts on the last dimension and treats leading dimensions as batch, which makes the hierarchy a reshape (FlattenConsecutive) plus the same Linear → [[hierarchical-progressive-fusion]]
- Longer context alone improves the baseline, 2.10 to 2.02 → [[context-length-scaling]]
- Rebuilding torch.nn: Linear, BatchNorm1d, Tanh, Embedding, Flatten, Sequential, parameters() → [[pytorch-style-layer-modules]]
- BatchNorm has running statistics, a train/eval flag and couples batch elements; forgetting eval mode and reducing over the wrong dims both caused bugs here → [[batchnorm-pitfalls]]
- Convolutions slide the same tree over the sequence inside CUDA kernels and reuse shared nodes; they do not change the model → [[convolutions-as-efficiency]]
- Train 2.05 vs val 2.10 means little overfitting, so scale up; normally you watch both losses together → [[train-and-validation-loss]]
- Without an evaluation harness he is guessing and checking, which he says is not a typical workflow → [[experimental-harness]]
- The makemore repo and its lecture series → [[makemore]]
- Prototype in Jupyter, paste into VS Code, kick off experiments from the repo → [[prototype-in-jupyter-then-repo]]
- Forward a tiny scratch batch, print every layer's class and output shape, break after the first iteration, avoid -1 in view → [[inspect-shapes-layer-by-layer]]
- Match parameter counts (22,000) before comparing a flat and a hierarchical architecture → [[control-for-parameter-count]]
- PyTorch docs are unmaintained and will mislead you → [[pytorch-documentation-is-unreliable]]
- Much of the work is making tensor shapes line up → [[deep-learning-is-largely-shape-gymnastics]]
- Convolution is strictly an efficiency device → [[convolutions-do-not-change-the-model]]
- State inside BatchNorm is harmful → [[batchnorm-state-is-a-source-of-bugs]]
- At equal parameters, the hierarchy did not beat the flat MLP before the BatchNorm fix → [[hierarchical-model-did-not-beat-flat-at-equal-parameters]]
- Guess-and-check with no harness is not representative of real deep learning work → [[guess-and-check-is-not-a-typical-workflow]]
- He prefers a channels-last (N, L, C) BatchNorm convention over PyTorch's (N, C, L) → [[he-prefers-channels-last-batchnorm]]

## Fed pages
- [[hierarchical-progressive-fusion]]
- [[context-length-scaling]]
- [[pytorch-style-layer-modules]]
- [[batchnorm-pitfalls]]
- [[convolutions-as-efficiency]]
- [[train-and-validation-loss]]
- [[experimental-harness]]
- [[makemore]]
- [[prototype-in-jupyter-then-repo]]
- [[inspect-shapes-layer-by-layer]]
- [[control-for-parameter-count]]
- [[pytorch-documentation-is-unreliable]]
- [[deep-learning-is-largely-shape-gymnastics]]
- [[convolutions-do-not-change-the-model]]
- [[batchnorm-state-is-a-source-of-bugs]]
- [[hierarchical-model-did-not-beat-flat-at-equal-parameters]]
- [[guess-and-check-is-not-a-typical-workflow]]
- [[he-prefers-channels-last-batchnorm]]
```

## Candidates

### topic: hierarchical-progressive-fusion
- existing: no
- aliases: WaveNet-style architecture, tree-like context fusion, dilated causal convolution stack, progressive fusion
- statements:
  - He wants more input characters than three and a deeper model that fuses the context progressively, because feeding everything into one hidden layer squashes too much information too quickly (@00:33).
  - Making the MLP more complex this way arrives at something very much like WaveNet, a 2016 autoregressive model for audio with the same modeling setup and a tree-like architecture (@00:33, @01:05).
  - In WaveNet, two characters are fused into a bigram representation, bigrams into four-character chunks, and so on, so context is fused slowly as the network deepens (@18:13, @18:49).
  - He says the dilated causal convolution framing sounds scary but the idea is simple, and the convolution is an implementation detail for speed (@18:49).
  - At each level the network fuses only two consecutive elements: two characters, then two bigrams, then two four-grams (@19:22).
  - PyTorch's matrix multiply works on the last dimension and treats all leading dimensions as batch dimensions, so a (4, 5, 80) input through an 80-by-200 weight gives (4, 5, 200) (@24:52, @25:27).
  - He uses this to process the four bigram groups of each example in parallel as an extra batch dimension: the flatten layer should output (4, 4, 20) rather than (4, 80), and the first Linear should expect 20 inputs (@26:01, @27:11, @27:46).
  - Explicitly concatenating even and odd positions gives the same result as simply calling view with the desired shape (@28:51, @30:03, @30:36).
  - He writes a FlattenConsecutive(n) module that views (B, T, C) as (B, T//n, C*n) and squeezes out a spurious dimension of size one, named differently from torch.flatten because the APIs differ (@31:42, @32:15, @33:23).
  - With FlattenConsecutive(2) and three Linear-BatchNorm-Tanh blocks, shapes go (4,8,10) → (4,4,20) → (4,4,200) → (4,2,400) → (4,200) → (4,400) → logits (@35:38, @36:10, @36:42).
  - The resulting three-layer network implements the WaveNet tree for a receptive field of 8; the paper's diagram has four layers and 16 (@37:15).
  - He did not implement WaveNet's gated linear units, residual connections or skip connections, only the structure (@47:13).
  - Bumping embeddings to 24 and hidden units up gives 76,000 parameters and validation loss 1.993 (@46:08).
- relation to an existing page: none

### topic: context-length-scaling
- existing: no
- aliases: block size, scaling context
- statements:
  - Changing block size from 3 to 8 means predicting the ninth character from eight of context, and the first Linear layer grows by about 10,000 parameters (@19:22, @19:56).
  - Running this flat model as a baseline, validation loss improves from 2.10 to 2.02 just from the longer context, and samples look qualitatively better (@20:29, @21:01).
  - He calls this a rough baseline with a lot of hyperparameter optimisation left on the table (@21:01).
- relation to an existing page: none

### topic: pytorch-style-layer-modules
- existing: no
- aliases: pytorchifying, rebuilding torch.nn, nn.Module containers, Sequential
- statements:
  - Since part 3 the layers are modules treated like Lego bricks, with APIs and signatures modelled on torch.nn so that, for example, his Linear mirrors torch.nn.Linear (@02:11, @02:44, @03:18).
  - He drops the per-layer generator argument in favour of seeding the torch RNG once globally for simplicity (@04:59).
  - He moves the embedding table and the view operation into Embedding and Flatten modules, both of which exist in PyTorch with extra keyword arguments he does not use, so the forward pass needs no special cases (@09:24, @10:31, @11:03, @11:36).
  - He introduces PyTorch-style containers: a Sequential that holds a list of layers, passes input through them in order, and reports the parameters of its children (@12:42, @13:16, @13:48).
  - The code then calls model(xb) and loss is cross-entropy on the logits, which simplifies training, evaluation and sampling (@14:22, @14:54, @15:30).
  - He says they have effectively re-implemented torch.nn on top of torch.tensor and now understand roughly what is in it, so future lectures will use torch.nn directly (@51:42, @52:15).
- relation to an existing page: none

### topic: batchnorm-pitfalls
- existing: no
- aliases: BatchNorm bugs, batch normalisation state, train/eval mode
- statements:
  - BatchNorm keeps running mean and variance trained outside backpropagation by exponential moving average, has a training flag because its behaviour differs between train and eval, and couples the activations of examples in a batch (@03:18, @03:52, @04:25).
  - He calls it a weird layer that causes a lot of bugs: you must set the right mode and wait for the statistics to settle (@04:25).
  - Sampling with BatchNorm left in training mode on a single example gave NaN, because the variance of one number is not a number; he calls this a bug introduced by not maintaining training state (@15:30, @16:03, @16:35).
  - On a 3-D input of (32, 4, 68) his BatchNorm1d reduced only over dimension 0, so it silently kept a running mean of shape (1, 4, 68), maintaining separate statistics for each of the four positions instead of 68 channels (@38:53, @39:26, @40:32).
  - torch.mean accepts a tuple of dimensions, so reducing over (0, 1) gives 68 channel statistics; he makes the reduce dims depend on x.ndim and raise for anything else (@41:42, @42:13, @42:49, @43:22).
  - PyTorch's BatchNorm1d expects (N, C) or (N, C, L) and reduces over dims 0 and 2, whereas his version assumes channels are last, (N, L, C); he keeps the deviation (@43:22, @43:55, @44:28).
  - The fix moved validation loss from 2.029 to 2.022, which he says may not be statistically significant but is expected because each statistic is now estimated from 32×4 numbers rather than 32 (@45:01, @45:35).
- relation to an existing page: none

### topic: convolutions-as-efficiency
- existing: no
- aliases: convolution as sliding a model, dilated causal convolutions
- statements:
  - The use of convolutions in WaveNet is strictly for efficiency and does not change the model implemented here (@47:46).
  - A seven-letter name like DeAndre is eight independent examples; forwarding them is eight separate model calls, or a Python for-loop (@47:46, @48:20, @48:53).
  - A convolution hides that for-loop inside CUDA kernels, sliding a linear filter over a one-dimensional input sequence (@48:53, @49:27).
  - The WaveNet diagram's black tree is what he implemented for one output; a convolution slides that tree to compute all outputs at once (@49:27, @50:01).
  - The second efficiency is variable reuse: an intermediate node is the right child of one parent and the left child of another, so it is computed once rather than twice (@50:34, @51:08).
  - He plans a future video converting the network to dilated causal convolutional layers (@51:08, @53:57).
- relation to an existing page: none

### topic: train-and-validation-loss
- existing: no
- aliases: dev set, overfitting check, loss curve smoothing
- statements:
  - Training loss 2.05 against validation 2.10 tells him the model is not overfitting much, so he can make progress by scaling the network up (@17:09).
  - The raw per-step loss plot is too noisy with a batch of 32; he smooths it by viewing the list of losses as 200 rows of 1000 and taking the row mean, which also makes the learning-rate decay visible (@05:33, @08:17, @08:51).
  - He admits they were only looking at training loss, whereas normally you look at training and validation loss together, and that things look different when squeezing out numbers (@46:42, @47:13).
- relation to an existing page: none

### topic: experimental-harness
- existing: no
- aliases: evaluation harness, experiment harness
- statements:
  - As experiments take longer he is in the dark about hyperparameters and learning rates, and says they are missing an experimental harness to run many experiments and tune the architecture (@46:42).
  - He does not want the 2.1 to 1.9 improvement to be the focus because without a harness they are guessing and checking (@46:42).
  - A typical workflow sets up an evaluation harness, scripts with many arguments, lots of kicked-off experiments, plots of training and validation losses, population-level analysis and hyperparameter searches; none of that was done here (@54:32, @55:06).
  - How to set up such a harness is a topic for another lecture (@55:06).
- relation to an existing page: possibly related to [[quick-experiment-loop]] (nanochat, 2026), which describes the harness he later built; a **Note:** connection only, no supports/extends relation between a topic and a method.

### artifact: makemore
- existing: no
- aliases: make more
- statements:
  - makemore is his character-level language model built up over a lecture series; this is part 5 (@00:00).
  - The dataset is a set of names split into examples of previous characters predicting the next; with block size 3 there are 182,000 examples (@01:36, @02:11).
  - Part 4 was the manual backpropagation exercise, an aside; part 5 starts from part 3's code (@01:36).
  - The starting model has about 12,000 parameters and validation loss 2.10, producing name-like samples not in the training set (@05:33, @06:06, @06:40).
  - The final model has 76,000 parameters and validation loss 1.993; he invites viewers to beat it by reallocating channels, changing embedding size, scaling the one-hidden-layer network, implementing WaveNet layers from the paper, or tuning initialisation and optimisation (@46:08, @55:06, @55:40, @56:12).
  - Future lectures he names: convolutional version, residual and skip connections, experimental harness, RNNs, LSTMs, GRUs, Transformers (@53:57, @54:32, @55:06).
- note: no repo URL is given in the video; `repo_url` for the artifact page would need the GitHub raw file (karpathy/makemore) when ingested. `language: Python`, `status` to be decided at merge.

### method: prototype-in-jupyter-then-repo
- existing: no
- aliases: Jupyter to VS Code workflow
- steps / statements:
  - Spend a lot of time in PyTorch documentation reading what shapes each layer accepts and what it does (@52:15).
  - Prototype layers and implementations in Jupyter notebooks, making sure all the shapes work out (@53:24).
  - Once satisfied with the functionality, copy-paste the code into the repository of actual training code, working in VS Code alongside the notebook (@53:24, @53:57).
  - Kick off experiments from the code repository (@53:57).
  - He presents this as roughly representative of the development process of building deep neural networks (@52:15, @53:57).
- relation to an existing page: none

### method: inspect-shapes-layer-by-layer
- existing: no
- aliases: layer inspector, shape debugging, break after first iteration
- steps / statements:
  - Create a scratch space with a temporary batch of four random examples and pass it through the model to inspect tensor shapes along the forward pass (@21:34, @22:06).
  - Iterate over the layers, printing each layer's class name and output shape (@35:06, @36:10).
  - Insert a break after the first training iteration to make sure one step runs before committing to a run (@12:10, @19:56, @44:28).
  - Verify that a layer that runs without errors also does the right thing, since broadcasting can hide a wrong reduction (@38:20, @39:26).
  - Avoid -1 in view and pass an explicit dimension to squeeze, so that wrong assumptions produce error messages (@32:49, @33:56).
  - Re-run every cell after editing it; a forgotten cell left BatchNorm in the wrong mode (@15:30).
- relation to an existing page: none

### method: control-for-parameter-count
- existing: no
- aliases: parameter-matched comparison
- steps / statements:
  - When comparing a new architecture against the old one, pick the hidden size so that total parameters match: 68 hidden units gives 22,000 parameters, the same as before (@37:15, @37:47).
  - Ask whether the parameters are used more efficiently by the new architecture rather than whether a bigger model does better (@37:47).
  - Remove debugging cells and rerun the optimisation before reading the result (@37:47).
  - Before concluding, check for bugs and note that the architecture has not been tuned (@38:20).
- relation to an existing page: none

### claim: pytorch-documentation-is-unreliable
- existing: no
- title: PyTorch's documentation is unmaintained and will mislead you
- confidence: stated
- quote: "as far as I can tell no one is maintaining any documentation" (@52:51)
- statements:
  - He says PyTorch's documentation is not very good: the team spends its time on hardcore engineering of distributed primitives while the docs are wrong, incomplete and unclear, and you do your best with them (@52:51).
  - Context: this is the first of his closing notes on what the deep learning development process looks like (@52:15).
- relation to an existing page: none

### claim: deep-learning-is-largely-shape-gymnastics
- existing: no
- title: Much of deep learning development is making tensor shapes work
- confidence: stated
- quote: "there's a lot of gymnastics around these multi-dimensional arrays" (@53:24)
- statements:
  - He says a ton of the work is making shapes work: whether arrays are 2-D, 3-D or 4-D, which layers take which shapes, NCL versus NLC, viewing and permuting (@52:51, @53:24).
  - He spends a lot of time babysitting shapes in notebooks before moving code to the repository (@53:24).
- relation to an existing page: none

### claim: convolutions-do-not-change-the-model
- existing: no
- title: Convolutions in WaveNet are strictly an efficiency device
- confidence: stated
- quote: "the use of convolutions is strictly for efficiency it doesn't actually change the model" (@47:46)
- statements:
  - A convolution moves the Python for-loop over positions into CUDA kernels and reuses shared intermediate nodes; the model computed is the same tree he implemented (@49:27, @50:34, @51:08).
- relation to an existing page: none

### claim: batchnorm-state-is-a-source-of-bugs
- existing: no
- title: BatchNorm's internal state makes it a frequent source of bugs
- confidence: stated
- quote: "there's state in this layer and state is harmful" (@04:25)
- statements:
  - BatchNorm's running statistics and train/eval flag have to be managed, and he says this introduces bugs when you forget the mode (@03:52, @04:25).
  - The lecture itself hits two such bugs: NaN from training mode on a single example, and wrong reduction dims on 3-D input (@16:03, @40:32).
- relation to an existing page: none

### claim: hierarchical-model-did-not-beat-flat-at-equal-parameters
- existing: no
- title: Controlling for parameters, his hierarchical model did not beat the flat MLP before the BatchNorm fix
- confidence: stated
- quote: "from the flat to hierarchical is not giving us anything yet" (@38:20)
- statements:
  - With 22,000 parameters in both, the hierarchical model's validation loss was 2.029 against 2.027 for the flat one (@37:47, @38:20).
  - He gives two caveats: the architecture was his first guess with no hyperparameter search, and BatchNorm1d might still have a bug, which it did (@38:20, @45:01).
  - After the fix it reached 2.022, an improvement he says is not clearly statistically significant (@45:01, @45:35).
  - He closes by saying it is not obvious a large enough one-hidden-layer network could not beat the hierarchical one, which would be embarrassing (@55:40).
- relation to an existing page: none

### claim: guess-and-check-is-not-a-typical-workflow
- existing: no
- title: Guess-and-check without an experimental harness is not how deep learning is normally done
- confidence: stated
- quote: "this is not representative of typical deep learning workflows" (@54:32)
- statements:
  - He says they are just guessing and checking everything with no experimental harness, and describes the typical alternative: evaluation harness, scripted experiments, plots of train and validation losses, population-level analysis, hyperparameter search (@54:32).
- relation to an existing page: supports topic [[experimental-harness]]; a reviewer may link it as context for [[quick-experiment-loop]] (the harness he describes in nanochat 2026) without asserting a relation.

### claim: he-prefers-channels-last-batchnorm
- existing: no
- title: He prefers a channels-last BatchNorm convention to PyTorch's (N, C, L)
- confidence: stated
- quote: "I prefer it this way honestly" (@44:28)
- statements:
  - PyTorch's BatchNorm1d takes (N, C) or (N, C, L) and reduces over dims 0 and 2; his takes (N, C) or (N, L, C) and reduces over 0 and 1 (@43:55, @44:28).
  - He acknowledges the deviation from PyTorch's API, says he thinks it is okay, and keeps it (@44:28).
- relation to an existing page: none

## Quotes
- "this makes it sound very scary but actually the idea is very simple" (@18:49)
- "we're crushing way too much information way too fast" (@19:56)
- "there's state in this layer and state is harmful" (@04:25)
- "I like to be as explicit as possible always" (@33:56)
- "from the flat to hierarchical is not giving us anything yet" (@38:20)
- "I prefer it this way honestly" (@44:28)
- "we have no experimental harness we're just guessing and checking" (@46:42)
- "the use of convolutions is strictly for efficiency it doesn't actually change the model" (@47:46)
- "we've overall pytorchified our code quite a bit more" (@51:42)
- "as far as I can tell no one is maintaining any documentation" (@52:51)
- "there's a lot of gymnastics around these multi-dimensional arrays" (@53:24)
- "I'm spending a lot of time basically babysitting the shapes" (@53:24)
- "I develop in Jupiter notebook I paste into vs code" (@53:57)
- "this is not representative of typical deep learning workflows" (@54:32)
- "would be kind of embarrassing if this did not do better" (@55:40)

## Notes for merge
- Caption misspellings, consistent throughout: "bathroom", "Bachelor", "bash Norm", "basharm", "bastron", "batch room" = BatchNorm; "10h" / "10ational neuralities" = tanh / tanh nonlinearities; "petroch", "pytortify", "patreon" = PyTorch; "Platinum", "pattern", "platform" = Flatten; "Jupiter" = Jupyter; "make more" = makemore; "the witness" / "weight net" = WaveNet; "auto aggressive" = autoregressive; "collusions" = convolutions; "diagram representation" = bigram representation; "logents" / "Lodges" = logits; "comnet" = convnet; "grooves" = GRUs; "reaper" = repo. Quotes above copy the caption spelling verbatim (e.g. "Jupiter").
- The paper is WaveNet (van den Oord et al., DeepMind 2016); the caption says "the point in 2016" (@01:05). He does not name the authors.
- Numbers to carry carefully: val 2.10 (flat, block 3) → 2.02 (flat, block 8) → 2.029 (hierarchical, 22k params) → 2.022 (after BatchNorm fix) → 1.993 (24-dim embeddings, more hidden units, 76k params). The 2.027 at @37:47 is the flat block-8 figure restated with more precision; also "2.1 down to 1.9" at @46:42 is his rounding.
- He says "64 sorry for 68 channels" at @42:13; the correct number is 68.
- Mentioned but not explained: gated linear units, residual and skip connections (@47:13, @53:57); RNNs, LSTMs, GRUs, Transformers (@55:06); CUDA kernels (@49:27). None are topic candidates.
- The loss-smoothing trick with view(-1, 1000).mean(1) (@07:12–@08:51) is a small demo of view semantics; I filed it under train-and-validation-loss rather than as its own topic. Merge may prefer to drop it.
- The three methods (prototype-in-jupyter-then-repo, inspect-shapes-layer-by-layer, control-for-parameter-count) are distilled from what he does on screen plus his explicit closing notes; the first is stated as his process (@53:24, @53:57), the other two are observed practice he narrates, so merge may label their definitions accordingly.
- The experimental-harness topic is defined mostly by its absence here; the only description of what one contains is @54:32. If merge wants a cross-link to [[quick-experiment-loop]] (nanochat, 2026), it must be a **Note:** connection, not evidence.
- No repo URL in the video; the makemore artifact page needs `repo_url` from a GitHub raw file that does not exist yet in raw/. If merge cannot fill a required field, consider holding the artifact until karpathy/makemore README is collected.
- He mentions he changed microphone at @12:42 and is recording from Kyoto at @00:00; neither is wiki content.
