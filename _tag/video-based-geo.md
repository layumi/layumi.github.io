---
title: "Video Based Geo"
collection: tag
permalink: /tag/video-based-geo
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'video based geo'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}