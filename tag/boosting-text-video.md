---
title: "boosting text video"
collection: tag
permalink: /tag/boosting text video
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", boosting text video | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}