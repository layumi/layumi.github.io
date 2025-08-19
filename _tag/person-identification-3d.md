---
title: "Person Identification 3D"
collection: tag
permalink: /tag/person-identification-3d
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'person identification 3d'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}