After the Pseudomonas Dataset analysis is complete, we can generate the metrics reported in the Results section of the publication and recreate Figures 4 and 5.

First, we run gene_count_filter.py on VIBES output. (We intend to integrate this script into the pipeline, but the initial version was run manually. In this version, the default gene threshold to pass the filter is 2, while the minimum acceptable overlap is 0.2. These can be supplied to the script as options if need be). This script is posted on the VIBES GitHub page at https://github.com/TravisWheelerLab/VIBES/tree/main/programs/python/extra_scripts.
`python3 gene_count_filter.py VIBES_output/tsv/bacterial_integrations/ VIBES_output/tsv/viral_gene_annotations/ VIBES_output/gene_count_filtered/tsv --force --output_histogram VIBES_output/gene_count_filtered/all_histogram.png`

The above command will generate Figure 5. Now, we move into the directory with TSVs filtered by match gene counts:
`cd VIBES_output/gene_count_filtered/tsv`

Then, we run some awk commands. They count the number of full integrations, the number of partial hits, the total number of reported events, and how many hits are composites made up of joined matches:
Full integration count
`awk -F'\t' 'BEGIN {id = 0; count = 0} {if (id != $NF && /^[^#]/ && $5 == "True") {count += 1}} {id = $NF} END {print count}' *.tsv`

Partial count
`awk -F'\t' 'BEGIN {id = 0; count = 0} {if (id != $NF && /^[^#]/ && $5 == "False") {count += 1}} {id = $NF} END {print count}' *.tsv`

Total count
`awk -F'\t' 'BEGIN {id = 0; count = 0} {if (id != $NF && /^[^#]/) {count += 1}} {id = $NF} END {print count}' *.tsv`

Joined count
`awk -F'\t' 'BEGIN {id = 0; count = 0} {if (id == $NF && /^[^#]/) {count += 1}} {id = $NF} END {print count}' *.tsv`

Next, we need the lengths of each match that passed the filter:
`awk 'function abs(x){return ((x < 0.0) ? -x : x)} BEGINFILE {id = 1; len = 0} {if (/^[^#]/ && id != $NF && len != 0) {print len; len = abs($12 - $11)} else {len += abs($12 - $11)} id = $NF} ENDFILE {print len}' *.tsv > ../all_element_lengths_joined_filtered.txt`

Finally, run generate_bin_plot.py, which is supplied in this directory. This file isn't intended for distribution via GitHub, and so its only argument (all_element_lengths_joined_filtered.txt) is hard-coded in.
python3 generate_bin_plot.py
