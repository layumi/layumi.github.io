---
title: "Real Data Robust"
layout: archive
collection: tag
permalink: /tag/real-data-robust
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'real data robust'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}