---
title: "Robust Aerial Geo"
layout: archive
collection: tag
permalink: /tag/robust-aerial-geo
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'robust aerial geo'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}