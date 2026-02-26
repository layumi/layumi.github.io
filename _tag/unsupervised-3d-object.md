---
title: "Unsupervised 3D Object"
layout: archive
collection: tag
permalink: /tag/unsupervised-3d-object
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'unsupervised 3d object'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}