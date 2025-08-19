---
title: "eyeglasses removal wild"
collection: tag
permalink: /tag/eyeglasses-removal-wild
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'eyeglasses removal wild'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}