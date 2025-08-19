---
title: "Based Person Retrieval"
collection: tag
permalink: /tag/based-person-retrieval
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'based person retrieval'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}