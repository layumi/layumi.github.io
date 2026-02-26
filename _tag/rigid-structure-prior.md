---
title: "Rigid Structure Prior"
layout: archive
collection: tag
permalink: /tag/rigid-structure-prior
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'rigid structure prior'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}