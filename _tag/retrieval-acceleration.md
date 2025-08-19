---
title: "Retrieval Acceleration"
layout: archive
collection: tag
permalink: /tag/retrieval-acceleration
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'retrieval acceleration'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}