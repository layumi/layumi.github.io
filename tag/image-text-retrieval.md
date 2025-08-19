---
title: "image text retrieval"
collection: tag
permalink: /tag/image text retrieval
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", image text retrieval | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}