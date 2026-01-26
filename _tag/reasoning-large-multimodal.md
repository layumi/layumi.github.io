---
title: "Reasoning Large Multimodal"
layout: archive
collection: tag
permalink: /tag/reasoning-large-multimodal
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'reasoning large multimodal'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}