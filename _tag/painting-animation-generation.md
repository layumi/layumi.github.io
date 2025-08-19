---
title: "Painting Animation Generation"
layout: archive
collection: tag
permalink: /tag/painting-animation-generation
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'painting animation generation'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}