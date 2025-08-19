---
title: "drones geotext"
collection: tag
permalink: /tag/drones-geotext
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'drones geotext'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}