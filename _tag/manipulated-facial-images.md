---
title: "Manipulated Facial Images"
layout: archive
collection: tag
permalink: /tag/manipulated-facial-images
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'manipulated facial images'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}