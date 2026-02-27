---
title: "Draw Differential Query"
layout: archive
collection: tag
permalink: /tag/draw-differential-query
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'draw differential query'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}