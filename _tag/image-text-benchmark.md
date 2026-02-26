---
title: "Image Text Benchmark"
layout: archive
collection: tag
permalink: /tag/image-text-benchmark
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'image text benchmark'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}