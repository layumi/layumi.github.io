---
title: "Filtering Wora Paradigm"
layout: archive
collection: tag
permalink: /tag/filtering-wora-paradigm
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'filtering wora paradigm'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}