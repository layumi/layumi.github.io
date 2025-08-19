---
title: "Text Video Retrieval"
collection: tag
permalink: /tag/text-video-retrieval
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'text video retrieval'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}