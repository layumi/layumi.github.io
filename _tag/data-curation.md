---
title: "Data Curation"
collection: tag
permalink: /tag/data-curation
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'data curation'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}