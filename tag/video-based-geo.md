---
title: "video based geo"
collection: tag
permalink: /tag/video based geo
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", video based geo | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}