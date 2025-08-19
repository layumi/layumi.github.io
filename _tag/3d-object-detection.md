---
title: "3D Object Detection"
layout: archive
collection: tag
permalink: /tag/3d-object-detection
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains '3d object detection'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}