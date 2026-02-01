---
title: "Object Interaction"
layout: archive
collection: tag
permalink: /tag/object-interaction
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'object interaction'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}