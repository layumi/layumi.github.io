---
title: "object re-identification"
collection: tag
permalink: /tag/object re-identification
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", object re-identification | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}