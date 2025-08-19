---
title: "video retrieval"
collection: tag
permalink: /tag/video retrieval
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", video retrieval | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}