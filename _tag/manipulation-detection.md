---
title: "Manipulation Detection"
layout: archive
collection: tag
permalink: /tag/manipulation-detection
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'manipulation detection'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}