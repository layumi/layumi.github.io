---
title: "person anomaly search"
collection: tag
permalink: /tag/person anomaly search
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", person anomaly search | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}