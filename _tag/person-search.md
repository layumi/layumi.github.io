---
title: "Person Search"
layout: archive
collection: tag
permalink: /tag/person-search
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'person search'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}