---
title: "Uav Reasoning"
layout: archive
collection: tag
permalink: /tag/uav-reasoning
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'uav reasoning'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}