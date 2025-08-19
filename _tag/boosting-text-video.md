---
title: "Boosting Text Video"
layout: archive
collection: tag
permalink: /tag/boosting-text-video
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'boosting text video'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}