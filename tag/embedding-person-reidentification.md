---
title: "embedding person reidentification"
collection: tag
permalink: /tag/embedding person reidentification
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", embedding person reidentification | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}