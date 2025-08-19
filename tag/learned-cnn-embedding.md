---
title: "learned cnn embedding"
collection: tag
permalink: /tag/learned-cnn-embedding
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'learned cnn embedding'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}