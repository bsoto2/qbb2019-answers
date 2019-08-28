#!/usr/bin/env python3

import sys

nrgn = []
search_pos = int(21378950)
#search_chr = "3R"

for line in open( sys.argv[1] ):
    column = line.rstrip('\r').split()
    if 'gene_biotype "protein_coding"' in line and "3R" in column[0] and "gene" in column[2]:
        info = (int(column[3]), int(column[4]), column[13])
        nrgn.append(info)
        #print(nrgn)
        
lo = 0
hi = len(nrgn) - 1
mid = 0
number_iterations = 0
while True:
    mid = int((hi+lo)/2)
    number_iterations = number_iterations + 1
    if (search_pos < nrgn[mid][0]):
        hi = int(mid)
    elif (search_pos < nrgn[mid][1]):
        lo = int(mid)
    else:
        print(nrgn[mid][2], number_iterations)
        break
        
        