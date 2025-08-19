---
title: "framework scene adaptation"
collection: tag
permalink: /tag/framework scene adaptation
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", framework scene adaptation | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}