---
title: "enhancing vehicle identification"
collection: tag
permalink: /tag/enhancing vehicle identification
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", enhancing vehicle identification | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}