---
title: "Multimodal Search Agent"
layout: archive
collection: tag
permalink: /tag/multimodal-search-agent
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'multimodal search agent'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}