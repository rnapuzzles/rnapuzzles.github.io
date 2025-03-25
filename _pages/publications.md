---
title: "Miao Lab - Publications"
layout: gridlay
excerpt: "Miao Lab -- Publications."
sitemap: false
permalink: /publication/
---
<head>
    <!-- Begin: HEAD Section -->
    <meta charset="utf-8">
    <title>RNA-Puzzles</title>
    <meta name="author" content="Chichau Miao">

    <!-- Mobile Optimization Meta Tags -->
    <meta name="HandheldFriendly" content="True">
    <meta name="MobileOptimized" content="320">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- SEO: Canonical URL, Favicon, and Alternate Feed -->
    <link rel="canonical" href="http://www.rnapuzzles.org/">
    <link href="/favicon.png" type="image/png" rel="icon">
    <link href="/atom.xml" rel="alternate" title="RNA-Puzzles" type="application/atom+xml">

    <!-- Open Graph / Twitter Meta Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta property="og:type" content="website">
    <meta property="og:url" content="http://www.rnapuzzles.org/">
    <meta property="og:title" content="RNA-Puzzles">
    <meta property="og:description" content="RNA-Puzzles a community-wide blind evaluation of RNA 3D structure prediction.">

    <!-- jQuery -->
    <script src="/js/jquery-3.2.1.min.js"></script>

    <!-- CSS Files -->
    <link href="/css/bootstrap.min.css" rel="stylesheet" type="text/css">
    <link href="/css/stylish-portfolio.css" rel="stylesheet" type="text/css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
    <link href="//jpswalsh.github.io/academicons/css/academicons.css" rel="stylesheet">
    <link href="/stylesheets/screen.css" media="screen, projection, print" rel="stylesheet" type="text/css">
    <!-- End: HEAD Section -->
</head>

# Publications

(# co-first author, * corresponding author)

## Group highlights

(For a full list of publications and patents see [below](#full-list-of-publications) or go to 
[Google Scholar](https://scholar.google.com/citations?user=OUFQCssAAAAJ), 
[ORCID](https://orcid.org/0000-0002-5777-9815))

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ publi.title }}</pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ publi.description }}</p>
  <p>{{ publi.authors }}</p>
  <p><em><strong><a href="{{ publi.link.url }}">{{ publi.link.display }}</a></strong></em></p>
  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>
  <p> {{ publi.news2 }}</p>
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<p> &nbsp; </p>


## Full List of publications

{% for publi in site.data.publist %}

  <b>{{ publi.title }}</b> <br />
  {{ publi.authors }} <br /><em><a href="{{ publi.link.url }}">{{ publi.link.display }}</a></em>

{% endfor %}
