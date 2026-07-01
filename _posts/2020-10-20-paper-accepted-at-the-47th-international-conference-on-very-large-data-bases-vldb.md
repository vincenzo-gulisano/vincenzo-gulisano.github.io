---
layout: "post"
title: "Paper accepted at the 47th International Conference on Very Large Data Bases (VLDB)!"
date: "2020-10-20 09:13:02"
categories: ["Data Streaming", "Research"]
tags: []
---

<p>Our paper titled "<em>Ananke: A Streaming Framework for Live Forward Provenance</em>" (Dimitris Palyvos-Giannas, Bastian Havers, Marina Papatriantafilou, Vincenzo Gulisano) has been accepted at the 47th International Conference on Very Large Data Bases (VLDB)!</p>

<p>This work, conducted within the scope of the VR project Haren and the Vinnova project AutoSPADA (in collaboration with Volvo), introduces the first streaming framework providing fine-grained forward provenance. As we explain in the paper, such a tool is valuable for distributed and parallel analysis in edge to cloud infrastructures, since it eases the retrieval of source data connected to analysis outcomes, while being able to discriminate whether each piece of source data could still contribute to future analysis outcomes or not. </p>

<p>Ananke is available in Github at the following link: <a rel="noreferrer noopener" href="https://github.com/dmpalyvos/ananke" target="_blank">https://github.com/dmpalyvos/ananke</a> and implemented on top of the <a rel="noreferrer noopener" href="https://flink.apache.org" target="_blank">Apache Flink</a> streaming processing engine (a framework used by Alibaba and Amazon Kinesis Data Analytics, among others). All the experiments we present in the paper can be reproduced with the scripts we made available in our repository.</p>

<p>The abstract follows:</p>

<p><em>Data streaming enables online monitoring of large and continuous event streams in Cyber-Physical Systems (CPSs). In such scenarios, fine-grained backward provenance tools can connect streaming query results to the source data producing them, allowing analysts to study the dependency/causality of CPS events. While CPS monitoring commonly produces many events, backward provenance does not help prioritize event inspection since it does not specify if an event’s provenance could still contribute to future results. To cover this gap, we introduce Ananke, a framework to extend any fine-grained backward provenance tool and deliver a live bi-partite graph of fine-grained forward provenance. With Ananke, analysts can prioritize the analysis of provenance data based on whether such data is still potentially being processed by the monitoring queries. We prove our solution is correct, discuss multiple implementations, including one leveraging streaming APIs for parallel analysis, and show Ananke results in small overheads, close to those of existing tools for fine-grained backward provenance.</em></p>
