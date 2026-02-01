---
title: "Language Guided Drones"
layout: archive
collection: tag
permalink: /tag/language-guided-drones
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'language guided drones'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}