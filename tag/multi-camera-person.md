---
title: "multi camera person"
collection: tag
permalink: /tag/multi-camera-person
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'multi camera person'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}