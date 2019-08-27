#!/usr/bin/env python3

"""
Compute the average FPKM
"""

import sys

for line in open( sys.argv[1] ):
   field = line.rstrip('\r').split()
   if "_DROME" in line:
       print(field[-2], field[-1])
      
       
       
           
           

