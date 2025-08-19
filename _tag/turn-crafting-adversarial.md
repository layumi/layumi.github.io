---
title: "turn crafting adversarial"
collection: tag
permalink: /tag/turn-crafting-adversarial
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'turn crafting adversarial'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}