---
title: "Cloud Representation"
layout: archive
collection: tag
permalink: /tag/cloud-representation
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'cloud representation'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}