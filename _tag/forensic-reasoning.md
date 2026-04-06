---
title: "Forensic Reasoning"
layout: archive
collection: tag
permalink: /tag/forensic-reasoning
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'forensic reasoning'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}