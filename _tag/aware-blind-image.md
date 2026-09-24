---
title: "Aware Blind Image"
layout: archive
collection: tag
permalink: /tag/aware-blind-image
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'aware blind image'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}