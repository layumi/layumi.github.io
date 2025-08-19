---
title: "person identification 3d"
collection: tag
permalink: /tag/person identification 3d
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", person identification 3d | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}