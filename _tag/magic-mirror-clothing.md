---
title: "Magic Mirror Clothing"
collection: tag
permalink: /tag/magic-mirror-clothing
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'magic mirror clothing'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}