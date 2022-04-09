# multiple plot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def LinearBaseline(x, y, points):
    x1 = x[0]
    x2 = x[len(x)-1]
    y1 = np.mean(y[0:points])
    y2 = np.mean(y[-points:-1])
    
    grad = (y2-y1)/(x2-x1)
    intercept = y1-grad*x1

    baseline_fit = grad*x + intercept
    
    return baseline_fit
  
  
