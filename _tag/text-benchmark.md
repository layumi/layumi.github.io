---
title: "text benchmark"
collection: tag
permalink: /tag/text-benchmark
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'text benchmark'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}