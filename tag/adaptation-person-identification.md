---
title: "adaptation person identification"
collection: tag
permalink: /tag/adaptation person identification
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", adaptation person identification | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}