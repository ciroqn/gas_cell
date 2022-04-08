# Plotting absorbances, correpsonding to max peaks in CO2 spectra, against pressures at which they were taken. Pressures for these measurements range 
# from 10-150 mbar.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# See overall plot beforehand:
data = pd.read_csv('pressab_gas2.csv', header=1)

data.head()

print(data.columns.tolist()) # again, had trouble with col name. Turns out there was an extra space...

x = data['pressure / mbar']
y = data['bend absorbance']

plt.rcParams['figure.figsize'] = (12, 8)
plt.scatter(x, y)

