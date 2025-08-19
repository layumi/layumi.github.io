---
title: "robust vehicle identification"
collection: tag
permalink: /tag/robust-vehicle-identification
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'robust vehicle identification'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}