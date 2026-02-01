---
title: "Content-Based Retrieval"
layout: archive
collection: tag
permalink: /tag/content-based-retrieval
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'content-based retrieval'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}