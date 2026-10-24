---
type: claim
stated_on: 2024-05-29
confidence: stated
sources: ["[[github-2024-05-29-llama2c-readme]]"]
supports: ["[[a-cognitive-core-could-be-a-billion-parameters-or-less]]"]
context: ["[[talk-2024-09-05-no-priors-ep-80]]"]
topic: "[[scaling-laws]]"
---
# Very small LLMs can perform surprisingly well if the domain is narrow enough
> "very small LLMs can have surprisingly strong performance" — [[github-2024-05-29-llama2c-readme]] §intro

## Context
Introducing llama2.c, he says you might think you need LLMs of many billions of parameters to do anything useful, but very small ones can be surprisingly strong if you make the domain narrow enough, and he cites the TinyStories paper as the reference ([[github-2024-05-29-llama2c-readme]] §intro). The repo's own models are a TinyStories series of 260K to 110M parameters; the 15M model runs at about 110 tokens/s on his laptop and the 42M samples more coherent stories ([[github-2024-05-29-llama2c-readme]] §feel the magic, §models). **Note:** the claim is conditional on a narrow domain; he does not say small models are strong in general ([[github-2024-05-29-llama2c-readme]] §intro).

In the contributing section he adds a prediction, introduced with "I think": a lot of interest in training or finetuning custom micro-LLMs, about 100M to 1B parameters and up to about 10B, across many applications, deployed in edge-adjacent environments such as MCUs, phones, web browsers and laptops; he wants llama2.c to be the simplest, most hackable repo for that workflow ([[github-2024-05-29-llama2c-readme]] §contributing).

## Related claims
- Supported by [[a-cognitive-core-could-be-a-billion-parameters-or-less]]: here small models are strong in a narrow domain and he expects micro-LLMs of about 100M to 1B parameters ([[github-2024-05-29-llama2c-readme]] §intro, §contributing); in the No Priors interview (published 2024-09-05) he expects a general cognitive core of about a billion parameters or fewer that uses tools for knowledge ([[talk-2024-09-05-no-priors-ep-80]] @27:27, @28:36). Related but different ideas, so support rather than extension.
