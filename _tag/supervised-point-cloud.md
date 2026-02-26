---
title: "Supervised Point Cloud"
layout: archive
collection: tag
permalink: /tag/supervised-point-cloud
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'supervised point cloud'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}