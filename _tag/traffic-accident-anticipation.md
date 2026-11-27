---
title: "Traffic Accident Anticipation"
layout: archive
collection: tag
permalink: /tag/traffic-accident-anticipation
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'traffic accident anticipation'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}