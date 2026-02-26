---
title: "Boosting Domain Adaptation"
layout: archive
collection: tag
permalink: /tag/boosting-domain-adaptation
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'boosting domain adaptation'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}