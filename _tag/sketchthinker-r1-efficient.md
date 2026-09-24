---
title: "Sketchthinker R1 Efficient"
layout: archive
collection: tag
permalink: /tag/sketchthinker-r1-efficient
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'sketchthinker r1 efficient'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}