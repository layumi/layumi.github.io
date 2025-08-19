---
title: "Adaptative Semantic Segmentation"
collection: tag
permalink: /tag/adaptative-semantic-segmentation
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'adaptative semantic segmentation'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}