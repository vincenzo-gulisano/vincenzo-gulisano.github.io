---
layout: "post"
title: "Our paper \"IP-LSH-DBSCAN: Integrated Parallel Density-Based Clustering through Locality-Sensitive Hashing\" has been accepted at Euro-Par 2022"
date: "2022-05-02 10:14:40"
categories: ["Uncategorized"]
tags: []
---

<p>Our paper titled “IP-LSH-DBSCAN: Integrated Parallel Density-Based Clustering through Locality-Sensitive Hashing” (Amir Keramatian, Vincenzo Gulisano, Marina Papatriantafilou, and Philippas Tsigas) has been accepted at Euro-Par 2022.</p>

<p>The abstract follows:<br></p>

<p>Locality-sensitive hashing (LSH) is an established method for fast data indexing and approximate similarity search, with useful parallelism properties. Although indexes and similarity measures are key for data clustering, little has been investigated on the benefits of LSH in the problem. Our proposition is that LSH can be extremely beneficial for parallelizing high-dimensional density-based clustering e.g., DBSCAN, a versatile method able to detect clusters of different shapes and sizes.</p>

<p>We contribute to fill the gap between the advancements in LSH and density-based clustering. In particular, we show how approximate DBSCAN clustering can be fused into the process of creating an LSH index structure, and, through data parallelization and fine-grained synchronization, also utilize efficiently available computing capacity as needed for massive data-sets. The resulting method, IP.LSH.DBSCAN, can effectively support a wide range of applications with diverse distance functions, as well as data distributions and dimensionality. Furthermore, IP.LSH.DBSCAN facilitates adjustable accuracy through LSH parameters. We analyse its properties and also evaluate our prototype implementation on a 36-core machine with 2-way hyper threading on massive data-sets with various numbers of dimensions. Our results show that IP.LSH.DBSCAN effectively complements established state-of-the-art methods by up to several orders of magnitude of speed-up on higher dimensional datasets, with tunable high clustering accuracy.</p>
