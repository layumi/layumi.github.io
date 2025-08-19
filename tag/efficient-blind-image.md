---
title: "efficient blind image"
collection: tag
permalink: /tag/efficient blind image
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", efficient blind image | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}