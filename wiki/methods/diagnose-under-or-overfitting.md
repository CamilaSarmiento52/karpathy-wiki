---
type: method
steps:
  - Overfit a handful of examples first
  - Train on the train split only
  - Compare train and dev loss
  - If roughly equal, scale the model up
  - If dev departs above train, overfitting has begun
  - Evaluate the test split once at the end
  - Match parameter counts before comparing architectures
  - Check for bugs before reading a null result
sources: ["[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2022-11-21-makemore-5-wavenet]]", "[[youtube-2024-06-09-reproduce-gpt-2]]"]
aliases: [overfit a single batch, compare train and dev loss, reading train vs dev loss, control for parameter count, parameter-matched comparison]
---
# Diagnose under- or overfitting
How he reads whether a model is too small or memorising: note that a few dozen examples are overfit to a very low loss, then compare the loss on the train and dev splits ([[youtube-2022-09-12-makemore-2-mlp]] @39:23, @1:00:20).

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

10. **Read the gap before scaling.** In the WaveNet lecture, train 2.05 against validation 2.10 means little overfitting, so he scales the network up ([[youtube-2022-11-21-makemore-5-wavenet]] @17:09).
11. **Match parameter counts.** When comparing a new architecture against the old one, he picks the hidden size so that total parameters match: 68 hidden units gives 22,000 parameters, the same as before, so the question is whether the parameters are used more efficiently rather than whether a bigger model does better ([[youtube-2022-11-21-makemore-5-wavenet]] @37:15, @37:47).
12. **Clean run.** He removes debugging cells and reruns the optimisation before reading the result ([[youtube-2022-11-21-makemore-5-wavenet]] @37:47).
13. **Suspect bugs before concluding.** Before reading the null result (2.029 against 2.027), he notes the architecture has not been tuned and that BatchNorm might still have a bug, which it did ([[youtube-2022-11-21-makemore-5-wavenet]] @38:20, @45:01).
14. **Watch both losses.** He admits to looking only at training loss and says normally you watch training and validation together ([[youtube-2022-11-21-makemore-5-wavenet]] @46:42, @47:13).

Step 2 again at GPT-2 scale: before real training he overfits a single 4 × 32 batch until the loss is very low, showing that the Transformer can memorise it ([[youtube-2024-06-09-reproduce-gpt-2]] @1:00:42, @1:01:14).

## Seen in
- [[youtube-2022-11-21-makemore-5-wavenet]]
- [[youtube-2022-09-12-makemore-2-mlp]]
- [[makemore]]
- [[youtube-2024-06-09-reproduce-gpt-2]]
