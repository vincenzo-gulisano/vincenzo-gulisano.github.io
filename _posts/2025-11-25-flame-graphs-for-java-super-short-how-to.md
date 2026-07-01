---
layout: "post"
title: "Flame graphs for Java (super-short how to)"
date: "2025-11-25 13:01:45"
categories: ["programming"]
tags: ["Flame graph", "Java", "Programming"]
---

<p class="has-medium-font-size">This is for Ubuntu!</p>

<p class="has-medium-font-size">Download async-profiler</p>

<p class="has-small-font-size"><code>wget https://github.com/async-profiler/async-profiler/releases/tag/v4.2.1#:~:text=async%2Dprofiler%2D4.2.1%2Dlinux%2Dx64.tar.gz<br>tar xvf async-profiler-4.2.1-linux-x64.tar.gz</code></p>

<p class="has-medium-font-size">Let user-space programs access Linux performance counters and expose kernel symbol addresses (can also make permanent)</p>

<p class="has-small-font-size"><code>sudo sysctl -w kernel.perf_event_paranoid=1<br>sudo sysctl -w kernel.kptr_restrict=0</code></p>

<p class="has-medium-font-size">Start Java and attach</p>

<p class="has-small-font-size"><code>java -jar &lt;jar path&gt; &lt;params&gt; &amp;<br>echo "PID = $!"<br>echo "Waiting 20 seconds for the system to start up…"<br>sleep 20<br>~/async-profiler-4.2.1-linux-x64/bin/asprof -e wall -d 30 -f wall.html $!<br>echo "Profiling complete. Output saved to profile.html. Killing the Java process."<br>kill $!</code></p>

<p>The option -e wall is for wallclock time. You can also remove to have only CPU time.</p>
