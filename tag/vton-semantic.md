---
title: "vton semantic"
collection: tag
permalink: /tag/vton semantic
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", vton semantic | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}