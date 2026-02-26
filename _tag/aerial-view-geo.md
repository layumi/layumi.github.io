---
title: "Aerial View Geo"
layout: archive
collection: tag
permalink: /tag/aerial-view-geo
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'aerial view geo'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}