python ../code/select.brain.genes.py GTEx_Analysis_v6_RNA-seq_RNA-SeQCv1.1.8_gene_reads.gct genes.GTEX.tsv

#select genes present at least in 1250 samples
awk -F "," '{if ($3>1250) print}' genes.GTEX.tsv | awk -F "." '{print $1}' >genes.GTEX.brain.2500.txt
