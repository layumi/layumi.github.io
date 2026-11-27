---
title: "Spatial Reasoning"
layout: archive
collection: tag
permalink: /tag/spatial-reasoning
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'spatial reasoning'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}