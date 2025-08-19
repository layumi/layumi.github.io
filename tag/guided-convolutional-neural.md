---
title: "guided convolutional neural"
collection: tag
permalink: /tag/guided-convolutional-neural
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'guided convolutional neural'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}