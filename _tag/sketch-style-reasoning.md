---
title: "Sketch Style Reasoning"
layout: archive
collection: tag
permalink: /tag/sketch-style-reasoning
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'sketch style reasoning'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}