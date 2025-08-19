---
title: "spg vton semantic"
collection: tag
permalink: /tag/spg vton semantic
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", spg vton semantic | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}