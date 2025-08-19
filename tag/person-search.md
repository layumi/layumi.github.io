---
title: "person search"
collection: tag
permalink: /tag/person search
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", person search | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}