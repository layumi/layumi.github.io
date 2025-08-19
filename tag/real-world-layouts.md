---
title: "real world layouts"
collection: tag
permalink: /tag/real world layouts
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", real world layouts | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}