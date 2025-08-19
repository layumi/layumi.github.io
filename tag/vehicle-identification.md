---
title: "vehicle identification"
collection: tag
permalink: /tag/vehicle identification
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", vehicle identification | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}