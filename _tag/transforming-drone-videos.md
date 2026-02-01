---
title: "Transforming Drone Videos"
layout: archive
collection: tag
permalink: /tag/transforming-drone-videos
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'transforming drone videos'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}