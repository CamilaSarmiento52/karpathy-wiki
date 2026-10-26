---
type: source
raw_path: raw/youtube/t3YJ5hKiMQ0.md
published: 2022-11-21
medium: youtube
summary: "Fifth makemore lecture, in which he grows the character-level MLP into a WaveNet-like hierarchical model, rebuilds torch.nn-style containers, fixes a BatchNorm bug on 3-D inputs, and reflects on how he develops deep learning code."
url: https://www.youtube.com/watch?v=t3YJ5hKiMQ0
title: "Building makemore Part 5: Building a WaveNet"
---
# Building makemore Part 5: Building a WaveNet
Raw: [[raw/youtube/t3YJ5hKiMQ0]] · Original: https://www.youtube.com/watch?v=t3YJ5hKiMQ0

## Summary
A 56-minute lecture continuing the makemore character-level language model (@00:00). He wants more context than three characters and a deeper network that fuses that context progressively rather than squashing it into one hidden layer, which leads to an architecture like the 2016 WaveNet paper (@00:33, @01:05). Along the way he "pytorchifies" the code: Embedding and Flatten modules, a Sequential container, and a model object replacing a bare list of layers (@09:24, @12:42, @13:16). Scaling the block size from 3 to 8 alone takes validation loss from 2.10 to 2.02 (@20:29, @21:01); the hierarchical version, with hidden units chosen so the parameter count matches, initially gives no gain (@37:47, @38:20), until he finds that his BatchNorm1d reduced over the wrong dimensions on 3-D inputs (@38:53, @40:32, @42:49). After the fix and a larger model he reaches 1.993 (@45:01, @46:08). He closes with notes on convolutions as an efficiency device, PyTorch documentation, shape wrangling, his Jupyter-to-repository workflow, and the missing experimental harness (@47:46, @52:51, @53:24, @53:57, @54:32).

## Key points
- Fuse two consecutive elements per level in a tree-like hierarchy instead of crushing all characters into the first layer; longer context alone improves the baseline; convolutions slide the same tree over the sequence and do not change the model → [[wavenet-hierarchical-model]]
- Rebuilding torch.nn: Embedding, Flatten, Sequential, parameters(); the loss-smoothing view trick; PyTorch's matmul over leading batch dimensions → [[pytorch]]
- BatchNorm has running statistics and a train/eval flag; forgetting eval mode and reducing over the wrong dims on 3-D input both caused bugs; he keeps a channels-last convention → [[batch-normalization]], [[avoid-batch-normalization-where-possible]]
- Train 2.05 vs val 2.10 means little overfitting, so scale up; normally you watch both losses together → [[overfitting-and-generalization]], [[diagnose-under-or-overfitting]]
- Match parameter counts (22,000) before comparing a flat and a hierarchical architecture → [[diagnose-under-or-overfitting]]
- Forward a tiny scratch batch, print every layer's class and output shape, break after the first iteration, avoid -1 in view → [[check-shapes-and-broadcasting]]
- Prototype in Jupyter, paste into VS Code, kick off experiments from the repo; without an evaluation harness he is guessing and checking → [[prototype-in-jupyter-then-repo]], [[gradient-descent]]
- Squashing all the context into one hidden layer is the MLP's limit → [[multilayer-perceptron]]
- PyTorch docs are unmaintained and will mislead you → [[pytorch-documentation-is-unreliable]]
- Much of the work is making tensor shapes line up → [[deep-learning-is-largely-shape-gymnastics]]
- The makemore repo at part 5: 12,000 to 76,000 parameters, 2.10 to 1.993 → [[makemore]]

## Fed pages
- [[wavenet-hierarchical-model]]
- [[pytorch]]
- [[batch-normalization]]
- [[avoid-batch-normalization-where-possible]]
- [[overfitting-and-generalization]]
- [[diagnose-under-or-overfitting]]
- [[check-shapes-and-broadcasting]]
- [[prototype-in-jupyter-then-repo]]
- [[gradient-descent]]
- [[multilayer-perceptron]]
- [[pytorch-documentation-is-unreliable]]
- [[deep-learning-is-largely-shape-gymnastics]]
- [[makemore]]
- [[how-he-explains]]
