# Disease Resistance Genes

## (NLRs)

`working directory: ./dk_disease_resistance genes/duckweed_nbarc/`

The HMM model for the NB-ARC domain (PF00931) was used to search the proteomes specified in Table 1 with HMMR version 3.1b2 using the gathering bit score threshold.


## (AMPs)

`working directory: ./dk_disease_resistance genes/duckweed_amp/`

A total of 268 antimicrobial peptide sequences were analyzed from the PhytAMP database (Hammammi et al., 2009). These peptide sequences were comprised of cyclotides, defensins, heveins, impatiens, knottins, lipid transfer proteins, sheperins, thionins, and vicilins. HMMR version 3.1b2 was used to build HMMs for each peptide family. These HMMs were then used to search the proteomes specified in Table 1 using the gathering bit score threshold.

 
## (PRRs)

`working directory: ./dk_disease_resistance genes/duckweed_prr/`

PRRs were defined as illustrated in Boutret and Zipfel (2017).
 
To find PRRs, TMHMM2.0 was used to find transmembrane proteins in the proteomes specified in Table 1.

To find LRR-type PRRs, transmembrane proteins were scanned with the following LRR HMM models: PF00560.34, PF07723.14, PF07725.13, PF12799.8, PF13306.7, PF07723.14, PF07723.14, PF07723.14, PF18831.2, and PF18805.2 . These LRR-containing transmembrane proteins were then scanned for a kinase domain (PF00069.26) to find LRR-RKs. Those LRR-containing transmembrane proteins without a kinase domain were designated as LRR-RPs.

To find LysM-type PRRs, transmembrane proteins were scanned for the LysM domain (PF01476.21). These LysM-containing transmembrane proteins were then scanned for a kinase domain (PF00069.26) to find LysM-RKs. Those LysM-containing transmembrane proteins without a kinase domain were designated as LysM-RPs.


## (References)

Boutrot, F. and Zipfel, C., 2017. Function, discovery, and exploitation of plant pattern recognition receptors for broad-spectrum disease resistance. Annual review of phytopathology, 55, pp.257-286.

Christopoulou, M., Wo, S.R.C., Kozik, A., McHale, L.K., Truco, M.J., Wroblewski, T. and Michelmore, R.W., 2015. Genome-wide architecture of disease resistance genes in lettuce. G3: Genes, Genomes, Genetics, 5(12), pp.2655-2669.
