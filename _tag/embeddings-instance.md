---
title: "Embeddings Instance"
collection: tag
permalink: /tag/embeddings-instance
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'embeddings instance'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}