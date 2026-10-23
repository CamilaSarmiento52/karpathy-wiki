---
type: method
steps:
  - Overfit a handful of examples first
  - Train on the train split only
  - Compare train and dev loss
  - If roughly equal, scale the model up
  - If dev departs above train, overfitting has begun
  - Evaluate the test split once at the end
sources: ["[[youtube-2022-09-12-makemore-2-mlp]]"]
aliases: [overfit a single batch, compare train and dev loss, reading train vs dev loss, sanity-check the training loop]
---
# Diagnose under- or overfitting
How he reads whether a model is too small or memorising: first check the training loop by overfitting a handful of examples, then compare the loss on the train and dev splits ([[youtube-2022-09-12-makemore-2-mlp]] @39:23, @1:00:20).

## Steps
1. **Tiny dataset.** He develops on the first five words, 32 examples, for efficiency and plans to erase that later ([[youtube-2022-09-12-makemore-2-mlp]] @10:02).
2. **Overfit it.** Running 1,000 steps on 32 examples gives a very low loss, because there are 3,400 parameters for so few examples ([[youtube-2022-09-12-makemore-2-mlp]] @38:50, @39:23).
3. **Inspect predictions.** He compares the max logits and their indices against the labels to see where they differ; the loss cannot be exactly zero where one input has several labels, and is correct where input to output is unique ([[youtube-2022-09-12-makemore-2-mlp]] @39:56, @40:28, @41:03).
4. **Full data.** Then he reads in the full dataset and optimises ([[youtube-2022-09-12-makemore-2-mlp]] @41:03, @41:35).
5. **Train, then evaluate on dev.** After training only on the train split he evaluates on dev, gets about 2.3, and compares it to the training loss ([[youtube-2022-09-12-makemore-2-mlp]] @59:12, @59:47).
6. **Equal means under-fitting.** Train and dev loss about equal means the model is not overfitting but under-fitting, so he expects gains from scaling the network ([[youtube-2022-09-12-makemore-2-mlp]] @1:00:20).
7. **Scale up.** He increases the hidden layer to 300 neurons and later the embedding to 10 dimensions ([[youtube-2022-09-12-makemore-2-mlp]] @1:00:52, @1:07:08).
8. **Watch for departure.** When train and validation performance slowly depart, the parameters may be large enough to start overfitting ([[youtube-2022-09-12-makemore-2-mlp]] @1:09:55).
9. **Test once.** Hyperparameters are tuned on dev performance across many experiments; the test set is evaluated a single time ([[youtube-2022-09-12-makemore-2-mlp]] @1:10:30).

## Seen in
- [[youtube-2022-09-12-makemore-2-mlp]]
- [[makemore]]
