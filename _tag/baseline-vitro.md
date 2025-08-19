---
title: "baseline vitro"
collection: tag
permalink: /tag/baseline-vitro
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'baseline vitro'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}