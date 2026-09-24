---
title: "Makeup Identity"
layout: archive
collection: tag
permalink: /tag/makeup-identity
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'makeup identity'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}