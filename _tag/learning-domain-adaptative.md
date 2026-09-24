---
title: "Learning Domain Adaptative"
layout: archive
collection: tag
permalink: /tag/learning-domain-adaptative
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'learning domain adaptative'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}