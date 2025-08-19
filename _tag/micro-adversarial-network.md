---
title: "Micro Adversarial Network"
collection: tag
permalink: /tag/micro-adversarial-network
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'micro adversarial network'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}