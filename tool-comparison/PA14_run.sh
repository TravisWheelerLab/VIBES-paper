#!/bin/bash
#SBATCH --no-requeue
#SBATCH --ntasks=1
#SBATCH -t 12:00:00
#SBATCH --mem=30gb
#SBATCH --partition=standard --account=twheeler
#SBATCH --chdir=/groups/twheeler/genomad/

time apptainer run genomad_latest.sif end-to-end --restart pa/Pseudomonas_aeruginosa_UCBPP-PA14_109.fna genomad_output/ genomad_db/
