---
title: "view geo localization"
collection: tag
permalink: /tag/view geo localization
author_profile: false
---
{% assign pubs_tag = site.publications | where:"keywords", view geo localization | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}