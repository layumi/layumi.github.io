---
title: "Adversarial Queries Opposite"
layout: archive
collection: tag
permalink: /tag/adversarial-queries-opposite
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'adversarial queries opposite'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}