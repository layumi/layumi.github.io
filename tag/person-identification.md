---
title: "person identification"
collection: tag
permalink: /tag/person identification
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", person identification | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}