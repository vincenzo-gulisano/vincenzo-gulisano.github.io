---
layout: "post"
title: "Slides for the paper \"Automatic Translation of Spatio-Temporal Logics to Streaming-Based Monitoring Applications for IoT-Equipped Autonomous Agents\" available in SlideShare"
date: "2020-01-15 12:59:05"
categories: ["Uncategorized"]
tags: []
---

The slides I used to present the paper "Automatic Translation of Spatio-Temporal Logics to Streaming-Based Monitoring Applications for IoT-Equipped Autonomous Agents" at the 2019 ACM/IFIP Middleware conference - 6th International Workshop on Middleware and Applications for the Internet of Things (M4IoT) are now available at SlideShare: <a href="https://www.slideshare.net/VincenzoGulisano/strel-streaming">https://www.slideshare.net/VincenzoGulisano/strel-streaming</a>.

The abstract of the paper follows:

<em>Environments in which IoT-equipped autonomous agents and humans tightly interact require safety rules that monitor the agents' behaviors. In this context, expressive and human-comprehensible rules based on Spatio-Temporal Logics (STLs) are desirable because they are informative and easy to maintain. Unfortunately, STLs usually build on ad-hoc platforms implementing the logic semantics.</em>
<em>We tackle this limitation with a mechanism to transparently compile STL rules to monitoring applications composed of standard data streaming operators, thus opening up the use of high-throughput and low-latency Stream Processing Engines for monitoring rule compliance in realistic, data-rich IoT scenarios. Our contribution can favor a broader and faster adoption of STLs for IoT-equipped agent monitoring by separating the concerns of designing a rule from those of implementing its semantics. Together with our formal description of how to translate STLs to the streaming domain, we evaluate our prototype implementation based on Apache Flink, studying the effects of parameters such as time and space resolution on the monitoring performance.</em>
