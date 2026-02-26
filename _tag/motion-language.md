---
title: "Motion Language"
layout: archive
collection: tag
permalink: /tag/motion-language
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'motion language'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}