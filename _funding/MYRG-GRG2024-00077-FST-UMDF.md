---
title: "MYRG-GRG2024-00077-FST-UMDF"
layout: archive
collection: funding
permalink: /funding/MYRG-GRG2024-00077-FST-UMDF
author_profile: false
---

{% assign pubs_fund = site.publications | where_exp:"item", "item.funding contains 'MYRG-GRG2024-00077-FST-UMDF'" | sort: "date" | reverse %}
{% for post in pubs_fund %}
  {% include archive-single.html %}
{% endfor %}