---
title: "Image Retrieval"
collection: tag
permalink: /tag/image-retrieval
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'image retrieval'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}