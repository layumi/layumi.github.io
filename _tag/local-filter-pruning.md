---
title: "Local Filter Pruning"
layout: archive
collection: tag
permalink: /tag/local-filter-pruning
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'local filter pruning'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}