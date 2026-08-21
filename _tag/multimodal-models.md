---
title: "Multimodal Models"
layout: archive
collection: tag
permalink: /tag/multimodal-models
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'multimodal models'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}