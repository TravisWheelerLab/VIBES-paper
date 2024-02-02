First, download Pseudomonas_aeruginosa_PAO1_107.fna (https://www.pseudomonas.com/downloads/pseudomonas/pgd_r_22_1/Pseudomonas_aeruginosa_PAO1_107/Pseudomonas_aeruginosa_PAO1_107.fna.gz) and Pseudomonas_aeruginosa_UCBPP-PA14_109.fna (https://www.pseudomonas.com/downloads/pseudomonas/pgd_r_22_1/Pseudomonas_aeruginosa_UCBPP-PA14_109/Pseudomonas_aeruginosa_UCBPP-PA14_109.fna.gz) from the Pseudomonas Genome Database or copy from complete genome database used in the pseudomonas_dataset analysis. Unzip the genome files.

Then, use some tool to isolate the prophage sequences from the pseudomonas genomes. I used esl-sfetch, as below:
`esl-sfetch -n Pf4 -c 785174..797794 -o Pf4.fna Pseudomonas_aeruginosa_PAO1_107.fna refseq\|NC_002516.2\|chromosome`
`esl-sfetch -n Pf5 -c 4345187..4354873 -o Pf5.fna Pseudomonas_aeruginosa_UCBPP-PA14_109.fna refseq\|NC_008463.1\|chromosome`

Store Pf4 and Pf5 in one multi-FASTA query file:
`cat Pf4.fna Pf5.fna > Pf4_Pf5.fna`

Then, submit to PHASTEST and DBSCAN-SWA web servers:
https://phastest.ca/submissions/new
http://www.microbiome-bigdata.com/PHISDetector/index/tools/DBSCAN-SWA

Download the geNomad Docker container and its default databases:
`apptainer pull docker://antoniopcamargo/genomad`
`apptainer run genomad_latest.sif download-database .`

geNomad jobs were submitted as .sh scripts (see PAO1_run.sh, PA14_run.sh in this directory)

VIBES was run with the following command. Parameters files are available in this directory:
`nextflow run workflow.nf -profile ua_hpc -params-file ground_truth.yaml -with-report gt_report_hpc.html -w /path/to/workdir/work/`