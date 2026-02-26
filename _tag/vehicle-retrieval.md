---
title: "Vehicle Retrieval"
layout: archive
collection: tag
permalink: /tag/vehicle-retrieval
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'vehicle retrieval'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}