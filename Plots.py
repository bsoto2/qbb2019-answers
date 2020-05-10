#!/usr/bin/env python3

import numpy as np
import sys
import matplotlib.pyplot as plt

fg = open(sys.argv[1])
fe = open(sys.argv[2])
ff = open(sys.argv[3])

fgs = []
fge = []
fgr = []
for line in fg:
    l1 = line.strip().split()
    fgs.append(l1[1])
    fge.append(l1[2])

fes = []
fee = []
for line in fe:
    l2 = line.strip().split()
    fes.append(l2[1])
    fee.append(l2[2])

prom = []
intr = []
exo = []
for line in ff:
    l3 = line.strip().split()
    if "promoter" in l3:
        prom.append(l3)
    if "exon" in l3:
        exo.append(l3)
    if "intron" in l3:
        intr.append(l3)
lprom = len(prom)
lint = len(intr)
lexo = len(exo)

# print(fes[0])
# print(fgs[0])
len1 = len(fgs)
len2 = len(fes)
# if len2 >= len1:
#     complen = len2
# else:
#     complen = len1
# i = 0
# k = 0
# j = 0
# while j != complen:
#     k = 0
#     while k != len(fes):
#         while int(fgs[j]) >= int(fes[k]):
#             diff = int(fgs[j]) - int(fes[k])
#             while diff >= 0:
#                 diff1 = int(fee[k]) - int(fes[k])
#                 while diff <= diff1:
#                     i += 1
#                     j += 1
#                     k += 1
#                 else:
#                     j += 1
#                     k += 1
#             else:
#                 j += 1
#                 k += 1
#         else:
#             j += 1
#             k += 1
#
#     else:
#         j += 1
        
# print(fee[3])
# g = 0
# k = 0
# while g != len(fgs):
#     l = 0
#     fgstart = int(fgs[g])
#     festart = int(fes[l])
#     feend = int(fee[l])
#     while k != len(fes):
#         while fgstart >= festart:
#             rem = 0
#             while fgstart <= feend:
#                 g = g + 1
#                 k = k + 1
#         else:
#             fes.remove(fes[0])
#             fee.remove(fee[0])
#             l = l + 1
#             k = k + 1
# else:
#     g = g + 1
#     k = k + 1
# print(g)
# print(l)



# i = 0
# k = len(l1)
# while i != k:
#     fgr.append(range(int(l1[1]), int(l1[2])))
# pring(fgr[1])

fig, (ax1, ax2) = plt.subplots(1, 2)
ax2.bar('G1E', len1)
ax2.bar('ER4', len2)
ax1.bar('Promoter', lprom)
ax1.bar('Exon', lexo)
ax1.bar('Intron', lint)
plt.show()