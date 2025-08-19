---
title: "macro micro adversarial"
collection: tag
permalink: /tag/macro-micro-adversarial
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'macro micro adversarial'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}