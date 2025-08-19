---
title: "bayesian query"
collection: tag
permalink: /tag/bayesian-query
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'bayesian query'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}