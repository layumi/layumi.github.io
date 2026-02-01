---
title: "Learning Person Identification"
layout: archive
collection: tag
permalink: /tag/learning-person-identification
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'learning person identification'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}