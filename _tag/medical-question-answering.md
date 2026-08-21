---
title: "Medical Question Answering"
layout: archive
collection: tag
permalink: /tag/medical-question-answering
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'medical question answering'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}