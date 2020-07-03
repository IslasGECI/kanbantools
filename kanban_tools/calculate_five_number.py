import numpy as np

def quantiles_25_50_75(data):
    return np.percentile(data,[25,50,75])

def ic_95(data):
    return np.percentile(data,[2.5,97.5])