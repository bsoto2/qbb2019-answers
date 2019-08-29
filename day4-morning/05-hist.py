#!/usr/bin/env python3

"""
Plot FPKM
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

fpkms = []
for i, line in enumerate( open(sys.argv[1]) ):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    if float(fields[11]) > 0:
        fpkms.append( float(fields[11]) )
    
print( len(fpkms) )

my_data = np.log2( fpkms )

mu = 4
sigma = 2

x = np.linspace( -5, 15, 100)
print(x) 
print( type(x) )
y = stats.norm.pdf( x, mu, sigma )

skdg = float(sys.argv[2]) #SkewedDistribution in Green
skmu = float(sys.argv[3])
sksig = float(sys.argv[4]) #Values for skdg = 0.5, skmu = 3.9, sksig = 1.95

a = np.linspace( -5, 15, 1000 )
b = stats.skewnorm.pdf( a, skdg, skmu, sksig )
Input = {"SKDG =":str(skdg),
         "SKMU =":str(skmu), 
         "SKSTD =":str(sksig)}

fig, ax = plt.subplots()
ax.set_title("FPKMS Histogram")
ax.set_xlabel( "Transcripts of Interest" )
ax.set_ylabel( "FPKMS Value" )
ax.text(-7, 0.22, Input, bbox=dict(facecolor='white', alpha=0.5))
ax.hist( my_data, bins=100, density=True )
ax.plot( x, y )
ax.plot( a, b )
fig.savefig( "fpkms.png" )
plt.close( fig )