---
title: "Unifying Uav Reasoning"
layout: archive
collection: tag
permalink: /tag/unifying-uav-reasoning
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'unifying uav reasoning'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}