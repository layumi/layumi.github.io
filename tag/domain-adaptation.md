---
title: "domain adaptation"
collection: tag
permalink: /tag/domain adaptation
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", domain adaptation | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}