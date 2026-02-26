---
title: "Pose Virtual Try"
layout: archive
collection: tag
permalink: /tag/pose-virtual-try
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'pose virtual try'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}