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
  {% if post.date == "2021-01-01"}
      {% include archive-single.html %}
{% endfor %}

### 2020

{% for post in site.publications reversed %}
  {% if post.date == "2020-01-01"}
      {% include archive-single.html %}
{% endfor %}

### 2019

{% for post in site.publications reversed %}
  {% if post.date == "2019-01-01"}
      {% include archive-single.html %}
{% endfor %}

### 2018

{% for post in site.publications reversed %}
  {% if post.date == "2018-01-01"}
      {% include archive-single.html %}
{% endfor %}

### 2017

{% for post in site.publications reversed %}
  {% if post.date == "2017-01-01"}
      {% include archive-single.html %}
{% endfor %}