---
title: "Oil Painting Normalization"
layout: archive
collection: tag
permalink: /tag/oil-painting-normalization
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'oil painting normalization'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}