---
layout: page
navbar: Archives
title: Group RNA-Puzzles
footer: false
---

<p>Introduction to the Group category here</p>

<!-- 开始：博客归档区域，使用 Schema.org 定义博客相关元数据 -->
<div id="blog-archives" itemscope itemtype="http://schema.org/Blog">

<!-- 开始：Schema.org 元数据 -->
<meta itemprop="name" content="{{ site.title }}" />
{% if site.description %}
<meta itemprop="description" content="{{ site.description }}" />
{% endif %}
<meta itemprop="url" content="{{ site.url }}" />
<!-- 结束：Schema.org 元数据 -->

<!-- 开始：循环遍历所有属于 "group" 分类的文章，使用 reverse 顺序（最新的在前） -->
{% for post in site.posts reverse %}
{% if post.categories contains 'group' %}

<!-- 捕获当前文章的年份 -->
{% capture this_year %}{{ post.date | date: "%Y" }}{% endcapture %}

<!-- 如果当前文章的年份与上一次不一致，则显示年份标题 -->
{% unless year == this_year %}
{% assign year = this_year %}
<h2 class="year">{{ year }}</h2>
{% endunless %}

<!-- 开始：单篇文章区域，使用 Schema.org 定义博客文章 -->
<article class="page-header" itemprop="blogPost" itemscope itemtype="http://schema.org/BlogPosting">
<!-- 包含每篇文章的归档模板，通过 include 引入 archive_post.html -->
{% include archive_post.html %}
</article>
<!-- 结束：单篇文章区域 -->

{% endif %}
{% endfor %}
<!-- 结束：循环遍历所有属于分类的文章 -->

</div>
<!-- 结束：博客归档区域 -->
