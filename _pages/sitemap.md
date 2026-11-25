---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

A list of all the posts and pages found on the site. For you robots out there is an [XML version]({{ base_path }}/sitemap.xml) available for digesting as well.

<h2>Pages</h2>
{% comment %}
  只列真正的 HTML 内容页。site.html_pages 已经排掉 .css / .json / .xml 这类构建产物
  （main.scss 编译出的 main.css、style.css、redirects.json、feed.xml、sitemap.xml 都曾是
  site.pages 的成员，在这里渲染成一串没有标题的空卡片）。
  sitemap: false 是 PDF 迁移后留下的重定向桩（files/*.pdf/index.md），
  redirect_from 生成的转跳页同样没有 title，两者都跳过。
{% endcomment %}
{% for post in site.html_pages %}
  {% if post.sitemap != false and post.title and post.title != "" %}
  {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2>Posts</h2>
{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}

{% capture written_label %}'None'{% endcapture %}

{% for collection in site.collections %}
{% unless collection.output == false or collection.label == "posts" %}
  {% capture label %}{{ collection.label }}{% endcapture %}
  {% if label != written_label %}
  <h2>{{ label }}</h2>
  {% capture written_label %}{{ label }}{% endcapture %}
  {% endif %}
{% endunless %}
{% for post in collection.docs %}
  {% unless collection.output == false or collection.label == "posts" %}
  {% if post.sitemap != false and post.title and post.title != "" %}
  {% include archive-single.html %}
  {% endif %}
  {% endunless %}
{% endfor %}
{% endfor %}