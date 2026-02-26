---
title: "Gan Improve Person"
layout: archive
collection: tag
permalink: /tag/gan-improve-person
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'gan improve person'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}