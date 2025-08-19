---
title: "Adaptation Robust Predictions"
collection: tag
permalink: /tag/adaptation-robust-predictions
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'adaptation robust predictions'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}