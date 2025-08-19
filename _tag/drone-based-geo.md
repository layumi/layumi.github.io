---
title: "Drone Based Geo"
layout: archive
collection: tag
permalink: /tag/drone-based-geo
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'drone based geo'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}