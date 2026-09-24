---
title: "Pillar Based Ranking"
layout: archive
collection: tag
permalink: /tag/pillar-based-ranking
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'pillar based ranking'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}