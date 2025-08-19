---
title: "detection 2d scene"
collection: tag
permalink: /tag/detection-2d-scene
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'detection 2d scene'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}