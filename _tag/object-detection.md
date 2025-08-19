---
title: "Object Detection"
collection: tag
permalink: /tag/object-detection
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'object detection'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}