---
title: "thinking text guided"
collection: tag
permalink: /tag/thinking-text-guided
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'thinking text guided'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}