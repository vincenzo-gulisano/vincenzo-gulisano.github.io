---
layout: "post"
title: "5 minutes Storm installation guide (single-node setup)"
date: "2015-07-30 10:30:07"
categories: ["Data Streaming", "programming", "Storm"]
tags: ["Programming"]
---

The following is a short guide to setup Storm quickly!

Note: this installation does not require sudo, logs and other data maintained by ZooKeeper and Storm are in my home folder

<span style="text-decoration:underline;">Create a directory for storm and enter it</span>
<code>mkdir storm</code>
<code>cd storm</code>

<span style="text-decoration:underline;">Create a data directory</span>
<code>mkdir -p datadir/zookeeper</code>

<span style="text-decoration:underline;">Download ZooKeeper and unzip it</span>
<code>wget <a href="http://apache.mirrors.spacedump.net/zookeeper/current/zookeeper-3.4.6.tar.gz">http://apache.mirrors.spacedump.net/zookeeper/current/zookeeper-3.4.6.tar.gz</a></code> (or the appropriate version)
<code>tar -xvf zookeeper-3.4.6.tar.gz</code>

<span style="text-decoration:underline;">Download Storm and unzip it</span>
<code>wget <a href="http://apache.mirrors.spacedump.net/storm/apache-storm-0.9.5/apache-storm-0.9.5.tar.gz">http://apache.mirrors.spacedump.net/storm/apache-storm-0.9.5/apache-storm-0.9.5.tar.gz</a></code> (or the appropriate version)
<code>tar -xvf apache-storm-0.9.5.tar.gz</code>

<span style="text-decoration:underline;">Configure ZooKeeper</span>
Add the following to <code>zookeeper-3.4.6/conf/zoo.cfg</code>
<code>tickTime=2000</code>
<code>dataDir=/home/username/datadir/zookeeper</code>
<code>clientPort=2181</code>

<span style="text-decoration:underline;">Configure Storm</span>
Uncomment/add the following to <code>apache-storm-0.9.5/conf/storm.yaml</code>
<code>storm.zookeeper.servers:</code>
<code>  - "127.0.0.1"</code>
<code>nimbus.host: "127.0.0.1”</code>
<code>storm.local.dir: "/home/username/storm/datadir/storm"</code>
<code>supervisor.slots.ports:</code>
<code>    - 6700</code>
<code>    - 6701</code>
<code>    - 6702</code>
<code>    - 6703</code>

<span style="text-decoration:underline;">Start ZooKeeper</span>
<code>zookeeper-3.4.6/bin/zkServer.sh start</code>

<span style="text-decoration:underline;">Start nimbus</span>
<code>apache-storm-0.9.5/bin/storm nimbus</code> (start in separate shell or in background with &amp;)

<span style="text-decoration:underline;">Start supervisor</span>
<code>apache-storm-0.9.5/bin/storm supervisor</code> (start in separate shell or in background with &amp;)

<span style="text-decoration:underline;">Start UI</span>
<code>apache-storm-0.9.5/bin/storm ui</code> (start in separate shell or in background with &amp;)

Try to connect to 127.0.0.1:8080, you see Storm UI? Enjoy!

Notes:
<ul>
	<li>I ssh a remote server, so I run  <code>ssh -L 8080:localhost:8080 username@server</code> to be able to locally access port 8080 on the server</li>
	<li>This setup creates 4 workers, if you want more/less modify supervisor.slots.ports</li>
</ul>
