import numpy as np
import pandas as pd

def quantiles_25_50_75(data):
    return np.percentile(data, [25, 50, 75])


def ic_95(data):
    return np.percentile(data, [2.5, 97.5])

def five_number(data):
    return  np.percentile(data,[0, 25, 50, 75, 100])

def table_AED(data):
    return pd.DataFrame(data)