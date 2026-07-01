---
layout: "post"
title: "STONE: A Streaming DDoS Defense Framework published! - Expert Systems With Applications (ESwA) 2015"
date: "2015-08-12 07:53:45"
categories: ["Data Streaming", "DDoS", "Research"]
tags: []
---

We recently got our STONE journal paper at the Expert Systems With Applications (ESwA)! Here you have the abstract.

<strong>Abstract</strong>
Distributed Denial-of-Service (DDoS) attacks aim at rapidly exhausting the communication and computational power of a network target by flooding it with large volumes of malicious traffic. In order to be effective, a DDoS defense mechanism should detect and mitigate threats quickly, while allowing legitimate users access to the attack's target. Nevertheless, defense mechanisms proposed in the literature tend not to address detection and mitigation challenges jointly, but rather focus solely on the detection or the mitigation facet. At the same time, they usually overlook the limitations of centralized defense frameworks that, when deployed physically close to a possible target, become ineffective if DDoS attacks are able to saturate the target's incoming links.
This paper presents STONE, a framework with expert system functionality that provides effective and joint DDoS detection and mitigation. STONE characterizes regular network traffic of a service by aggregating it into common prefixes of IP addresses, and detecting attacks when the aggregated traffic deviates from the regular one. Upon detection of an attack, STONE allows traffic from known sources to access the service while discarding suspicious one. STONE relies on the data streaming processing paradigm in order to characterize and detect anomalies in real time. We implemented STONE on top of StreamCloud, an elastic and parallel-distributed Stream Processing Engine. The evaluation, conducted on real network traces, shows that STONE detects DDoS attacks rapidly, provides minimal degradation of legitimate traffic while mitigating a threat, and also exhibits a processing throughput that scales linearly with the number of nodes used to deploy and run it.
