---
title: "sparse sampling"
collection: tag
permalink: /tag/sparse sampling
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", sparse sampling | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}