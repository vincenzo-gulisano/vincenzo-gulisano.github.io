---
layout: "post"
title: "Accepted paper at Elsevier - Future Generation Computer Systems Journal"
date: "2018-05-29 07:30:04"
categories: ["Uncategorized"]
tags: []
---

Our journal paper titled <em>Viper: A Module for Communication-Layer Determinism and Scaling in Low-Latency Stream Processing</em> has been accepted at the Elsevier journal <em>Future Generation Computer Systems</em>!

The abstract follows:

<em>Stream Processing Engines (SPEs) process continuous streams of data and produce results in a real-time fashion, typically through one-at-a-time tuple analysis. In Fog architectures, the limited resources of the edge devices, enabling close-to-the-source scalable analysis, demand for computationally- and energy-efficient SPEs. When looking into the vital SPE processing properties required from applications, determinism, which ensures consistent results independently of the way the analysis is parallelized, has a strong position besides scalability in throughput and low processing latency. SPEs scale in throughput and latency by relying on shared-nothing parallelism, deploying multiple copies of each operator to which tuples are distributed based on its semantics. The coordination of the asynchronous analysis of parallel operators required to enforce determinism is then carried out by additional dedicated sorting operators. To prevent this costly coordination from becoming a bottleneck, we introduce the Viper communication module, which can be integrated in the SPE communication layer and boost the coordination of the parallel threads analyzing the data. Using Apache Storm and data extracted from the Linear Road benchmark and a real-world smart grid system, we show benefits in the throughput, latency and energy efficiency coming from the utilization of the Viper module.</em>
