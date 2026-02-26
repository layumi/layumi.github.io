---
title: "Cnn Embedding Person"
layout: archive
collection: tag
permalink: /tag/cnn-embedding-person
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'cnn embedding person'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}