---
title: "retrieval"
collection: tag
permalink: /tag/retrieval
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", retrieval | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}