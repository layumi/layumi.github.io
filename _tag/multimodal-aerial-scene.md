---
title: "Multimodal Aerial Scene"
layout: archive
collection: tag
permalink: /tag/multimodal-aerial-scene
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'multimodal aerial scene'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}