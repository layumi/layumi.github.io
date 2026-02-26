---
title: "Image Text Embeddings"
layout: archive
collection: tag
permalink: /tag/image-text-embeddings
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'image text embeddings'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}