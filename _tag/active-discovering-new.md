---
title: "Active Discovering New"
layout: archive
collection: tag
permalink: /tag/active-discovering-new
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'active discovering new'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}