---
title: "Aware Bounding Boxes"
layout: archive
collection: tag
permalink: /tag/aware-bounding-boxes
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'aware bounding boxes'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}