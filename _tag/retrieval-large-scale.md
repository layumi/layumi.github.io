---
title: "Retrieval Large Scale"
collection: tag
permalink: /tag/retrieval-large-scale
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'retrieval large scale'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}