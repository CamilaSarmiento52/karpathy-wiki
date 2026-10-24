---
type: claim
stated_on: 2024-09-05
confidence: stated
sources: ["[[talk-2024-09-05-no-priors-ep-80]]"]
context: ["[[talk-2023-05-19-stanford-cs25-transformers]]", "[[talk-2024-03-26-sequoia-making-ai-accessible]]"]
topic: "[[transformer-architecture]]"
supports: ["[[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]"]
---
# The neural-network architecture no longer fundamentally holds progress back; the dataset and loss function have become the bottlenecks
> "those have become the bottlenecks almost" — [[talk-2024-09-05-no-priors-ep-80]] @16:29

## Context
Asked about the data wall and the cost of another generation of scale, he says he does not think the neural-network architecture is fundamentally holding us back anymore; before the Transformer it was the bottleneck, now it is not ([[talk-2024-09-05-no-priors-ep-80]] @15:56, @16:29). The talk is now about the loss function and the dataset, and he says the companies applying the technology are not thinking about the architecture ([[talk-2024-09-05-no-priors-ep-80]] @16:29). In the Llama release the Transformer has changed little: RoPE positional encodings are the major change, everything else is worth about plus 3%, and everyone takes the architecture for granted and innovates on the dataset and loss function ([[talk-2024-09-05-no-priors-ep-80]] @16:29, @17:01). Data is where the activity is: internet data is not the data you want but a nearest neighbour that gets you surprisingly far ([[talk-2024-09-05-no-priors-ep-80]] @17:33).

## Related claims
- Supports [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]]: he again calls it a general-purpose training computer, a differentiable computer, and again says it has barely changed ([[talk-2024-09-05-no-priors-ep-80]] @14:49, @15:24, @17:01; [[talk-2023-05-19-stanford-cs25-transformers]] @21:39, @59:18).
- **Note:** no relation with [[the-transformer-is-probably-not-the-final-architecture]]: in the Sequoia interview he expects a pretty big change someday ([[talk-2024-03-26-sequoia-making-ai-accessible]] @33:51); here the architecture is not the bottleneck now ([[talk-2024-09-05-no-priors-ep-80]] @16:29). Both can hold.
