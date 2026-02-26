---
title: "Drones Geotext 1652"
layout: archive
collection: tag
permalink: /tag/drones-geotext-1652
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'drones geotext 1652'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}