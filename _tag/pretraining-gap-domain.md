---
title: "Pretraining Gap Domain"
layout: archive
collection: tag
permalink: /tag/pretraining-gap-domain
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'pretraining gap domain'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}