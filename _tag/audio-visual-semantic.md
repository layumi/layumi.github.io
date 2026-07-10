---
title: "Audio Visual Semantic"
layout: archive
collection: tag
permalink: /tag/audio-visual-semantic
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'audio visual semantic'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}