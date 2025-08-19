---
title: "data person identification"
collection: tag
permalink: /tag/data-person-identification
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'data person identification'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}