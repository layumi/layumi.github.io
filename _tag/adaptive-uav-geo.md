---
title: "Adaptive Uav Geo"
layout: archive
collection: tag
permalink: /tag/adaptive-uav-geo
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'adaptive uav geo'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}