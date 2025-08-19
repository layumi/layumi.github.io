---
title: "3D Identity"
collection: tag
permalink: /tag/3d-identity
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains '3d identity'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}