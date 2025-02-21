---
layout: post
title: "Bujnicki Group"
date: 2017-11-16 10:44:22 +0000
comments: false
categories: 
- group
---
<!--
# [Bujnicki Group]()
-->
<a href="https://genesilico.pl/people" target="_blank">**Bujnicki** </a> group is International Institute of Molecular and Cell Biology in Warsaw, Poland.
<a href="https://genesilico.pl/" target="_blank"><strong></br>(Click here to find more information about Bujnicki Group)</strong></a>
</br>
</br>
* [**ModeRNA**](http://iimcb.genesilico.pl/modernaserver/): RNA tertiary structure prediction with ModeRNA.</br>
* [**SimRNA**](http://genesilico.pl/SimRNAweb/): a coarse-grained method for RNA folding simulations and 3D structure prediction.</br>
* [**ModeRNA program**](http://www.genesilico.pl/moderna/)</br>
* [**SimRNA program**](http://genesilico.pl/software/stand-alone/simrna/)

## Prediction Approaches:
**Strategy I**: Typically, we use a hybrid modeling strategy based on the approach used earlier for protein structure prediction. First, the RNA target sequence is analyzed to identify homologous sequences and to generate a multiple sequence alignment. At this stage we also try to determine similarity to any other RNA with experimentally determined structure. If such RNA is identified, it is used as a template to build a model of the target molecule (or its parts) using a template-based (comparative) modeling method ModeRNA. If the molecule lacks a template, or if certain regions of the molecule cannot be modeled by template-based modeling, they are subjected to template-free folding simulations using the coarse-grained method SimRNA. Template-free folding can be aided by spatial restraints obtained from computational predictions (e.g., information on the secondary structure predicted from the sequence alignment) and from experimental analyses (e.g., on contacts between residues that interact in 3D). Finally, models are refined using the QRNAS method that extends the AMBER force field with energy terms explicitly modeling hydrogen bonds, idealizes base pair planarity and regularizes the backbone conformation. A tutorial that presents this strategy with a detailed example is available: Piatkowski P, Kasprzak JM, Kumar D, Magnus M, Chojnowski G, Bujnicki JM. RNA 3D Structure Modeling by Combination of Template-Based Method ModeRNA, Template-Free Folding with SimRNA, and Refinement with QRNAS. Methods Mol Biol. 2016;1490:217-35

**Strategy II**: Recently, in collaboration with the Das group, we have started exploring another strategy, also inspired by successful protein structure prediction. This approach requires a sequence alignment of the target RNA with several homologs. Initially, models are built using the template-free approach for several different sequences. Structural fragments corresponding to the evolutionary conserved regions (in particular helices) – determined from the alignment – are extracted from all models and clustered to identify the most common structural arrangement. The model of the target RNA can be then subjected to refinement, e.g., as in strategy I. This approach is currently under development.

## A real case:
Prokaryotic ribosomal protein genes are typically grouped within highly conserved operons. In many cases, one or more of the encoded proteins not only bind to a specific site in the ribosomal RNA, but also to a motif localized within their own mRNA, and thereby regulate expression of the operon. We used computational methods to predict an RNA motif present in many bacterial phyla within the 5′ untranslated region of operons encoding ribosomal proteins S6 and S18. We demonstrated experimentally that this region in RNA indeed functions as the S6:S18 complex-binding motif (S6S18CBM). This motif contains a conserved CCG sequence presented in a bulge flanked by a stem and a hairpin structure. A similar structure containing a CCG trinucleotide forms the S6:S18 complex binding site in 16S ribosomal RNA. We have constructed a 3D structural model of a S6:S18 complex with S6S18CBM, using a combination of template-based and template-free modeling. The model explained how the CCG trinucleotide in a specific structural context could be specifically recognized by the S18 protein. Our prediction was supported by site-directed mutagenesis of both RNA and protein components. Overall, this study, which combined RNA sequence analysis, computational structure modeling, and biochemical analyses, provided a molecular basis for understanding protein-RNA recognition in the regulation of S6 and S18 protein expression.
[fig]
S6:S18 ribosomal protein complex interacts with a structural motif present in its own mRNA. Matelska D, Purta E, Panek S, Boniecki MJ, Bujnicki JM, Dunin-Horkawicz S. RNA. 2013 Oct;19(10):1341-8.
## Publications:
<!-- >
1.	Magnus, M. et al. RNA-Puzzles toolkit: a computational resource of RNA 3D structure benchmark datasets, structure manipulation, and evaluation tools. Nucleic Acids Res. 48, 576–588 (2020).
8.	Wirecki, T. K. et al. RNAProbe: a web server for normalization and analysis of RNA structure probing data. Nucleic Acids Res. 48, W292–W299 (2020).
9.	Chojnowski, G., Waleń, T. & Bujnicki, J. M. RNA Bricks—a database of RNA 3D motifs and their interactions. Nucleic Acids Res. 42, D123–D131 (2013).
10.	Ruiz-Carmona, S. et al. rDock: A Fast, Versatile and Open Source Program for Docking Ligands to Proteins and Nucleic Acids. PLoS Comput. Biol. 10, e1003571 (2014).
11.	Tuszynska, I., Magnus, M., Jonak, K., Dawson, W. & Bujnicki, J. M. NPDock: a web server for protein–nucleic acid docking. Nucleic Acids Res. 43, W425–W430 (2015).
12.	Boniecki, M. J. et al. SimRNA: a coarse-grained method for RNA folding simulations and 3D structure prediction. Nucleic Acids Res. 44, e63 (2016).
13.	Wirecki, T. K., Nithin, C., Mukherjee, S., Bujnicki, J. M. & Boniecki, M. J. Modeling of Three-Dimensional RNA Structures Using SimRNA. Protein Structure Prediction 103–125 (2020).
14.	Stasiewicz, J., Mukherjee, S., Nithin, C. & Bujnicki, J. M. QRNAS: software tool for refinement of nucleic acid structures. BMC Struct. Biol. 19, 1–11 (2019).
15.	Szulc, N. A., Mackiewicz, Z., Bujnicki, J. M. & Stefaniak, F. fingeRNAt—A novel tool for high-throughput analysis of nucleic acid-ligand interactions. PLoS Comput. Biol. 18, e1009783 (2022).
69.	Perez, A., MacCallum, J. L. & Dill, K. A. Accelerating molecular simulations of proteins using Bayesian inference on weak information. Proc. Natl. Acad. Sci. U. S. A. 112, 11846–11851 (2015).
<-->

1.	Wirecki TK, Merdas K, Bernat A, Boniecki MJ, Bujnicki JM, Stefaniak F. [RNAProbe: a web server for normalization and analysis of RNA structure probing data.](https://pubmed.ncbi.nlm.nih.gov/32504492/) Nucleic Acids Res. 2020 Jul 2;48(W1):W292-W299. 
2.	Chojnowski G, Walen T, Bujnicki JM. [RNA Bricks--a database of RNA 3D motifs and their interactions.](https://pubmed.ncbi.nlm.nih.gov/24220091/) Nucleic Acids Res. 2014 Jan;42(Database issue):D123-31. 
3. Tuszynska I, Magnus M, Jonak K, Dawson W, Bujnicki JM. [NPDock: a web server for protein-nucleic acid docking.](https://pubmed.ncbi.nlm.nih.gov/25977296/) Nucleic Acids Res. 2015 Jul 1;43(W1):W425-30. 
4. Boniecki MJ, Lach G, Dawson WK, Tomala K, Lukasz P, Soltysinski T, Rother KM, Bujnicki JM. [SimRNA: a coarse-grained method for RNA folding simulations and 3D structure prediction.](https://pubmed.ncbi.nlm.nih.gov/26687716/) Nucleic Acids Res. 2016 Apr 20;44(7):e63. 
5. Wirecki TK, Nithin C, Mukherjee S, Bujnicki JM, Boniecki MJ. [Modeling of Three-Dimensional RNA Structures Using SimRNA.](https://pubmed.ncbi.nlm.nih.gov/32621221/) Methods Mol Biol. 2020;2165:103-125. 
6. Stasiewicz J, Mukherjee S, Nithin C, Bujnicki JM. [QRNAS: software tool for refinement of nucleic acid structures.](https://pubmed.ncbi.nlm.nih.gov/30898165/) BMC Struct Biol. 2019 Mar 21;19(1):5. 
7. Szulc NA, Mackiewicz Z, Bujnicki JM, Stefaniak F. [fingeRNAt-A novel tool for high-throughput analysis of nucleic acid-ligand interactions.](https://pubmed.ncbi.nlm.nih.gov/35653385/) PLoS Comput Biol. 2022 Jun 2;18(6):e1009783.

