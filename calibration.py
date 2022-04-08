import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define straight-line model
def StrtLineModel(x, m, c):
    y_lin = m*x + c
    return (y_lin)

# x-values and y-values here:

x = np.array([545, 5842]) #Put ADC values here (vacuum and atmospheric pressures, respectively)
y = np.array([0, 1021])  # Latter number will vary (Check OU Weather Station for pressure). Vacuum is, of course, 0.
