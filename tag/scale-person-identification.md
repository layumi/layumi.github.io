---
title: "scale person identification"
collection: tag
permalink: /tag/scale person identification
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", scale person identification | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}