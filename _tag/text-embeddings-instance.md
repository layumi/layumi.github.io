---
title: "Text Embeddings Instance"
collection: tag
permalink: /tag/text-embeddings-instance
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'text embeddings instance'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}