---
title: "painting animation generation"
collection: tag
permalink: /tag/painting animation generation
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", painting animation generation | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}