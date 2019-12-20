#!/usr/bin/env python3

"""
Create a timecourse of a given transcript for females
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt


#Load metadata
# soi = samples.loc[:, "sex"] == "female"
# srr_ids = samples.loc[soi, "sample"]

#This is specifying the transcript target of interest
t_name = sys.argv[1]
samples = pd.read_csv( sys.argv[2])
fpkms = pd.read_csv( sys.argv[3], index_col="t_name" )
replicates = pd.read_csv( sys.argv[4] )
  
def pull_the_sex(sex): #Equivalent to Kate's get_srr_ids
    soi = samples.loc[:, "sex"] == sex
    #srr_ids = samples.loc[soi, "sample"]
    stages = samples.loc[soi,"stage"]
    return(stages)
  

def data_production(fpkms, t_name, stages, sex):
    dataset = []  
    for stage in stages:
        stage += '\n'
        dataset.append(fpkms.loc[t_name, str((sex, stage))])
    return(dataset)
    
def rep_stg( sex ):
    soi = replicates.loc[:, "sex"] == sex
    stages = replicates.loc[soi, "stage"]
    return(stages)
    
    
male_stages= pull_the_sex("male")
female_stages = pull_the_sex("female")
rep_stages_f = rep_stg("female")
rep_stages_m = rep_stg("male")

markers = ["10", "11", "12", "13", "14A", "14B", "14C", "14D"]
tickers = [0, 50, 100, 150, 200, 250, 300]
female_dataset = data_production(fpkms, t_name, female_stages, "female")
male_dataset = data_production(fpkms, t_name, male_stages, "male")
replicate_dataset_f = data_production(fpkms, t_name, rep_stages_f, "female")
replicate_dataset_m = data_production(fpkms, t_name, rep_stages_m, "male")

# print(len(female_dataset))
# print(len(male_dataset))

# print( srr_ids )
#
# #Load FPKMs
# fpkms = pd.read_csv( sys.argv[3], index_col="t_name" )

#Extract data
# my_data = []
# for srr_id in srr_ids:
#     print( srr_id )
#     my_data.append( fpkms.loc[t_name, srr_id] )
#
# print(my_data)
fig, ax = plt.subplots()
ax.plot( male_dataset, color="blue", label="Male" )
ax.plot( female_dataset, color="red", label="Female" )
plt.legend( loc='center left' )
ax.set_xticklabels( markers, rotation=90, fontsize=12 )
plt.title("Sxl", fontsize=16)
plt.xlabel("developmental stage", fontsize=14)
plt.ylabel("mRNA abundance (RPKM)", fontsize=14)
ax.scatter( [4, 5, 6, 7], replicate_dataset_m, color="lightblue")
ax.scatter( [4, 5, 6, 7], replicate_dataset_f, color="pink")
fig.savefig( "timecourse.png" )
plt.close( fig )