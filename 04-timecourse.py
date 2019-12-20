#!/usr/bin/env python3

"""
Create a timecourse of a given transcript for females
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

#Specify transcript of interest
t_name = sys.argv[1]

#Load metadata
samples = pd.read_csv( sys.argv[2])
for "sex" in samples:
    loc[:, "sex"]
    if == female:
        fems = samples.loc[fems, "sample"]
    else:
        mals = samples.loc[mals, "sample"]
# soi = samples.loc[:, "sex"] == "female"
# srr_ids = samples.loc[soi, "sample"]

print(fems)
## print( srr_ids )
#
# #Load FPKMs
# fpkms = pd.read_csv( sys.argv[3], index_col="t_name" )
#
# #Extract data
# sex = [fems, mals]
# my_data = []
# for  in srr_ids:
#     print( srr_id )
#     my_data.append( fpkms.loc[t_name, srr_id] )
#
#
# print(my_data)
# fig, ax = plt.subplots()
# ax.plot( my_data )
# fig.save( "timecourse.png" )
# plt.close( fig )