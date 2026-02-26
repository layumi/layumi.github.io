---
title: "Mirror Clothing"
layout: archive
collection: tag
permalink: /tag/mirror-clothing
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'mirror clothing'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}