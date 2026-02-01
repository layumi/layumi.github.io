---
title: "Queries Opposite Direction"
layout: archive
collection: tag
permalink: /tag/queries-opposite-direction
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'queries opposite direction'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}