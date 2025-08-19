---
title: "Retrieval Hierarchical Uncertainty"
collection: tag
permalink: /tag/retrieval-hierarchical-uncertainty
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'retrieval hierarchical uncertainty'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}