---
title: "painting animation"
collection: tag
permalink: /tag/painting animation
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", painting animation | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}