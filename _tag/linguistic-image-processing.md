---
title: "Linguistic Image Processing"
layout: archive
collection: tag
permalink: /tag/linguistic-image-processing
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'linguistic image processing'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}