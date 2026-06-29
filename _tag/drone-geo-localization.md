---
title: "Drone Geo Localization"
layout: archive
collection: tag
permalink: /tag/drone-geo-localization
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'drone geo localization'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}