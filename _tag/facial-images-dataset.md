---
title: "Facial Images Dataset"
layout: archive
collection: tag
permalink: /tag/facial-images-dataset
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'facial images dataset'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}