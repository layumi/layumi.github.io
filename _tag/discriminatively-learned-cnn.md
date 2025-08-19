---
title: "Discriminatively Learned Cnn"
collection: tag
permalink: /tag/discriminatively-learned-cnn
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'discriminatively learned cnn'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}