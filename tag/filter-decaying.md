---
title: "filter decaying"
collection: tag
permalink: /tag/filter decaying
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", filter decaying | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}