---
title: "Invariant Drone Geo"
layout: archive
collection: tag
permalink: /tag/invariant-drone-geo
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'invariant drone geo'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}