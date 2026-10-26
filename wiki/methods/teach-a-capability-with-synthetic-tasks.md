---
type: method
steps:
  - Write a task that generates conversations with the correct answer attached
  - Randomise the user prompt, including other languages
  - Write the answer as a manual attempt, then a tool check
  - Format the answer around the tokenizer
  - Break the problem into its implicit steps with explicit state
  - Add a simpler sub-task for the part the model gets wrong
  - Improve later with mistakes, RL, more entropy and a data engine
sources: ["[[github-2025-10-24-nanochat-strawberry-guide]]"]
aliases: [add a capability to nanochat, SpellingBee, SimpleSpelling, synthetic task, data engine, how to add abilities]
---
# Teach a capability with synthetic tasks
How he adds a new ability to nanochat, shown on teaching d32 to count the r's in "strawberry", which he offers as a cute example of how any arbitrary computing capability can be added ([[github-2025-10-24-nanochat-strawberry-guide]] §intro). As usual, he says, it is done through synthetic data generation during midtraining and SFT ([[github-2025-10-24-nanochat-strawberry-guide]] §intro).

## Steps
1. **Write a task.** A new task under `tasks/`, `SpellingBee`, generates synthetic two-turn conversations, the user asking and the assistant answering in a set style, with the intended correct solution attached for nanochat to imitate when finetuned on them ([[github-2025-10-24-nanochat-strawberry-guide]] §intro).
2. **Randomise the prompt.** The user prompts are "fudged" randomly from a list of templates, with a few other languages at the bottom so the task is triggered even when asked in another language; he calls this important as a data augmentation, so the skill can be evoked however the user asks ([[github-2025-10-24-nanochat-strawberry-guide]] §Entropy).
3. **Give the answer a reasoning shape.** The answer tries a manual approach and then double-checks with the Python interpreter tool ([[github-2025-10-24-nanochat-strawberry-guide]] §Reasoning structure). Because every generated instance is clean, the two always agree, so for now he calls it "smoke and mirrors"; it sets up a schema of problem solving and habituates the network to it, and he says nanochat might transfer-learn it if many tasks share it ([[github-2025-10-24-nanochat-strawberry-guide]] §Reasoning structure).
4. **Format around the tokenizer.** He wraps the word in single quotes, which the tokenizer's regex guarantees is a token boundary, and spells it with commas and no space after ":", so each letter becomes its own token ([[github-2025-10-24-nanochat-strawberry-guide]] §Spelling). The reasons are on [[tokenization]] ([[github-2025-10-24-nanochat-strawberry-guide]] §Spelling).
5. **Spell out every implicit step.** The answer breaks the problem into all its implicit calculations, with an explicit running count the model can attend back to and add one, so no single token carries too much computation ([[github-2025-10-24-nanochat-strawberry-guide]] §Counting).
6. **Drill the weak part.** Playing with early versions he saw the model often got the spelling wrong, so he added `SimpleSpelling`, which only asks the model to spell, a very token-efficient way to learn it, and mixed it into training so the harder part gets more loss ([[github-2025-10-24-nanochat-strawberry-guide]] §Spelling).
7. **Improve later.** He lists simulating small mistakes and recoveries in SFT, RL on the task as nanochat already does for GSM8K, the task deeper in a conversation, more entropy in user and assistant messages, and a round of "data engine" that finds words nanochat cannot spell and mixes them into `SimpleSpelling` ([[github-2025-10-24-nanochat-strawberry-guide]] §Reasoning structure, §Summary). In practice, he says, you usually want both imitation and RL: reasoning shown in SFT as a "prior", then RL to string it together for reward ([[github-2025-10-24-nanochat-strawberry-guide]] §Reasoning structure).

The d32 deployed on nanochat.karpathy.ai can now count letters, he says ([[github-2025-10-24-nanochat-strawberry-guide]] §Summary).

## Seen in
- [[github-2025-10-24-nanochat-strawberry-guide]]
- [[nanochat]] — where the tasks live
- [[tokenization]] — why the formatting matters
- [[transformers-need-tokens-to-think]] — why each step is kept small
- [[synthetic-data-is-the-future-if-you-keep-its-entropy]] — **Note:** step 2 adds entropy on purpose
- [[rl-lets-models-discover-their-own-thinking-strategies]] — **Note:** step 7's prior-then-RL
