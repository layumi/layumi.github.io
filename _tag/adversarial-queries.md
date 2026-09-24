---
title: "Adversarial Queries"
layout: archive
collection: tag
permalink: /tag/adversarial-queries
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'adversarial queries'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}