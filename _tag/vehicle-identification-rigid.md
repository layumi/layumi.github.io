---
title: "vehicle identification rigid"
collection: tag
permalink: /tag/vehicle-identification-rigid
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'vehicle identification rigid'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}