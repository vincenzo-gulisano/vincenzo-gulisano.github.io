---
layout: "post"
title: "DRIVEN article accepted at Elsevier’s Future Generation Computer Systems."
date: "2020-01-31 08:29:20"
categories: ["Uncategorized"]
tags: []
---

Our paper <strong>DRIVEN: a framework for efficient Data Retrieval and clusterIng in VEhicular Networks</strong> has been accepted for publication at Elsevier’s Future Generation Computer Systems journal. This work is an extension of the conference publication:

<em>Havers, Bastian, et al. "DRIVEN: a framework for efficient Data Retrieval and clusterIng in VEhicular Networks." 2019 IEEE 35th International Conference on Data Engineering (ICDE). IEEE, 2019.</em>

In this extended version, we build on and extend our framework, which leverages streaming-based Piecewise Linear Approximation and clustering for edge-to-core analysis. We show that real-world raw data such as GPS, LiDAR and other vehicular signals can be compressed (within each vehicle, in a streaming fashion) to 5-35 % of its original size, significantly reducing communication costs and overheads, and clustered (at the cloud, in a streaming fashion) with an accuracy loss below 10%.

&nbsp;

The abstract follows:

The growing interest in data analysis applications for Cyber-Physical Systems stems from the large amounts of data such large distributed systems sense in a continuous fashion.  A key research question in this context is how to jointly address the efficiency and effectiveness challenges of such data analysis applications.

DRIVEN proposes a way to jointly address these challenges for a data gathering and distance-based clustering tool in the context of vehicular networks.  To cope with the limited communication bandwidth (compared to the sensed data volume) of vehicular networks and data transmission’s monetary costs, DRIVEN avoids gathering raw data from vehicles, but  rather  relies  on  a  streaming-based  and  error-bounded  approximation,  through  Piecewise  Linear  Approximation (PLA), to compress the volumes of gathered data.  Moreover,  a streaming-based approach is also used to cluster the collected  data  (once  the  latter  is  reconstructed  from  its  PLA-approximated  form).   DRIVEN’s  clustering  algorithm leverages  the  inherent  ordering  of  the  spatial  and  temporal  data  being  collected  to  perform  clustering  in  an  online fashion,  while data is being retrieved.  As we show,  based on our prototype implementation using Apache Flink and thorough evaluation with real-world data such as GPS, LiDAR and other vehicular signals,  the accuracy loss for the clustering performed on the gathered approximated data can be small (below 10 %), even when the raw data is compressed to 5-35 % of its original size, and the transferring of historical data itself can be completed in up to one-tenth of the duration observed when gathering raw data.

&nbsp;
