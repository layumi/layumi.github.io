---
title: "mirror clothing reconstruction"
collection: tag
permalink: /tag/mirror-clothing-reconstruction
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'mirror clothing reconstruction'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}