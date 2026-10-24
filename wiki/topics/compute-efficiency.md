---
type: topic
aliases: [Compute efficiency, training efficiency, energy efficiency, precision, mixed precision, bfloat16, TF32, sparsity, torch.compile, flash attention, distributed data parallel, DDP, quantization, hardware co-design, von Neumann bottleneck]
first_seen: 2024-03-26
last_updated: 2024-03-26
sources: ["[[talk-2024-03-26-sequoia-making-ai-accessible]]"]
related: ["[[scaling-laws]]", "[[transformer-architecture]]"]
---
# Compute efficiency
How much useful model you get per unit of compute and energy. In the Sequoia interview he names a massive gap in the energetic efficiency of running these models as one of the open research problems ([[talk-2024-03-26-sequoia-making-ai-accessible]] @12:55).

## What he says
His brain runs on roughly 20 watts, while the supercomputers Jensen described at GTC are measured in megawatts; he does not know how much you need exactly, but thinks it safe to say we are probably off by a factor of a thousand to a million ([[talk-2024-03-26-sequoia-making-ai-accessible]] @12:55, @13:27). Part of the reason is that computers were not designed for this workload, which needs extremely high parallelism rather than data-dependent sequential computation; he calls Nvidia GPUs a good step in that direction ([[talk-2024-03-26-sequoia-making-ai-accessible]] @13:27).

His levers: adapt computer architecture to the new workload; keep lowering precision, which has come down from 64-bit doubles to a few bits or even 1.58 depending on the paper; and sparsity, since the brain is not always fully activated ([[talk-2024-03-26-sequoia-making-ai-accessible]] @13:59). The last lever is the von Neumann architecture, whose shuttling of data between memory and compute cores he calls kind of broken and unlike how the brain works ([[talk-2024-03-26-sequoia-making-ai-accessible]] @14:33). He says he is not a computer architect but expects a very exciting time in computer architecture ([[talk-2024-03-26-sequoia-making-ai-accessible]] @14:33). Asked later about changing the Transformer, he returns to precision, sparsity and co-design with the hardware ([[talk-2024-03-26-sequoia-making-ai-accessible]] @34:24, @34:57).

He also calls good dataset preparation and better algorithms compute-efficiency gains, alongside scale ([[talk-2024-03-26-sequoia-making-ai-accessible]] @09:38).

## Claims
- [[ai-is-far-less-energy-efficient-than-the-brain]]

## Related
- [[scaling-laws]] — scale ranked first, efficiency gains alongside
- [[transformer-architecture]] — an architecture designed for the GPU
- [[the-transformer-is-probably-not-the-final-architecture]] — precision and sparsity as levers for change
