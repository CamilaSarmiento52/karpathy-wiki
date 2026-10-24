---
type: method
steps:
  - Start with the most capable model, whatever it costs
  - Squeeze prompting before anything else
  - Get it to work at all, however expensive the flow
  - Consider finetuning only after prompting is exhausted
  - Then make concessions toward cheaper models and shorter prompts
  - Distill the expensive pipeline into a smaller model
sources: ["[[talk-2023-05-25-state-of-gpt]]", "[[talk-2024-03-26-sequoia-making-ai-accessible]]"]
aliases: [performance first, then cost, top performance then optimise cost, go after accuracy first, distill the expensive pipeline]
---
# Make it work, then make it cheap
His recommended order for building with LLMs: achieve top performance first and optimise cost second ([[talk-2023-05-25-state-of-gpt]] @37:12). In the Sequoia interview he describes it as the paradigm a few people he talked to say works for them, then gives it as his own suggestion: get it to work as well as possible no matter what, then make it cheaper ([[talk-2024-03-26-sequoia-making-ai-accessible]] @29:28, @30:01).

## Steps
1. **Most capable model first.** Start with GPT-4, the most capable model by far ([[talk-2023-05-25-state-of-gpt]] @37:12); start with the most capable model regardless of cost ([[talk-2024-03-26-sequoia-making-ai-accessible]] @28:56).
2. **Squeeze the prompt.** Write very detailed prompts, retrieve and add relevant context, show few-shot examples, offload hard tasks to tools, and think in chains and multiple samples ([[talk-2023-05-25-state-of-gpt]] @37:12, @37:44, @38:17).
3. **Make it work at all.** Even if that takes ten or twenty prompts and picking the best, or some debate flow ([[talk-2024-03-26-sequoia-making-ai-accessible]] @29:28, @30:01).
4. **Finetune only after that.** Consider finetuning only once prompting is squeezed, with RLHF a fragile research zone ([[talk-2023-05-25-state-of-gpt]] @38:17).
5. **Then concessions.** Cut cost with lower-capacity models or shorter prompts ([[talk-2023-05-25-state-of-gpt]] @38:51); check which kinds of queries can fall back to GPT-3.5 ([[talk-2024-03-26-sequoia-making-ai-accessible]] @29:28).
6. **Distill.** Run the expensive pipeline over a large distribution of problems to get labels, then finetune a smaller, cheaper model on them ([[talk-2024-03-26-sequoia-making-ai-accessible]] @30:01).

## Seen in
- [[talk-2023-05-25-state-of-gpt]]
- [[talk-2024-03-26-sequoia-making-ai-accessible]]
- [[prompting-llms]] — the prompting half of step 2
