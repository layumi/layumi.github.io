---
title: "sampling dense reaction"
collection: tag
permalink: /tag/sampling dense reaction
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", sampling dense reaction | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}