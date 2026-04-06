---
title: "Aerial Scene Reasoning"
layout: archive
collection: tag
permalink: /tag/aerial-scene-reasoning
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'aerial scene reasoning'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}