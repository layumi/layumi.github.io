---
title: "data curation"
collection: tag
permalink: /tag/data curation
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", data curation | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}