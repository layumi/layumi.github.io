---
title: "adversarial networks 3d"
collection: tag
permalink: /tag/adversarial-networks-3d
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'adversarial networks 3d'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}