#!/usr/bin/env python3

"""
Input ctab file to compare num_exons vs length
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

exons1 = []
fpkm1 = []
for i, line in enumerate( open(sys.argv[1]) ):
    if i == 0:
        continue
    fields = line.rstrip('\r').split('\t')
    fpkm1.append( float(fields[11]) )

exons2 = []
fpkm2 = []
for i, line in enumerate( open(sys.argv[2]) ):
    if i == 0:
        continue
    fields = line.rstrip('\r').split('\t')
    fpkm2.append( float(fields[11]) )


fpkm1 = np.array(fpkm1)
fpkm2 = np.array(fpkm2)
lfpkm1 = np.log2( fpkm1 + 1 )
lfpkm2 = np.log2( fpkm2 + 1 )

fig, ax = plt.subplots()
ax.set_title("FPKM Comparison of Two Sets")
ax.set_xlabel( "FPKMs2" )
ax.set_ylabel( "FPKMs1" )
ftln = np.polyfit(lfpkm1, lfpkm2, 1)
fteq = np.poly1d(ftln)
xp = np.linspace(0, 13, 100)
ax.scatter( lfpkm2, lfpkm1, s=100, color="pink", alpha=0.2)
ax.plot( xp, fteq(xp))
fig.savefig("fpkmcompare.png")
plt.close(fig)
print(fteq)


# fig, ax = plt.subplots()
# ax.set_title("FPKMS Histogram")
# ax.set_xlabel( "Transcripts of Interest" )
# ax.set_ylabel( "FPKMS Value" )
# ax.text(-7, 0.22, Input, bbox=dict(facecolor='white', alpha=0.5))
# ax.hist( my_data, bins=100, density=True )
# ax.plot( x, y )
# ax.plot( a, b )
# fig.savefig( "fpkms.png" )
# plt.close( fig )