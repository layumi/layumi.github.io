---
title: "Collaborative Group"
layout: archive
collection: tag
permalink: /tag/collaborative-group
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'collaborative group'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}