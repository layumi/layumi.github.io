---
title: "sparse sampling dense"
collection: tag
permalink: /tag/sparse sampling dense
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", sparse sampling dense | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}