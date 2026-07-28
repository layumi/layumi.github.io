---
title: "University of Macau Advanced Research Institute in Hengqin"
layout: archive
collection: funding
permalink: /funding/University-of-Macau-Advanced-Research-Institute-in-Hengqin
author_profile: false
---

{% assign pubs_fund = site.publications | where_exp:"item", "item.funding contains 'University of Macau Advanced Research Institute in Hengqin'" | sort: "date" | reverse %}
{% for post in pubs_fund %}
  {% include archive-single.html %}
{% endfor %}