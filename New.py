#!/usr/bin/env python3

import sys
import numpy as np
import matplotlib.pyplot as plt

N = int(sys.argv[1])
trials = int(sys.argv[2])
stfrq = float(sys.argv[3])
selection = (float(sys.argv[4]))
# poplist = []
# poplist = (np.arange(N, 10000000, 100000).tolist())
# frqlist = [0.01, 0.1, 0.3, 0.45, 0.52, 0.6, 0.8, 0.99]
# print(poplist)
n = N * 2
# n = []
# for value in poplist:
#     n.append(value*2)
selcoeff = selection + 1
print(selcoeff)
def simulation(n, p): #n is the number of alleles in the pop and p is the allele freq
     # for value in frqlist:
    ttf = 0
    alleles = np.random.binomial(n,p)
    p = (alleles*selcoeff)/(n - alleles + (alleles*selcoeff))
    while alleles != 0 and alleles != n:
        alleles = np.random.binomial(n,p)
        p = (alleles*selcoeff)/(n - alleles + (alleles*selcoeff))
        ttf += 1
    return ttf
trial = simulation(n, stfrq)

trialsss = []
for i in range(trials):
    i=simulation(n, stfrq)
    trialsss.append(i)
print(trialsss)

fig, ax = plt.subplots()
ax.hist(trialsss)
ax.set_xlabel("Selection",fontsize=16)
ax.set_ylabel("Time To Fixation",fontsize=16)
fig.savefig("Part 4.png")
plt.tight_layout()
plt.show()
