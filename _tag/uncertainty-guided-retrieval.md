---
title: "Uncertainty Guided Retrieval"
layout: archive
collection: tag
permalink: /tag/uncertainty-guided-retrieval
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'uncertainty guided retrieval'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}