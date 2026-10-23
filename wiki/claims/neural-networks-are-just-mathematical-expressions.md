---
type: claim
stated_on: 2022-08-16
confidence: stated
sources: ["[[youtube-2022-08-16-micrograd]]"]
topic: "[[backpropagation]]"
supports: ["[[backpropagation-is-more-general-than-neural-networks]]", "[[micrograd-is-all-you-need-everything-else-is-efficiency]]"]
---
# Neural networks are just a class of mathematical expressions
> "neural networks are just mathematical expressions just like this one" — [[youtube-2022-08-16-micrograd]] @04:19

## Context
Introducing micrograd on a made-up expression, he says a neural net takes the data and the weights as inputs and outputs predictions or the loss; it is a certain class of mathematical expression, slightly less crazy than his example ([[youtube-2022-08-16-micrograd]] @04:19, @04:51). He repeats it in the summary: an MLP is a fairly simple expression for the forward pass followed by a loss ([[youtube-2022-08-16-micrograd]] @2:13:49, @2:14:22).

## Related claims
- Supported by [[backpropagation-is-more-general-than-neural-networks]]: in the same passage he says backprop works on arbitrary expressions and neural nets happen to use that machinery ([[youtube-2022-08-16-micrograd]] @04:51).
- Supported by [[micrograd-is-all-you-need-everything-else-is-efficiency]]: because the math is a scalar expression, about 150 lines suffice and tensors only add efficiency ([[youtube-2022-08-16-micrograd]] @06:30, @07:35).
