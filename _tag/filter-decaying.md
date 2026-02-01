---
title: "Filter Decaying"
layout: archive
collection: tag
permalink: /tag/filter-decaying
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'filter decaying'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}