---
title: "improving person identification"
collection: tag
permalink: /tag/improving person identification
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", improving person identification | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}