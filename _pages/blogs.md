---
layout: archive
title: "Blogs"
permalink: /blogs/
author_profile: true
---

{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% for post in site.blogs %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% if year != written_year %}
    {% capture written_year %}{{ year }}{% endcapture %}
  {% endif %}
  {% include archive-single.html %}
{% endfor %}
