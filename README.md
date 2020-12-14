# Disease Resistance Genes

## (NLRs)

`Analysis Directory: ./dk_disease_resistance genes/duckweed_nbarc/`

`Analysis Code: workflow.dk_nbarc.txt` 

To find NLRs, the NB-ARC domain (PF00931) was used to scan the proteomes specified in Table 1 with HMMR (version 3.1b2) using the gathering bit score threshold.

## (AMPs)

`Analysis Directory: ./dk_disease_resistance genes/duckweed_amp/`

`Analysis Code: workflow.dk_amp.txt`

A total of 268 antimicrobial peptide sequences were analyzed from the PhytAMP database (Hammami et al., 2009). These peptide sequences were comprised of cyclotides, defensins, heveins, impatiens, knottins, lipid transfer proteins, sheperins, thionins, and vicilins. HMMR (version 3.1b2) was used to build HMMs for each peptide family. These HMMs were then used to search the proteomes specified in Table 1 using the gathering bit score threshold.
 
## (PRRs)

`Analysis Directory: ./dk_disease_resistance genes/duckweed_prr/`

`Analysis Code: workflow.dk_prr.txt`

PRRs were defined as illustrated in Boutret and Zipfel (2017).
 
To find PRRs, TMHMM2.0 was used to find transmembrane proteins in the proteomes specified in Table 1 (Krogh et al., 2001).

To find LRR-type PRRs, transmembrane proteins were scanned with the following LRR HMM models: PF00560.34, PF07723.14, PF07725.13, PF12799.8, PF13306.7, PF07723.14, PF07723.14, PF07723.14, PF18831.2, and PF18805.2 (Christopoulou et al., 2015). These LRR-containing transmembrane proteins were then scanned for a kinase domain (PF00069.26) to find LRR-RKs. Those LRR-containing transmembrane proteins without a kinase domain were designated as LRR-RPs.

To find LysM-type PRRs, transmembrane proteins were scanned for the LysM domain (PF01476.21). These LysM-containing transmembrane proteins were then scanned for a kinase domain (PF00069.26) to find LysM-RKs. Those LysM-containing transmembrane proteins without a kinase domain were designated as LysM-RPs.

## (References)

Boutrot, F. and Zipfel, C., 2017. Function, discovery, and exploitation of plant pattern recognition receptors for broad-spectrum disease resistance. Annual review of phytopathology, 55, pp.257-286.

Christopoulou, M., Wo, S.R.C., Kozik, A., McHale, L.K., Truco, M.J., Wroblewski, T. and Michelmore, R.W., 2015. Genome-wide architecture of disease resistance genes in lettuce. G3: Genes, Genomes, Genetics, 5(12), pp.2655-2669.

Hammami, R., Ben Hamida, J., Vergoten, G. and Fliss, I., 2009. PhytAMP: a database dedicated to antimicrobial plant peptides. Nucleic acids research, 37(suppl_1), pp.D963-D968.

Krogh, A., Larsson, B., Von Heijne, G. and Sonnhammer, E.L., 2001. Predicting transmembrane protein topology with a hidden Markov model: application to complete genomes. Journal of molecular biology, 305(3), pp.567-580.

# Lemnaceae Phylogeny Using Plastid Barcodes

`Analysis Directory: ./dw_barcode_tree/`

`Analysis Code: workflow.dk_spp_tree.txt`

The following files contain GenBank sequences used in this analysis (GenBank information included below file name):

`wang-2010.accessions` <br />
Authors: Wang,W., Wu,Y., Yan,Y., Ermakova,M., Kerstetter,R. and Messing,J. <br />
Title:   DNA barcoding of the Lemnaceae, a family of aquatic monocots <br />
Journal: BMC Plant Biol. 10, 205 (2010) <br />

`borisjuk_lam-2014.accessions` <br />
Authors: Borisjuk,N. and Lam,E. <br />
Title:   DNA barcoding of Lemna and Wolffiella species <br />
Journal: Unpublished <br />

`borisjuk-2015.accessions` <br />
Authors: Borisjuk,N., Chu,P., Gutierrez,R., Zhang,H., Acosta,K., Friesen,N., Sree,K.S., Garcia,C., Appenroth,K.J. and Lam,E. <br />
Title:   Assessment, validation and deployment strategy of a two-barcode protocol for facile genotyping of duckweed species <br />
Journal: Plant Biol. (2014) In press <br />

`bog-2018.accessions` <br />
Authors: Bog,M., Appenroth,K.J. and Sree,K.S. <br />
Title:   Molecular Taxonomy of Lemnaceae - State of Art <br />
Journal: Unpublished <br />

`bog-2019.accessions` <br />
Authors: Bog,M., Sree,K.S., Xu,S., Himmelbach,A., Brandt,R., Fuchs,J., Hoang,P.T.N., Schubert,I., Kuever,J., Rabenstein,A., Paolacci,S., Jansen,M.A.K. and Appenroth,K.J. <br />
Title:   A taxonomic revision of the section Uninerves within the genus Lemna <br />
Journal: Unpublished <br />

This resulted in 186 _atpF-atpH_ sequences and 153 _psbK-psbI_ sequences.

Phylogenetic analysis was performed separately on each barcode to determine the best fit evolutionary model (Kalyaanamoorthy et al., 2017). Sequences were aligned using MUSCLE (v3.8.1551) and maximum likelihood was generated using iqtree (version 1.6.12)(Edgar, 2004; Nguyen et al., 2015). These analyses revealed the best fit model for the _atpF-atpH_ barcode was K3Pu+F+R3 and the best fit model for the _psbK-psbI_ barcode was TPM2u+F+R3 (Kalyaanamoorthy et al., 2017).

A total of 139 _atpF-atpH_ and _psbK-psbI_ barcodes were concatenated from the same duckweed clone. _Colocasia esculenta_ (JN105690.1) was used an outgroup. To find the respective barcode sequences for this outgroup, a separate BLASTN search was performed using each set of duckweed barcodes. Each set of barcodes sequences containing the outgroup sequence were aligned using MUSCLE (v3.8.1551)(Edgar, 2004). The alignments were then concatenated using the linux command paste. Phylogeny was performed using concatenated alignments with iqtree (version 1.6.12) with a partition model (part 1: 1-800,K3Pu+F+R3; part 2: 801-1652,TPM2u+F+R3) and 1000 bootstrap replicates (Chernomor et al., 2016). _Lemna yungensis_ clones were renamed to _Lemna valdiviana_ (Bog et al., 2020) and _Spirodela polyrhiza_ 9203 was renamed to _Spirodela intermedia_ 9203 (Borisjuk et al., 2015).


## (References)

Bog, M., Sree, K.S., Fuchs, J., Hoang, P.T., Schubert, I., Kuever, J., Rabenstein, A., Paolacci, S., Jansen, M.A. and Appenroth, K.J., 2020. A taxonomic revision of Lemna sect. Uninerves (Lemnaceae). Taxon, 69(1), pp.56-66.

Borisjuk, N., Chu, P., Gutierrez, R., Zhang, H., Acosta, K., Friesen, N., Sree, K.S., Garcia, C., Appenroth, K.J. and Lam, E., 2015. Assessment, validation and deployment strategy of a two‐barcode protocol for facile genotyping of duckweed species. Plant Biology, 17, pp.42-49.

Chernomor, O., Von Haeseler, A. and Minh, B.Q., 2016. Terrace aware data structure for phylogenomic inference from supermatrices. Systematic biology, 65(6), pp.997-1008.

Edgar, R.C., 2004. MUSCLE: multiple sequence alignment with high accuracy and high throughput. Nucleic acids research, 32(5), pp.1792-1797.

Kalyaanamoorthy, S., Minh, B.Q., Wong, T.K., von Haeseler, A. and Jermiin, L.S., 2017. ModelFinder: fast model selection for accurate phylogenetic estimates. Nature methods, 14(6), pp.587-589.

Nguyen, L.T., Schmidt, H.A., Von Haeseler, A. and Minh, B.Q., 2015. IQ-TREE: a fast and effective stochastic algorithm for estimating maximum-likelihood phylogenies. Molecular biology and evolution, 32(1), pp.268-274.
