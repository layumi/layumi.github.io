---
title: "pruning image retrieval"
collection: tag
permalink: /tag/pruning image retrieval
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", pruning image retrieval | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}