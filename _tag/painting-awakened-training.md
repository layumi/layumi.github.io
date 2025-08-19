---
title: "Painting Awakened Training"
collection: tag
permalink: /tag/painting-awakened-training
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'painting awakened training'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}