---
title: "text retrieval"
collection: tag
permalink: /tag/text retrieval
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", text retrieval | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}