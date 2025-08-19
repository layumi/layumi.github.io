---
title: "path convolutional image"
collection: tag
permalink: /tag/path-convolutional-image
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'path convolutional image'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}