---
title: "Drone Videos Bevs"
layout: archive
collection: tag
permalink: /tag/drone-videos-bevs
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'drone videos bevs'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}