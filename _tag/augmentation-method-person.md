---
title: "Augmentation Method Person"
layout: archive
collection: tag
permalink: /tag/augmentation-method-person
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'augmentation method person'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}