---
title: "Person Anomaly"
layout: archive
collection: tag
permalink: /tag/person-anomaly
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'person anomaly'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}