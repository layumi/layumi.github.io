---
title: "Unsupervised Eyeglasses"
layout: archive
collection: tag
permalink: /tag/unsupervised-eyeglasses
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'unsupervised eyeglasses'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}