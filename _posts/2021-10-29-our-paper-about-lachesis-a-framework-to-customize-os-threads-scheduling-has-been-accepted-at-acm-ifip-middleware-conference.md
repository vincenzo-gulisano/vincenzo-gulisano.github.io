---
layout: "post"
title: "Our paper about Lachesis, a framework to customize OS-threads scheduling, has been accepted at ACM/IFIP Middleware Conference!"
date: "2021-10-29 12:08:52"
categories: ["Data Streaming", "Research"]
tags: ["Scheduling", "Stream Processing Engines"]
---

<p>Our paper titled “Lachesis: A Middleware for Customizing OS Scheduling of Stream Processing Queries” (Dimitris Palyvos-Giannas, Gabriele Mencagli, Marina Papatriantafilou, Vincenzo Gulisano) has been accepted at the 22ns ACM/IFIP International Middleware Conference.</p>

<p>This work, in collaboration with Gabriele Mencagli, from the University of Pisa, studies how the scheduling kernel threads can be orchestrated, through mechanisms as <em>nice</em> and <em>cgroups</em>, to customize the execution of stream processing applications. Lachesis makes a novel key contribution: the ability to customize the scheduling goals of streaming applications without altering the architecture of the Stream Processing Engine running them!</p>

<p>The abstract follows:<br>Data streaming applications in Cyber-Physical Systems enable high-throughput, low-latency transformations of raw data into value. The performance of such applications, run by Stream Processing Engines (SPEs), can be boosted through custom CPU scheduling. Previous schedulers in the literature require alterations to SPEs to control the scheduling through user-level threads. While such alterations allow for fine-grained control, they hinder the adoption of such schedulers due to the high implementation cost and potential limitations in application semantics (e.g., blocking I/O).<br>Motivated by the above, we explore the feasibility and benefits of custom scheduling without alterations to SPEs but, instead, by orchestrating the OS scheduler (e.g., using <em>nice</em> and <em>cgroup</em>) to enforce the scheduling goals. We propose <em>Lachesis</em>, a standalone scheduling middleware, decoupled from any specific SPE, that can schedule multiple streaming applications, run in one or many nodes, and possibly multiple SPEs. Our evaluation with real-world and synthetic workloads, several SPEs and hardware setups, shows its benefits over default OS scheduling and other state-of-the-art schedulers: up to 75\% higher throughput, and 1130x lower average latency once such SPEs reach their peak processing capacity.</p>
