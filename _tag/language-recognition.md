---
title: "Language Recognition"
layout: archive
collection: tag
permalink: /tag/language-recognition
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'language recognition'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}