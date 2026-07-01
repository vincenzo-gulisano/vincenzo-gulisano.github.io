---
layout: "post"
title: "Erebus accepted at VLDB!"
date: "2022-09-20 06:54:25"
categories: ["Uncategorized"]
tags: []
---

<p>Our paper, titled "Erebus: Explaining the Outputs of Data Streaming Queries", written by Dimitris Palyvos-Giannas (Chalmers), Katerina Tzompanaki (CY Cergy Paris University), Marina Papatriantafilou (Chalmers), and Vincenzo Gulisano (Chalmers) has been accepted at the 49th International Conference on Very Large Data Bases (VLDB)!!!</p>

<p>The paper introduces the novel concept (and the theoretical foundations) for why-not provenance in the context of stream processing, supporting analysts in understanding why some expected results are not observed in the outcome of their streaming applications.</p>

<p>The abstract follows:</p>

<p><em>In data streaming, why-provenance can explain why a given outcome is observed but offers no help in understanding why an expected outcome is missing. Explaining missing answers has been addressed in DBMSs, but these solutions are not directly applicable to the streaming setting, because of the extra challenges posed by limited storage and by the unbounded nature of data streams.<br>With our framework, Erebus, we tackle the unaddressed challenges behind explaining missing answers in streaming applications. Erebus allows users to define expectations about the results of a query, verifying at runtime if such expectations hold, and also providing explanations when expected and observed outcomes diverge (missing answers). To the best of our knowledge, Erebus is the first such solution in data streaming. Our thorough evaluation on real data shows that Erebus can explain the (missing) answers with small overheads, both in low- and higher-end devices, even when large portions of the processed data are part of such explanations.</em></p>
