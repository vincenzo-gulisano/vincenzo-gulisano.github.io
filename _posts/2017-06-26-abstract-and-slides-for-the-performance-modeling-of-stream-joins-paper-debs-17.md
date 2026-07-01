---
layout: "post"
title: "Abstract and slides for the \"Performance Modeling of Stream Joins\" paper (DEBS 17)"
date: "2017-06-26 07:40:05"
categories: ["Uncategorized"]
tags: []
---

I just uploaded the slides I used to present the paper "Performance Modeling of Stream Joins" at the DEBS 17 conference. You can find them <a href="https://www.slideshare.net/VincenzoGulisano/performance-modeling-of-stream-joins" target="_blank" rel="noopener">here</a>.

<strong>Abstract</strong>
Streaming analysis is widely used in a variety of environments, from cloud computing infrastructures up to the network’s edge. In these contexts, accurate modeling of streaming operators’ performance enables fine-grained prediction of applications’ behavior without the need of costly monitoring. This is of utmost importance for computationally-expensive operators like stream joins, that observe throughput and latency very sensitive to rate-varying data streams, especially when deterministic processing is required.
In this paper, we present a modeling framework for estimating the throughput and the latency of stream join processing. The model is presented in an incremental step-wise manner, starting from a centralized non-deterministic stream join and expanding up to a deterministic parallel stream join. The model describes how the dynamics of throughput and latency are influenced by the number of physical input streams, as well as by the amount of parallelism in the actual processing and the requirement for determinism. We present an experimental validation of the model with respect to the actual implementation. The proposed model can provide insights that are catalytic for understanding the behavior of stream joins against different system deployments, with special emphasis on the influences of determinism and parallelization.
