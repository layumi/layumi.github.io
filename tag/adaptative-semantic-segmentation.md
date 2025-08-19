---
title: "adaptative semantic segmentation"
collection: tag
permalink: /tag/adaptative semantic segmentation
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", adaptative semantic segmentation | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}