---
title: "data curation filtering"
collection: tag
permalink: /tag/data-curation-filtering
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'data curation filtering'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}