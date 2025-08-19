---
title: "video moment retrieval"
collection: tag
permalink: /tag/video moment retrieval
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", video moment retrieval | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}