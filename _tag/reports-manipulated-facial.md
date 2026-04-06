---
title: "Reports Manipulated Facial"
layout: archive
collection: tag
permalink: /tag/reports-manipulated-facial
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'reports manipulated facial'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}