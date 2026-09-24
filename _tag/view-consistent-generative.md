---
title: "View Consistent Generative"
layout: archive
collection: tag
permalink: /tag/view-consistent-generative
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'view consistent generative'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}