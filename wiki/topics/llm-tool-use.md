---
type: topic
aliases: [Tool use, LLM tool use, tools and plugins, retrieval, retrieval-augmented generation, RAG, browsing, code interpreter, calculator, vector store, multimodality, customization, GPTs]
first_seen: 2023-05-25
last_updated: 2023-11-23
sources: ["[[talk-2023-05-25-state-of-gpt]]", "[[youtube-2023-11-23-intro-to-llms]]"]
context: ["[[talk-2024-09-05-no-priors-ep-80]]"]
related: ["[[prompting-llms]]", "[[llms-as-operating-systems]]", "[[no-rag-needed-for-a-small-wiki]]"]
---
# LLM tool use
Giving an LLM tools such as calculators, code interpreters and search, as people lean on tools for what they are bad at, and filling its context window with retrieved information ([[talk-2023-05-25-state-of-gpt]] @31:41, @32:15, @32:48).

## What he says
**Tools (State of GPT, 2023).** Since models may not know what they don't know, he suggests telling them in the prompt that they are not very good at mental arithmetic and spelling out how to call the calculator ([[talk-2023-05-25-state-of-gpt]] @32:15, @32:48). In ReAct-style prompting the model's actions in its thought–action–observation rollout can include tool use ([[talk-2023-05-25-state-of-gpt]] @28:54, @29:28).

**Retrieval.** He says the pendulum swung from retrieval-only systems to memory-only LLMs, and the retrieval-augmented space in between works extremely well in practice ([[talk-2023-05-25-state-of-gpt]] @32:48). The context window is the Transformer's working memory, and loading it with information relevant to the task makes it work extremely well ([[talk-2023-05-25-state-of-gpt]] @32:48, @33:21). The emerging recipe is to chunk documents, embed them, store the vectors, and at test time query and stuff relevant chunks into the prompt; LlamaIndex is his data-connector example ([[talk-2023-05-25-state-of-gpt]] @33:21, @33:53). He likens it to people looking things up in a textbook or documentation rather than relying on memory ([[talk-2023-05-25-state-of-gpt]] @33:53, @34:27).

**Tools in ChatGPT (Intro to LLMs, November 2023).** Finetuning teaches ChatGPT that some queries call for tools rather than a direct answer; it emits special words that trigger, for example, a search, and the results are fed back as text ([[youtube-2023-11-23-intro-to-llms]] @27:43, @28:18, @28:49). His demo on Scale AI's funding rounds uses the browser to find them, a calculator to impute missing valuations because, like people, the model is not good at math in its head, Python with matplotlib to plot, and DALL-E to make an image ([[youtube-2023-11-23-intro-to-llms]] @28:49, @29:53, @30:25, @31:00, @32:40). Tool use ties existing computing infrastructure together with words; it is not just working in its head and sampling words, and people solve problems with tools in the same way ([[youtube-2023-11-23-intro-to-llms]] @32:07, @33:12). The valuation extrapolation in that demo is ChatGPT's fitted trend line, which he congratulates the team on in jest, not his estimate ([[youtube-2023-11-23-intro-to-llms]] @31:00, @31:34).

**Multimodality and customization.** He calls multimodality a major axis: seeing images, as when Greg Brockman's pencil sketch of a joke website is turned into working HTML and JavaScript, generating them, and hearing and speaking in speech-to-speech mode ([[youtube-2023-11-23-intro-to-llms]] @33:12, @33:45, @34:19). Customization is another: OpenAI's GPTs app store allows custom instructions and uploaded files, which ChatGPT references through retrieval-augmented generation, like browsing your files, and future customization might include finetuning ([[youtube-2023-11-23-intro-to-llms]] @40:27, @41:00, @41:32). The aim is many expert models for specific tasks rather than one model for everything ([[youtube-2023-11-23-intro-to-llms]] @42:06).

**The cognitive core (No Priors, 2024-09-05).** He describes a small cognitive core as a thing that thinks and, when it needs information, knows how to use tools to look it up; see [[a-cognitive-core-could-be-a-billion-parameters-or-less]] ([[talk-2024-09-05-no-priors-ep-80]] @27:27).

## Related
- [[prompting-llms]] — tools as one of his prompting recommendations
- [[llms-as-operating-systems]] — tools as resources the kernel coordinates
- [[no-rag-needed-for-a-small-wiki]] — **Note:** a different scale and claim (a ~100-article wiki); not a contradiction
