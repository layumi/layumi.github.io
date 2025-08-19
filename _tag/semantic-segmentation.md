---
title: "Semantic Segmentation"
collection: tag
permalink: /tag/semantic-segmentation
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'semantic segmentation'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}