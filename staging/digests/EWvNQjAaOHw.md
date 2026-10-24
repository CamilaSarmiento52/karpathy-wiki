# Digest: How I use LLMs
- raw: raw/youtube/EWvNQjAaOHw.md · published: 2025-02-27 · medium: youtube · words: ~25,500 (2:11:12)
- source slug: youtube-2025-02-27-how-i-use-llms

## Source page

```
---
type: source
raw_path: raw/youtube/EWvNQjAaOHw.md
published: 2025-02-27
medium: youtube
summary: "A practical, general-audience tour of LLM apps as he uses them: the chat as a token window, model tiers, thinking models, search, deep research, file uploads, the Python interpreter, Claude artifacts, Cursor, voice, images, video, memory, custom instructions and custom GPTs."
url: https://www.youtube.com/watch?v=EWvNQjAaOHw
title: "How I use LLMs"
---
# How I use LLMs
Raw: [[raw/youtube/EWvNQjAaOHw]] · Original: https://www.youtube.com/watch?v=EWvNQjAaOHw

## Summary
A follow-up in his general-audience series that moves from how LLMs are trained to how he uses the apps, with examples from his own life (@00:00). He describes the ecosystem of ChatGPT and its competitors, then frames a chat as user and model writing into one token sequence, the context window, which "new chat" wipes, and the model itself as a lossy, slightly out-of-date "zip file" of the internet with a post-trained assistant persona (@01:08, @06:15, @06:48, @07:55, @10:41, @12:20). He advises starting a new chat per topic, knowing which model and pricing tier you are on, and trying a non-thinking model before switching to a thinking model for hard math and code (@16:14, @20:07, @29:41). Most of the video tours tools: internet search for recent or niche facts, deep research, file uploads for reading papers and books, the Python interpreter and Advanced Data Analysis, Claude artifacts and diagrams, and Cursor's Composer, where he names vibe coding (@31:20, @39:03, @42:26, @51:13, @55:03, @59:02, @1:04:39, @1:09:07, @1:14:07, @1:18:01). He then covers modalities (voice input and output, "true" audio, NotebookLM podcasts, images in and out, video) and quality-of-life features (memory, custom instructions, custom GPTs as saved few-shot prompts), and closes with a summary of what to keep track of across apps (@1:23:04, @1:27:32, @1:37:06, @1:40:30, @1:53:21, @1:58:48, @2:07:46). Throughout he cautions that outputs can be hallucinated and should be checked against sources, citations and code (@13:58, @48:26, @1:06:19).

## Key points
- 2025 has a rich ecosystem of ChatGPT-like apps; ChatGPT is the incumbent and most feature-rich; leaderboards help track them → [[ai-ecosystem]], [[chatgpt-is-a-very-good-default-llm-app]]
- A chat is a one-dimensional token sequence both sides write into; the context window is working memory → [[tokenization]]
- The model is a lossy, probabilistic zip file of the internet with an assistant persona from post-training, and a knowledge cutoff → [[pretraining-and-finetuning]]
- Ask it directly only about common, non-recent knowledge, and check primary sources → [[ask-the-model-directly-for-common-non-recent-knowledge]], [[verify-citations]]
- Start a new chat when you switch topics: extra tokens distract the model and cost a little more → [[start-a-new-chat-when-switching-topics]]
- Know which model and tier you are using; use the most powerful model that works for you; he asks several LLMs the same question → [[choose-a-model-tier]], [[use-the-most-powerful-model-that-works-for-you]], [[he-asks-several-llms-the-same-question]]
- Thinking models, tuned with RL, help on hard math and code; try a non-thinking model first → [[system-1-and-system-2-thinking]], [[try-a-non-thinking-model-first]]
- Search for recent, changing or niche information; deep research as a long search-plus-thinking report to treat as a first draft → [[llm-tool-use]], [[use-search-for-recent-or-niche-information]], [[treat-deep-research-reports-as-a-first-draft]]
- Upload papers and book chapters into the context and read them with the LLM → [[read-with-an-llm]], [[dont-read-books-alone]]
- The Python interpreter and Advanced Data Analysis act like a junior data analyst whose code you must read → [[llm-tool-use]], [[llm-code-tools-need-a-user-who-can-verify-the-code]]
- Claude artifacts write small custom apps and diagrams that render in the chat → [[llm-gui]]
- For professional coding he uses Cursor rather than a chat web page; Composer is an agent on the codebase, and giving it control is vibe coding → [[partial-autonomy-apps]], [[vibe-coding]], [[chat-web-apps-are-too-slow-for-his-professional-coding]]
- Different LLMs have different tools; without a code tool they may hallucinate arithmetic → [[keep-track-of-which-tools-each-llm-has]]
- Use voice input; about half his queries are spoken → [[voice-input]], [[use-voice-instead-of-typing]]
- Audio and images can be tokenized and modelled natively, unlike speech-to-text "fake audio" → [[llm-tool-use]], [[tokenization]]
- Custom GPTs save a few-shot prompt; few-shot examples always increase accuracy in his experience → [[prompting-llms]], [[few-shot-examples-increase-accuracy-in-his-experience]]

## Fed pages
- [[ai-ecosystem]]
- [[tokenization]]
- [[pretraining-and-finetuning]]
- [[system-1-and-system-2-thinking]]
- [[llm-tool-use]]
- [[prompting-llms]]
- [[partial-autonomy-apps]]
- [[llm-gui]]
- [[vibe-coding]]
- [[sampling-from-language-models]]
- [[choose-a-model-tier]]
- [[start-a-new-chat-per-topic]]
- [[verify-citations]]
- [[read-with-an-llm]]
- [[voice-input]]
- [[ask-the-model-directly-for-common-non-recent-knowledge]]
- [[start-a-new-chat-when-switching-topics]]
- [[use-the-most-powerful-model-that-works-for-you]]
- [[he-asks-several-llms-the-same-question]]
- [[try-a-non-thinking-model-first]]
- [[use-search-for-recent-or-niche-information]]
- [[treat-deep-research-reports-as-a-first-draft]]
- [[dont-read-books-alone]]
- [[llm-code-tools-need-a-user-who-can-verify-the-code]]
- [[chat-web-apps-are-too-slow-for-his-professional-coding]]
- [[keep-track-of-which-tools-each-llm-has]]
- [[use-voice-instead-of-typing]]
- [[few-shot-examples-increase-accuracy-in-his-experience]]
- [[chatgpt-is-a-very-good-default-llm-app]]
- [[use-llms-as-copilots-with-human-oversight]]
- [[transformers-need-tokens-to-think]]
- [[pretraining-is-lossy-compression-of-the-internet]]
```

## Candidates

### topic: ai-ecosystem
- existing: yes
- aliases: add "LLM apps", "LLM providers", "chatbot arena", "leaderboards"
- statements:
  - He calls ChatGPT the "Original Gangster" incumbent, most popular and most feature-rich because it has been around longest, with clones that sometimes offer unique experiences (@01:08).
  - He lists Gemini, Meta AI and Copilot from Google, Meta and Microsoft, Claude from Anthropic, Grok from xAI, DeepSeek (Chinese) and Le Chat from Mistral (French) (@01:08, @01:42).
  - To keep track of them he points to Chatbot Arena's ELO rankings and Scale's SEAL leaderboard (@01:42, @02:16).
  - In summary he calls it a rapidly growing, shifting ecosystem in which other apps reach feature parity or overtake ChatGPT in specific cases (@2:06:40).
  - He names his per-task picks: Perplexity for search, Claude artifacts for prototyping web apps and diagrams, ChatGPT advanced voice for talking, Grok when ChatGPT is too cagey (@2:07:13).

### topic: tokenization
- existing: yes
- aliases: add "context window", "token window", "conversation format"
- statements:
  - Under the hood, the query and the response are chopped into tokens; Tiktokenizer shows his haiku request as 15 tokens from a vocabulary of roughly 200,000 for GPT-4o (@03:57).
  - A conversation adds special tokens marking where user and assistant messages begin and end; the two chat bubbles came to 42 tokens (@05:05, @05:40, @06:15).
  - User and model take turns writing into one one-dimensional token stream, the context window, which he calls the working memory of the conversation; "new chat" resets it to zero (@06:48, @07:21).
  - Audio can be chunked into tokens by quantizing small spectrogram windows into a vocabulary of, say, 100,000 audio chunks; images by quantizing patches of a grid (@1:28:08, @1:40:30).
  - The Transformer does not know which tokens are text, audio or images; only the encoder and decoder do (@1:41:03, @1:41:36).

### topic: pretraining-and-finetuning
- existing: yes
- statements:
  - He describes pretraining as compressing the internet into a lossy, probabilistic zip file, about one terabyte for roughly one trillion parameters, that predicts the next token on internet documents (@07:55, @08:28, @09:00).
  - Pretraining costs tens of millions of dollars and months, so it is done rarely and models have a knowledge cutoff (@09:33, @10:09).
  - Post-training is "attaching a smiley face" to the zip file by swapping in human-built conversation data so it takes on an assistant persona (@10:41).
  - Reinforcement learning is a third stage in which the model practises on math and code problems and discovers thinking strategies that are hard for a labeler to hardcode (@22:56, @23:28).
  - His summary introduction for ChatGPT: a one-terabyte zip file whose knowledge comes from reading the internet about six months ago and whose personality was programmed by example by human labelers (@12:20).
  - Things mentioned often on the internet are remembered better than rare things (@12:52).

### topic: system-1-and-system-2-thinking
- existing: yes
- aliases: add "thinking models", "reasoning models"
- statements:
  - Thinking models are additionally tuned with RL; they think longer, sometimes for minutes, and give higher accuracy on hard math and code, while simple questions may not benefit (@24:36, @25:12).
  - He calls this RL stage relatively recent, a year or two old, and points to DeepSeek's paper as the first to talk about it publicly (@24:02).
  - His gradient-check bug was not solved by GPT-4o but was solved by o1 pro after a minute of thinking; Claude 3.5 Sonnet, Gemini and Grok 3 also solved it, Sonnet without thinking (@25:44, @27:25, @28:00).
  - He likes Perplexity for hosting DeepSeek R1 because its raw thoughts are visible (@28:35, @29:08).
  - He usually starts with a non-thinking model for speed and switches to a thinking model when he suspects the answer could be better (@29:41, @30:13).

### topic: llm-tool-use
- existing: yes (aliases already include code interpreter, browsing, multimodality, GPTs)
- aliases: add "internet search", "deep research", "file uploads", "Advanced Data Analysis", "Claude artifacts", "memory", "custom instructions", "custom GPTs", "advanced voice mode"
- statements:
  - Without tools the model is a self-contained zip file: no calculator, Python interpreter or web browsing (@11:48).
  - For search, the model emits a special token, the app stops sampling, runs the query, and pastes the pages' text into the context window (@32:24, @32:57).
  - Search is needed for things like a TV episode's release date that were decided after the model was trained (@33:31, @34:04).
  - Some models decide to search by themselves; sometimes you are better off telling it to; in his tests in the video Claude and Gemini 2.0 Pro lacked search (@35:44, @36:50, @37:56, @38:29).
  - Deep research combines internet search and thinking over tens of minutes and returns something like a custom research paper with citations; he found ChatGPT's the most thorough, Perplexity's and Grok's shorter (@42:26, @46:44, @47:53).
  - File uploads put documents such as a PDF into the context window; he thinks the PDF is probably converted to text and images may be discarded (@51:13, @52:50, @53:22).
  - With the Python interpreter the model writes a program, special tokens make the app run it, and the result comes back as text; OpenAI taught ChatGPT by example when to use tools (@59:02, @1:01:16, @1:01:51).
  - ChatGPT answers 30 × 9 from memory, but uses the interpreter for a large multiplication (@1:00:07, @1:00:40).
  - Advanced Data Analysis acts like a junior data analyst: in his OpenAI-valuation example it silently put 0.1 for an unknown 2015 value and misreported a 2030 extrapolation (@1:04:39, @1:05:46, @1:06:53, @1:07:27).
  - ChatGPT's memory is a database of text strings about the user, prepended to every conversation; he is "coming around" to it (@1:55:35, @1:56:08, @1:56:39).
  - Custom instructions change ChatGPT's behaviour globally; he told it to be educational and set a Korean formality level (@1:57:12, @1:57:44).
  - "Fake audio" pipes speech through speech-to-text and text-to-speech; advanced voice mode handles audio tokens natively in the model (@1:27:32, @1:28:40, @1:29:14).
  - Image generation in ChatGPT then (DALL-E 3) wrote a caption sent to a separate image model, stitched together rather than native (@1:48:16, @1:48:50).
  - Models that handle modalities natively ("omni" or multimodal) are more powerful than ones that tack on a separate model through text (@2:09:23, @2:09:58).
- relation: possibly a new topic `multimodality` (audio tokens, image patches, true vs fake audio, video as frames); batch 2 folded multimodality into llm-tool-use as an alias. Merge decides.

### topic: prompting-llms
- existing: yes
- aliases: add "custom GPTs", "XML tags in prompts"
- statements:
  - A custom GPT is just a saved prompt; nothing special happens beyond prompting, and it saves you retyping a prompt you reuse (@1:59:23, @2:00:31, @2:01:06).
  - He gives LLMs a description plus concrete examples, a few-shot prompt rather than a zero-shot one (@1:59:58, @2:00:31).
  - For longer examples he uses XML-like tags so the model sees where each example begins and ends (@2:03:17, @2:03:49).
  - He compares this to teaching a human: showing by example works much better than explaining in words (@2:03:49).
  - His Korean custom GPTs: a vocabulary extractor that outputs Anki-ready lines, a detailed translator, and one that OCRs, translates and breaks down screenshots of subtitles (@1:58:48, @2:02:11, @2:04:21, @2:04:55).

### topic: partial-autonomy-apps
- existing: yes
- statements:
  - For coding he uses an app on his file system, currently Cursor, which calls Claude 3.7 Sonnet through the API and has the context of the files (@1:14:40, @1:15:12, @1:15:47).
  - Cursor's features progressed from Cmd-K (change this line) to Cmd-L (explain this chunk) to Cmd-I, Composer, which with agent integration is an autonomous agent on the codebase that runs commands and edits multiple files (@1:16:51, @1:17:26, @1:18:01).
  - Composer paused and waited for him to confirm commands explicitly (@1:20:46).
- relation: **Note:** these are concrete instances of the autonomy levels this topic describes; merge can link.

### topic: vibe-coding
- existing: yes
- statements:
  - He says the name for giving control to Composer, telling it what to do and hoping it works, is vibe coding, a name he says he "probably minted" (@1:18:01).
  - Worst case, you fall back to ordinary programming because all the files are there to inspect (@1:18:01, @1:21:55).
  - He built a tic-tac-toe app by writing about five sentences; adding confetti and a sound he says he was not keeping full track of the code (@1:16:19, @1:19:40, @1:21:55).

### topic: llm-gui
- existing: yes
- aliases: add "Claude artifacts", "diagrams"
- statements:
  - Claude artifacts write a React app, such as a flashcard app, that runs in the browser inside the chat; he calls this a different paradigm from engineers shipping one app for everyone (@1:09:40, @1:10:15, @1:10:48, @1:11:20).
  - He is not a daily artifacts user; the use he finds useful is conceptual diagrams of book chapters via Mermaid (@1:11:20, @1:11:53, @1:12:26).
  - As a visual thinker he likes laying information out as a tree to see how an argument is arranged (@1:13:33).

### topic: sampling-from-language-models
- existing: yes (weak; merge may drop)
- statements:
  - The model emits a special "I'm done" token, at which point the app hands control back to the user (@07:21).
  - More tokens in the window make sampling the next token slightly slower and more expensive (@17:20).

### method: choose-a-model-tier
- existing: no (related: [[make-it-work-then-make-it-cheap]], which is about building apps, not personal use)
- aliases: model selection, pricing tier, LLM council
- steps:
  - Check which model you are actually on
  - Compare the provider's pricing tiers
  - Pay for the top tier if the work is professional
  - Use the most powerful model that works for you
  - Ask several providers the same question
- statements:
  - Check the model selector; a logged-out user may get a smaller model and OpenAI does not say which (@17:53, @18:26).
  - The free tier's GPT-4o mini is smaller, less creative, knows less and hallucinates more (@19:01).
  - Bigger models cost more to run, so they cost more; decide whether cheaper tiers are enough, and consider top tiers if using them professionally (@20:07).
  - He pays for ChatGPT Pro and Claude's professional plan because for his coding work it is still very cheap (@20:40).
  - Other providers have the same tier structure; pay enough to get e.g. Grok 3 rather than Grok 2 (@20:40, @21:48).
  - He often pays for several and asks them all the same question, his "LLM council" (@22:22).
  - In his summary: large models have more world knowledge and write better; small ones hallucinate more (@2:07:46, @2:08:18).

### method: start-a-new-chat-per-topic
- existing: no
- aliases: keep the context clean, new chat, context window hygiene
- steps:
  - Start a new chat when you switch topic
  - Keep only task-relevant tokens in the window
  - Keep the context as short as you can
- statements:
  - New chat wipes the token window (@06:48, @16:14).
  - Old tokens can distract the model and lower accuracy, and make each next token slightly more expensive (@16:46, @17:20).
  - Keep information that is related to the task (@17:53).
- note: overlaps the claim [[start-a-new-chat-when-switching-topics]]; merge may keep only one of the two.

### method: verify-citations
- existing: no (related: [[verify-against-a-reference-implementation]] is about code parity, different idea)
- aliases: check primary sources, treat it as a first draft, scrutinize the code, transcribe before asking
- steps:
  - Check facts against primary sources
  - Follow the citations to the pages
  - Treat reports as a first draft
  - Read the code it ran
  - Have it transcribe images to text first
- statements:
  - He checked the caffeine figure against primary sources and the NyQuil box's ingredients, because he does not always fully trust the output (@13:58, @15:06).
  - Search answers come with citations you can visit to check for hallucinations (@35:12).
  - Deep research can be hallucinated anywhere, so the citations matter: he reads the papers to see whether the model understood them (@48:26).
  - His US-LLM-labs table missed xAI and included labs it should not have, so he uses it as a first draft (@50:06, @50:39).
  - He reads the code Advanced Data Analysis writes; it hid an assumption and misreported a number (@1:05:46, @1:06:19, @1:06:53).
  - For an image he first asks for a transcription into text so he can check the model read the values correctly, then asks questions (@1:42:10, @1:43:50).
  - For medical results he calls it a first draft and something to discuss with a doctor (@1:44:24, @1:44:58).

### method: read-with-an-llm
- existing: no
- aliases: reading papers with an LLM, reading books with an LLM, don't read books alone
- steps:
  - Get the raw text of the paper or chapter
  - Paste or upload it into the context window
  - Ask for a summary first
  - Read and ask questions as you go
  - Ask for a conceptual diagram of the chapter
- statements:
  - He uploaded the Evo 2 paper and asked for a summary, then asked questions while reading the abstract and introduction (@52:18, @53:22, @54:30).
  - For The Wealth of Nations he copies the chapter from Project Gutenberg into Claude because the model probably does not remember the chapter exactly (@55:37, @56:13, @56:47).
  - He starts with a summary, then reads and asks questions (@57:22).
  - The clunky copy-paste is all he has; he knows of no tool to highlight a passage and ask about it (@58:28).
  - He also asks Claude for a Mermaid conceptual diagram of a chapter (@1:11:53, @1:12:26).
  - NotebookLM can turn uploaded sources into an on-demand podcast, which he uses for niche topics on walks or drives (@1:37:06, @1:37:41, @1:38:46, @1:39:19).

### method: voice-input
- existing: no
- aliases: use voice, speech-to-text, SuperWhisper, dictation
- steps:
  - Use the app's microphone on mobile
  - Bind a system-wide dictation key on desktop
  - Type names that transcribe badly
  - Use read-aloud for output
- statements:
  - On the phone he uses the ChatGPT app's microphone to transcribe (@1:23:36).
  - On his MacBook he uses SuperWhisper, a system-wide transcription app bound to F5 (@1:24:45, @1:25:19).
  - He types product or library names that do not transcribe well (@1:25:53).
  - For output, apps may have read-aloud, or a system-wide text-to-speech app (@1:25:53, @1:26:26, @1:26:59).

### claim: ask-the-model-directly-for-common-non-recent-knowledge
- title: He asks the model directly, without tools, when the knowledge is common and not recent
- confidence: stated
- quote: "you're talking to a zip file" (@11:48)
- statements: the caffeine question is fine because it is not recent and is extremely frequent on the internet (@13:25); the DayQuil/NyQuil example is common, not recent, and not high stakes, and he still checked (@15:39, @16:14).
- relation: supports [[pretraining-is-lossy-compression-of-the-internet]] (2023-11-23): both frame the model's knowledge as a vague, lossy recollection of the internet (@07:55, @12:52 here). Note only if merge wants; same framing, not new evidence.

### claim: start-a-new-chat-when-switching-topics
- title: Start a new chat when you switch topics
- confidence: stated
- quote: "anytime you are switching topic I encourage you to always start a new chat" (@16:14)
- second quote: "think of the tokens in the context window as a precious resource" (@17:20)
- statements: tokens can distract and slightly slow the model (@16:46, @17:20).
- relation: none

### claim: use-the-most-powerful-model-that-works-for-you
- title: Be mindful of which model you are using, and use the most powerful one that works for you
- confidence: stated
- quote: "be mindful of the models that you're using" (@20:07); "use the most powerful model that uh kind of like works for you" (@21:13)
- relation: **Note:** [[make-it-work-then-make-it-cheap]] (2023) also starts from the most capable model, but for building apps; merge may link as related, not supports.

### claim: he-asks-several-llms-the-same-question
- title: He often pays for several LLMs and asks them all the same question
- confidence: stated
- quote: "I kind of refer to all these models as my llm Council" (@22:22)
- statements: the Zermatt travel example with Claude and Gemini (@21:13, @21:48).
- relation: none

### claim: try-a-non-thinking-model-first
- title: He tries a non-thinking model first and switches to a thinking model when the answer could be better
- confidence: stated
- quote: "I usually try out the non-thinking models because their responses are really fast" (@29:41)
- statements: thinking models help most on hard math and code; travel advice does not benefit (@29:41); repeated in his summary (@2:08:18).
- relation: **supports [[transformers-need-tokens-to-think]]** (2023-05-25). There he says the model spends the same compute per token, so reasoning must be spread over more tokens ([[talk-2023-05-25-state-of-gpt]] @22:45, @24:59). Here thinking models emit "tons and tons of tokens" over minutes and get higher accuracy on hard problems (@24:36, @25:12), and a model doing big multiplication "in its head" gets close but wrong (@1:02:58, @1:04:06). Evidence for the same idea; he does not cite the earlier claim himself, so not extends.
- relation (optional, merge decides): extends [[llms-currently-only-have-a-system-1]] (2023-11-23): that claim is dated to November 2023; here he describes RL-trained thinking models as a stage only a year or two old (@24:02). Both can be true; if linked, add to a timeline.

### claim: use-search-for-recent-or-niche-information
- title: He uses search when the answer is recent, changing, or niche
- confidence: stated
- statements: whenever the answer is in the top links of a Google-like search he uses Perplexity, out of habit (@39:03); fresh or changing information (market holiday, Vercel offerings, Apple launch rumours) (@39:36, @40:12); esoteric and possibly changed (Bryan Johnson's toothpaste) (@40:45, @41:17); a gist of something trending (@41:17, @41:52).
- quote: none needed beyond the general ones; merge may reuse "you're talking to a zip file".
- relation: none

### claim: treat-deep-research-reports-as-a-first-draft
- title: Treat deep research reports as a first draft, not as definitely true
- confidence: stated
- quote: "treat this as your first draft treat this as papers to look at" (@48:26)
- statements: any of it can be hallucinated or misunderstood (@48:26); his LLM-labs table was hit and miss (@50:06, @50:39).
- relation: **supports [[use-llms-as-copilots-with-human-oversight]]** (2023-05-25). In 2023 he recommended human oversight and using models as a source of suggestions because they fabricate and hallucinate ([[talk-2023-05-25-state-of-gpt]] @39:24, @39:57). Here he treats reports as drafts he checks against the papers (@48:26) and reads data-analysis code himself (@1:06:19). Same stance, applied to newer tools; not extends, since he adds no new scope.

### claim: llm-code-tools-need-a-user-who-can-verify-the-code
- title: He hesitates to recommend LLM data-analysis tools to people who cannot read and verify the code
- confidence: stated
- quote: "I would always encourage you to scrutinize the code" (@1:05:46); "it is kind of like a very very Junior data analyst" (@1:08:01)
- statements: hesitant to recommend if people cannot read and verify it (@1:06:19); "a lot of promise but be careful" (@1:08:33).
- relation: **supports [[use-llms-as-copilots-with-human-oversight]]** (as above, @39:57 there; @1:06:19 here).

### claim: dont-read-books-alone
- title: Reading with an LLM dramatically increases his retention and understanding
- confidence: stated
- quote: "don't read books alone" (@58:28)
- statements: he rarely reads books by himself any more (@54:30, @55:03); it helps most with other fields or old texts and makes reading more accessible (@57:22, @57:55).
- relation: none

### claim: chat-web-apps-are-too-slow-for-his-professional-coding
- title: He does not use chat web apps for code snippets in professional work; he uses Cursor
- confidence: stated
- statements: most of his time is writing code, but asking ChatGPT for snippets is too slow and lacks context (@1:14:07, @1:14:40).
- relation: none (possible **Note:** link to [[claude-code-is-the-first-convincing-llm-agent]], 2025-12-19, as a later tool; no logical relation asserted)

### claim: keep-track-of-which-tools-each-llm-has
- title: Different LLMs have different tools, and without one they may just hallucinate a result
- confidence: stated
- statements: Grok 3 without an interpreter did a large multiplication in its head and got it slightly wrong; Gemini 2.0 Pro was close but wrong on a harder one (@1:02:24, @1:02:58, @1:03:32, @1:04:06); features differ between web and mobile apps too (@2:10:31).
- relation: none

### claim: use-voice-instead-of-typing
- title: Use voice instead of typing; about half his queries are spoken
- confidence: stated
- quote: "don't type stuff out use voice it works quite well" (@1:26:59)
- statements: he speaks about 50% of his queries overall and about 80% on his phone (@1:23:04); roughly half of his queries, probably a bit more, are audio (@1:26:59).
- relation: none

### claim: few-shot-examples-increase-accuracy-in-his-experience
- title: In his experience, giving LLMs examples always increases accuracy
- confidence: stated
- quote: "I find that this always increases the accuracy of LMS" (@2:00:31)
- relation: supports the few-shot content on [[prompting-llms]] (topic, not a claim). Among claims, none.

### claim: chatgpt-is-a-very-good-default-llm-app
- title: In February 2025 he called ChatGPT a very good default and the most feature-rich incumbent
- confidence: stated
- statements: other apps have strengths in specific cases (@2:06:40, @2:07:13, @2:07:46); he prefers ChatGPT over dedicated translators for Korean (@2:02:44, @2:03:17).
- quote: none clean (caption reads "Chachi by far is a very good default"); paraphrase.
- relation: none

## Quotes
- "you're talking to a zip file" (@11:48)
- "I don't always fully trust what's coming out here" (@15:06)
- "anytime you are switching topic I encourage you to always start a new chat" (@16:14)
- "think of the tokens in the context window as a precious resource" (@17:20)
- "be mindful of the models that you're using" (@20:07)
- "use the most powerful model that uh kind of like works for you" (@21:13)
- "I kind of refer to all these models as my llm Council" (@22:22)
- "I usually try out the non-thinking models because their responses are really fast" (@29:41)
- "treat this as your first draft treat this as papers to look at" (@48:26)
- "I always involve an LM to help me read a book" (@55:03)
- "don't read books alone" (@58:28)
- "I would always encourage you to scrutinize the code" (@1:05:46)
- "it is kind of like a very very Junior data analyst" (@1:08:01)
- "the name for this is called Vibe coding" (@1:18:01)
- "don't type stuff out use voice it works quite well" (@1:26:59)
- "I find that this always increases the accuracy of LMS" (@2:00:31)

All grepped verbatim against the raw.

## Notes for merge
- Caption spellings: "chpd / Chachi PT / chashi" = ChatGPT; "Claud" = Claude; "Gro / grock" = Grok; "perplexity doai" = perplexity.ai; "01 Pro" = o1 pro; "Dolly / DOI" = DALL-E; "eny" = Anki; "versel" = Vercel; "C AKG / CG" = Ca-AKG; "zerat" = Zermatt; "neighor or Papo" = Naver/Papago; "notbook colum" = NotebookLM; "V2" = Veo 2 (he says "I think"); "kg" = cagey; "super whisper" = SuperWhisper; "Tik tokenizer" = Tiktokenizer; "railay" = Rayleigh.
- Pricing slip: he says "$100 per month" for Pro at @19:34 and "$200" elsewhere (@26:52, @42:26). Use $200 or omit.
- At @47:53 he says "deep research from Google uh from Chach", a slip; ChatGPT is the one he means.
- Other voices are not him: the advanced voice mode, Grok voice modes (@1:29:47–@1:36:33) and the NotebookLM podcast hosts (@1:38:12) are AI-generated. Do not quote any of it. The Grok "conspiracy" and "sexy" mode content should not be paraphrased.
- He hedges vibe coding: "a name with that I think I probably minted" (@1:18:01, garbled caption). The term's origin is on [[vibe-coding]] from x-2025-02-02-vibe-coding.
- Many tool-availability statements are dated and he says so: Claude without search or a thinking model, then Claude 3.7 released "while I was filming" (@36:50, @51:13); advanced voice "rolling out to free users" (@1:32:37); memory "unique to ChatGPT" in his belief (@1:56:39). Write them as as-of-the-video.
- He refers to his previous video "Deep Dive into LLMs" (@00:00); it is not in the wiki index.
- Mentioned but not explained: SEAL leaderboard, Windsurf, Ideogram, Sora/Veo, NotebookLM interactive mode, video input as ~one image per second (his guess, @1:52:10).
- Personal details (cold medicine, blood test, supplements): keep to what the method needs; no health specifics.
- He was "not 100% sure" about several mechanics (PDF image handling @52:50, video frames @1:51:36, Grok deep search ≈ deep research @45:40); keep hedges.
- Method/claim overlap: start-a-new-chat-per-topic (method) and start-a-new-chat-when-switching-topics (claim); verify-citations (method) and treat-deep-research-reports-as-a-first-draft / llm-code-tools-need-a-user-who-can-verify-the-code (claims). Merge may collapse.
