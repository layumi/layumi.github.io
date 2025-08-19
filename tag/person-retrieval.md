---
title: "person retrieval"
collection: tag
permalink: /tag/person retrieval
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", person retrieval | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}