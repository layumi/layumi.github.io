---
title: "Identification 3D Space"
layout: archive
collection: tag
permalink: /tag/identification-3d-space
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'identification 3d space'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}