---
title: "camera style adaptation"
collection: tag
permalink: /tag/camera style adaptation
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", camera style adaptation | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}