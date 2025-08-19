---
title: "oriented conversation"
collection: tag
permalink: /tag/oriented conversation
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", oriented conversation | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}