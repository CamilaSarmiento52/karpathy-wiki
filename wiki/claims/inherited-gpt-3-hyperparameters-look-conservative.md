---
type: claim
stated_on: 2024-06-09
confidence: stated
sources: ["[[youtube-2024-06-09-reproduce-gpt-2]]", "[[github-2024-07-11-llmc-gpt-2-1-6b]]"]
topic: "[[gradient-descent]]"
---
# The GPT-3 hyperparameters he inherited look conservative and are probably not tuned precisely
> "the gpt3 hyper parameters that we are inheriting are actually extremely conservative" — [[youtube-2024-06-09-reproduce-gpt-2]] @3:51:29

## Context
**2024-06-09, GPT-2 lecture.** He takes his optimisation settings from the GPT-3 paper because the GPT-2 paper is vague and OpenAI released only inference code ([[youtube-2024-06-09-reproduce-gpt-2]] @2:15:20, @2:15:55). At the end he says some people in a previous related repository found the maximum learning rate can be almost tripled, so it is possible these inherited settings are extremely conservative, that a higher learning rate would train faster, and that the hyperparameters are quite tunable and probably not set precisely ([[youtube-2024-06-09-reproduce-gpt-2]] @3:50:56, @3:51:29). Earlier in the run he calls the 715-step warmup very mild and says probably even 100 would be good enough, while keeping GPT-3's value for now ([[youtube-2024-06-09-reproduce-gpt-2]] @3:20:10). His wording is hedged ("it's possible", "for some reason"); the evidence he cites is other people's experiments, not his own sweep ([[youtube-2024-06-09-reproduce-gpt-2]] @3:51:29).

**2024-07-11, llm.c 1.6B post.** He again follows the GPT-3 paper in most settings because GPT-2's release had weights but very few details ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Args guide)). The GPT-3 paper says 2e-4 for this model size; he tripled it to 6e-4, it seems to train faster without issues, and he says this was not tuned very carefully yet ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Args guide)). Under "Coming up" he writes that the hyperparameters cited by OpenAI in the GPT-3 paper appear to be quite suboptimal, crediting @Yuchenj_UW on X with finding that 3X the learning rate trains faster with no apparent downsides, and expects other low-hanging fruit ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Coming up)). The 3X finding is someone else's; his own evidence is that his tripled rate "seems to" work ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Args guide)).

## Related claims
- **Note:** none of the existing claims covers hyperparameter choice; the settings themselves are on [[gradient-descent]] ([[youtube-2024-06-09-reproduce-gpt-2]] @2:16:28).
