---
title: "person re-id"
collection: tag
permalink: /tag/person re-id
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", person re-id | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}