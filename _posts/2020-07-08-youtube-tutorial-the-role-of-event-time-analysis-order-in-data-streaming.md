---
layout: "post"
title: "YouTube tutorial: The Role of Event-Time Analysis Order in Data Streaming"
date: "2020-07-08 06:56:33"
categories: ["Data Streaming", "Presentation", "Research", "Teaching"]
tags: []
---

<p>Our tutorial, titled “The Role of Event-Time Analysis Order in Data Streaming”, will be presented next week at the 14<sup>th</sup> ACM International Conference on Distributed and Event-Based Systems (DEBS) conference. We have recorded the tutorial, and you can find the videos at the following links:</p>

<p>Part 1: <a href="https://youtu.be/SW_WS6ULsdY" target="_blank" rel="noreferrer noopener">https://youtu.be/SW_WS6ULsdY</a></p>

<p>Part 2: <a href="https://youtu.be/bq3ECNvPwOU" target="_blank" rel="noreferrer noopener">https://youtu.be/bq3ECNvPwOU</a></p>

<p>You can find the slides, as well as the code examples, <a href="https://github.com/vincenzo-gulisano/debs2020_tutorial_event_time" target="_blank" rel="noreferrer noopener">here</a>. The slides are also available at SlideShare (<a href="https://www.slideshare.net/VincenzoGulisano/tutorial-the-role-of-eventtime-analysis-order-in-data-streaming" target="_blank" rel="noreferrer noopener">here</a>)</p>

<p>Abstract:</p>

<p>The data streaming paradigm was introduced around the year 2000 to overcome the limitations of traditional store-then-process paradigms found in relational databases (DBs). Opposite to DBs’ “first-the-data-then-the-query” approach, data streaming applications build on the “first-the-query then-the-data” alternative. More concretely, data streaming applications do not rely on storage to initially persist data and later query it, but rather build on continuous single-pass analysis in which incoming streams of data are processed on the fly and result in continuous streams of outputs.</p>

<p>In contrast with traditional batch processing, data streaming applications require the user to reason about an additional dimension in the data: event-time. Numerous models have been proposed in the literature to reason about event-time, each with different guarantees and trade-offs. Since it is not always clear which of these models is appropriate for a particular application, this tutorial studies the relevant concepts and compares the available options. This study can be highly relevant for people working with data streaming applications, both researchers and industrial practitioners.</p>
