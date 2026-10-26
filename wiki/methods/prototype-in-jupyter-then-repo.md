---
type: method
steps:
  - Read the PyTorch docs for what shapes each layer takes
  - Prototype layers in a Jupyter notebook until the shapes work
  - Paste the working code into the training repo in VS Code
  - Kick off experiments from the repo
  - Build an evaluation harness before tuning
sources: ["[[youtube-2022-11-21-makemore-5-wavenet]]", "[[youtube-2024-06-09-reproduce-gpt-2]]"]
aliases: [Jupyter to VS Code workflow, experimental harness, evaluation harness, experiment harness]
---
# Prototype in Jupyter, then move to the repo
How he says he develops deep-learning code, presented at the end of the WaveNet lecture as roughly representative of the development process of building neural networks ([[youtube-2022-11-21-makemore-5-wavenet]] @52:15, @53:57).

## Steps
1. **Read the docs for shapes.** He spends a lot of time in PyTorch documentation reading what shapes each layer accepts and what it does ([[youtube-2022-11-21-makemore-5-wavenet]] @52:15).
2. **Prototype in Jupyter.** He prototypes layers and implementations in Jupyter notebooks, making sure all the shapes work out ([[youtube-2022-11-21-makemore-5-wavenet]] @53:24).
3. **Paste into the repo.** Once satisfied with the functionality, he copy-pastes the code into the repository of actual training code, working in VS Code alongside the notebook ([[youtube-2022-11-21-makemore-5-wavenet]] @53:24, @53:57).
4. **Kick off experiments from the repo.** Experiments are launched from the code repository, not the notebook ([[youtube-2022-11-21-makemore-5-wavenet]] @53:57).
5. **Have a harness.** As experiments take longer he is in the dark about hyperparameters and learning rates, and says they are missing an experimental harness to run many experiments and tune the architecture; without one they are guessing and checking, which he does not want to be the focus ([[youtube-2022-11-21-makemore-5-wavenet]] @46:42). A typical workflow, he says, sets up an evaluation harness, scripts with many arguments, lots of kicked-off experiments, plots of training and validation losses, population-level analysis and hyperparameter searches; none of that was done in the lecture, and how to set one up is a topic for another lecture ([[youtube-2022-11-21-makemore-5-wavenet]] @54:32, @55:06).

**The same split in 2024.** In the GPT-2 lecture he runs Jupyter inside VS Code to keep one interface, and runs `train_gpt2.py` from the terminal on a cloud GPU box that VS Code connects to ([[youtube-2024-06-09-reproduce-gpt-2]] @05:32, @30:18, @1:23:11).

**Note:** [[quick-experiment-loop]] is the harness he later describes around nanochat; the connection is this wiki's, not his ([[youtube-2022-11-21-makemore-5-wavenet]] @54:32).

## Seen in
- [[youtube-2022-11-21-makemore-5-wavenet]]
- [[makemore]]
- [[check-shapes-and-broadcasting]] — the shape discipline step 2 relies on
- [[youtube-2024-06-09-reproduce-gpt-2]]
