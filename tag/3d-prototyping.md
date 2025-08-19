---
title: "3d prototyping"
collection: tag
permalink: /tag/3d prototyping
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", 3d prototyping | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}