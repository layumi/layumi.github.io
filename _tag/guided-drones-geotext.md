---
title: "Guided Drones Geotext"
layout: archive
collection: tag
permalink: /tag/guided-drones-geotext
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'guided drones geotext'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}