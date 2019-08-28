#!/bin/bash

chmod +x doRNA-seq.sh

GENOME=~/qbb2019-answers/day2-lunch/BDGP6
ANNOTATION=~/qbb2019-answers/day2-lunch/BDGP6.Ensembl.81.gtf
THREADS=4

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  echo "*** Processing $SAMPLE"
  cp ../rawdata/$SAMPLE.fastq .
  fastqc $SAMPLE.fastq
  hisat2 -p $THREADS -x $GENOME -U $SAMPLE.fastq -S $SAMPLE.sam
  samtools sort $SAMPLE.sam -@ $THREADS -o $SAMPLE.bam
  samtools index $SAMPLE.bam
  stringtie $SAMPLE.bam -e -B -p $THREADS -G $ANNOTATION -o $SAMPLE.stringtie.gtf
done
