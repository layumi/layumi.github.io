---
title: "Visual Rules"
layout: archive
collection: tag
permalink: /tag/visual-rules
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'visual rules'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}