#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA 

for line in open( sys.argv[1] ):
    column = line.rstrip('\r').split('\t')
    if line.startswith("t_id"):
        continue
    else:
        # print(line)
        if column[2] == "+":
            startl = int(column[3]) - 500
            startr = int(column[3]) + 500
            if startl < 0:
                startl = 0
        else:
            endl = int(column[4]) - 500
            if endl < 0:
                endl = 0
            endr = int(column[4]) + 500
    if column[2] == "+":
        column[3] = startl
        column[4] = startr
    else:
        column[3] = endl
        column[4] = endr
    print(column[1], column[3], column[4], column[0])
