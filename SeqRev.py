#!/usr/bin/env python2

import sys
from fasta import FASTAReader
import numpy as np
import matplotlib.pyplot as plt

r1 = (open(sys.argv[1]))
r2 = (open(sys.argv[2]))
#
# aa = []
# for ident, seq in r1:
#     aa.append(seq)
#
# nt = []
# for ident, seqnt in r2:
#     nt.append(nt)
#
# inex = []
# for sequence, protein in zip(aa, nt):
#     seq_gap = ""
#     position = 0
#     for num, i in enumerate(protein):
#         if i =="-":
#             seq_gap = seq_gap + "---"
#         else:
#             seq_gap = seq_gap + sequence[position]
#             position += 3
#         inex.append(seq_gap)
#     print(inex)

aa1 = []
for line in r1:
    linew = line.rstrip("\n")
    for aa in linew:
        aa1.append(aa)
# print(aa1)

aa2 = []
for line in r2:
    aa2.append(line[1])

# print(aa2)
# print(len(aa1))
# print(len(aa2))
rev = {"I":"ATA", "M":"ATG", "T":"ACA", "N":"AAC", "K":"AAA", "S":"AGC", "R":"AGA", "L":"CTA", "P":"CCA", "H":"CAC", "Q":"CAG", "V":"GTA", "A":"GCA", "D":"GAC", 
            "E":"GAG", "G":"GGA", "S":"TCA", "F":"TTC", "L":"TTG", "Y":"TAC", "C":"TGC", "*":"TGA", "_":"---", " ":"---", "W":"TGG", "X":"---"}

ntc1 = []
ntc2 = []
i = 0
while i != len(aa2):
    ntc1.append(rev[aa2[i]])
    ntc2.append(rev[aa1[i]])
    i += 1

nuc1 = []
nuc2 = []
for nt in ntc1:
    for nu in nt:
        nuc1.append(nu)
for nt1 in ntc2:
    for nu2 in nt1:
        nuc2.append(nu2)

# print((nuc2))
# print((nuc1))
k = 0
lod = []
while k != len(nuc1):
    if str(nuc1[k]) == str(nuc2[k]):
        lod.append(int(1))
        k += 1
    else:
        lod.append(int(0))
        k += 1

stdd = np.std(lod)
meann = np.mean(lod)
# print(stdd)
# print(meann)

zsc = []
for number in lod:
    score = (number - meann)/stdd
    zsc.append(score)
# print(zsc)
xax = []
lmn = 0
while lmn != len(zsc):
    xax.append(lmn)
    lmn += 1
    

fig, ax = plt.subplots()
ax.scatter(xax, zsc)
plt.show()