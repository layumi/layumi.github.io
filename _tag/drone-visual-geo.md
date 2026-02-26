---
title: "Drone Visual Geo"
layout: archive
collection: tag
permalink: /tag/drone-visual-geo
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'drone visual geo'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}