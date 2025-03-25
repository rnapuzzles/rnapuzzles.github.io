---
title: "Miao Lab - Home"
layout: homelay
excerpt: "Miao Lab at Guangzhou Laboratory"
sitemap: false
permalink: /
---



<!-- 这是主页，受到default.html和homelay.html的影响，使用news.html作为侧边栏 -->
<html class="no-js" lang="en">

{% include style.html %}

  <body>
    <!-- Begin: Skip Link (for Accessibility) -->
    <a href="#content" class="sr-only sr-only-focusable">Skip to main content</a>
    <!-- End: Skip Link -->

    <!-- Begin: Main Wrapper -->
    <div id="wrap">
      <!-- Begin: Main Content Section -->
      <div id="main" role="main" class="container">
        <div id="content">
          <div class="row">
            <!-- Begin: Blog/Content Area (占用8列) -->
            <div class="page-content col-md-8">
              <div class="blog-index" itemscope itemtype="http://schema.org/Blog">
                <!-- Schema.org Metadata -->
                <meta itemprop="name" content="RNA-Puzzles" />
                <meta itemprop="description" content="RNA-Puzzles a community-wide blind evaluation of RNA 3D structure prediction." />
                <meta itemprop="url" content="http://www.rnapuzzles.org" />

                <!-- 主要标题及简介 -->
                <h2>RNA-Puzzles</h2> is a collective experiment for blind RNA structure prediction.<br/>
                The sequence of a solved RNA structure is confidentially communicated to participating modelling groups a couple of weeks prior to publication. The results are assessed and presented in common publications involving structuralists and modellers.<br/>
                <hr/>

                <!-- Begin: Panel - Aims of the Project -->
                <div class="panel panel-info">
                  <div class="panel-heading">
                    <h3 class="panel-title">Aims of the project</h3>
                  </div>
                  <!-- 项目目标列表 -->
                  <li>To determine the capabilities and limitations of current computational methods of 3D RNA structure prediction based on sequence;</li>
                  <li>To assess progress made and to improve assessment protocols and methods;</li>
                  <li>To identify whether there are specific bottlenecks that hold back progress;</li>
                  <li>To promote the available methods and guide potential users in the choice of suitable tools;</li>
                  <li>To encourage the RNA structure prediction community in their efforts to improve the current tools and to make automated prediction tools available;</li>
                  <li>To explore the underlying mechanism of ligand-RNA binding and associated conformational changes.</li>
                </div>
                <!-- End: Panel - Aims of the Project -->

                <!-- Begin: Panel - Basic Rules -->
                <div class="panel panel-info">
                  <div class="panel-heading">
                    <h3 class="panel-title">
                      Basic Rules <a style="color:red">(PLEASE READ CAREFULLY)</a>
                    </h3>
                  </div>
                  <!-- 基本规则列表 -->
                  <li>Confidential agreement required from new users: "I will use the provided sequence data for prediction purposes only. I will not distribute the sequences in any form outside my working group."</li>
                  <li>It is strongly recommended to avoid assessment error that all the predictions be formatted in standard <b><a href="https://cdn.rcsb.org/wwpdb/docs/documentation/file-format/PDB_format_1992.pdf">PDB format</a></b>. We provide a python script <b><a href="https://chichaumiau.github.io/RNA-Puzzles_format/">here</a></b> for generating standard PDB format files into which the coordinates need to be replaced by the predictors.</li>
                  <li>Please name the submission file without space in the file name. The suggested names are: PZ#_Method.pdb for web servers and PZ#_GroupName.pdb for human predictors.</li>
                  <li>RNA chains should be named in alphabetical order: A for the first chain, B for the second chain, and so on.</li>
                  <li>Up to <b>FIVE</b> prediction models should be submitted as the final results for each puzzle from each prediction method. Each prediction group can submit results from several prediction methods (automatic or manual, etc.).</li>
                  <li>Please put all prediction models together in one PDB file as in the NMR format (Separate models by lines: "MODEL n" and "ENDMDL").</li>
                  <li>For submission, please either use the online <a href="http://www.rnapuzzles.org/open-puzzle/">registration and submission</a> portal (see the open-puzzle tag: http://www.rnapuzzles.org/open-puzzle/) or send us an <b><a href="mailto:e.westhof@ibmc-cnrs.unistra.fr?cc=ibmc.cnrs@gmail.com&amp;subject=RNA-Puzzles%20Submission">email</a></b> (Please send an email to e.westhof@ibmc-cnrs.unistra.fr and cc. ibmc.cnrs@gmail.com).</li>
                  <li>For structure comparison metrics, please refer to RNA-Puzzles toolkit at <a href="https://chichaumiau.github.io/rnapuzzlestoolkit">https://chichaumiau.github.io/rnapuzzlestoolkit</a>. Please find the reference at <a href="https://pubmed.ncbi.nlm.nih.gov/31799609/">Nucleic Acids Res. 2020 Jan 24;48(2):576-588</a>. To use evaluation metrics in CASP15, please also refer to the repos: <a href="https://github.com/DasLab/casp-rna">https://github.com/DasLab/casp-rna</a> and <a href="https://github.com/DasLab/CASP15_RNA_EM">https://github.com/DasLab/CASP15_RNA_EM</a>. The reference can be found at <a href="">biorxiv</a>.</li>
                </div>
                <!-- End: Panel - Basic Rules -->

                <!-- Begin: Panel - Call for Participants -->
                <div class="panel panel-info">
                  <div class="panel-heading">
                    <h3 class="panel-title">Call for participants</h3>
                  </div>
                  <!-- 参与者招募信息 -->
                  <li>We hope more structural biologists can help us in providing more crystallographic, cryo-EM or NMR structures. Any kind of RNA related structure information is encouraged. Anyone who may have a RNA structure ready for publication please contact <a href="mailto:e.westhof@ibmc-cnrs.unistra.fr?cc=ibmc.cnrs@gmail.com&amp;subject=[RNA-Puzzles]%20Structure%20Provide">us</a> (Please send an email to e.westhof@ibmc-cnrs.unistra.fr and cc. ibmc.cnrs@gmail.com).</li>
                  <li>We encourage more predictors who are interested in RNA structure prediction to take part in this compitition to push forward the field. Anyone who is interested please send us an <a href="mailto:e.westhof@ibmc-cnrs.unistra.fr?subject=[Help]%20RNA-Puzzles&cc=ibmc.cnrs@gmail.com">email</a> (Please send an email to e.westhof@ibmc-cnrs.unistra.fr and cc. ibmc.cnrs@gmail.com).</li>
                </div>
                <!-- End: Panel - Call for Participants -->

                <!-- Begin: Panel - Updates -->
                <div class="panel panel-info">
                  <div class="panel-heading">
                    <h3 class="panel-title">Updates</h3>
                  </div>
                  <!-- 最近更新列表 -->
                  <div class="list-group">
                    <article class="list-group-item">
                      <span class="glyphicon glyphicon-tags"></span>&nbsp;
                      <span class="categories">
                        <a class="category" href="ç">news</a>
                      </span>
                      &nbsp;&nbsp;&nbsp;
                      <a href="/news/2023/10/07/Submission-Process.html" itemprop="url">Submission Process</a>
                    </article>
                    <article class="list-group-item">
                      <span class="glyphicon glyphicon-tags"></span>&nbsp;
                      <span class="categories">
                        <a class="category" href="/blog/news_category/">news</a>
                      </span>
                      &nbsp;&nbsp;&nbsp;
                      <a href="/news/2023/10/07/Research-Spectrum.html" itemprop="url">Research Spectrum</a>
                    </article>
                    <article class="list-group-item">
                      <span class="glyphicon glyphicon-tags"></span>&nbsp;
                      <span class="categories">
                        <a class="category" href="/blog/news_category/">news</a>
                      </span>
                      &nbsp;&nbsp;&nbsp;
                      <a href="/news/2023/10/07/Recent-Engagements.html" itemprop="url">Recent Engagements</a>
                    </article>
                    <article class="list-group-item">
                      <span class="glyphicon glyphicon-tags"></span>&nbsp;
                      <span class="categories">
                        <a class="category" href="/blog/news_category/">news</a>
                      </span>
                      &nbsp;&nbsp;&nbsp;
                      <a href="/news/2023/10/07/Participating-Teams.html" itemprop="url">Participating Teams</a>
                    </article>
                    <article class="list-group-item">
                      <span class="glyphicon glyphicon-tags"></span>&nbsp;
                      <span class="categories">
                        <a class="category" href="/blog/news_category/">news</a>
                      </span>
                      &nbsp;&nbsp;&nbsp;
                      <a href="/news/2023/10/07/Methodological-Progress.html" itemprop="url">Methodological Progress</a>
                    </article>
                    <article class="list-group-item">
                      <span class="glyphicon glyphicon-tags"></span>&nbsp;
                      <span class="categories">
                        <a class="category" href="/blog/news_category/">news</a>
                      </span>
                      &nbsp;&nbsp;&nbsp;
                      <a href="/news/2023/10/07/Future-Outlook.html" itemprop="url">Future Outlook</a>
                    </article>
                    <article class="list-group-item">
                      <span class="glyphicon glyphicon-tags"></span>&nbsp;
                      <span class="categories">
                        <a class="category" href="/blog/results_category/">results</a>
                      </span>
                      &nbsp;&nbsp;&nbsp;
                      <a href="/results/2017/11/18/PZ39.html" itemprop="url">Puzzle 39</a>
                    </article>
                    <article class="list-group-item">
                      <span class="glyphicon glyphicon-tags"></span>&nbsp;
                      <span class="categories">
                        <a class="category" href="/blog/results_category/">results</a>
                      </span>
                      &nbsp;&nbsp;&nbsp;
                      <a href="/results/2017/11/18/PZ38.html" itemprop="url">Puzzle 38</a>
                    </article>
                    <article class="list-group-item">
                      <span class="glyphicon glyphicon-tags"></span>&nbsp;
                      <span class="categories">
                        <a class="category" href="/blog/results_category/">results</a>
                      </span>
                      &nbsp;&nbsp;&nbsp;
                      <a href="/results/2017/11/18/PZ37.html" itemprop="url">Puzzle 37</a>
                    </article>
                    <article class="list-group-item">
                      <span class="glyphicon glyphicon-tags"></span>&nbsp;
                      <span class="categories">
                        <a class="category" href="/blog/results_category/">results</a>
                      </span>
                      &nbsp;&nbsp;&nbsp;
                      <a href="/results/2017/11/18/PZ36.html" itemprop="url">Puzzle 36</a>
                    </article>
                  </div>
                </div>
                <!-- End: Panel - Updates -->
              </div>
            </div>
            <!-- End: Blog/Content Area -->
          </div>
        </div>
      </div>
      <!-- End: Main Content Section -->
    </div>
    <!-- End: Main Wrapper -->

    <!-- Begin: Footer Section -->
    <footer role="contentinfo">
      <div class="container">
        <p class="text-muted credits" align="center">
          &copy; 2025 - 
          <a href="mailto:miao_zhichao@gzlab.ac.cn">Chichau Miao</a>; 
          The website is powered by <a href="https://www.cloudna.cn/">cloudna</a>.
          <a id="to-top" href="#top" class="btn btn-dark btn-lg">
            <i class="fa fa-chevron-up fa-fw fa-1x"></i>
          </a>
        </p>
      </div>
    </footer>
    <!-- End: Footer Section -->

    <!-- Begin: Disqus Comment Count Script -->
    <script type="text/javascript">
      var disqus_shortname = 'rna-puzzles';
      var disqus_script = 'count.js';
      (function () {
        var dsq = document.createElement('script');
        dsq.type = 'text/javascript';
        dsq.async = true;
        dsq.src = '//' + disqus_shortname + '.disqus.com/' + disqus_script;
        (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
      }());
    </script>
    <!-- End: Disqus Comment Count Script -->

    <!-- Begin: JavaScript Files -->
    <script src="/js/bootstrap_puzzles.min.js"></script>
    <script src="/javascripts/modernizr.js"></script>
    <!-- Custom Theme JavaScript -->
    <script>
      // Closes the sidebar menu when #menu-close is clicked
      $("#menu-close").click(function(e) {
        e.preventDefault();
        $("#sidebar-wrapper").toggleClass("active");
      });
      // Opens the sidebar menu when #menu-toggle is clicked
      $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#sidebar-wrapper").toggleClass("active");
      });
      // Smooth scroll for internal anchor links
      $(function() {
        $('a[href*=#]:not([href=#],[data-toggle],[data-target],[data-slide])').click(function() {
          if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') || location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
              $('html,body').animate({
                scrollTop: target.offset().top
              }, 1000);
              return false;
            }
          }
        });
      });
    </script>
    <!-- End: JavaScript Files -->
  </body>
</html>
