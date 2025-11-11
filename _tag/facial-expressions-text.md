---
title: "Facial Expressions Text"
layout: archive
collection: tag
permalink: /tag/facial-expressions-text
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'facial expressions text'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}