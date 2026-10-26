---
type: topic
aliases: [LLM security, jailbreak, jailbreaks, prompt injection, data poisoning, backdoor attack, sleeper agent attack, adversarial suffix]
first_seen: 2023-11-23
last_updated: 2023-11-23
sources: ["[[youtube-2023-11-23-intro-to-llms]]"]
context: ["[[talk-2023-05-25-state-of-gpt]]"]
related: ["[[llms-as-operating-systems]]", "[[jagged-intelligence]]"]
---
# LLM security
In his framing, just as the original operating-system stack had security challenges, the LLM computing paradigm brings new ones specific to language models: jailbreaks, prompt injection and data poisoning ([[youtube-2023-11-23-intro-to-llms]] @45:25, @45:59).

## What he says
**Jailbreaks.** Role-play, such as asking ChatGPT to act as a deceased grandmother who used to explain how to make napalm, gets it past its refusal ([[youtube-2023-11-23-intro-to-llms]] @45:59, @46:33, @47:06). Base64-encoded queries jailbreak Claude because the refusal training data is mostly English, so it learns to refuse harmful queries mostly in English; multilingual data helps, but there are many encodings to cover ([[youtube-2023-11-23-intro-to-llms]] @47:38, @48:10, @48:44, @49:17). He reports a paper's universal transferable suffix, found by optimisation, that jailbreaks models; adding it to training does not help because the optimisation can be rerun to find another ([[youtube-2023-11-23-intro-to-llms]] @49:17, @49:50, @50:22). An image of a panda with optimised noise jailbreaks a vision model, so the new ability to see images is also a new attack surface ([[youtube-2023-11-23-intro-to-llms]] @50:22, @50:55).

**Prompt injection.** Prompt injection hijacks the model with what look like new instructions ([[youtube-2023-11-23-intro-to-llms]] @51:27, @51:59). His examples are faint text in an image, a web page retrieved by Bing that inserts a fraud link, and a shared Google Doc that makes Bard exfiltrate personal data through image URLs or, once Google's content security policy blocked that, through Apps Script into an attacker's Google Doc ([[youtube-2023-11-23-intro-to-llms]] @51:59, @52:32, @53:05, @53:37, @54:10, @54:45, @55:20, @55:54). He says he does not know exactly what Apps Script is ([[youtube-2023-11-23-intro-to-llms]] @55:20).

**Data poisoning.** In a backdoor or "sleeper agent" attack, a trigger phrase planted in training data, such as "James Bond", corrupts the model's outputs; he notes the paper showed it for finetuning, that he is not aware of a convincing pretraining demonstration, and that it is possible in principle ([[youtube-2023-11-23-intro-to-llms]] @56:28, @57:00, @57:32, @58:06).

Many of these attacks have published defenses and may no longer work; he calls it the cat-and-mouse game of traditional security, now in LLM security, a new and rapidly evolving field ([[youtube-2023-11-23-intro-to-llms]] @58:40, @59:11). In State of GPT (published 2023-05-25) he had also listed prompt injection, jailbreaks and data poisoning among the limitations that keep LLMs to low-stakes uses ([[talk-2023-05-25-state-of-gpt]] @39:24).

## Claims
- [[use-llms-as-copilots-with-human-oversight]] — security attacks among the reasons for human oversight

## Related
- [[llms-as-operating-systems]] — the computing stack these attacks target
- [[jagged-intelligence]] — the 2025 gullibility point
