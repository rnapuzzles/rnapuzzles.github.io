---
layout: post
title: "Chen Group"
date: 2017-11-16 11:07:03 +0000
comments: false
categories: 
- group
---
<!--
# [Chen Group](http://vfold.missouri.edu/)
-->
<a href="https://vfold.missouri.edu/chen-people02.html" target="_blank">**Chen** </a> group is from University of Missouri investigates the physical mechanism of RNA folding and develops predictive models for RNA structure and function.
<a href="https://vfold.missouri.edu/chen-lab02.html" target="_blank"><strong></br>(Click here to find more information about Chen Group)</strong></a>
</br>

* [**Vfold2D**](http://rna.physics.missouri.edu/vfold2D/index.html): Physics-based 2D structure prediction.
* [**VfoldCPX**](http://rna.physics.missouri.edu/vfoldCPX/index.html): RNA/RNA complexes 2D structure prediction.
* [**VfoldMTF**](http://rna.physics.missouri.edu/vfoldMTF): Motifs database with various topologies.
* [**Vfold3D**](http://rna.physics.missouri.edu/vfold3D/index.html): Motif-based 3D structure prediction.

## Prediction Approaches:
Generally, RNA structure prediction is based on a hierarchical strategy. First, for a given RNA sequence, the minimum free energy and suboptimal 2D structures are predicted by Vfold2D, which uses Vfold-derived motif-based loop free energies. In this stage, if the homologous sequence alignment data is available from Rfam or BLAST, we can also incorporate the information as constraint to the Vfold2D algorithm to predict the 2D structures. Second, from the given sequence and the 2D structure, Vfold3D predicts the 3D structures by assembling A-form helices and motif templates from known RNA structures. We use the sequence similarity scores to search for the optimal motif templates in the VfoldMTF database. To effectively enlarge the search space for the fragments, we allow zipping/unzipping of the terminal base pairs of the helix stems in order to relax the restrictions on the lengths of the loop branches. After that, some slight adjustments for the spatial arrangement of motifs may be necessary to eliminate inter-motif clash. Finally, the 3D structures are refined by the all-atom energy minimization through AMBER or NAMD. A tutorial that illustrates this strategy with detailed examples can be found in the following reference: Xu X, Chen SJ. A Method to Predict the 3D Structure of an RNA Scaffold. Methods Mol Biol. 2015;1316:1-11.
	
In the above approach, it is possible that no template can be found in the VfoldMTF database. Moreover, the current workflow of the Vfold software for 3D structure prediction is only semi-automated because it may require some manual efforts to, for example, remove steric clashes. A fully automated software/server is currently under development.

## A real case:
RNA aptamers are short single-stranded oligonucleotide ligands that can bind with high affinity and specificity to target molecules. The use of aptamers represents an emerging class of therapeutic strategy that can be easily adapted for personalized and precision medicine. Knowledge of the RNA aptamer’s structure would greatly facilitate and expedite the post-selection optimization steps required for translation, including truncation, chemical modification and chemical conjugation. Here, we use Vfold2D/Vfold3D computational model to predict the 2D and 3D structures of a 70-nucleotide long RNA aptamer (A9) for prostate specific membrane antigen (PSMA) and identify the key sequence/structure motifs (Reference: Rockey, et al. Zou, X., Chen, SJ., Giangrande, P.H. (2011) Rational truncation of an RNA aptamer to prostate specific membrane antigen using computational structural modeling. Nucleic Acid Therapeutic, 21: 299-314). Based on the predicted 2D structure of A9, a series of systematic changes, including nucleotide deletions/insertions/mutations, were introduced to alter the aptamer’s 2D/3D structure (predicted by Vfold2D/Vfold3D). The altered RNA sequences were then in vitro transcribed and validated experimentally to assess activity in an established functional assay. From the structure-activity relationship for different sequences and structures, the sequence and structural motifs that are essential for aptamer activity were identified. The stem-loop motif of A9g were found to be essential for the function. Overall, a structure modeling methodology, in combination with a standard functional assay, was used to determine key sequence and structural motifs of an RNA aptamer and this methodology can be easily applied to optimize other aptamers with therapeutic potential.
[fig]
The figures show the Vfold-predicted 2D and 3D structures of RNA aptamers. Reference: Xu X, Dickey DD, Chen SJ, Giangrande PH. Structural computational modeling of RNA aptamers. Methods. 2016;103:175-9.
## Publications:
1. Cheng Y, Zhang S, Xu X, Chen SJ. [Vfold2D-MC: A Physics-Based Hybrid Model for Predicting RNA Secondary Structure Folding.](https://pubmed.ncbi.nlm.nih.gov/34473508/) J Phys Chem B. 2021 Sep 16;125(36):10108-10118.
2. Cao S, Chen SJ. [Predicting RNA pseudoknot folding thermodynamics.](https://pubmed.ncbi.nlm.nih.gov/16709732/) Nucleic Acids Res. 2006 May 18;34(9):2634-52. 
3. Cao S, Chen SJ. [Predicting structures and stabilities for H-type pseudoknots with interhelix loops.](https://pubmed.ncbi.nlm.nih.gov/19237463/) RNA. 2009 Apr;15(4):696-706. 
4. Xu X, Zhao P, Chen SJ. [Vfold: a web server for RNA structure and folding thermodynamics prediction.](https://pubmed.ncbi.nlm.nih.gov/25215508/) PLoS One. 2014 Sep 12;9(9):e107504. 
5. Zhang S, Cheng Y, Guo P, Chen SJ. [VfoldMCPX: predicting multistrand RNA complexes.](https://pubmed.ncbi.nlm.nih.gov/35058350/) RNA. 2022 Apr;28(4):596-608. 
6. Xu X, Chen SJ. [A Method to Predict the Structure and Stability of RNA/RNA Complexes.](https://pubmed.ncbi.nlm.nih.gov/27665593/) Methods Mol Biol. 2016;1490:63-72. 
7. Cao S, Xu X, Chen SJ. [Predicting structure and stability for RNA complexes with intermolecular loop-loop base-pairing.](https://pubmed.ncbi.nlm.nih.gov/24751648/) RNA. 2014 Jun;20(6):835-45. 
8. Cao S, Chen SJ. [Physics-based de novo prediction of RNA 3D structures.](https://pubmed.ncbi.nlm.nih.gov/21413701/) J Phys Chem B. 2011 Apr 14;115(14):4216-26. 
9. Xu X, Zhao C, Chen SJ. [VfoldLA: A web server for loop assembly-based prediction of putative 3D RNA structures.](https://pubmed.ncbi.nlm.nih.gov/31173857/) J Struct Biol. 2019 Sep 1;207(3):235-240. 
10. Li J, Chen SJ. [RNAJP: enhanced RNA 3D structure predictions with non-canonical interactions and global topology sampling.](https://pubmed.ncbi.nlm.nih.gov/36864729/) Nucleic Acids Res. 2023 Apr 24;51(7):3341-3356.
11. Li J, Chen SJ. [RNA 3D Structure Prediction Using Coarse-Grained Models.](https://pubmed.ncbi.nlm.nih.gov/34277713/) Front Mol Biosci. 2021 Jul 2;8:720937. 
12. Li J, Zhang S, Chen SJ. [Advancing RNA 3D structure prediction: Exploring hierarchical and hybrid approaches in CASP15.](https://pubmed.ncbi.nlm.nih.gov/37615235/) Proteins. 2023 Dec;91(12):1779-1789. 
