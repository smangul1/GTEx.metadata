wget http://www.gtexportal.org/static/datasets/gtex_analysis_v6/rna_seq_data/GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_reads.gct.gz

grep Brain E-MTAB-5214.sdrf.txt | awk '{print $1}' | sort | uniq >brain.samples.txt
