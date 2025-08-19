---
title: "adjacent filter decaying"
collection: tag
permalink: /tag/adjacent-filter-decaying
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'adjacent filter decaying'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}