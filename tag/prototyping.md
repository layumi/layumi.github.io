---
title: "prototyping"
collection: tag
permalink: /tag/prototyping
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", prototyping | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}