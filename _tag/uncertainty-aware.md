---
title: "Uncertainty Aware"
layout: archive
collection: tag
permalink: /tag/uncertainty-aware
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'uncertainty aware'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}