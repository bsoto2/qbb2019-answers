#!/usr/bin/env python3

"""
Boxplot all transcripts for a given gene
"""



import sys
import pandas as pd
import matplotlib.pyplot as plt

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]
# print(fpkm_file)
# print(type(open(fpkm_file)))
# for a in fpkm_file:
#     print(a)

df = pd.read_csv( fpkm_file, index_col="t_name" ) #Provides row name
goi = df.loc[:,"gene_name"] == gene_name
fpkms = df.drop( columns="gene_name") #Drop will remove a column
# print( fpkms.loc[goi,:] )
malelist = []
femalelist = []
for column in fpkms:
    # print(type(column))
# for row in enumerate(fpkm_file):
    if "female" in column:
        femalelist.append(column)
    else: 
        malelist.append(column)
maldat = df.loc[:, malelist]
femdat = df.loc[:, femalelist]

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.boxplot( maldat.loc[goi,:] .T)
ax1.set_title("Male Sxl Transcripts")
ax2.boxplot( femdat.loc[goi,:] .T)
ax2.set_title("Females Sxl Transcripts")
fig.savefig( "boxplot.png" )
plt.close( fig )