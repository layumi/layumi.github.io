---
title: "Identity Preservation Makeup"
layout: archive
collection: tag
permalink: /tag/identity-preservation-makeup
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'identity preservation makeup'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}