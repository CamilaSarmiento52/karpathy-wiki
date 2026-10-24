---
type: topic
aliases: [Sampling, sampling from a language model, temperature, top-p, autoregressive sampling, autoregressive generation, diffusion, nucleus sampling, top-k]
first_seen: 2023-05-19
last_updated: 2024-06-09
sources: ["[[talk-2023-05-19-stanford-cs25-transformers]]", "[[youtube-2023-11-23-intro-to-llms]]", "[[talk-2024-03-26-sequoia-making-ai-accessible]]", "[[github-2024-05-29-llama2c-readme]]", "[[youtube-2024-06-09-reproduce-gpt-2]]"]
related: ["[[character-level-language-modeling]]", "[[he-does-not-love-autoregressive-sampling]]"]
---
# Sampling from language models
Generating from an autoregressive model, as he walks through it for nanoGPT, means starting from a start token, sampling the next element from the predicted distribution, feeding it back in, and repeating ([[talk-2023-05-19-stanford-cs25-transformers]] @41:34, @42:06).

## What he says
In the CS25 lecture he generates "infinite Shakespeare" from a model with block size eight: start with a token such as a newline, get the distribution for the first character, decode it, re-encode it as an integer and feed it back with its positional encoding, and keep going ([[talk-2023-05-19-stanford-cs25-transformers]] @41:34, @42:06). Once the context reaches the block size the model was trained on, it must be cropped, because the model can never take more than eight positions ([[talk-2023-05-19-stanford-cs25-transformers]] @42:06).

Asked about the autoregressive approach, he says he does not love it: sampling a token and committing to it seems weird to him, and he would find hybrids with diffusion, or ways to edit sequences later, really cool ([[talk-2023-05-19-stanford-cs25-transformers]] @50:15). He finds diffusion, an up-and-coming modeling approach, much more appealing, because when he writes he does a first draft and then a better second draft rather than committing chunk by chunk ([[talk-2023-05-19-stanford-cs25-transformers]] @50:15, @50:48).

In Intro to LLMs he describes the same loop at scale: sample a word, feed it back in, and the network "dreams" internet documents such as Java code, a product page or a Wikipedia-like article, filling the right form with knowledge that may be memorized or hallucinated ([[youtube-2023-11-23-intro-to-llms]] @08:50, @09:25, @10:30, @11:02).

In the Sequoia interview he finds it odd that diffusion and autoregressive models sit as two separate, extremely good points in model space with nothing in between, and thinks a hybrid or unification is probably possible ([[talk-2024-03-26-sequoia-making-ai-accessible]] @12:22, @12:55).

**Temperature and top-p (llama2.c).** For about the best results he recommends sampling at temperature 1.0 with top-p 0.9, both llama2.c's defaults ([[github-2024-05-29-llama2c-readme]] §feel the magic). Intuitively, he says, top-p keeps tokens with tiny probabilities from being sampled, so you cannot get "unlucky" and are less likely to go "off the rails" afterwards ([[github-2024-05-29-llama2c-readme]] §feel the magic). To control diversity, vary either the temperature with top-p off or top-p with temperature at 1, but not both ([[github-2024-05-29-llama2c-readme]] §feel the magic).

**Top-k in the GPT-2 lecture (2024-06-09).** His sampling loop takes only the last position's logits, applies softmax and then top-k with k = 50, the Hugging Face pipeline default, which keeps the model from sampling rare tokens and going off the rails ([[youtube-2024-06-09-reproduce-gpt-2]] @37:39, @38:13, @38:45). His samples did not match the pipeline's; replicating his loop on the Hugging Face model gave his results, so he concludes his model is correct and the pipeline does something extra ([[youtube-2024-06-09-reproduce-gpt-2]] @40:26, @40:59).

## Claims
- [[he-does-not-love-autoregressive-sampling]]

## Related
- [[llama2c]] — the `-t` and `-p` sampling flags
- [[character-level-language-modeling]] — his bigram and MLP sampling loops with `torch.multinomial`
- [[transformer-architecture]] — the decoder whose mask makes this sampling possible
