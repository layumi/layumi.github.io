---
title: "Blooming!!"
excerpt: "Blooming!!"
sitemap: false
permalink: /redbutton.html
---

![](https://zdzheng.xyz/images/boom.png)

Oh! You press the red button. A warning is sent to Dr. Zheng. 

The server of Zhedong will be shut down in several minutes!  He will have 5 minutes to take a rest!

Perhaps you were looking for one of these? 

<hr>

### Sitemap

<strong><a href="https://zdzheng.xyz/sitemap"> [https://zdzheng.xyz/sitemap]</a></strong> 

### Recent Publications

{% for post in site.publications reversed %}
  {%if post.pub_year == '2022' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}
