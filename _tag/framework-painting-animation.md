---
title: "Framework Painting Animation"
layout: archive
collection: tag
permalink: /tag/framework-painting-animation
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'framework painting animation'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}