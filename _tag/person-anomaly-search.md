---
title: "Person Anomaly Search"
collection: tag
permalink: /tag/person-anomaly-search
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'person anomaly search'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}