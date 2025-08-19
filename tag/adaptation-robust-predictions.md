---
title: "adaptation robust predictions"
collection: tag
permalink: /tag/adaptation robust predictions
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", adaptation robust predictions | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}