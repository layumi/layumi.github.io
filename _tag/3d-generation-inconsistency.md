---
title: "3D Generation Inconsistency"
layout: archive
collection: tag
permalink: /tag/3d-generation-inconsistency
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains '3d generation inconsistency'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}