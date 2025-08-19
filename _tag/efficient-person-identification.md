---
title: "Efficient Person Identification"
collection: tag
permalink: /tag/efficient-person-identification
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'efficient person identification'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}