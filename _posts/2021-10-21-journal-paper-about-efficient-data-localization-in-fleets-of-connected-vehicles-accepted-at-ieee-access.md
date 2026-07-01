---
layout: "post"
title: "Journal paper about efficient data localization in fleets of connected vehicles accepted at IEEE Access"
date: "2021-10-21 13:28:39"
categories: ["Uncategorized"]
tags: []
---

<p>Our paper titled “<em>Time- and Computation-Efficient Data Localization at Vehicular Networks’ Edge.</em>” (Romaric Duvignau, Bastian Havers, Vincenzo Gulisano and Marina Papatriantafilou) has been accepted at the IEEE Access journal.</p>

<p>This work, conducted within the scope of the Vinnova project AutoSPADA (in collaboration with Volvo) and the VR project Haren, introduces a novel approach for localizing data in an evolving distributed system of connected vehicles, and extends our previous work titled "<em>Querying Large Vehicular Networks: How to Balance On-Board Workload and Queries Response Time?</em>" (Romaric Duvignau, Bastian Havers, Vincenzo Gulisano, Marina Papatriantafilou) which was published at the 22nd Intelligent Transportation Systems Conference (ITSC) in 2019.</p>

<p>The paper (open access) is available here: <a href="https://ieeexplore.ieee.org/abstract/document/9562541">https://ieeexplore.ieee.org/abstract/document/9562541</a>. The abstract follows:</p>

<p>As Vehicular Networks rely increasingly on sensed data to enhance functionality and safety, efficient and distributed data analysis is needed to effectively leverage new technologies in real-world applications. Considering the tens of GBs per hour sensed by modern connected vehicles, traditional analysis, based on global data accumulation, can rapidly exhaust the capacity of the underlying network, becoming increasingly costly, slow, or even infeasible.<br>Employing the edge processing paradigm, which aims at alleviating this drawback by leveraging vehicles' computational power, we are the first to study how to localize, efficiently and distributively, relevant data in a vehicular fleet for analysis applications. This is achieved by appropriate methods to spread requests across the fleet, while efficiently balancing the time needed to identify relevant vehicles, and the computational overhead induced on the Vehicular Network.<br>We evaluate our techniques using two large sets of real-world data in a realistic environment where vehicles join or leave the fleet during the distributed data localization process. As we show, our algorithms are both efficient and configurable, outperforming the baseline algorithms by up to a $40\times$ speedup while reducing computational overhead by up to $3\times$, while providing good estimates for the fraction of vehicles with relevant data and fairly spreading the workload over the fleet. All code as well as detailed instructions are available at \url{https://github.com/dcs-chalmers/dataloc_vn}.</p>
