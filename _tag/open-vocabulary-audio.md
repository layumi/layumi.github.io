---
title: "Open Vocabulary Audio"
layout: archive
collection: tag
permalink: /tag/open-vocabulary-audio
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'open vocabulary audio'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}