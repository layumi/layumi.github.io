---
title: "image retrieval"
collection: tag
permalink: /tag/image retrieval
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", image retrieval | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}