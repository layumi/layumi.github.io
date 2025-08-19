---
title: "regularization vivo"
collection: tag
permalink: /tag/regularization vivo
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", regularization vivo | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}