---
title: "Collaborative Linguistic Image"
layout: archive
collection: tag
permalink: /tag/collaborative-linguistic-image
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'collaborative linguistic image'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}