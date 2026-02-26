---
title: "High Fidelity Makeup"
layout: archive
collection: tag
permalink: /tag/high-fidelity-makeup
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'high fidelity makeup'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}