---
title: "Ranking Image Text"
layout: archive
collection: tag
permalink: /tag/ranking-image-text
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'ranking image text'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}