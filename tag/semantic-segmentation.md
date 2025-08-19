---
title: "semantic segmentation"
collection: tag
permalink: /tag/semantic segmentation
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", semantic segmentation | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}