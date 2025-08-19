---
title: "Parallel Voice Conversion"
collection: tag
permalink: /tag/parallel-voice-conversion
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'parallel voice conversion'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}