---
title: "magic mirror clothing"
collection: tag
permalink: /tag/magic mirror clothing
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", magic mirror clothing | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}