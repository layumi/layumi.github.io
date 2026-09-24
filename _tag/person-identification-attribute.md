---
title: "Person Identification Attribute"
layout: archive
collection: tag
permalink: /tag/person-identification-attribute
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'person identification attribute'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}