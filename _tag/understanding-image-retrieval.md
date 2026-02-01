---
title: "Understanding Image Retrieval"
layout: archive
collection: tag
permalink: /tag/understanding-image-retrieval
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'understanding image retrieval'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}