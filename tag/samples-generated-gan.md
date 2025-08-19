---
title: "samples generated gan"
collection: tag
permalink: /tag/samples generated gan
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", samples generated gan | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}