---
layout: "post"
title: "2 minutes Apache Flink installation"
date: "2016-06-30 16:29:08"
categories: ["Uncategorized"]
tags: []
---

Continuing my effort of keeping track of useful and short guides (more for myself than others), here you have the one to setup Apache Flink quickly.

Note: this installation does not require sudo, is for a single-node cluster (with JAVA_HOME set and Java up to date) with out-of-the-box configuration and DOES NOT use HDFS.

<span style="text-decoration:underline;">Connect to your server</span>
<code>ssh -L 8081:localhost:8081 username@server</code>

<span style="text-decoration:underline;">Create a directory for storm and enter it</span>
<code>mkdir flink</code>
<code>cd flink</code>

<span style="text-decoration:underline;">Download Apache Flink and unzip it</span>
<code>wget <a href="http://apache.mirrors.spacedump.net/flink/flink-1.0.3/flink-1.0.3-bin-hadoop1-scala_2.10.tgz">http://apache.mirrors.spacedump.net/flink/flink-1.0.3/flink-1.0.3-bin-hadoop1-scala_2.10.tgz</a></code> (or the appropriate version)
<code>tar -xvf flink-1.0.3-bin-hadoop1-scala_2.10.tgz</code>

<span style="text-decoration:underline;">Start cluster</span>
<code>./bin/start-cluster</code>

Open your web browser and go to localhost:8081. Do you see the UI? good...

Notes:
<ul>
	<li>Have a look at conf/flink-conf.yaml and conf/slaves and  to understand (i) what is going on and (ii) why the installation is so straightforward (read: what parameters are already set for you)</li>
	<li>Read <a href="https://ci.apache.org/projects/flink/flink-docs-release-1.0/setup/cluster_setup.html">https://ci.apache.org/projects/flink/flink-docs-release-1.0/setup/cluster_setup.html</a>!</li>
</ul>
