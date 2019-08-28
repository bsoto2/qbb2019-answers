head -n 40000 SRR072893.fastq  > SRR072893.10k.fastq
fastqc SRR072893.10k.fastq 
hisat2 -x BDGP6 -U SRR072893.10k.fastq -S SRR072893.10k.sam
samtools sort -@ 4 SRR072893.10k.sam > SRR072893.10k.sorted.sam
samtools index SRR072893.10k.sorted.sam > stdout
StringTie SRR072893.10k.sorted.sam -e -B -p 4 -G BDGP6.Ensembl.81.gtf -o SRR072893.10k.sorted.bam