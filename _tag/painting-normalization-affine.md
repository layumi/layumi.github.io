---
title: "Painting Normalization Affine"
layout: archive
collection: tag
permalink: /tag/painting-normalization-affine
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'painting normalization affine'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}