---
title: "Retrieval Consensus"
layout: archive
collection: tag
permalink: /tag/retrieval-consensus
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'retrieval consensus'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}