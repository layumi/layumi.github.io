---
title: "text embeddings instance"
collection: tag
permalink: /tag/text embeddings instance
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", text embeddings instance | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}