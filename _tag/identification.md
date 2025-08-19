---
title: "Identification"
collection: tag
permalink: /tag/identification
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'identification'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}