---
title: "ctrl robust"
collection: tag
permalink: /tag/ctrl-robust
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'ctrl robust'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}