---
title: "Robust Vehicle"
collection: tag
permalink: /tag/robust-vehicle
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'robust vehicle'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}