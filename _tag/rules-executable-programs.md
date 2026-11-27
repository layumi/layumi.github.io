---
title: "Rules Executable Programs"
layout: archive
collection: tag
permalink: /tag/rules-executable-programs
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'rules executable programs'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}