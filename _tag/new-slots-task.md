---
title: "new slots task"
collection: tag
permalink: /tag/new-slots-task
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'new slots task'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}