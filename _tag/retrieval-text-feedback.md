---
title: "Retrieval Text Feedback"
collection: tag
permalink: /tag/retrieval-text-feedback
author_profile: false
---
{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'retrieval text feedback'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}