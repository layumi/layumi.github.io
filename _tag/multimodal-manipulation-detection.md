---
title: "Multimodal Manipulation Detection"
layout: archive
collection: tag
permalink: /tag/multimodal-manipulation-detection
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'multimodal manipulation detection'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}