---
title: "Modification Text Generation"
layout: archive
collection: tag
permalink: /tag/modification-text-generation
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'modification text generation'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}