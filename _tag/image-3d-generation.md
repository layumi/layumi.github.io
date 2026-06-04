---
title: "Image 3D Generation"
layout: archive
collection: tag
permalink: /tag/image-3d-generation
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'image 3d generation'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}