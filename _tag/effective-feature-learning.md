---
title: "effective feature learning"
collection: tag
permalink: /tag/effective-feature-learning
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'effective feature learning'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}