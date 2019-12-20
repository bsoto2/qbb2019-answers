#!/usr/bin/env python3

import sys 
import matplotlib.pyplot as plt 
import seaborn as sns

ref = open(sys.argv[1]) #run on fimo.tsv
# stuff = open(sys.argv[2])
#
#Do Over

scr = []
loc = []

for line in ref:
    if "motif_id" in line:
        continue
    if line.startswith("#"):
        continue
    field = line.rstrip().split("\t")
    score = field[6]
    scr.append(score)
    location = field[4]
    loc.append(location)

sortd = loc.sort()

rel_pos = []
for i in loc:
    relative == (i/(loc[-1]))
    rel_pos.append(relative)

# seaborn histogram
sns.distplot(rel_pos, hist=True, kde=False, 
             bins=int(180/5), color = 'blue',
             hist_kws={'edgecolor':'black'})
# Add labels
plt.title('Histogram of Motif Binding')
plt.xlabel('Relative Location')
plt.ylabel('Binding Score')
fig.savefig("MotifDist.png")
plt.close(fig)














 # This doesn't seem to work... new plan
# length = []
# for line in ref:
#     if ">" in line:
#         continue
#     else:
#         length_length = len(line)
#     length.append(length_length)
# lngth_chrm = sum(length)
# # print(lngth_chrm)
#
# lov = []
# app = []
# for row in stuff:
#     if row.startswith("#"):
#         continue
#     else:
#         fields = row.split()
#         if float(fields[4]) >= 0:
#             app.append(float(fields[4]))
#             info = fields[8].split(";")
#             print(info[18:])
#             # for info in line:
#    #              length_seq = len(info[5][9:])
#    #              lov.append(length_seq)
#    #          print(lov)
#    #          print(app)
#    #      else:
#    #          continue
#


        