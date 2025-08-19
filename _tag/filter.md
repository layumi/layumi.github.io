---
title: "Filter"
collection: tag
permalink: /tag/filter
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'filter'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}