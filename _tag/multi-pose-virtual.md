---
title: "Multi Pose Virtual"
layout: archive
collection: tag
permalink: /tag/multi-pose-virtual
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'multi pose virtual'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}