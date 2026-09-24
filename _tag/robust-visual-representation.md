---
title: "Robust Visual Representation"
layout: archive
collection: tag
permalink: /tag/robust-visual-representation
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'robust visual representation'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}