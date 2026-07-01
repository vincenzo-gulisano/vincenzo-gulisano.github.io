---
layout: "post"
title: "ScaleJoin accepted at IEEE Big Data 2015!"
date: "2015-09-07 08:39:43"
categories: ["Concurrent Data Structures", "Data Streaming", "Research", "ScaleGate"]
tags: []
---

We got our ScaleJoin paper accepted at the IEEE International Conference on Big Data (IEEE Big Data)!
You can find the abstract below. See you in California!

<strong>Abstract</strong>
The inherently large and varying volumes of data generated to facilitate autonomous functionality in large scale cyber-physical systems demand near real-time processing of data streams, often as close to the sensing devices as possible. In this context, data streaming is imperative for data-intensive processing infrastructures. Stream joins, the streaming counterpart of database joins, compare tuples coming from different streams and constitute one of the most important and expensive data streaming operators. Dictated by the needs of big data streaming analytics, algorithmic implementations of stream joins have to be capable of efficiently processing bursty and rate-varying data streams in a deterministic and skew-resilient fashion. To leverage the design of modern multicore architectures, scalability and parallelism need to be addressed also in the algorithmic design.
In this paper we present ScaleJoin, an algorithmic construction for deterministic and parallel stream joins that guarantees all the above properties, thus filling in a gap in the existing state-of-the art. Key to the novelty of ScaleJoin is a new data structure, Scalegate, and its lock-free implementation. ScaleGate facilitates concurrent data exchange and balances independent actions among processing threads; it also enables fine-grain parallelism while providing the necessary synchronization for deterministic processing. As a result, it allows ScaleJoin to run on an arbitrary number of processing threads that can evenly share the overall comparisons run in parallel and achieve high processing throughput and low processing latency. As we show, ScaleJoin not only guarantees deterministic, disjoint and skew-resilient parallelism, but also achieves higher throughput than state-of-the-art parallel stream joins.
