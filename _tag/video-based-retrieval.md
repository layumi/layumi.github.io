---
title: "Video Based Retrieval"
layout: archive
collection: tag
permalink: /tag/video-based-retrieval
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'video based retrieval'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}