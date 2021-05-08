---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on <u><a href="https://scholar.google.com/citations?user=XT17oUEAAAAJ">my Google Scholar profile</a>.</u>

Publications:  [2021](#2021), [2020](#2020), [2019](#2019), [2018](#2018), [2017](#2017)

<hr>

{% include base_path %}

### 2021

{% for post in site.publications reversed %}
  {%if post.pub_year == '2021' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}

### 2020

{% for post in site.publications reversed %}
  {% if post.pub_year == '2020' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}

### 2019

{% for post in site.publications reversed %}
  {% if post.pub_year == '2019' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}

### 2018

{% for post in site.publications reversed %}
  {% if post.pub_year == '2018' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}

### 2017

{% for post in site.publications reversed %}
  {% if post.pub_year == '2017' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}