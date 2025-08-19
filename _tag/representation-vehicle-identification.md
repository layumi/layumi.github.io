---
title: "Representation Vehicle Identification"
collection: tag
permalink: /tag/representation-vehicle-identification
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'representation vehicle identification'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}