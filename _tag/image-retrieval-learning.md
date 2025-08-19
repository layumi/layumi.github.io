---
title: "Image Retrieval Learning"
layout: archive
collection: tag
permalink: /tag/image-retrieval-learning
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'image retrieval learning'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}