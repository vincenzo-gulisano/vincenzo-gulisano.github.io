---
layout: "post"
title: "BEST PAPER AWARD at DEBS 2017"
date: "2017-06-23 07:04:37"
categories: ["Uncategorized"]
tags: []
---

I am very happy to share that our paper <strong>Maximizing Determinism in Stream Processing Under Latency Constraints, </strong>a join work between<strong> </strong>Nikos Zacheilas, Vana Kalogeraki, Yiannis Nikolakopoulos, Marina Papatriantafilou, Philippas Tsigas and me got the BEST PAPER AWARD at the 11th ACM International Conference on Distributed Event-Based Systems (DEBS 2017)!!!

ABSTRACT

The problem of coping with the demands of determinism and meeting latency constraints is challenging in distributed data stream processing systems that have to process high volume data streams that arrive from different unsynchronized input sources. In order to deterministically process the streaming data, they need mechanisms that synchronize the order in which tuples are processed by the operators. On the other hand, achieving real-time response in such a system requires careful tradeoff between determinism and low latency performance. We build on a recently proposed approach to handle data exchange and synchronization in stream processing, namely ScaleGate, which comes with guarantees for determinism and an efficient lock-free implementation, enabling high scalability. Considering the challenge and trade-offs implied by real-time constraints, we propose a system which comprises (a) a novel data structure called Slack-ScaleGate (SSG), along with its algorithmic implementation; SSG enables us to guarantee the deterministic processing of tuples as long as they are able to meet their latency constraints, and (b) a method to dynamically tune the maximum amount of time that a tuple can wait in the SSG data structure, relaxing the determinism guarantees when needed, in order to satisfy the latency constraints. Our detailed experimental evaluation using a traffic monitoring application deployed in the city of Dublin, illustrates the working and benefits of our approach.

&nbsp;
