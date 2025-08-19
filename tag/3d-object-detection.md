---
title: "3d object detection"
collection: tag
permalink: /tag/3d object detection
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", 3d object detection | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}