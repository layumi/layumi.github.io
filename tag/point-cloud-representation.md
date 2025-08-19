---
title: "point cloud representation"
collection: tag
permalink: /tag/point cloud representation
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", point cloud representation | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}