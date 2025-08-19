---
title: "annotations sufficient video"
collection: tag
permalink: /tag/annotations-sufficient-video
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'annotations sufficient video'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}