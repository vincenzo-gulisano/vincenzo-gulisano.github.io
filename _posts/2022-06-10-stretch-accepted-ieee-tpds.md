---
layout: "post"
title: "STRETCH accepted @ IEEE TPDS!"
date: "2022-06-10 06:51:44"
categories: ["Concurrent Data Structures", "Data Streaming", "Research", "ScaleGate"]
tags: []
---

<p>Our paper titled "STRETCH: Virtual Shared-Nothing Parallelism for Scalable and Elastic Stream Processing" has been accepted at the IEEE Transactions on Parallel and Distributed Processing (TPDS) journal!</p>

<p>STRETCH is the result of many years of collaborations with several researchers. As we discuss in the paper, STRETCH defines a general stateful streaming operator that encapsulates and extends the semantics of the stateful operators commonly found in Stream Processing Engines (Aggregates and Joins). Furthermore, it takes advantage of shared memory to boost the scaling up of such an operator and to provide ultra-fast state-transfer-free elastic reconfigurations.</p>

<p>The full abstract follows:</p>

<p><em>Stream processing applications extract value from raw data through Directed Acyclic Graphs of data analysis tasks. Shared-nothing (SN) parallelism is the de-facto standard to scale stream processing applications. Given an application, SN parallelism instantiates several copies of each analysis task, making each instance responsible for a dedicated portion of the overall analysis, and relies on dedicated queues to exchange data among connected instances. On the one hand, SN parallelism can scale the execution of applications both up and out since threads can run task instances within and across processes/nodes. On the other hand, its lack of sharing can cause unnecessary overheads and hinder the scaling up when threads operate on data that could be jointly accessed in shared memory. This trade-off motivated us in studying a way for stream processing applications to leverage shared memory and boost the scale up (before the scale out) while adhering to the widely-adopted and SN-based APIs for stream processing applications.</em></p>

<p><em>We introduce STRETCH, a framework that maximizes the scale up and offers instantaneous elastic reconfigurations (without state transfer) for stream processing applications. We propose the concept of Virtual Shared-Nothing (VSN) parallelism and elasticity and provide formal definitions and correctness proofs for the semantics of the analysis tasks supported by STRETCH, showing they extend the ones found in common Stream Processing Engines. We also provide a fully implemented prototype and show that \xxx{}'s performance exceeds that of state-of-the-art frameworks such as Apache Flink and offers, to the best of our knowledge, unprecedented ultra-fast reconfigurations, taking less than 40 ms even when provisioning tens of new task instances.</em></p>
