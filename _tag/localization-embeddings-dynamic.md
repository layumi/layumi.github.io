---
title: "Localization Embeddings Dynamic"
collection: tag
permalink: /tag/localization-embeddings-dynamic
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'localization embeddings dynamic'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}