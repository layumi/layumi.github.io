---
title: "Eyeglasses Removal"
layout: archive
collection: tag
permalink: /tag/eyeglasses-removal
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'eyeglasses removal'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}