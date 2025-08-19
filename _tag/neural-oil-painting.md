---
title: "Neural Oil Painting"
layout: archive
collection: tag
permalink: /tag/neural-oil-painting
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'neural oil painting'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}