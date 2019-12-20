#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import sys

File = open(sys.argv[1])

Read_Depth = []
Overall_Quality = []
Frequency = []
PredEff = []

for line in File:
    if line.startswith("#"):
        continue
    rows = line.rstrip().split()
    info = rows[7].split(";")

    #Will append the numerical element of Read Depth defined as DP in vcf file
    Depth = info[7][3:]
    Read_Depth.append((Depth))

    Quality = rows[5]
    Overall_Quality.append((Quality))

    Frequency_Temp = info[3][3:]
    Frequency.append((Frequency_Temp))

    Ann_Effect = info[4][3:]
    PredEff.append((Ann_Effect))



#GRAPHING
fig, axs = plt.subplots(2, 2)
axs[0, 0].hist(Depth)
axs[0, 0].set_title('Read Depth [0, 0]')
axs[0, 1].hist(Overall_Quality)
axs[0, 1].set_title('Read Quality [0, 1]')
axs[1, 0].hist(Frequency)
axs[1, 0].set_title('Frequency of Occurence [1, 0]')
axs[1, 1].plot(Ann_Effect)
axs[1, 1].set_title('Effect Annotation [1, 1]')

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')

# Hide x labels and tick labels for top plots and y ticks for right plots.
fig. savefig("finalplot.png")
plt.close(fig)