---
title: "Grained Pedestrian Anomaly"
layout: archive
collection: tag
permalink: /tag/grained-pedestrian-anomaly
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'grained pedestrian anomaly'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}