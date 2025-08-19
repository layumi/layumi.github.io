---
title: "based geo localization"
collection: tag
permalink: /tag/based-geo-localization
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'based geo localization'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}