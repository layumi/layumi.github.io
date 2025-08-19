---
title: "ctrl robust conditional"
collection: tag
permalink: /tag/ctrl robust conditional
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", ctrl robust conditional | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}