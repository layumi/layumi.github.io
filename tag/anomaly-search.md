---
title: "anomaly search"
collection: tag
permalink: /tag/anomaly-search
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'anomaly search'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}