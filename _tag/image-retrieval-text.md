---
title: "Image Retrieval Text"
layout: archive
collection: tag
permalink: /tag/image-retrieval-text
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'image retrieval text'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}