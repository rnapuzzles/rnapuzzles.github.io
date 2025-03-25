---
layout: post
title: "Xiao Group"
date: 2017-11-16 11:08:41 +0000
comments: false
categories: 
- group
---
<!--
# [Xiao Group](http://biophy.hust.edu.cn) 
[<i class="fa fa-envelope-square fa-fw fa-2x"></i>](mailto:wj_hust08@hust.edu.cn?cc=yxiao@hust.edu.cn)
-->

<a href="" target="_blank">**Xiao** </a> group is from School of Physics of Huazhong University of Science and Technology in Wuhan, China.
<!--
<a href="" target="_blank"><strong></br>(Click here to find more information about Xiao Group)</strong></a>
</br>
-->

* [**3dRNA**](http://biophy.hust.edu.cn/3dRNA): Automatic building of ncRNA 3D structures.
* [**3dRNAscore**](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4446410/): Evaluation of RNA 3D structures.
* [**3dRNA program**](https://github.com/hust220/nsp): Automatic building of ncRNA 3D structures.
* [**3dRNAscore program**](http://biophy.hust.edu.cn/new/resources/3dRNAscore): Evaluation of RNA 3D structures.

## Prediction Approaches:
3dRNA is a fast and automated method of building ncRNA 3D structure based on sequence and 2D structure. It builds 3D RNA
				structure from the smallest secondary elements (SSEs), which are defined as helix, hairpin loop, internal loop, bulge
				loop, and junction loop. 3dRNA works as follows: in the first step, it uses a secondary structure tree (SST) to represent
				the RNA secondary structure. Each node in an SST corresponds to an SSE; in the second step, 3dRNA traverses the tree and
				match one or more suitable templates for each node from the 3D structure templates library. In the third step, 3dRNA traverses
				the tree again and assembles the matched templates of the node and its parent node every time it visits a node. So when
				finishing the traversing, a complete tertiary structure would be generated. Since each SSE may have multiple templates,
				we can get a lot of tertiary structures by using different templates for each SSE. When there are no appropriate templates
				for certain SSE, 3dRNA uses a distance geometry (DG) method to build a raw template for it. The last step is to cluster
				all the structures and then use 3dRNAscore to score cluster centers for the user to choose an appropriate structure.

## A real case:
3NDB is the Crystal structure of a signal sequence bound to the signal recognition particle in Methanocaldococcus jannaschii.
				We predicted the RNA chain (136 nt) of 3NDB. The secondary structure of 3NDB consists of 9 loops including 2 hairpin loops
				(HL), 5 internal loops (IL), 1 bulge loop (BL) and 1 multi-branch loop (ML). The 3D template of each of these loops can
				be found from the 3D structure templates library. The table shows the sources of the templates of all these loops. The
				3D structure of the rest helices are built according to the parameters of standard helix. We then assembled all the 3D
				structures of these loops and helices into an integral 3D structure. The RMSD of the predicted structure is 4.26 &#197;.
<!--
<img src="http://biophy.hust.edu.cn/image/xiao-intro.png" height=600/>
-->

## Publications:
<!--
1. Zhao, Y., et al., [Automated and fast building of three-dimensional RNA structures](https://www.nature.com/articles/srep00734). Scientific Reports, 2012. 2: p. 734.
2. Wang, J., et al., [3dRNAscore: a distance and torsion angle dependent evaluation function of 3D RNA structures](https://academic.oup.com/nar/article/43/10/e63/2408972?login=true). Nucleic Acids Res, 2015. 43(10): p. e63.
-->
1. Zhao Y, Huang Y, Gong Z, Wang Y, Man J, Xiao Y. [Automated and fast building of three-dimensional RNA structures.](https://pubmed.ncbi.nlm.nih.gov/23071898/) Sci Rep. 2012;2:734. 
2. Wang J, Zhao Y, Zhu C, Xiao Y. [3dRNAscore: a distance and torsion angle dependent evaluation function of 3D RNA structures.](https://pubmed.ncbi.nlm.nih.gov/25712091/) Nucleic Acids Res. 2015 May 26;43(10):e63. 