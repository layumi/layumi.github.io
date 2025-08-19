---
title: "Ctrl Robust Conditional"
collection: tag
permalink: /tag/ctrl-robust-conditional
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'ctrl robust conditional'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}