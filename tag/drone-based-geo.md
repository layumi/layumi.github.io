---
title: "drone based geo"
collection: tag
permalink: /tag/drone based geo
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", drone based geo | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}