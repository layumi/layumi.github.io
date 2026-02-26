---
title: "Reaction Predictions"
layout: archive
collection: tag
permalink: /tag/reaction-predictions
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'reaction predictions'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}