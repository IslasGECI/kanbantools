import numpy as np

def quantiles_25_50_75(data):
    return np.percentile(data,[25,50,75])