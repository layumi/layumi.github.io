---
title: "crafting adversarial queries"
collection: tag
permalink: /tag/crafting-adversarial-queries
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'crafting adversarial queries'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}