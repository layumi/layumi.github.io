---
title: "Samples Generated Gan"
layout: archive
collection: tag
permalink: /tag/samples-generated-gan
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'samples generated gan'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}