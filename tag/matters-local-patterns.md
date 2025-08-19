---
title: "matters local patterns"
collection: tag
permalink: /tag/matters local patterns
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", matters local patterns | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}