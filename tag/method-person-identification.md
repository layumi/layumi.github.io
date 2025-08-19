---
title: "method person identification"
collection: tag
permalink: /tag/method person identification
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", method person identification | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}