---
title: "Identification Network Pruning"
layout: archive
collection: tag
permalink: /tag/identification-network-pruning
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'identification network pruning'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}