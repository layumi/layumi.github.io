---
title: "Uncertainty Detecting Hallucination"
collection: tag
permalink: /tag/uncertainty-detecting-hallucination
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'uncertainty detecting hallucination'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}