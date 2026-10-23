---
type: claim
stated_on: 2022-10-04
confidence: stated
sources: ["[[youtube-2022-10-04-makemore-3-activations-batchnorm]]"]
topic: "[[weight-initialization]]"
---
# Residual connections, normalization layers and better optimisers make exact initialisation less important
> "it's become less important to initialize these networks exactly right" — [[youtube-2022-10-04-makemore-3-activations-batchnorm]] @36:26

## Context
About seven years before the lecture you had to be extremely careful with activation and gradient ranges and gains, and he says everything was finicky and fragile ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @35:55). He names three innovations that changed this: residual connections, normalization layers (batch, layer, group), and better optimisers such as RMSprop and especially Adam ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @36:26, @37:00). He skips the details of the Kaiming paper intentionally for this reason ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @35:55). He still says Kaiming normal, as implemented in PyTorch's `kaiming_normal`, is in his opinion "probably the most common way of initializing neural networks" as of 2022, while in practice he himself just normalises by the square root of fan-in ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @33:45, @37:00). He also hedges at the close: the field has certainly not solved initialisation or backpropagation, and he did not fully explain why changing the gain needs a different learning rate, which would need the backward pass of each layer; the best initialisation and update rule are still being worked out, but there are at least tools to tell whether training is on track ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:54:48, @1:55:22).

## Related claims
- **Note:** [[avoid-batch-normalization-where-possible]] is the other side of the same lecture: normalization layers are one of the innovations named here, and the layer he nonetheless tells learners to avoid ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @36:26, @1:17:07).
