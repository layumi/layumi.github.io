---
title: "composed image retrieval"
collection: tag
permalink: /tag/composed image retrieval
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", composed image retrieval | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}