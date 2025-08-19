---
title: "Non Parallel Voice"
collection: tag
permalink: /tag/non-parallel-voice
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'non parallel voice'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}