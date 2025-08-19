---
title: "Visual Representation Vehicle"
layout: archive
collection: tag
permalink: /tag/visual-representation-vehicle
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'visual representation vehicle'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}