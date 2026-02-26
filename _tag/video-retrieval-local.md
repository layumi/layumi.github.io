---
title: "Video Retrieval Local"
layout: archive
collection: tag
permalink: /tag/video-retrieval-local
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'video retrieval local'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}