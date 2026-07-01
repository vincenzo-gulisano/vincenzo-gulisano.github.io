---
layout: "post"
title: "SHIELD paper accepted at DEBS26!"
date: "2026-04-23 06:53:31"
categories: ["Uncategorized"]
tags: []
---

<p>I’m happy to share that our paper “<strong>SHIELD: Evolutionary Synthesis of Privacy-Preserving Pipelines for Live Stream Data Sharing</strong>” has been accepted at <a href="https://2026.debs.org/">ACM DEBS 2026</a>!</p>

<p>This work is about a challenge that feels increasingly important: how to share realistic live-stream data for testing, benchmarking, and optimization without exposing sensitive information.</p>

<p>I am particularly proud of this one. It is a collaboration with a colleague from the <a href="https://www.linkedin.com/company/universitadeglistudiditrieste/"><strong>Università degli Studi di Trieste</strong></a>, where I studied, and which I will soon be travelling to as a visiting professor. Congratulations to my co-authors <a href="https://www.linkedin.com/in/silvia-perelli-b81a9a403/"><strong>Silvia Perelli</strong></a> and <a href="https://www.linkedin.com/in/ericmedvet/"><strong>Eric Medvet</strong></a>—very glad to share this with you.</p>

<p><strong>Abstract</strong>:<br>Modern data-driven organizations rely on pipelines that transform data from infrastructure, applications, and users, where correctness and performance are critical for reliability and business value. These pipelines are often developed and optimized by teams separate from the data owners defining semantics, so meaningful testing and benchmarking require sharing representative data. This creates a tension: real data is needed to validate semantics, detect subtle errors, and tune performance, yet it is often sensitive and restricted by legal and commercial constraints.<br>To enable privacy-preserving data sharing while preserving utility, we present SHIELD, a framework that automatically constructs privacy-preserving pipelines to transform sensitive data on the fly into shareable data while preserving the characteristics required for downstream processing and optimization. Internally, SHIELD leverages evolutionary computation to synthesize executable privacy-preserving queries under predefined privacy constraints and utility requirements. Using real-world use cases, we show that SHIELD can synthesize privacy-preserving pipelines that retain analytical value while scaling to realistic workloads.</p>
