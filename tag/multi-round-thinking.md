---
title: "multi round thinking"
collection: tag
permalink: /tag/multi round thinking
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", multi round thinking | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}