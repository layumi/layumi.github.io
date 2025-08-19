---
title: "vehicle identification high"
collection: tag
permalink: /tag/vehicle-identification-high
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'vehicle identification high'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}