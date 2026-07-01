---
layout: "post"
title: "Accepted paper at the 2018 ACM/IFIP/USENIX International Middleware Conference!"
date: "2018-08-27 06:38:10"
categories: ["Uncategorized"]
tags: []
---

Great news!

Our paper titled "GeneaLog: Fine-Grained Data Streaming Provenance at the Edge" has been accepted at the 2018 ACM/IFIP/USENIX International Middleware Conference.

The abstract follows:
<em>Fine-grained data provenance in stream processing allows linking each result tuple back to the source data that contributed to its generation, something beneficial for many big data applications; e.g., in security and safety-related applications, it can help debug analytical queries, thus facilitating the inspection of the conditions triggering an alert. Furthermore, when data transmission or storage has to be minimized, such as in edge computing and cyber-physical systems, it can help to identify which fraction of the source data should be prioritized.</em>
<em>The memory and processing time costs of fine-grained data provenance, which can be afforded by high-end servers, can nonetheless be prohibitive for the resource-constrained devices deployed in edge computing and cyber-physical systems. Motivated by this challenge, we present GeneaLog, a novel fine-grained data provenance technique for data streaming applications. Leveraging the logical dependencies of the data, GeneaLog takes advantage of cross-layer properties of the software stack and incurs a minimal, constant size per-tuple overhead. Furthermore, it allows for a modular and efficient algorithmic implementation using only standard data streaming operators. This is particularly useful for streaming applications distributed at different physical nodes since the provenance processing can be executed at third nodes, orthogonal to the data-processing. We evaluate a full-fledged implementation of GeneaLog using vehicular and smart grid applications, confirming it efficiently captures fine-grained provenance data with minimal overhead.</em>
