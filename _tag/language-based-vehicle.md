---
title: "Language Based Vehicle"
layout: archive
collection: tag
permalink: /tag/language-based-vehicle
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'language based vehicle'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}