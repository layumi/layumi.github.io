---
title: "Image Retrieval Consensus"
layout: archive
collection: tag
permalink: /tag/image-retrieval-consensus
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'image retrieval consensus'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}