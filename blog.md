---
layout: "page"
title: "Blog"
permalink: "/blog/"
---

<div class="post-list">
{% for post in site.posts %}
  <article class="post-list-item">
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %-d, %Y" }}</time>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    <p>{{ post.excerpt | strip_html | normalize_whitespace | truncatewords: 42 }}</p>
  </article>
{% endfor %}
</div>
