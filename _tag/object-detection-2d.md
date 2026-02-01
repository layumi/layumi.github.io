---
title: "Object Detection 2D"
layout: archive
collection: tag
permalink: /tag/object-detection-2d
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'object detection 2d'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}