---
title: "Aigc"
layout: archive
collection: tag
permalink: /tag/aigc
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'aigc'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}