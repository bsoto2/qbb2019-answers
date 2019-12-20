#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy

dfk3me1 = pd.read_csv(sys.argv[1], index_col = "t_name")
dfk3me2 = pd.read_csv(sys.argv[2], index_col = "t_name")
dfk9me3 = pd.read_csv(sys.argv[3], index_col = "t_name")
col_names = df.columns.values.tolist()

goi = pd.DataFrame(df.loc[sys.argv[4]].iloc[2:3])

histone_dict = {"FPKM" : df.loc[:,"FPKM"],
               "H3K4me1": df2.iloc[:,-1],  ##i to specify column
               "H3K4me3": df3.iloc[:,-1],
               "H3K9me3": df4.iloc[:,-1]}

histone_df = pd.DataFrame(histone_dict)

model = sm.formula.ols(formula = "FPKM ~ H3K4me1 + H3K4me3 + H3K9me3", data = histone_df) #input ~ out
ols_results = model.fit()

print(ols_results.summary())

fig, ax = plt.subplots()
ax.hist(ols_results.resid)
plt.xlabel("Residuals")
plt.ylabel("Frequency")
fig.savefig(RegRes.png)
plt.close(fig)

lgrg = np.log(ols_results.resid)

fig,ax = plt.subplots()
ax.hist(lgrg)
plt.xlabel("Log Residuals")
plt.ylabel("Frequency")
fig.savefig(LogRegRes.png)
plt.close(fig)