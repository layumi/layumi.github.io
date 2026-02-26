---
title: "Person Retrieval Large"
layout: archive
collection: tag
permalink: /tag/person-retrieval-large
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'person retrieval large'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}