import numpy as np
from scipy.stats import linregress

def compute_trend(time_list, ndvi_series):
    slope, intercept, r, p, _ = linregress(time_list, ndvi_series)
    return {
        "slope": slope,
        "r": r,
        "p": p
    }