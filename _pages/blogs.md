---
layout: archive
title: "Blogs"
permalink: /blogs/
author_profile: true
---

Most posts are personal reading notes written for academic discussion and knowledge dissemination. The comments focus on technical content and reflect the author's understanding at the time of writing. Errors and alternative interpretations are welcome.

{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% for post in site.posts %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% if year != written_year %}
    {% capture written_year %}{{ year }}{% endcapture %}
  {% endif %}
  {% include archive-single.html %}
{% endfor %}
