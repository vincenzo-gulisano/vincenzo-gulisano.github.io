---
layout: "post"
title: "Accepted paper at IEEE ICDCS!!!"
date: "2018-04-28 13:32:47"
categories: ["Uncategorized"]
tags: []
---

Great news!

Our paper titled <em>Continuous and Parallel LiDAR Point-cloud Clustering</em> has been accepted at the 38th IEEE International Conference on Distributed Computing Systems (ICDCS)!

The abstract follows:

In distributed digitalized environments in the context of Internet of Things, we often need to do analysis of big data originating at high rate-sensors at the edge of the infrastructure. A characteristic example is the light detection and ranging (LiDAR) technology, that allows to sense surrounding objects with fine-grained resolution in large areas. Their data (known as point clouds), generated continuously at very high rates, through appropriate analysis can provide information to support automated functionality in distributed cyberphysical systems; clustering of point clouds is a key problem to extract this type of information. Methods for solving the problem in a continuous fashion can facilitate improved processing in fog architectures, through enabling low-latency, efficient continuous and streaming processing of data close to the sources; moreover, parallelism is a key requirement to exploit a variety of computing architectures in this context.

We propose Lisco, a single-pass continuous Euclidean-distance-based clustering of LiDAR point clouds, that maximizes the granularity of the data processing pipeline and thus shows the potential for data- and pipeline-parallelism. We further present its parallel version, P-Lisco, that is architecture-independent and exploits the parallelism revealed by Lisco’s algorithmic approach. Besides their algorithmic analysis, we provide a thorough experimental evaluation on architectures representative of high-end servers and of resource-constrained embedded devices and highlight the multiplicative improvements and scalability benefits of the proposed algorithms compared to the baseline, using both real-world datasets as well as synthetic ones to fully explore a wide spectrum of stress-levels for the algorithms.
