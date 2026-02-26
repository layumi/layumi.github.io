---
title: "Self Supervised Point"
layout: archive
collection: tag
permalink: /tag/self-supervised-point
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'self supervised point'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}