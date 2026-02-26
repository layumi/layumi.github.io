---
title: "Mllm Crafted Narratives"
layout: archive
collection: tag
permalink: /tag/mllm-crafted-narratives
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'mllm crafted narratives'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}