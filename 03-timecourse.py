#!/usr/bin/env python3

"""
Usage: ./03-timecourse.py <t_name> <samples.csv> <all.csv>f
Create a timecourse of a given transcript for females
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

#Specify transcript of interest
t_name = sys.argv[1]
#Load metadata
#sexes = {'sex':["male", "female"]}

samples = pd.read_csv( sys.argv[3])
for i in range(samples.shape[0]):
    for j in range[ 9, 19 ]:
        if samples.iloc[i:j] == "
        
#soi = samples.loc[:, "sex"] == "female"
#srr_ids = samples.loc[soi, "sample"]
print(samples.shape)

# #Load FPKMs
# fpkms = pd.read_csv( sys.argv[3], index_col="t_name" )
#
# #Extract data
# my_data_fem = []
# my_data_mal = []
# for femd in femds:
#     print( femd )
#     my_data_fem.append( fpkms.loc[t_name, femd] )
# for mald in malds:
#     print( mald )
#     my_data_mal.append( fpkms.loc[t_name, mald] )
#

# print(my_data)
# fig, ax = plt.subplots()
# ax.plot( my_data )
# fig.save( "timecourse.png" )
# plt.close( fig )