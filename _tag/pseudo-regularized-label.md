---
title: "Pseudo Regularized Label"
layout: archive
collection: tag
permalink: /tag/pseudo-regularized-label
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'pseudo regularized label'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}