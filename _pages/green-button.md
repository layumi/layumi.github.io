---
title: "Blooming!!"
excerpt: "Blooming!!"
sitemap: false
permalink: /greenbutton.html
---

![](https://zdzheng.xyz/images/boom.png)

Oh! You press the green button. A warning is sent to Dr. Zheng. 

The server of Zhedong will be restarted in several minutes!  He will have one minute to take a rest!

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
