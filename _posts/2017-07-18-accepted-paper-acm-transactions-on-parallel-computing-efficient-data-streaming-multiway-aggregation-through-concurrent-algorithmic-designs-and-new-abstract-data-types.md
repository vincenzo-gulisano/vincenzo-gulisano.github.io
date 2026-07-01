---
layout: "post"
title: "Accepted paper, ACM Transactions on Parallel Computing: Efficient data streaming multiway aggregation through concurrent algorithmic designs and new abstract data types"
date: "2017-07-18 10:33:41"
categories: ["Uncategorized"]
tags: []
---

I am glad to share that our paper <strong>Efficient data streaming multiway aggregation through concurrent algorithmic designs and new abstract data types </strong>has been accepted at the ACM Transactions on Parallel Computing (TOPC) journal!!!

Abstract:
Data streaming relies on continuous queries to process unbounded streams of data in a real-time fashion. It is commonly demanding in computation capacity, given that the relevant applications involve very large volumes of data. Data structures act as articulation points and maintain the state of data streaming operators, potentially supporting high parallelism and balancing the work among them. Prompted by this fact, in this work we study and analyze parallelization needs of these articulation points, focusing on the problem of streaming multiway aggregation, where large data volumes are received from multiple input streams. The analysis of the parallelization needs, as well as of the use and limitations of existing aggregate designs and their data structures, leads us to identify needs for appropriate shared objects that can achieve low-latency and high throughput multiway aggregation. We present the requirements of such objects as abstract data types and we provide efficient lock-free linearizable algorithmic implementations of them, along with new multiway aggregate algorithmic designs that leverage them, supporting both deterministic order-sensitive and order insensitive aggregate functions. Furthermore, we point out future directions that open through these contributions. The paper includes an extensive experimental study, based on a variety of continuous aggregation queries on two large datasets extracted from SoundCloud, a music social network, and from a Smart Grid network. In all the experiments, the proposed data structures and the enhanced aggregate operators improved the processing performance significantly, up to one order of magnitude, in terms of both throughput and latency, over the commonly-used techniques based on queues.
