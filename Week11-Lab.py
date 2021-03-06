#!/usr/bin/env python3

import scanpy as sc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
#Make variable names (in this case the genes) unique
adata.var_names_make_unique()

sc.pp.filter_genes(adata, min_counts = 1) #only consider genes with more than 1 count
sc.pp.normalize_per_cell(adata, key_n_counts = 'n_counts_all') #normalize with total UMI count per cell
filter_result = sc.pp.filter_genes_dispersion(adata.X, flavor = 'cell_ranger', n_top_genes=1000, log = False)
adata = adata[:, filter_result.gene_subset] #filter genes



sc.pp.normalize_per_cell(adata)  # need to redo normalization after filtering
sc.pp.log1p(adata)
sc.pp.scale(adata)
sc.pp.neighbors(adata)
sc.tl.louvain(adata, resolution=0.3)
sc.tl.rank_genes_groups(adata, 'louvain', groups=['1', '6', '9', '7'], method="t-test")

#PCA Plotting
# sc.tl.pca(adata,n_comps=50)
# sc.pl.pca(adata)x
sc.pl.pca(sc.tl.rank_genes_groups)

#UMAP
# sc.tl.umap(adata)
# sc.tl.louvain(adata, resolution=0.3)
# sc.pl.umap(adata, color='louvain')

# #GeneLabeledPCA
# sc.tl.rank_genes_groups(adata, 'louvain', groups=['1', '6', '9', '7'])
# sc.pl.rank_genes_groups(adata, n_genes=30)

#tSNE
# sc.tl.tsne(adata)
# sc.pl.tsne(adata, color='louvain', legend_loc='on data')
# adata.write(results_file)