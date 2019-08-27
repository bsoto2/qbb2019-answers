#!/usr/bin/env python3

#FBID is in key [1] unipro is in value [0]
import sys

gene_id = {}

for line in open( sys.argv[1] ):
    genes_of_interest = line.rstrip('\r').split()
    comp = genes_of_interest[1]
    gene_id[comp] = genes_of_interest[0]

for i, line in enumerate( sys.stdin ):
    if i == 0:
        continue
    fields = line.rstrip('\r').split("\t")
    compar = fields[8]
    if compar in gene_id:
        print(fields[8] + line)
    elif gene_id == 0:
        print()
    elif gene_id == 0:
        print(line + "Nope")
        
