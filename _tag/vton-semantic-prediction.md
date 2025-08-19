---
title: "Vton Semantic Prediction"
collection: tag
permalink: /tag/vton-semantic-prediction
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'vton semantic prediction'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}