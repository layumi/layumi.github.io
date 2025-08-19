---
title: "thinking text guided"
collection: tag
permalink: /tag/thinking text guided
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", thinking text guided | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}