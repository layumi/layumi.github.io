---
title: "Image Retrieval Ranking"
layout: archive
collection: tag
permalink: /tag/image-retrieval-ranking
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'image retrieval ranking'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}