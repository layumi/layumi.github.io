---
title: "pedestrian alignment"
collection: tag
permalink: /tag/pedestrian alignment
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", pedestrian alignment | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}