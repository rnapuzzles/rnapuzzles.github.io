---
layout: page
title: "show"
date: 2018-01-23 11:09
comments: false
sharing: false
footer: false
---
<!-- 以下内容直接作为文章主体，使用 include 进行模块化 -->
{% include molstar-params.html %}

<table class="clear" cellspacing="5">
  <tr>
    <script type="text/javascript">
      document.write(`Puzzle <b>${puzzlen}</b>  Model <b>${modeln}</b> from <b>${lab}</b> lab<br/><br/>`);
    </script>
  </tr>
</table>

{% include molstar-resources.html %}

<table class="clear" cellspacing="5">
  <tr valign="top">
    <td class="clear" width="600">
      <div id="myViewer1" style="display: block;"></div>
      <div id="layer_dp" style="display: none;">
        <div class="result_title">Deformation Profile Matrix</div>
        <script type="text/javascript">
          document.write(`<div id="gallery"><a href="/pdbFiles/${puzzlen}/dp/${idParam}.webp" title="${idParam}.png"><img src="/pdbFiles/${puzzlen}/dp/${idParam}.webp" height="500"/></a></div>`);
        </script>
        Click figure to zoom in.
      </div>
    </td>
    <td class="clear">
      <table class="preview-table" cellspacing="5">
        <tr>
          <td class="left">
            <div id="myViewer_small" style="display: block;"></div>
            <a class="btn btn-info" href="javascript:toggle('molstar');"><< show Molstar</a>
          </td>
        </tr>
        <tr>
          <td class="left">
            <div id="small_png" style="display: block;">
              <img id="small_png_img" style="max-width:100%; max-height:100%;" alt="PNG preview">
            </div>
            <a class="btn btn-info" href="javascript:toggle('image');"><< show PNG</a>
            <script type="text/javascript">
              document.getElementById('small_png_img').src = '/pdbFiles/' + puzzlen + '/dp/' + idParam + '.webp';
            </script>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>

{% include molstar-init.html %}
{% include toggle-function.html %}

<span style="color:green;">GREEN</span>: <span style="color:black;">X-Ray structure</span>; <span style="color:blue;">BLUE</span>: Proposed model.
