---
title: "Navigation Uavs"
layout: archive
collection: tag
permalink: /tag/navigation-uavs
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'navigation uavs'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}