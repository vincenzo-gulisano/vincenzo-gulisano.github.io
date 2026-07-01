---
layout: "post"
title: "ScaleJoin journal - IEEE Transactions on Big Data"
date: "2016-11-15 09:28:33"
categories: ["Concurrent Data Structures", "Data Streaming", "Research", "ScaleGate"]
tags: []
---

I am happy to share with you that our ScaleJoin has been accepted for a journal publication at the IEEE Transactions on Big Data!

This work extends our previous conference submission in 2 directions. First, we discuss how ScaleJoin can be used to join streams both on <em>time-based windows</em> and <em>tuple-based windows. </em>Second, we implement and evaluate ScaleJoin on the Xeon Phi coprocessor unit, based on Intel® Many Integrated Core (Intel MIC) architecture, which allows for a scalability study of up to 220 physical threads<i>.</i>

Abstract:
<div class="page" title="Page 1">
<div class="layoutArea">
<div class="column">

The inherently large and varying volumes of information generated in large scale systems demand near real-time processing of data streams. In this context, data streaming is imperative for data-intensive processing infrastructures. Stream joins, the streaming counterpart of database joins, compare tuples coming from different streams and constitute one of the most important and expensive data streaming operators. Algorithmic implementations of stream joins have to be capable of efficiently processing bursty and rate-varying data streams in a deterministic and skew-resilient fashion. To leverage the design of modern multicore architectures, scalability and parallelism need to be addressed also in the algorithmic design.

In this paper we present ScaleJoin, an algorithmic construction for deterministic and parallel stream joins that guarantees all the above properties, thus filling in a gap in the existing state-of-the-art. Key to the novelty of ScaleJoin is the ScaleGate data structure and its lock-free implementation. ScaleGate facilitates concurrent data exchange and balances independent actions among process- ing threads; enabling fine-grain parallelism and deterministic processing. It allows ScaleJoin to run on an arbitrary number of processing threads, evenly sharing the overall comparisons run in parallel and achieving disjoint and skew-resilient high processing throughput and low processing latency.

</div>
</div>
</div>
