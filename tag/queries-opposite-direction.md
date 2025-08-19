---
title: "queries opposite direction"
collection: tag
permalink: /tag/queries opposite direction
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", queries opposite direction | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}