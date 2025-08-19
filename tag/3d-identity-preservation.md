---
title: "3d identity preservation"
collection: tag
permalink: /tag/3d identity preservation
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", 3d identity preservation | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}