import pandas as pd

def sqi_generic(series, low=None, high=None):
    s = pd.to_numeric(series, errors='coerce')
    mask = s.notna()
    if low is not None:
        mask &= s >= low
    if high is not None:
        mask &= s <= high
    return mask.astype(float)
