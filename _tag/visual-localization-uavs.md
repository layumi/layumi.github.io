---
title: "Visual Localization Uavs"
layout: archive
collection: tag
permalink: /tag/visual-localization-uavs
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'visual localization uavs'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}