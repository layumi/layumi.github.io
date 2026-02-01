---
title: "Vehicle Identification"
layout: archive
collection: tag
permalink: /tag/vehicle-identification
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'vehicle identification'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}