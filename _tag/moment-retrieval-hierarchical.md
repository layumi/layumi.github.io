---
title: "Moment Retrieval Hierarchical"
layout: archive
collection: tag
permalink: /tag/moment-retrieval-hierarchical
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'moment retrieval hierarchical'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}