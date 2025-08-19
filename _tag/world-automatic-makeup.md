---
title: "World Automatic Makeup"
layout: archive
collection: tag
permalink: /tag/world-automatic-makeup
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'world automatic makeup'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}