---
title: "3D Motion Generation"
layout: archive
collection: tag
permalink: /tag/3d-motion-generation
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains '3d motion generation'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}