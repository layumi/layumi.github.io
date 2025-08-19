---
title: "sign language recognition"
collection: tag
permalink: /tag/sign language recognition
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", sign language recognition | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}