---
title: "Smile Generating Diverse"
layout: archive
collection: tag
permalink: /tag/smile-generating-diverse
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'smile generating diverse'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}