---
title: "Spatial Intelligence"
layout: archive
collection: tag
permalink: /tag/spatial-intelligence
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'spatial intelligence'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}