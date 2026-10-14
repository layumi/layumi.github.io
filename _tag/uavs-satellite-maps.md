---
title: "Uavs Satellite Maps"
layout: archive
collection: tag
permalink: /tag/uavs-satellite-maps
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'uavs satellite maps'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}