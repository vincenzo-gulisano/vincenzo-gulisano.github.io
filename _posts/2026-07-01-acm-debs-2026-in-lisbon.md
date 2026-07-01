---
layout: "post"
title: "ACM DEBS 2026 in Lisbon"
date: "2026-07-01 00:00:00"
categories: ["Uncategorized"]
tags: []
---

Last week I was in Lisbon for ACM DEBS 2026. As always, DEBS was a great opportunity to catch up on the latest research in distributed systems, and in stream processing in particular, in an environment that strongly encourages discussion and interaction!

I was co-author of two contributions:

**SHIELD: Evolutionary Synthesis of Privacy-Preserving Pipelines for Live Stream Data Sharing** (together with Silvia Perellia and Eric Medvet)

and

**Chill: Runtime Reconfiguration of Windowed Stream Aggregates with Semantic Guarantees** (together with Jingyu Liu)

SHIELD is a framework based on Evolutionary Algorithms that automatically designs stream-processing pipelines for data anonymization. The goal is to preserve privacy while at the same time minimizing the impact of anonymization on the utility of downstream applications that rely on the data.

Chill is an algorithm that allows practitioners to define stream aggregates using a set of window sizes and a set of window advances, rather than a single configuration only, and to switch among them at runtime. The approach supports both at-most-once and exactly-once semantics, enabling trade-offs between computational cost, result freshness, and result completeness.

If you want to know more, you can find the papers here: [SHIELD](/assets/uploads/2026/06/shield.pdf) and [Chill](/assets/uploads/2026/06/chill.pdf), and the slides for SHIELD here: [SHIELD slides](/assets/uploads/2026/06/shield_presentation.pdf).
