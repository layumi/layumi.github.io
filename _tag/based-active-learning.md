---
title: "Based Active Learning"
layout: archive
collection: tag
permalink: /tag/based-active-learning
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'based active learning'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}