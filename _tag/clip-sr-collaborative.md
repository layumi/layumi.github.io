---
title: "Clip Sr Collaborative"
layout: archive
collection: tag
permalink: /tag/clip-sr-collaborative
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'clip sr collaborative'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}