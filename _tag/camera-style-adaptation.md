---
title: "Camera Style Adaptation"
collection: tag
permalink: /tag/camera-style-adaptation
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'camera style adaptation'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}