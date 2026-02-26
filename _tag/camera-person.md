---
title: "Camera Person"
layout: archive
collection: tag
permalink: /tag/camera-person
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'camera person'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}