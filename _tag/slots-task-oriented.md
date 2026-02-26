---
title: "Slots Task Oriented"
layout: archive
collection: tag
permalink: /tag/slots-task-oriented
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'slots task oriented'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}