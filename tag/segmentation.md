---
title: "segmentation"
collection: tag
permalink: /tag/segmentation
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", segmentation | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}