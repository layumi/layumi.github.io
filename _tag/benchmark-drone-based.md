---
title: "Benchmark Drone Based"
layout: archive
collection: tag
permalink: /tag/benchmark-drone-based
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'benchmark drone based'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}