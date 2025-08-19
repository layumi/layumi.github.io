---
title: "Real World Layouts"
layout: archive
collection: tag
permalink: /tag/real-world-layouts
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'real world layouts'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}