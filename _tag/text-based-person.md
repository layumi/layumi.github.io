---
title: "Text Based Person"
layout: archive
collection: tag
permalink: /tag/text-based-person
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'text based person'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}