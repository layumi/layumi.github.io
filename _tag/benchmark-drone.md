---
title: "Benchmark Drone"
layout: archive
collection: tag
permalink: /tag/benchmark-drone
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'benchmark drone'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}