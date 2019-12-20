#!/usr/bin/env python3

"""
Count all kmers in a FASTA file
"""

from fasta import FASTAReader
import sys

reader1 = FASTAReader( open(sys.argv[1]) ) #This is a function that returns an object AND was generated by us
k = int(sys.argv[2])
reader2 = FASTAReader( open(sys.argv[3]) )

#query to 1 k to 2 and target to 3

kmers = {}

for ident, sequence in reader1:
    for i in range( 0, len(sequence) - k + 1 ):
        kmer = sequence[i:i+k]
        if kmer in kmers: 
            kmers[kmer].append((i, ident))
        else:
            kmers[kmer] = [(i, ident)]
    
extk = {}
for ident1, sequence1 in reader2:
    for i in range( 0, len(sequence1) - k + 1 ):
        kmerQ = sequence1[i:i+k]
        if kmerQ in kmers:
            print(i, kmerQ, kmers[kmerQ])
            extk[kmer].append((ident1))

for ident2, sequence2 in reader:
    count = 0
    for i in range( 0, len(sequence1) - k + 1 ):
            while kmerQ == kmer:
                kmerN = kmer + 1 + k
                if kmerN == extk:
                    count += 1
                    continue
                else: 
                    print(kmerN)
                    print(count)
                
    
            

                
#for kmer, count in sorted( kmers.items(), key=lambda t: t[1] ):
 #   print( kmer, count, sep="\t" ) #Allows us to iterate key and value 
    