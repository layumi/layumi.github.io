---
title: "Scene Adaptation"
layout: archive
collection: tag
permalink: /tag/scene-adaptation
author_profile: false
---

{% assign pubs_tag = site.publications | where_exp:"item", "item.keywords contains 'scene adaptation'" | sort: "venue" %}
{% for post in pubs_tag %}
  {% include archive-single.html %}
{% endfor %}